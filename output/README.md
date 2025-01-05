# Navigating the Output Files

The output files in this folder are titled according to the model and dataset used to produce their contents. The code used to generate
raw outputs differed depending on which model/dataset combo was being tested, and so some outputs are found in .csv files while others are in
.json

The naming scheme for the output csv and json files is `<model_name>_<dataset_name>`. `<dataset_name>` is one of "original", "normal", and "irrelevant".
"original" corresponds to original GSM8K questions, "normal" signifies our dataset with numbers/entities altered, and "irrelevant" is the
dataset with numbers/entities altered alongside the addition of an irrelevant sentence.

In addition to the 18 raw output files, we also have `gold_labels.csv`, which stores the correct answers to the problems in the "normal" and 
"irrelevant" datasets we generated (the answers are the same for both datasets since "irrelevant" questions are identical to "normal" aside
from the addition of a sentence that doesn't affect the final answer), and `gold_labels_original.csv`, which has the answers to the random sample
of GSM8K problems we used to do a baseline evaluation on the LLMs.

Finally, there are a number of .txt files that display raw accuracy values outputted by our evaluation scripts.

# Evaluation Script


Our evaluation script, `score.py`, can be run on the command line as follows:

```bash
python score.py <model_output> <gold_labels>
```

where `<model_output>` is the set of answers predicted by an LLM and `<gold_labels>` is the set of correct answers to the word problems
in the dataset.

The output of `score.py` consists of the total number of correct predictions, the number of problems in the dataset, and the final accuracy
(equal to the quotient of the first two values).

An example output (from the GP4-4o results on the "irrelevant" dataset) is shown below:
```bash
Correct:  1895

Total:  2700

Acc:  0.7018518518518518
```
