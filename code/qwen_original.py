import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import re
import pandas as pd
from datasets import Dataset
import json

# Load dataset
splits = {'train': 'main/train-00000-of-00001.parquet',
                  'test': 'main/test-00000-of-00001.parquet'}
df = pd.read_parquet("hf://datasets/openai/gsm8k/" + splits["train"])
questions = df.sample(n=2700, random_state=42)
dataset = Dataset.from_pandas(questions)

# Load model
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-3B-Instruct",
    device_map="cuda",
    torch_dtype="auto",
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-3B-Instruct", padding_side="left")

# Define text generation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    batch_size=8,
    model_kwargs={"torch_dtype": torch.bfloat16},
)

def extract_final_number(text):
    # Find all numbers in the text
    numbers = re.findall(r'\d+[.,\d]*\d+|\d', text)
    if numbers:
        # Convert the last number found to an integer
        # return int(numbers[-1])
        stripped = numbers[-1].replace(",", "")
        if '.' in stripped:
          try:
              res = float(stripped)
              return res
          except ValueError:
              return None
        return int(stripped)
    return None  # Return None if no numbers are found

def format_prompt(question):
    return [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Elsa has 5 apples. Anna has 2 more apples than Elsa. How many apples do they have together?"},
        {"role": "assistant", "content": "Anna has 2 more apples than Elsa, so Anna has 2 + 5 = 7 apples. Elsa and Anna have 5 + 7 = 12 apples together. The answer is 12."},
        {"role": "user", "content": question},
    ]

# Prepare prompts
formatted_prompts = [format_prompt(question) for question in questions["question"]] # normal or irrelevant

# Perform batch processing
outputs = pipe(formatted_prompts, max_new_tokens=512)

# Save the original list structure to JSON
with open("res/qwen_original.json", "w") as f:
    json.dump(outputs, f)

# Get accuracy
predictions = [extract_final_number(output[0]['generated_text'][-1]['content']) for output in outputs]
answers_list = [extract_final_number(answer) for answer in questions["answer"]]
correct_predictions = sum(1 for true, pred in zip(answers_list, predictions) if abs(true - pred) <= 0.05)

assert len(answers_list) == len(predictions), "Mismatch in number of predictions and ground truth values!"
accuracy = (correct_predictions / len(answers_list)) * 100

print(f"Accuracy: {accuracy:.2f}%")

with open("res/qwen_original_acc.txt", "w") as f:
    f.write(f"Accuracy: {accuracy:.2f}%")

