# Are LLMs Smarter than an Eighth Grader? Exploring Mathematical Abilities of Large Language Models

## Overview

This repository explores and implements concepts inspired by the research paper "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models" by Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, and Mehrdad Farajtabar from Apple Machine Learning Research. The repository contains a detailed report and presentation of the study, along with code for dataset generation and evaluation.

## Paper Details

-   **Title**: GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models
-   **Authors**: Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, Mehrdad Farajtabar
-   **Link**: [Read the paper](https://arxiv.org/pdf/2410.05229)
-   **Published**: 2024

## Repository Structure

-   Report.pdf - a concise and comprehensive report of our method and findings
-   data/ - a subdirectory containing all the data that was used for evaluating model performance along with the code that was used to generate the data
-   code/ - all code that was used for the evaluation scripts as well as code that was used for running the HuggingFace and OpenAI models
-   output/ - a subdirectory containing all models' raw outputs on the evaluation sets, along with the gold labels

## Instruction to run code

1. source .venv/bin/activate
2. pip install -r requirements.txt
3. run file in /code

## Key Concepts

The research introduces an improved benchmark created from symbolic templates that allow for the generation of a diverse set of questions to evaluate the reasoning capabilities of language models. Our implementation generates instantiations of questions from the GSM8K dataset by changing information such as the specific numbers, names of people, and their relationships to each other. Additionally, irrelevant information is injected into the question to test LLMs' robustness to these alterations.

## Team Members

John-Wesley Appleton, Tin Do, Edmund Doerksen, William Qi
