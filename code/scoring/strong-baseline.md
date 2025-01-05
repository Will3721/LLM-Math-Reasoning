Much like for our simple baseline, we are again performing one-shot CoT prompting. Our prompt is the same as what was used for `simple-baseline.py`.
The only difference between `strong-baseline.py` and `simple-baseline.py` is the choice of model. Here, we use ChatGPT-4o, which is widely considered
one of the strongest LLMs ever developed. The code in `strong-baseline.py` runs the model on the 2700 math questions in the dataset we generated that do
not contain irrelevant additional context.

Sample outputs are the same as in `simple-baseline.py`.

Note that we managed to finish running on 1123 questions in total for the Milestone 3 deadline. The result was 478 correct responses, for an accuracy of 0.426
