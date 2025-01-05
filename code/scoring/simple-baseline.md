Our simple baseline is gemma-2-2b-it LLM from Google, the simplest LLM we are testing, with approximately 2 billion parameters. The provided `simple-baseline.py` program
shuffles our dataset and queries the LLM for its answers to the math problems in series using one-shot chain-of-thought prompting. The prompt template we use
is taken from https://arxiv.org/pdf/2302.00093 and is as follows:

Q: Elsa has 5 apples. Anna has 2 more apples than Elsa. How
many apples do they have together?
A: Anna has 2 more apples than Elsa, so Anna has 2 + 5 = 7 apples. Elsa and Anna
have 5 + 7 = 12 apples together. The answer is 12.
Q: [Question]
A:

This form of prompting is designed to help the LLM understand that it is supposed to solve a simple math problem and provide a step-by-step solution. Once we have iterated through the entire dataset, the results are stored in a list called `our_list`. `our_list` only contains the numerical solution to each problem, so we
have defined a function `extract_final_number()` to parse the answer from the raw respnoses provided by the gemma model.
At the same time, the correct numerical answers are extracted from our dataset and stored in
`answers_list`

An example output (i.e. `our_list`) would look something like this list of integers: [116, 2560, 1512, 16, 3520, 90, 2673, 520, 14990, 42, 1568, 5200, 47, 3872, ...].
