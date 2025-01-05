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
            4,
            lambda female_names, male_names, female_relations, male_relations, ints: f"She also has a cow and a rooster. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]}'s ducks lay {ints[0] + ints[1] + ints[2]} eggs per day. {irrelevant_string}She eats {ints[1]} for breakfast every morning and bakes muffins for her friends every day with {ints[2]}. She sells the remainder at the farmers' market daily for ${ints[3]} per fresh duck egg. How much in dollars does she make every day at the farmers' market?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} sells {ints[0] + ints[1] + ints[2]} - {ints[1]} - {ints[2]} = <<{ints[0] + ints[1] + ints[2]}-{ints[1]}-{ints[2]}={ints[0]}>>{ints[0]} duck eggs a day. She makes {ints[0]} * 2 = $<<{ints[0]}*{ints[3]}={ints[0] * ints[3]}>>{ints[0] * ints[3]} every day at the farmer’s market. #### {ints[0] * ints[3]}"
        ),
        Problem(
            0,
            0,
            0,
            0,
            1,
            lambda female_names, male_names, female_relations, male_relations, ints: f"Red fiber costs twice as much as white fiber. ",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: f"A robe takes {ints[0] * 2} bolts of blue fiber and half that much white fiber. How many bolts in total does it take?",
            lambda female_names, male_names, female_relations, male_relations, ints: f"It takes {ints[0] * 2}/2=<<{ints[0] * 2}/2={ints[0]}>>{ints[0]} bolt of white fiber So the total amount of fabric is {ints[0] * 2}+{ints[0]}=<<{ints[0] * 2}+{ints[0]}={ints[0] * 3}>>{ints[0] * 3} bolts of fabric #### {ints[0] * 3}"
        ),
        Problem(
            num_female_names=0,
            num_male_names=1,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=3,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"He also bought a new car for his wife. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} decides to try flipping a house. He buys a house for ${ints[0] * 1000} and then puts in ${ints[1] * 1000} in repairs. "
                f"{irrelevant_string}This increased the value of the house by {ints[2]}%. How much profit did he make?"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"The cost of the house and repairs came out to {ints[0] * 1000}+{ints[1] * 1000}="
                f"$<<{ints[0] * 1000}+{ints[1] * 1000}={ (ints[0] + ints[1]) * 1000 }>>{ (ints[0] + ints[1]) * 1000 }. "
                f"He increased the value of the house by {ints[0] * 1000}*{ints[2]}/100="
                f"<<{ints[0] * 1000}*{ints[2]}/100={ ints[0] * 1000 * ints[2] / 100 }>>{ ints[0] * 1000 * ints[2] / 100 }. "
                f"So the new value of the house is {ints[0] * 1000}+{ ints[0] * 1000 * ints[2] / 100 }="
                f"$<<{ints[0] * 1000}+{ ints[0] * 1000 * ints[2] / 100 }={ ints[0] * 1000 + ints[0] * 1000 * ints[2] / 100 }>>"
                f"{ ints[0] * 1000 + ints[0] * 1000 * ints[2] / 100 }. "
                f"So he made a profit of { ints[0] * 1000 + ints[0] * 1000 * ints[2] / 100 }-{ (ints[0] + ints[1]) * 1000 }="
                f"$<<{ ints[0] * 1000 + ints[0] * 1000 * ints[2] / 100 }-{ (ints[0] + ints[1]) * 1000 }="
                f"{ ints[0] * 1000 + ints[0] * 1000 * ints[2] / 100 - (ints[0] + ints[1]) * 1000 }>>"
                f"{ ints[0] * 1000 + ints[0] * 1000 * ints[2] / 100 - (ints[0] + ints[1]) * 1000 } "
                f"#### { ints[0] * 1000 + ints[0] * 1000 * ints[2] / 100 - (ints[0] + ints[1]) * 1000 }"
            )
        ),
        Problem(
            num_female_names=0,
            num_male_names=1,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=3,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"He also does yoga on the weekends. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} decides to run {ints[0]} sprints {ints[1]} times a week. He runs {ints[2]} meters each sprint. "
                f"{irrelevant_string}How many total meters does he run a week?"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"He sprints {ints[0]}*{ints[1]}=<<{ints[0]}*{ints[1]}={ints[0] * ints[1]}>>{ints[0] * ints[1]} times. "
                f"So he runs {ints[0] * ints[1]}*{ints[2]}=<<{ints[0] * ints[1]}*{ints[2]}={ints[0] * ints[1] * ints[2]}>>{ints[0] * ints[1] * ints[2]} meters "
                f"#### {ints[0] * ints[1] * ints[2]}"
            )
        ),
        Problem(
            num_female_names=1,
            num_male_names=0,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=4,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"She also has a few ducks in her yard. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"Every day, {female_names[0]} feeds each of her chickens {ints[0]} cups of mixed chicken feed, containing seeds, mealworms, and vegetables "
                f"to help keep them healthy. She gives the chickens their feed in three separate meals. In the morning, she gives her flock of chickens "
                f"{ints[1]} cups of feed. In the afternoon, she gives her chickens another {ints[2]} cups of feed. "
                f"{irrelevant_string}How many cups of feed does she need to give her chickens in the final meal of the day if the size of {female_names[0]}'s flock is {ints[3]} chickens?"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"If each chicken eats {ints[0]} cups of feed per day, then for {ints[3]} chickens they would need {ints[0]}*{ints[3]}="
                f"<<{ints[0]}*{ints[3]}={ints[0] * ints[3]}>>{ints[0] * ints[3]} cups of feed per day. "
                f"If she feeds the flock {ints[1]} cups of feed in the morning, and {ints[2]} cups in the afternoon, then the final meal would require "
                f"{ints[0] * ints[3]}-{ints[1]}-{ints[2]}=<<{ints[0] * ints[3]}-{ints[1]}-{ints[2]}={ints[0] * ints[3] - ints[1] - ints[2]}>>"
                f"{ints[0] * ints[3] - ints[1] - ints[2]} cups of chicken feed. #### {ints[0] * ints[3] - ints[1] - ints[2]}"
            ),
            condition=lambda female_names, male_names, female_relations, male_relations, ints: ints[0] * ints[3] - ints[1] - ints[2] > 0
        ),
        Problem(
            num_female_names=0,
            num_male_names=1,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=3,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"He also considered buying some plates. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} went to the store to buy glasses for his new apartment. One glass costs ${ints[0]}, but every second glass costs only "
                f"{ints[1]}% of the price. {male_names[0]} wants to buy {ints[2] * 2} glasses. {irrelevant_string}How much does he need to pay for them?"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"The discount price of one glass is {ints[1]}/100 * {ints[0]} = $<<{ints[1]}/100*{ints[0]}={ints[1] / 100 * ints[0]}>>{ints[1] / 100 * ints[0]}. "
                f"If every second glass is cheaper, that means {male_names[0]} is going to buy {ints[2] * 2} / 2 = <<{ints[2] * 2}/2={ints[2]}>>{ints[2]} cheaper glasses. "
                f"So for the cheaper glasses, {male_names[0]} is going to pay {ints[2]} * {ints[1] / 100 * ints[0]} = $<<{ints[2]}*{ints[1] / 100 * ints[0]}="
                f"{(ints[2]) * (ints[1] / 100 * ints[0])}>>{(ints[2]) * (ints[1] / 100 * ints[0])}. "
                f"And for the regular-priced glasses, {male_names[0]} will pay {ints[2]} * {ints[0]} = $<<{ints[2]}*{ints[0]}="
                f"{(ints[2]) * ints[0]}>>{(ints[2]) * ints[0]}. "
                f"So in total {male_names[0]} needs to pay {(ints[2]) * (ints[1] / 100 * ints[0])} + {(ints[2]) * ints[0]} = "
                f"$<<{(ints[2]) * (ints[1] / 100 * ints[0])}+{(ints[2]) * ints[0]}="
                f"{(ints[2]) * (ints[1] / 100 * ints[0]) + (ints[2]) * ints[0]}>>"
                f"{(ints[2]) * (ints[1] / 100 * ints[0]) + (ints[2]) * ints[0]} for the glasses he wants to buy. "
                f"#### {(ints[2]) * (ints[1] / 100 * ints[0]) + (ints[2]) * ints[0]}"
            )
        ),
        Problem(
            num_female_names=0,
            num_male_names=3,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=2,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"They also each have several goats. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} has twice as many sheep as {male_names[1]}. {male_names[1]} has {ints[1]} times as many sheep as {male_names[2]}. "
                f"How many sheep do {male_names[0]}, {male_names[1]}, and {male_names[2]} have together if {male_names[2]} has {ints[0]} sheep? {irrelevant_string}"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"If {male_names[2]} has {ints[0]} sheep, {male_names[1]} has {ints[1]} * {ints[0]} sheep = "
                f"<<{ints[1]}*{ints[0]}={ints[1] * ints[0]}>>{ints[1] * ints[0]} sheep. "
                f"{male_names[0]} has twice as many sheep as {male_names[1]}, which is 2 * {ints[1] * ints[0]} sheep = "
                f"<<2*{ints[1] * ints[0]}={2 * ints[1] * ints[0]}>>{2 * ints[1] * ints[0]} sheep. "
                f"Together, they have {ints[0]} sheep + {2 * ints[1] * ints[0]} sheep + {ints[1] * ints[0]} sheep = "
                f"<<{ints[0]}+{2 * ints[1] * ints[0]}+{ints[1] * ints[0]}={ints[0] + 2 * ints[1] * ints[0] + ints[1] * ints[0]}>>"
                f"{ints[0] + 2 * ints[1] * ints[0] + ints[1] * ints[0]} sheep #### {ints[0] + 2 * ints[1] * ints[0] + ints[1] * ints[0]}"
            )
        ),
        Problem(
            num_female_names=1,
            num_male_names=0,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=4,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"She also considered downloading additional files later. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{female_names[0]} is downloading a {ints[0]} GB file. Normally she can download {ints[1]} GB/minute, "
                f"but {ints[2]}% of the way through the download, Windows forces a restart to install updates, which takes {ints[3]} minutes. "
                f"Then {female_names[0]} has to restart the download from the beginning. {irrelevant_string}How long does it take to download the file?"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"First, find how many gigabytes are in {ints[2]}% of the file: {ints[0]} GB * {ints[2]}% = "
                f"<<{ints[0]}*{ints[2]}*.01={ints[0] * ints[2] * 0.01}>>{ints[0] * ints[2] * 0.01} GB. "
                f"Then divide that number by the download rate to find the time until Windows restarts: "
                f"{ints[0] * ints[2] * 0.01} GB / {ints[1]} GB/minute = <<{ints[0] * ints[2] * 0.01}/{ints[1]}="
                f"{(ints[0] * ints[2] * 0.01) / ints[1]}>>{(ints[0] * ints[2] * 0.01) / ints[1]} minutes. "
                f"Then find the time to download the whole file after the restart: {ints[0]} GB / {ints[1]} GB/minute = "
                f"<<{ints[0]}/{ints[1]}={ints[0] / ints[1]}>>{ints[0] / ints[1]} minutes. "
                f"Then add the time to download {ints[2]}% of the file, to download the whole file, and to wait for Windows to update: "
                f"{(ints[0] * ints[2] * 0.01) / ints[1]} minutes + {ints[0] / ints[1]} minutes + {ints[3]} minutes = "
                f"<<{(ints[0] * ints[2] * 0.01) / ints[1]}+{ints[0] / ints[1]}+{ints[3]}="
                f"{(ints[0] * ints[2] * 0.01) / ints[1] + ints[0] / ints[1] + ints[3]}>>"
                f"{(ints[0] * ints[2] * 0.01) / ints[1] + ints[0] / ints[1] + ints[3]} minutes "
                f"#### {(ints[0] * ints[2] * 0.01) / ints[1] + ints[0] / ints[1] + ints[3]}"
            )
        ),
        Problem(
            num_female_names=1,
            num_male_names=0,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=3,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"She sometimes works extra shifts on weekends. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{female_names[0]}'s rate per hour for the first {ints[0]} hours she works each week is ${ints[1]}. "
                f"She also receives an overtime pay of {ints[2]} times her regular hourly rate. If {female_names[0]} worked for {ints[0] + 5} hours this week, "
                f"how much are her earnings for this week? {irrelevant_string}"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{female_names[0]} is entitled to {ints[0] + 5} - {ints[0]} = <<{ints[0] + 5}-{ints[0]}=5>>5 hours of overtime pay. "
                f"Her hourly rate for the overtime pay is ${ints[1]} x {ints[2]} = $<<{ints[1]}*{ints[2]}={ints[1] * ints[2]}>>{ints[1] * ints[2]}. "
                f"So, {female_names[0]} will receive ${ints[1] * ints[2]} x 5 = $<<{ints[1] * ints[2]}*5={ints[1] * ints[2] * 5}>>{ints[1] * ints[2] * 5} for overtime pay. "
                f"Her regular weekly earning is ${ints[1]} x {ints[0]} = $<<{ints[1]}*{ints[0]}={ints[1] * ints[0]}>>{ints[1] * ints[0]}. "
                f"Thus, {female_names[0]} will receive a total of ${ints[1] * ints[0]} + ${ints[1] * ints[2] * 5} = "
                f"$<<{ints[1] * ints[0]}+{ints[1] * ints[2] * 5}={ints[1] * ints[0] + ints[1] * ints[2] * 5}>>{ints[1] * ints[0] + ints[1] * ints[2] * 5} for this week's work. "
                f"#### {ints[1] * ints[0] + ints[1] * ints[2] * 5}"
            ),
            condition=lambda female_names, male_names, female_relations, male_relations, ints: ints[0] > 0 and ints[1] > 0 and ints[2] > 1,
            modification=None
        ),
        Problem(
            num_female_names=0,
            num_male_names=0,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=3,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"It was highly recommended on tech blogs. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"A new program had {ints[0]} downloads in the first month. The number of downloads in the second month was "
                f"{ints[1]} times as many as the downloads in the first month, but then reduced by {ints[2]}% in the third month. "
                f"How many downloads did the program have total over the three months? {irrelevant_string}"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"The number of downloads of the program in the second month increased to {ints[1]} * {ints[0]} = "
                f"<<{ints[1]}*{ints[0]}={ints[1] * ints[0]}>>{ints[1] * ints[0]}. "
                f"In the first two months, the total number of downloads of the program was {ints[1] * ints[0]} + {ints[0]} = "
                f"<<{ints[1] * ints[0]}+{ints[0]}={ints[1] * ints[0] + ints[0]}>>{ints[1] * ints[0] + ints[0]}. "
                f"In the third month, the number of downloads of the program reduced by {ints[2]}/100 * {ints[1] * ints[0]} = "
                f"<<{ints[2]}/100*{ints[1] * ints[0]}={ints[2] / 100 * ints[1] * ints[0]}>>{ints[2] / 100 * ints[1] * ints[0]}. "
                f"There were {ints[1] * ints[0]} - {ints[2] / 100 * ints[1] * ints[0]} = "
                f"<<{ints[1] * ints[0]}-{ints[2] / 100 * ints[1] * ints[0]}={ints[1] * ints[0] - ints[2] / 100 * ints[1] * ints[0]}>>"
                f"{ints[1] * ints[0] - ints[2] / 100 * ints[1] * ints[0]} downloads in the third month. "
                f"In the three months, the total number of downloads of the program was "
                f"{ints[1] * ints[0] - ints[2] / 100 * ints[1] * ints[0]} + {ints[1] * ints[0] + ints[0]} = "
                f"<<{ints[1] * ints[0] - ints[2] / 100 * ints[1] * ints[0]}+{ints[1] * ints[0] + ints[0]}="
                f"{ints[1] * ints[0] - ints[2] / 100 * ints[1] * ints[0] + ints[1] * ints[0] + ints[0]}>>"
                f"{ints[1] * ints[0] - ints[2] / 100 * ints[1] * ints[0] + ints[1] * ints[0] + ints[0]} downloads "
                f"#### {ints[1] * ints[0] - ints[2] / 100 * ints[1] * ints[0] + ints[1] * ints[0] + ints[0]}"
            )
        ),
        Problem(
            num_female_names=1,
            num_male_names=0,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=6,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"{female_names[0]} recently got a raise at her job. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{female_names[0]} went to the bakery and bought various types of pastries.  {irrelevant_string}She bought {ints[0]} dozen donuts which cost ${ints[1]} per dozen, "
                f"{ints[2]} dozen mini cupcakes which cost ${ints[3]} per dozen, and {ints[4]} dozen mini cheesecakes for ${ints[5]} per dozen. "
                f"How much was the total cost?"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"The total charge for the donuts was {ints[0]} x ${ints[1]} = $<<{ints[0]}*{ints[1]}={ints[0] * ints[1]}>>{ints[0] * ints[1]}. "
                f"The total charge for the mini cupcakes was {ints[2]} x ${ints[3]} = $<<{ints[2]}*{ints[3]}={ints[2] * ints[3]}>>{ints[2] * ints[3]}. "
                f"The total charge for the mini cheesecakes was {ints[4]} x ${ints[5]} = $<<{ints[4]}*{ints[5]}={ints[4] * ints[5]}>>{ints[4] * ints[5]}. "
                f"Therefore the total amount {female_names[0]} paid for the pastries was {ints[0] * ints[1]} + {ints[2] * ints[3]} + {ints[4] * ints[5]} = "
                f"$<<{ints[0] * ints[1]}+{ints[2] * ints[3]}+{ints[4] * ints[5]}="
                f"{ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5]}>>{ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5]}. "
                f"#### {ints[0] * ints[1] + ints[2] * ints[3] + ints[4] * ints[5]}"
            )
        ),
        Problem(
            num_female_names=0,
            num_male_names=1,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=4,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"He is also considering investing in real estate next month. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"A merchant wants to make a choice of purchase between 2 purchase plans: jewelry worth ${ints[0]} or electronic gadgets worth ${ints[1]}.  {irrelevant_string}"
                f"His financial advisor speculates that the jewelry market will go up {ints[2]}% while the electronic gadgets market will rise {ints[3]}% within the same month. "
                f"If the merchant is looking to maximize profit at the end of this month by making a choice, how much profit would this be?"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"If he purchases jewelry, he will make a profit of {ints[2]}% which is ${ints[0]}*({ints[2]}/100) = "
                f"$<<{ints[0]}*({ints[2]}/100)={ints[0] * (ints[2] / 100)}>>{ints[0] * (ints[2] / 100)}. "
                f"If he purchases electronic gadgets, he will make a profit of {ints[3]}% which is ${ints[1]}*({ints[3]}/100) = "
                f"$<<{ints[1]}*({ints[3]}/100)={ints[1] * (ints[3] / 100)}>>{ints[1] * (ints[3] / 100)}. "
                f"If he wants to maximize profit, since ${ints[0] * (ints[2] / 100)} > ${ints[1] * (ints[3] / 100)}, he will choose to purchase jewelry, "
                f"thereby making a profit of $<<{ints[0] * (ints[2] / 100)}={ints[0] * (ints[2] / 100)}>>{ints[0] * (ints[2] / 100)}. "
                f"#### {ints[0] * (ints[2] / 100)}"
            )
        ),
        Problem(
            num_female_names=1,
            num_male_names=0,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=5,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"She also volunteers on weekends. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{female_names[0]} gets paid ${ints[0]} per hour to teach and ${ints[1]} to be a cheerleading coach. {irrelevant_string}"
                f"If she works {ints[2]} weeks a year, {ints[3]} hours a week as a teacher and {ints[4]} hours a week as a coach, "
                f"what's her annual salary?"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"First, find the total amount {female_names[0]} makes per week teaching: ${ints[0]}/hour * {ints[3]} hours/week = "
                f"$<<{ints[0]}*{ints[3]}={ints[0] * ints[3]}>>{ints[0] * ints[3]}/week. "
                f"Then find the total amount {female_names[0]} makes per week coaching: ${ints[1]}/hour * {ints[4]} hours/week = "
                f"$<<{ints[1]}*{ints[4]}={ints[1] * ints[4]}>>{ints[1] * ints[4]}/week. "
                f"Then add those two amounts to find the total amount {female_names[0]} makes per week: "
                f"${ints[0] * ints[3]}/week + ${ints[1] * ints[4]}/week = "
                f"$<<{ints[0] * ints[3]}+{ints[1] * ints[4]}={ints[0] * ints[3] + ints[1] * ints[4]}>>{ints[0] * ints[3] + ints[1] * ints[4]}/week. "
                f"Then multiply that number by the number of weeks {female_names[0]} works in a year to find her annual salary: "
                f"${ints[0] * ints[3] + ints[1] * ints[4]}/week * {ints[2]} weeks/year = "
                f"$<<{ints[0] * ints[3] + ints[1] * ints[4]}*{ints[2]}={ (ints[0] * ints[3] + ints[1] * ints[4]) * ints[2] }>>"
                f"{ (ints[0] * ints[3] + ints[1] * ints[4]) * ints[2] } #### { (ints[0] * ints[3] + ints[1] * ints[4]) * ints[2] }"
            )
        ),
        Problem(
            num_female_names=1,
            num_male_names=0,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=2,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"In addition to her breakfast, she has a morning exercise routine. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{female_names[0]} makes a {ints[0]} egg omelet every morning for breakfast. {irrelevant_string}"
                f"How many dozens of eggs will she eat in {ints[1]} weeks?"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"She eats {ints[0]} eggs every day and there are 7 days in a week, so she eats {ints[0]}*7 = "
                f"<<{ints[0]}*7={ints[0] * 7}>>{ints[0] * 7} eggs a week. "
                f"After {ints[1]} weeks, she will have eaten {ints[1]}*{ints[0] * 7} = "
                f"<<{ints[1]}*{ints[0] * 7}={ints[1] * ints[0] * 7}>>{ints[1] * ints[0] * 7} eggs. "
                f"There are 12 eggs in 1 dozen, so she'll eat {ints[1] * ints[0] * 7}/12 = "
                f"<<{ints[1] * ints[0] * 7}/12={ints[1] * ints[0] * 7 / 12}>>{ints[1] * ints[0] * 7 / 12} dozen eggs "
                f"#### {ints[1] * ints[0] * 7 / 12}"
            )
        ),
        Problem(
            num_female_names=0,
            num_male_names=1,
            num_female_relations=0,
            num_male_relations=0,
            num_ints=4,
            irrelevant_string_generator=lambda female_names, male_names, female_relations, male_relations, ints: f"He also sells Blu-ray discs occasionally. ",
            question_generator=lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} sells DVDs. He has {ints[0]+ints[1]+ints[2]} customers on Tuesday. His first {ints[1]} customers buy one DVD each. "
                f"{irrelevant_string}His next {ints[2]} customers buy {ints[3]} DVDs each. His last {ints[0]} customers don't buy any DVDs. "
                f"How many DVDs did {male_names[0]} sell on Tuesday?"
            ),
            answer_generator=lambda female_names, male_names, female_relations, male_relations, ints: (
                f"His first {ints[1]} customers buy {ints[1]} * 1 = <<{ints[1]}*1={ints[1] * 1}>>{ints[1] * 1} DVDs. "
                f"His next {ints[2]} customers buy {ints[2]} * {ints[3]} = <<{ints[2]}*{ints[3]}={ints[2] * ints[3]}>>{ints[2] * ints[3]} DVDs. "
                f"He sells a total of {ints[1] * 1} + {ints[2] * ints[3]} + 0 = "
                f"<<{ints[1] * 1}+{ints[2] * ints[3]}+0={ints[1] * 1 + ints[2] * ints[3] + 0}>>{ints[1] * 1 + ints[2] * ints[3] + 0} DVDs. "
                f"#### {ints[1] * 1 + ints[2] * ints[3] + 0}"
            )
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
