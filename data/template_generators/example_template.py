# This is an example template from the paper.

from template_generator import Problem

"""
A problem is created as follows:
    Problem(
        num_female_names,
        num_male_names,
        num_female_relations,
        num_male_relations,
        num_ints,
        irrelevant_string_generator,
        question_generator,
        answer_generator,
        condition,
        modification
    )
"""

problem = Problem(
        1,
        0,
        0,
        1,
        4,
        lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]}'s favorite toy is the building blocks. ",
        lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"When {female_names[0]} watches her {male_relations[0]}, she gets out a variety of toys for him. The bag of building blocks has {ints[0]} blocks in it. {irrelevant_string}The bin of stuffed animals has {ints[1]} stuffed animals inside. The tower of stacking rings has {ints[2]} multicolored rings on it. {female_names[0]} recently bought a tube of bouncy balls, bringing her total number of toys she bought for her {male_relations[0]} up to {sum(ints)}. How many bouncy balls came in the tube?",
        lambda female_names, male_names, female_relations, male_relations, ints: f"Let T be the number of bouncy balls in the tube. After buying the tube of balls, {female_names[0]} has {ints[0]} + {ints[1]} + {ints[2]} + T = {ints[0] + ints[1] + ints[2]} + T = {sum(ints)} toys for her {male_relations[0]}. Thus, T = {sum(ints)} - {ints[0] + ints[1] + ints[2]} = <<{sum(ints)}-{ints[0] + ints[1] + ints[2]}={ints[3]}>>{ints[3]} bouncy balls came in the tube.",
)

question, irrelevant_question, answer = problem.generate_problem()

print("Original Question: \n", question, "\n")
print("Question with Irrelevant Information: \n", irrelevant_question, "\n")
print("Answer: \n", answer, "\n")
