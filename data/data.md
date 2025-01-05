# Data

Our data comes from the GSM8K dataset. This dataset contains grade 8 math questions and their respective answers. Each answer contains the reasoning process for that question. The file `train.parquet` contains the downloaded training data. The file `test.parquet` contains the downloaded testing data.

Here is an example GSM8K question:

Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?

Our project requires us to create variants of multiple questions to evaluate the relative performance of different models on each variant. To create the variants, we create a template by replacing names, relations, and quantities by variables. We then sample different values to generate the question and answers. For each problem we have a second variant which contains an additional string that does not contain any additional information.

Here is a GSM8K variant with names and numbers randomized:

Mia sold clips to 12 of her friends in April, and then she sold half as many clips in May. How many clips did Mia sell altogether in April and May?

You can see that the person involved in the word problem has a different name, and the number of items she has has also changed.

In addition, here is the same GSM8K problem with names and numbers randomized as well as an additional string added (which only contains irrelevant filler):

Mia sold clips to 12 of her friends in April, and then she sold half as many clips in May. Mia sold 7 dogs in April, and 3 in May. How many clips did Mia sell altogether in April and May?

Since our project deals with the evaluation of different models, we do not need to split our dataset. Our dataset will contain 10,000 problems. These problems are generated as follows:
1. Create templates for 100 GSM8K questions.
2. For each template, generate 50 variants.
3. For each variant, genarate another version with additional irrelevant information.

The template creation process is completely manual and very tedious. We currently have 54 templates (totalling 5,400 problems), but we will continue generating more until we reach 100 templates.
