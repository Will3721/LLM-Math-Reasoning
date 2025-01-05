import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import re
import pandas as pd
from datasets import Dataset
import pandas as pd
# from google.colab import drive
import os

'''
code for working with Google Drive folder using Google Colab notebook
'''
# drive.mount('/content/drive')

# folder_path = "/content/drive/My Drive/cis530"

# Change the current working directory to the specified folder
# os.chdir(folder_path)


questions = pd.read_csv('data/variants_data.csv', names=['normal', 'irrelevant', 'answer'])
#dataset = Dataset.from_pandas(questions)
questions.head()

# OR
# splits = {'train': 'main/train-00000-of-00001.parquet',
#           'test': 'main/test-00000-of-00001.parquet'}
# df = pd.read_parquet("hf://datasets/openai/gsm8k/" + splits["train"])
# questions = df.sample(n=2700, random_state=42)

type_of_questions = "normal"

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

# !pip install openai --upgrade

# Commented out IPython magic to ensure Python compatibility.
import openai
# %set_env OPENAI_API_KEY="fill in your key"

def answer_quest(question):
    prompt = '''
Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How
many apples do they have together?
A: Anna has 2 more apples than Elsa, so Anna has 2 + 5 = 7 apples. Elsa and Anna
have 5 + 7 = 12 apples together. The answer is 12.
Q: ''' + question + '\nA:'
    response = openai.chat.completions.create(
        model="gpt-4o-mini", # or "gpt-4o"
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    long_ans = response.choices[0].message.content
    #res = extract_final_number(long_ans)
    #print(res)
    return long_ans

from tqdm import tqdm


normal_list = questions['normal'].tolist()
results = [answer_quest(question) for question in tqdm(normal_list, desc="Processing Questions")]
predictions = [extract_final_number(ans) for ans in results]

answers_list = [extract_final_number(answer) for answer in questions["answer"]]

correct_predictions = sum(1 for true, pred in zip(answers_list, predictions) if abs(true - pred) <= 0.05)

assert len(answers_list) == len(predictions), "Mismatch in number of predictions and ground truth values!"
accuracy = (correct_predictions / len(answers_list)) * 100


output_df = pd.DataFrame({
    "Generated_Output": results,
    "Extracted_From_Output": predictions,
    "Expected_Answer": questions["answer"].tolist(),
    "Extracted_From_Expected_Answer": answers_list
})
output_df.to_csv("4omini;normal.csv", index=False)

print(f"Accuracy: {accuracy:.2f}%")