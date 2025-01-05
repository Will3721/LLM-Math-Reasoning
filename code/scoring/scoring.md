Our evaluation metric is simple: find the accuracy of the LLM on the given dataset.

As such, we compute with the following formula: Accuracy = (# correct responses) / (# questions). A model's response is considered correct if it has value identical to the response given in the provided answer key.

The accuracy metric is well established as a means of assessing LLM performance on mathematics datasets as seen in these papers:

https://arxiv.org/pdf/2410.05229

https://arxiv.org/pdf/2302.00093


# Scoring Script

The scoring script is ran as `python scoring/score.py [output_file] [answer_file]`, where `output_file` is the filepath for the system output and `answer_file` is the filepath for the gold standard answers.
