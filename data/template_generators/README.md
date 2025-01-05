# Generating Templates

It's pretty simple. Read the entire README and refer to `wes_templates.py` and `example_template.py` as an example.

## Data

The raw data files are stored in the parent directory. There is a data viewer at https://huggingface.co/datasets/openai/gsm8k/viewer. You can select the train or test set, and sort by ascending or descending. We will split the questions as follows:
1. Wes -> beginning questions in train set.
2. Tin -> ending questions in train set.
3. Will -> beginning questions in test set.
4. Edmund -> ending questions in test set.

## Process

Questions and answers can be found in the datafiles located in the parent directory. Coordinate with others to ensure there is no question overlap between people.

You should define a function `get_problem_templates()` that returns a list of `Problem` objects. Each problem object has the following:

1. `num_female_names`: the number of unique female names in the problem.
2. `num_male_names`: the number of unique male names in the problem.
3. `num_female_relations`: the number of females identified by their relation to the main person.
4. `num_male_relations`: the number of males identified by their relation to the main person.
5. `num_ints`: the number of integers in the questions. Should not include the answer.
6. `irrelevant_string_generator`: a function that generates an irrelevant string from its sample inputs. Make sure to add a space at the end of the generated string. Its parameters are: `female_names`, `male_names`, `female_relations`, `male_relations`, `ints`.
6. `question_generator`: a function that generates a string question from its sample inputs. Its parameters are: `irrelevant_string`, `female_names`, `male_names`, `female_relations`, `male_relations`, `ints`.
7. `answer_generator`: a function that generates a string answer from its sample inputs. Its parameters are: `female_names`, `male_names`, `female_relations`, `male_relations`, `ints`.
8. `condition`: an optional function that checks if the inputs are valid. See note below on this (you should avoid using this while still guaranteeing that the inputs are valid). Its parameters are: `female_names`, `male_names`, `female_relations`, `male_relations`, `ints`.
9. `modification`: an optional function that modifies the invalid inputs to make them valid. See note below on this (you should avoid using this while still guaranteeing that the inputs are valid). Its parameters are: `female_names`, `male_names`, `female_relations`, `male_relations`, `ints`.

## Important Notes

Questions must be valid questions. For example, Jimmy cannot have -3 apples.

The best way to ensure valid questions is to think carefully about how you define the inputs. In the example found in the `example_template.py`, a constraint is enforced by carefully choosing which values were randomly selected.

I would argue that most templates can enforce their constraints without needing to use the `condition` or `modification` parameters. If it is not possible to do so, either skip the question or read below for advice on using the `condition` and `modification` parameters.

If both `condition` and `modification` are provided, invalid inputs will be modified using `modification`. It is up to you to decide how to modify the input. Be wary, however, because if a large number of generated inputs are invalid and modified the same way, we are not getting the diverse dataset that we are expecting.

If only `condition` is provided, we make a recursive call until a set of valid inputs is generated. Be aware of the probability of a valid input, and its associated runtime. For example, if we generate integers between 1 and 100, and we want to enforce that the integers are divisible by 23, you should not only use condition as it will take many recursive calls until we obtain valid integers. This is a situation where it would make sense to just modify the input by multiplying the generated integer by 23 (see the first problem in `wes_templates.py` as an example).
