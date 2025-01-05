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
            1,
            0,
            0,
            4,
            lambda female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} received $50 the following day from his grandfather. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} and {female_names[0]} divided ${ints[0]*5} in the ratio 3:2. {irrelevant_string}If {male_names[0]} spent ${ints[1]} on a book, how much money did he have left?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"The ${ints[0]*5} was divided into 3 + 2 = <<3+2=5>>5 parts. So each part is ${ints[0]*5}/5 = $<<{ints[0]*5}/5={ints[0]}>>{ints[0]}. So Gerald received ${ints[0]} x 3 = $<<{ints[0]}*3={ints[0]*3}>>{ints[0]*3}. Gerald bought a book at $<<{ints[1]}={ints[1]}>>{ints[1]}. Therefore, Gerald was left with ${ints[0]*3} - ${ints[1]} = $<<{ints[0]*3}-{ints[1]}={ints[0]*3-ints[1]}>>{ints[0]*3-ints[1]}. #### "
        ),
        Problem(
            1,
            0,
            0,
            0,
            3,
            lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]}'s dog is 3 times faster than her cat. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]}'s cat is {ints[0]} times faster than her turtle. {irrelevant_string}If the cat can run {ints[0]*ints[1]} feet/second, how many feet can her turtle crawl in {ints[2]} seconds?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"First find the speed of the turtle by dividing the cat's speed by {ints[0]}: {ints[0]*ints[1]} feet/second / {ints[0]} = <<{ints[0]*ints[1]}/{ints[0]}={ints[1]}>>{ints[1]} feet/second Then multiply the turtle's speed by the number of seconds it spends crawling to find how far it crawls: {ints[2]} seconds * {ints[1]} feet/second = <<{ints[2]}*{ints[1]}={ints[2]*ints[1]}>>{ints[2]*ints[1]} feet #### {ints[2]*ints[1]}"
        ),
        Problem(
            0,
            0,
            0,
            0,
            3,
            lambda female_names, male_names, female_relations, male_relations, ints: f"The local firefighters are donating to the Alzheimer's foundation. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"The local firefighters are doing a “fill the boot” fundraiser. Their goal is to raise {ints[0] * (ints[1] + ints[2])}. After the first {ints[1]} hours, they have raised {ints[1] * ints[0]}. {irrelevant_string}For how many hours do they have to fundraise in total to reach their goal, assuming an equal amount raised in every hour?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"{ints[1]*ints[0]} / {ints[1]} = $<<{ints[1]*ints[0]}/{ints[1]}={ints[0]}>>{ints[0]} per hour. They have to fundraise for {ints[0] *(ints[1]+ints[2])} / {ints[0]} = <<{ints[0] *(ints[1]+ints[2])}/{ints[0]}={ints[1]+ints[2]}>>{ints[1]+ints[2]} hours. #### {ints[1]+ints[2]}"
        ),
        Problem(
            1,
            0,
            0,
            0,
            3,
            lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} works very hard every day. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{irrelevant_string}Given a {ints[0]}-day week, how much does {female_names[0]} charge for {ints[1]} weeks of tutoring if she charges ${ints[2]} per day?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"A week has {ints[0]} days, therefore {ints[1]} weeks have {ints[1]}*{ints[0]}= <<{ints[1]}*{ints[0]}={ints[1] * ints[0]}>>{ints[1]}*{ints[0]} days. If {female_names[0]} charges ${ints[2]} per day, then in {ints[1]}*{ints[0]} days she would charge ${ints[2]}*({ints[1]}*{ints[0]}) = $<<{ints[2]}*{ints[1]*ints[0]}={ints[2] * (ints[1] * ints[0])}>>{ints[2]}*({ints[1]}*{ints[0]}) #### {ints[2] * (ints[1] * ints[0])}"
        ),
        Problem(
            0,
            0,
            0,
            0,
            5,
            lambda female_names, male_names, female_relations, male_relations, ints: f"The factory will shut down next week. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"An ice cream factory makes {ints[0]} quarts of chocolate ice cream in {ints[1]} hours. It can make {ints[2]} quarts of vanilla ice cream in {ints[3]} hours. {irrelevant_string}How many quarts in total would be made in {ints[4]} hours?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"Chocolate ice cream can be made at {ints[0]} quarts / {ints[1]} hours = [{ints[0] / ints[1]}] quarts per hour. Vanilla ice cream can be made at {ints[2]} quarts / {ints[3]} hours = [{ints[2] / ints[3]}] quarts per hour. In {ints[4]} hours there would be {ints[4]} * [{ints[0] / ints[1]}] quarts = [{ints[4] * (ints[0] / ints[1])}] quarts of chocolate ice cream. In {ints[4]} hours there would be {ints[4]} * [{ints[2] / ints[3]}] quarts = [{ints[4] * (ints[2] / ints[3])}] quarts of vanilla ice cream. Combined there would be [{ints[4] * (ints[0] / ints[1])}] chocolate + [{ints[4] * (ints[2] / ints[3])}] vanilla = [{ints[4] * (ints[0] / ints[1]) + ints[4] * (ints[2] / ints[3])}] quarts of ice cream. #### [{ints[4] * (ints[0] / ints[1]) + ints[4] * (ints[2] / ints[3])}]"
        ),
        Problem(
            0,
            1,
            0,
            0,
            9,
            lambda female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} loyalty card is Visa. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} ordered {ints[0]} croissants at ${ints[1]} apiece, {ints[2]} cinnamon rolls at ${ints[3]} each, {ints[4]} mini quiches for ${ints[5]} apiece and {ints[6]} blueberry muffins that were ${ints[7]} apiece. At check out, {male_names[0]} shows his loyalty card that gives him {ints[8]}% off of his purchase. {irrelevant_string}What is {male_names[0]}' total bill?",
            lambda female_names, male_names, female_relations, male_relations, ints: f" {ints[0]} croissants cost ${ints[1]} each so they cost {ints[0]}*{ints[1]} = $<<{ints[0]}*{ints[1]}={ints[0] * ints[1]}>>{ints[0] * ints[1]} {ints[2]} cinnamon rolls cost ${ints[3]} each so they cost {ints[2]}*{ints[3]} =$<<{ints[2]}*{ints[3]}={ints[2] * ints[3]}>>{ints[2] * ints[3]} {ints[4]} mini quiches cost ${ints[5]} each so they cost {ints[4]}*{ints[5]} = $<<{ints[4]}*{ints[5]}={ints[4] * ints[5]}>>{ints[4] * ints[5]} {ints[6]} blueberry muffins cost ${ints[7]} each so they cost {ints[6]}*{ints[7]} = $<<{ints[6]}*{ints[7]}={ints[6] * ints[7]}>>{ints[6] * ints[7]} All total, his pastries cost {ints[0] * ints[1]}+{ints[2] * ints[3]}+{ints[4] * ints[5]}+{ints[6] * ints[7]} = $<<{ints[0] * ints[1]}+{ints[2] * ints[3]}+{ints[4] * ints[5]}+{ints[6] * ints[7]}={ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7]}>>{ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7]} He has a {ints[8]}% coupon for his ${ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7]} purchase so that saves him .{ints[8]}*{ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7]} = $<<.01*{ints[8]}*{ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7]}={ints[8] * .01 * (ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7])}>>{ints[8] * .01 * (ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7])} His total bill is ${ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7]} minus his discount of ${ints[8] * .01 * (ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7])} so {ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7]}-{ints[8] * .01 * (ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7])} = $<<{ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7] - ints[8] * .01 * (ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7])}>>{ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7] - ints[8] * .01 * (ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7])} #### {ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7] - ints[8] * .01 * (ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5] + ints[6] * ints[7])}"
        ),
        Problem(
            1,
            0,
            0,
            0,
            3,
            lambda female_names, male_names, female_relations, male_relations, ints: f"Waffle cones are unavailable today. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"The ice cream parlor was offering a deal, buy {ints[0]} scoops of ice cream, get 1 scoop free. Each scoop cost ${ints[1]}. {irrelevant_string}If {female_names[0]} had ${ints[2]}, how many scoops of ice cream should she buy?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"Each scoop cost ${ints[1]}. If she buys {ints[0]}, she gets one free. So it will cost her {ints[0]} * {ints[1]} = $<<{ints[0]}*{ints[1]}={ints[0] * ints[1]}>>{ints[0] * ints[1]} for {ints[0] + 1} scoops total. If you break it down, {ints[0] + 1} scoops of ice cream cost ${ints[0] * ints[1]} so {ints[0] * ints[1]}/{(ints[0] + 1)} = $<<{(ints[0]) * ints[1]}/{ints[0] + 1}={(ints[0]) * ints[1] / (ints[0] + 1)}>>{(ints[0]) * ints[1] / (ints[0] + 1)} per scoop {female_names[0]} has ${ints[2]} and each scoop ends up costing ${(ints[0]) * ints[1] / (ints[0] + 1)} each then {ints[2]}/{(ints[0]) * ints[1] / (ints[0] + 1)} = <<{ints[2]}/{(ints[0]) * ints[1] / (ints[0] + 1)}={ints[2] /  (ints[0]) * ints[1] / (ints[0] + 1)}>>{ints[2] /  (ints[0]) * ints[1] / (ints[0] + 1)} scoops total #### {ints[2] /  (ints[0]) * ints[1] / (ints[0] + 1)}"
        ),
        Problem(
            0,
            1,
            0,
            0,
            3,
            lambda female_names, male_names, female_relations, male_relations, ints: f"He has 3 kinds of tiles at his disposal. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"Mr {male_names[0]} is remodeling his bathroom. For every square foot, he needs {ints[0]} mosaic tiles. {irrelevant_string}How many mosaic tiles would Mr {male_names[0]} need to cover two thirds of his {ints[1] * 3} sq ft bathroom?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"A third of Mr. {male_names[0]}'s bathroom is {ints[1] * 3}/3 = <<{ints[1]*3}/3={ints[1]}>>{ints[1]} sqft Two thirds of Mr. {male_names[0]}'s bathroom is {ints[1]} x 2 = <<{ints[1]}*2={ints[1] * 2}>>{ints[1]*2} sq ft Mr. {male_names[0]} needs {ints[1]*2} x {ints[0]} = <<{ints[1]*2}*{ints[0]} = {ints[1]*ints[0]*2}>>{ints[1]*ints[0]*2} mosaic tiles #### {ints[1]*ints[0]*2}"
        ),
        Problem(
            0,
            1,
            0,
            0,
            5,
            lambda female_names, male_names, female_relations, male_relations, ints: f"He makes 4 pancakes. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} makes himself a {ints[0]} egg omelet with {ints[1]} oz of cheese and an equal amount of ham. Eggs are {ints[2]} calories each. Cheese is {ints[3]} calories per ounce. Ham is {ints[4]} calories per ounce. {irrelevant_string}How many calories is the omelet?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"The eggs contributed {ints[0]}*{ints[2]}=<<{ints[0]}*{ints[2]}={ints[0]*ints[2]}>>{ints[0]*ints[2]} calories He eats {ints[1]}*{ints[3]}=<<{ints[1]}*{ints[3]}={ints[1]*ints[3]}>>{ints[1]*ints[3]} calories of cheese He eats {ints[1]}*{ints[4]}=<<{ints[1]}*{ints[4]}={ints[1]*ints[4]}>>{ints[1]*ints[4]} calories of ham So in total he eats {ints[0]*ints[2]}+{ints[1]*ints[3]}+{ints[1]*ints[4]}=<<{ints[0]*ints[2]}+{ints[1]*ints[3]}+{ints[1]*ints[4]}={ints[0]*ints[2]+ints[1]*ints[3]+ints[1]*ints[4]}>>{ints[0]*ints[2]+ints[1]*ints[3]+ints[1]*ints[4]} calories #### {ints[0]*ints[2]+ints[1]*ints[3]+ints[1]*ints[4]}"
        )        
    ]
    return templates


def main():
    # Use this to experiement and check templates.
        for problem in get_problem_templates():
          print("----------------------------------------------------------------------")
          question, irrelevant_question, answer = problem.generate_problem()
          print("Original Question: \n", question, "\n")
          print("Question with Irrelevant Information: \n", irrelevant_question, "\n")
          print("Answer: \n", answer, "\n")

if __name__ == "__main__":
    main()
