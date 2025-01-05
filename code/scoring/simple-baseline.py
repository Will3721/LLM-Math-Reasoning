# -*- coding: utf-8 -*-
"""cis530_final.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13ppACu7qhETs3XHPPQ8x43Wl9Xtpyc6D
"""

import torch
from transformers import pipeline

import os
import re
import pandas as pd
!pip3 install datasets
from datasets import Dataset
# Set your token as an environment variable
# os.environ['HF_TOKEN'] = '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'

!pip install light-the-torch
!ltt install torch torchvision

pipe = pipeline(
    "text-generation",
    model="google/gemma-2-2b-it",
    model_kwargs={"torch_dtype": torch.bfloat16},
    device="cuda",  # replace with "mps" to run on a Mac device
    batch_size=8
)


messages = [
    {"role": "user", "content": "Who are you? Please, answer in pirate-speak."},
]

outputs = pipe(messages, max_new_tokens=256)
assistant_response = outputs[0]["generated_text"][-1]["content"].strip()
print(assistant_response)

questions = pd.read_csv('variants_data.csv')
questions = questions.sample(frac=1).reset_index(drop=True)
questions

dataset = Dataset.from_pandas(questions)

dataset

def extract_final_number(text):
    # Find all numbers in the text
    numbers = re.findall(r'\b\d+\b', text)
    if numbers:
        # Convert the last number found to an integer
        return int(numbers[-1])
    return None  # Return None if no numbers are found

def perform_task(question):
  request = '''
Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How
many apples do they have together?
A: Anna has 2 more apples than Elsa, so Anna has 2 + 5 = 7 apples. Elsa and Anna
have 5 + 7 = 12 apples together. The answer is 12.
Q: ''' + question + '\nA:'
  messages = [
      {"role": "user", "content": request},
  ]

  outputs = pipe(messages, max_new_tokens=256)
  assistant_response = outputs[0]["generated_text"][-1]["content"].strip()
  res = extract_final_number(assistant_response)
  print(res)
  return res

our_list = [perform_task(row[0]) for _, row in questions.iterrows()]

answers_list = [extract_final_number(row[2]) for _, row in questions.iterrows()]
answers_list

num = 0
for ans in answers_list:
  if ans >= 100000:
    num += 1
num
