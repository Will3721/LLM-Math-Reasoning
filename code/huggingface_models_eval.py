import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import re
import pandas as pd
import json


# This code is for GSM8K
# splits = {'train': 'main/train-00000-of-00001.parquet',
#           'test': 'main/test-00000-of-00001.parquet'}
# df = pd.read_parquet("hf://datasets/openai/gsm8k/" + splits["train"])
# questions = df.sample(n=2700, random_state=42)

# This code is for our data
questions = pd.read_csv('data/variants_data.csv', names=['normal', 'irrelevant', 'answer'])

from huggingface_hub import login

login("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")

model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2-2b-it", # change depending on model
    device_map="cuda",
    torch_dtype="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-2b-it")

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
        #{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Elsa has 5 apples. Anna has 2 more apples than Elsa. How many apples do they have together?"},
        {"role": "assistant", "content": "Anna has 2 more apples than Elsa, so Anna has 2 + 5 = 7 apples. Elsa and Anna have 5 + 7 = 12 apples together. The answer is 12."},
        {"role": "user", "content": question},
    ]

# Prepare prompts
formatted_prompts = [format_prompt(question) for question in questions["irrelevant"]] # change to question or normal or irrelevant

# Perform batch processing
outputs = pipe(formatted_prompts, max_new_tokens=512)

# Save the original list structure to JSON
with open("generated_outputs_gsm.json", "w") as f:
    json.dump(outputs, f)

predictions = [extract_final_number(output[0]['generated_text'][-1]['content']) for output in outputs]

answers_list = [extract_final_number(answer) for answer in questions["answer"]]

correct_predictions = sum(1 for true, pred in zip(answers_list, predictions) if abs(true - pred) <= 0.05)

assert len(answers_list) == len(predictions), "Mismatch in number of predictions and ground truth values!"
accuracy = (correct_predictions / len(answers_list)) * 100

print(f"Accuracy: {accuracy:.2f}%")

pred_text = [output[0]['generated_text'][-1]['content'] for output in outputs]
wrong_pred_txt = [(true, pred, true_txt, txt) for true, pred, true_txt, txt in zip(answers_list, predictions, questions['answer'], pred_text) if abs(true - pred) > 0.05]
wrong_pred_txt[:5]