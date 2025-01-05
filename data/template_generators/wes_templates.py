# This is a script that will generate templates for the dataset questions.

from problem import Problem

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

def get_problem_templates():
    templates = [
        Problem(
            1,
            0,
            0,
            0,
            1,
            lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} sold three times as many in June. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} sold clips to {ints[0]*2} of her friends in April, and then she sold half as many clips in May. {irrelevant_string}How many clips did {female_names[0]} sell altogether in April and May?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} sold {ints[0]*2}/2 = <<{ints[0]*2}/2={ints[0]}>>{ints[0]} clips in May. {female_names[0]} sold {ints[0]*2}+{ints[0]} = <<{ints[0]*2}+{ints[0]}={ints[0]*3}>>{ints[0]*3} clips altogether in April and May. #### {ints[0]*3}"
        ),
        Problem(
            1,
            0,
            0,
            0,
            2,
            lambda female_names, male_names, female_relations, male_relations, ints: f"She didn't do any babysitting today. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} earns ${ints[0]} an hour for babysitting. Yesterday, she just did {ints[1]} minutes of babysitting. {irrelevant_string}How much did she earn?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} earns {ints[0]}/60 = $<<{ints[0]}/60={ints[0]/60}>>{ints[0]/60} per minute. Working {ints[1]} minutes, she earned {ints[0]/60} x {ints[1]} = $<<{ints[0]/60}*{ints[1]}={(ints[0]/60)*ints[1]}>>{(ints[0]/60)*ints[1]}. #### {(ints[0]/60)*ints[1]}"
        ),
        Problem(
            1,
            0,
            1,
            1,
            1,
            lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]}'s friends did not give her any money. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} is saving money for a new wallet which costs ${ints[0] * 10}. {female_names[0]} has only half of the money she needs. Her {female_relations[0]} decided to give her ${ints[0]} for that purpose, and her {male_relations[0]} twice as much as her {female_relations[0]}. {irrelevant_string}How much more money does {female_names[0]} need to buy the wallet?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"In the beginning, {female_names[0]} has only {ints[0]*10} / 2 = $<<{ints[0]*10}/2=>>{ints[0]*5}. {female_names[0]}'s {male_relations[0]} gave her {ints[0]} * 2 = $<<{ints[0]}*2={ints[0]*2}>>{ints[0]*2}. This means, {female_names[0]} needs {ints[0]*10} - {ints[0]*5} - {ints[0]*2} - {ints[0]} = $<<{ints[0]*10}-{ints[0]*5}-{ints[0]*2}-{ints[0]}>>{ints[0]*2} more. #### {ints[0]*2}"
        ),
        Problem(
            1,
            0,
            0,
            0,
            1,
            lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} really loves this book! ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} is reading a {ints[0]*10}-page book. {irrelevant_string}Yesterday, she was able to read {ints[0]} pages and today, she read twice as many pages as yesterday. If she wants to read half of the remaining pages tomorrow, how many pages should she read?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} read {ints[0]} x 2 = <<{ints[0]}*2={ints[0]*2}>>{ints[0]*2} pages today. So she was able to read a total of {ints[0]} + {ints[0]*2} = <<{ints[0]}+{ints[0]*2}={ints[0]*3}>>{ints[0]*3} pages since yesterday. There are {ints[0]*10} - {ints[0]*3} = <<{ints[0]*10}-{ints[0]*3}={ints[0]*7}>>{ints[0]*7} pages left to be read. Since she wants to read half of the remaining pages tomorrow, then she should read {ints[0]*7}/2 = <<{ints[0]*7}/2={ints[0]*7/2}>>{ints[0]*7/2} pages. #### {ints[0]*7/2}"
        ),
        Problem(
            0,
            1,
            0,
            0,
            2,
            lambda female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} has many friends all around the world. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} writes a {ints[0]}-page letter to {ints[1]} different friends twice a week. {irrelevant_string}How many pages does he write a year?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"He writes each friend {ints[0]}*2=<<{ints[0]}*2={ints[0]*2}>>{ints[0]*2} pages a week. So he writes {ints[0]*2}*{ints[1]}=<<{ints[0]*2}*{ints[1]}={ints[0]*ints[1]*2}>>{ints[0]*ints[1]*2} pages every week. That means he writes {ints[0]*ints[1]*2}*52=<<{ints[0]*ints[1]*2}*52={ints[0]*ints[1]*104}>>{ints[0]*ints[1]*104} pages a year #### {ints[0]*ints[1]*104}"
        ),
        Problem(
            0,
            1,
            0,
            0,
            3,
            lambda females_names, males_names, female_relations, male_relations, ints: f"All pizzas are pepperoni pizzas. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} is wondering how much pizza he can eat in one day. He buys {ints[0]} large pizzas and {ints[1]} small pizzas. A large pizza has {ints[2]*2} slices and a small pizza has {ints[2]} slices. {irrelevant_string}If he eats it all, how many pieces does he eat that day?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"He eats {ints[0]*ints[2]*2} from the largest pizzas because {ints[0]} x {ints[2]*2} = <<{ints[0]}*{ints[2]*2}={ints[0]*ints[2]*2}>>{ints[0]*ints[2]*2}. He eats {ints[1]*ints[2]} from the small pizza because {ints[1]} x {ints[2]} = <<{ints[1]}*{ints[2]}={ints[1]*ints[2]}>>{ints[1]*ints[2]}. He eats {ints[0]*ints[2]*2+ints[1]*ints[2]} pieces because {ints[0]*ints[2]*2} + {ints[1]*ints[2]} = <<{ints[0]*ints[2]*2}+{ints[1]*ints[2]}={ints[0]*ints[2]*2+ints[1]*ints[2]}>>{ints[0]*ints[2]*2+ints[1]*ints[2]} #### {ints[0]*ints[2]*2+ints[1]*ints[2]}"
        ),
        Problem(
            0,
            1,
            0,
            0,
            1,
            lambda female_names, male_names, female_relations, male_relations, ints: f"He does not have any apple trees. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} has {ints[0]*4} mango trees on his farm. He also has {ints[0]} less than half as many coconut trees as mango trees. {irrelevant_string}How many trees does {male_names[0]} have in all on his farm?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"Half of the number of {male_names[0]}'s mango trees is {ints[0]*4}/2 = <<{ints[0]*4}/2={ints[0]*2}>>{ints[0]*2} trees. So {male_names[0]} has {ints[0]*2} - {ints[0]} = <<{ints[0]*2}-{ints[0]}={ints[0]}>>{ints[0]} coconut trees. Therefore, {male_names[0]} has {ints[0]*4} + {ints[0]} = <<{ints[0]*4}+{ints[0]}={ints[0]*5}>>{ints[0]*5} trees on his farm. #### {ints[0]*5}"
        ),
        Problem(
            1,
            0,
            0,
            0,
            3,
            lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} is a fast reader! ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} can read {ints[0]} pages of a book in {ints[1]} minutes. {irrelevant_string}How many hours will it take her to read {ints[2]*20} pages?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"In one hour, there are {60/ints[1]} sets of {ints[1]} minutes. So, {female_names[0]} can read {ints[0]} x {60/ints[1]} = <<{ints[0]}*{60/ints[1]}={ints[0]*60/ints[1]}>>{ints[0]*60/ints[1]} pages in an hour. It will take her {ints[2]*20}/{ints[0]*60/ints[1]} = <<{ints[2]*20}/{ints[0]*60/ints[1]}={ints[2]*20/(ints[0]*60/ints[1])}>>{ints[2]*20/(ints[0]*60/ints[1])} hours to read {ints[2]*20} pages. #### {ints[2]*20/(ints[0]*60/ints[1])}"
        ),
        Problem(
            1,
            0,
            0,
            0,
            1,
            lambda female_names, male_names, female_relations, male_relations, ints: f"The post office didn't have any baseball stamps. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} bought stamps at the post office. Some of the stamps had a snowflake design, some had a truck design, and some had a rose design. {female_names[0]} bought {ints[0]*10} snowflake stamps. She bought {ints[0]} more truck stamps than snowflake stamps, and {ints[0]*2} fewer rose stamps than truck stamps. {irrelevant_string}How many stamps did {female_names[0]} buy in all?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"The number of truck stamps is {ints[0]*10} + {ints[0]} = <<{ints[0]*10}+{ints[0]}={ints[0]*11}>>{ints[0]*11}. The number of rose stamps is {ints[0]*11} − {ints[0]*2} = <<{ints[0]*11}-{ints[0]*2}={ints[0]*9}>>{ints[0]*9}. {female_names[0]} bought {ints[0]*10} + {ints[0]*11} + {ints[0]*9} = <<{ints[0]*10}+{ints[0]*11}+{ints[0]*9}={ints[0]*30}>>{ints[0]*30} stamps in all. #### {ints[0]*30}"
        ),
        Problem(
            0,
            0,
            0,
            0,
            4,
            lambda female_names, male_names, female_relations, male_relations, ints: f"The jaguars are the apex predators of this ecosystem. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"Each bird eats {ints[0]} beetles per day, each snake eats {ints[1]} birds per day, and each jaguar eats {ints[2]} snakes per day. {irrelevant_string}If there are {ints[3]} jaguars in a forest, how many beetles are eaten each day?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"First find the total number of snakes eaten: {ints[2]} snakes/jaguar * {ints[3]} jaguars = <<{ints[2]}*{ints[3]}={ints[2]*ints[3]}>>{ints[2]*ints[3]} snakes. Then find the total number of birds eaten per day: {ints[2]*ints[3]} snakes * {ints[1]} birds/snake = <<{ints[2]*ints[3]}*{ints[1]}={ints[1]*ints[2]*ints[3]}>>{ints[1]*ints[2]*ints[3]} birds. Then multiply the number of birds by the number of beetles per bird to find the total number of beetles eaten per day: {ints[1]*ints[2]*ints[3]} * {ints[0]} beetles/bird = <<{ints[1]*ints[2]*ints[3]}*{ints[0]}={ints[0]*ints[1]*ints[2]*ints[3]}>>{ints[0]*ints[1]*ints[2]*ints[3]} beetles. #### {ints[0]*ints[1]*ints[2]*ints[3]}"
        ),
        Problem(
            1,
            0,
            0,
            0,
            3,
            lambda female_names, male_names, female_relations, male_relations, ints: f"She prefers to shop on Saturdays because there are too many people on Sundays and she doesn't like to wait in line. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} does her grocery shopping on Saturday. {irrelevant_string}She does her shopping only at a specific store where she is allowed a credit of ${ints[0]*50}, which must be paid in full before her next shopping trip. That week she spent the full credit limit and paid ${ints[1]} of it on Tuesday and ${ints[2]} of it on Thursday. How much credit will {female_names[0]} need to pay before her next shopping trip?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"So far, {female_names[0]} has paid back ${ints[1]} + ${ints[2]} = $<<{ints[1]}+{ints[2]}={ints[1]+ints[2]}>>{ints[1]+ints[2]} of the credit. So she still needs to pay ${ints[0]*50} - ${ints[1]+ints[2]} =$<<{ints[0]*50}-{ints[1]+ints[2]}={ints[0]*50-ints[1]-ints[2]}>>{ints[0]*50-ints[1]-ints[2]} #### {ints[0]*50-ints[1]-ints[2]}"
        ),
        Problem(
            0,
            1,
            0,
            0,
            2,
            lambda female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} shudders as he recalls the events of the Lord of the Flies. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} is stranded on a desert island. He wants some salt to season his fish. {irrelevant_string}He collects {ints[0]} liters of seawater in an old bucket. If the water is {ints[1]}% salt, how many ml of salt will {male_names[0]} get when all the water evaporates?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"First find how many liters of the seawater are salt: {ints[0]} liters * {ints[1]}% = <<{ints[0]}*{ints[1]}*0.01={ints[0]*ints[1]*0.01}>>{ints[0]*ints[1]*0.01} liters. Then multiply that amount by 1000 ml/liter to find the number of ml of salt {male_names[0]} gets: {ints[0]*ints[1]*0.01} liters * 1000 ml/liter = <<{ints[0]*ints[1]*0.01}*1000={ints[0]*ints[1]*0.01*1000}>>{ints[0]*ints[1]*0.01*1000} ml. #### {ints[0]*ints[1]*0.01*1000}"
        ),
        Problem(
            0,
            0,
            0,
            0,
            2,
            lambda female_names, male_names, female_relations, male_relations, ints: f"The homes were decorated by the renown outdoor designer, Amanda Steele. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"There are 5 houses on a street, and each of the first four houses has {ints[0]} gnomes in the garden. {irrelevant_string}If there are a total of {ints[0]*4+ints[1]} gnomes on the street, how many gnomes does the fifth house have?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"In the first four houses, there are a total of 4 houses * {ints[0]} gnomes = <<4*{ints[0]}={ints[0]*4}>>{ints[0]*4} gnomes. Therefore, the fifth house had {ints[0]*4+ints[1]} total gnomes – {ints[0]*4} gnomes = <<{ints[0]*4+ints[1]}-{ints[0]*4}={ints[1]}>>{ints[1]} gnomes. #### {ints[1]}"
        ),
        Problem(
            0,
            0,
            0,
            0,
            3,
            lambda female_names, male_names, female_relations, male_relations, ints: f"The roads are poorly maintained and contain many potholes. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"A car is driving through a tunnel with many turns. {irrelevant_string}After a while, the car must travel through a ring that requires a total of 4 right-hand turns. After the 1st turn, it travels {ints[0]} meters. After the 2nd turn, it travels {ints[1]} meters. After the 3rd turn, it travels a little further and at the 4th turn, it immediately exits the tunnel. If the car has driven a total of {sum(ints)} meters around the ring, how far did it have to travel after the 3rd turn?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"From the details given, the car has traveled {ints[0]} meters at the 1st turn + {ints[1]} meters after the 2nd turn + 0 meters after the 4th turn = <<{ints[0]}+{ints[1]}+0={ints[0]+ints[1]}>>{ints[0]+ints[1]} meters around the ring. It must therefore have driven {sum(ints)} total meters – {ints[0]+ints[1]} calculated meters = {ints[2]} meters after the 3rd turn. #### {ints[2]}"
        ),
        Problem(
            0,
            3,
            0,
            1,
            1,
            lambda female_names, male_names, female_relations, male_relations, ints: f"{male_names[2]} is Mr. {male_names[0]}'s favorite {male_relations[0]}. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"Mr. {male_names[0]} shared a certain amount of money between his two {male_relations[0]}, {male_names[1]} and {male_names[2]}. {irrelevant_string}If {male_names[1]} got ${ints[0]}, and {male_names[2]} got twice as much as {male_names[1]}, how much was the money shared?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"{male_names[2]} got twice ${ints[0]} which is 2*${ints[0]} = $<<2*{ints[0]}={ints[0]*2}>>{ints[0]*2} The total amount shared was ${ints[0]}+${ints[0]*2} = $<<{ints[0]}+{ints[0]*2}={ints[0]*3}>>{ints[0]*3} #### {ints[0]*3}"
        )
    ]
    return templates


def main():
    # Use this to experiement and check templates.
    templates = get_problem_templates()
    print("There are {len(templates)} templates.")
    for i, problem in enumerate(templates):
        print(f"========================= Question {i+1} =========================")
        question, irrelevant_question, answer = problem.generate_problem()
        print("Original Question: \n", question, "\n")
        print("Question with Irrelevant Information: \n", irrelevant_question, "\n")
        print("Answer: \n", answer, "\n")


if __name__ == "__main__":
    main()
