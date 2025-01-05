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
            0,
            0,
            0,
            0,
            3,  # Using 3 integers to represent the three groups of customers
            lambda female_names, male_names, female_relations, male_relations, ints: (
                "It was a busy day at the pet store, and customers were eager to buy cat food on sale!"
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"There was a big sale on cat food at the pet store. {ints[0] + ints[1] + ints[2]} people bought cat food that day. "
                f"The first {ints[0]} customers bought 3 cases each. The next {ints[1]} customers bought 2 cases each. "
                f"The last {ints[2]} customers of the day only bought 1 case each. How many cases of cat food were sold?"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"The first {ints[0]} customers bought {ints[0]}*3=<<{ints[0]}*3={ints[0]*3}>>{ints[0]*3} cases. "
                f"The next {ints[1]} customers bought {ints[1]}*2=<<{ints[1]}*2={ints[1]*2}>>{ints[1]*2} cases. "
                f"The last {ints[2]} customers bought {ints[2]}*1=<<{ints[2]}*1={ints[2]}>>{ints[2]} cases. "
                f"In total, {ints[0]*3}+{ints[1]*2}+{ints[2]}=<<{ints[0]*3}+{ints[1]*2}+{ints[2]}="
                f"{ints[0]*3 + ints[1]*2 + ints[2]}>>{ints[0]*3 + ints[1]*2 + ints[2]} cases were sold #### {ints[0]*3 + ints[1]*2 + ints[2]}"
            ),
        ),
        Problem(
            0,
            1,
            0,
            0,
            3,  # 3 integers for the prices of model cars, paint bottles, and paintbrushes
            lambda female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} is excited about his new hobby collection!",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} bought 5 model cars that cost ${ints[0]} each and 5 bottles of paint that cost ${ints[1]} each. "
                f"He also bought 5 paintbrushes that cost ${ints[2]} each. How much did {male_names[0]} spend in total?"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"The 5 model cars cost ${ints[0]} x 5 = $<<{ints[0]}*5={ints[0]*5}>>{ints[0]*5}. "
                f"The 5 bottles of paint cost ${ints[1]} x 5 = $<<{ints[1]}*5={ints[1]*5}>>{ints[1]*5}. "
                f"The 5 paintbrushes cost ${ints[2]} x 5 = $<<{ints[2]}*5={ints[2]*5}>>{ints[2]*5}. "
                f"Thus, {male_names[0]} spent ${ints[0]*5} + ${ints[1]*5} + ${ints[2]*5} = "
                f"$<<{ints[0]*5}+{ints[1]*5}+{ints[2]*5}={ints[0]*5 + ints[1]*5 + ints[2]*5}>>{ints[0]*5 + ints[1]*5 + ints[2]*5} in total. "
                f"#### {ints[0]*5 + ints[1]*5 + ints[2]*5}"
            ),
        ),
        Problem(
            0,
            1,  # 1 male name for Ravi
            0,
            0,
            4,  # 3 integers for jump heights and 1 for the multiplier
            lambda female_names, male_names, female_relations, male_relations, ints: f"{male_names[0]} is known for his impressive jumping skills!",
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} can jump higher than anyone in the class. In fact, he can jump {ints[3]} times higher than the "
                f"average jump of the three next highest jumpers. If the three next highest jumpers can jump {ints[0]} inches, "
                f"{ints[1]} inches, and {ints[2]} inches, how high can {male_names[0]} jump?"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"The total height the next three highest can jump is {ints[0]} + {ints[1]} + {ints[2]} = "
                f"<<{ints[0]}+{ints[1]}+{ints[2]}={ints[0]+ints[1]+ints[2]}>>{ints[0]+ints[1]+ints[2]} inches. "
                f"The average height they can jump is {ints[0]+ints[1]+ints[2]} / 3 = <<{ints[0]+ints[1]+ints[2]}/3="
                f"{(ints[0]+ints[1]+ints[2])/3}>>{(ints[0]+ints[1]+ints[2])/3} inches. "
                f"{male_names[0]} can jump {(ints[0]+ints[1]+ints[2])/3} x {ints[3]} = "
                f"<<{(ints[0]+ints[1]+ints[2])/3}*{ints[3]}={(ints[0]+ints[1]+ints[2])/3 * ints[3]}>>{(ints[0]+ints[1]+ints[2])/3 * ints[3]} inches high. "
                f"#### {(ints[0]+ints[1]+ints[2])/3 * ints[3]}"
            ),
        ),
        Problem(
            1,  # 1 female name for Jean
            0,
            0,
            1,  # 1 male relation to represent "friends" in a general sense
            1,  # 1 integer for the base number, which we multiply by 4 to ensure divisibility
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"Everyone is excited to play a classic game!"
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{female_names[0]} and her three {male_relations[0]} are playing a game of dominoes. "
                f"There are {ints[0] * 4} dominoes in the set, and {female_names[0]} wants each player to receive "
                f"the same number of dominoes. {irrelevant_string} How many dominoes will {female_names[0]} and her {male_relations[0]} each receive?"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"There are 1 + 3 = <<1+3=4>>4 of them playing games of dominoes. "
                f"Thus, each of them will receive {ints[0] * 4}/4 = <<{ints[0] * 4}/4={ints[0]}>>{ints[0]} dominoes. #### {ints[0]}"
            ),
        ),
        Problem(
            0,  # No female names needed
            1,  # 1 male name for Dylan
            1,  # 1 female relation (mother)
            1,  # 1 male relation (father/husband)
            2,  # 2 integers: one for the number of guest cars, and another for the number of wheels per car
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]}'s {female_relations[0]} is organizing a big celebration!"
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]}'s {female_relations[0]} is throwing a baby shower for her best friend. "
                f"She is expecting 40 guests, of whom she has cleared the parking lot to park in, leaving only her car "
                f"and her {male_relations[0]}'s jeep in the parking lot. The 40 guests, though, arrive in only {ints[0]} cars "
                f"that they park in the parking lot. If each car has {ints[1]} wheels, how many car wheels are there in the parking lot, "
                f"including both of {male_names[0]}'s parent's car wheels? {irrelevant_string}"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{ints[0]} cars are parked around for the party, {ints[0]} x {ints[1]} wheels each car = <<{ints[0]}*{ints[1]}="
                f"{ints[0] * ints[1]}>>{ints[0] * ints[1]} wheels total. {male_names[0]}'s parents both have a car with "
                f"{ints[1]} wheels each, 2 x {ints[1]} = <<2*{ints[1]}={2 * ints[1]}>>{2 * ints[1]} more wheels. "
                f"Combined, there are {ints[0] * ints[1]} + {2 * ints[1]} = <<{ints[0] * ints[1]}+{2 * ints[1]}="
                f"{ints[0] * ints[1] + 2 * ints[1]}>>{ints[0] * ints[1] + 2 * ints[1]} wheels total on the {male_names[0]} family property. "
                f"#### {ints[0] * ints[1] + 2 * ints[1]}"
            ),
        ),
        Problem(
            0,
            1,
            0,
            1,
            2,
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} wanted to treat his parents to a memorable art exhibit!"
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} bought art exhibit tickets for his parents and himself. Tickets were ${ints[0]} per person. "
                f"He was also charged an ${ints[1]} service fee for the online transaction. What is the total amount he paid for the tickets? "
                f"{irrelevant_string}"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"Tickets for {male_names[0]} and his parents cost ${ints[0]} x 3 = $<<{ints[0]}*3={ints[0] * 3}>>{ints[0] * 3}. "
                f"Tickets and service charge cost ${ints[0] * 3} + ${ints[1]} = $<<{ints[0] * 3}+{ints[1]}={ints[0] * 3 + ints[1]}>>"
                f"{ints[0] * 3 + ints[1]}. #### {ints[0] * 3 + ints[1]}"
            ),
        ),
        Problem(
            3,  # 3 female names (e.g., Ia, Sophia, etc.)
            1,  # 1 male name (e.g., Mateo)
            1,  # 1 female relation (for "mother")
            0,
            4,  # 4 integers: three for the number of photos each person brings and one for additional slots
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"The siblings are excited to surprise their {female_relations[0]} with a thoughtful gift!"
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{female_names[0]}, {male_names[0]}, and {female_names[2]} are preparing a photo album for their {female_relations[0]}. "
                f"{irrelevant_string} {female_names[0]} brings {ints[0]} photos, {male_names[0]} brings {ints[1]} photos, and "
                f"{female_names[2]} brings {ints[2]} photos. If the photo album has {ints[0] + ints[1] + ints[2] + ints[3]} slots available, "
                f"how many photos does {female_names[1]} need to bring to complete the photo album?"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"Excluding {female_names[1]}, there are {ints[0]} + {ints[1]} + {ints[2]} = "
                f"<<{ints[0]}+{ints[1]}+{ints[2]}={ints[0] + ints[1] + ints[2]}>>{ints[0] + ints[1] + ints[2]} photos. "
                f"{female_names[1]} needs to bring {(ints[0] + ints[1] + ints[2] + ints[3])} – {ints[0] + ints[1] + ints[2]} = "
                f"<<{ints[0] + ints[1] + ints[2] + ints[3]}-{ints[0] + ints[1] + ints[2]}="
                f"{(ints[0] + ints[1] + ints[2] + ints[3]) - (ints[0] + ints[1] + ints[2])}>>"
                f"{(ints[0] + ints[1] + ints[2] + ints[3]) - (ints[0] + ints[1] + ints[2])} photos to complete the album. "
                f"#### {(ints[0] + ints[1] + ints[2] + ints[3]) - (ints[0] + ints[1] + ints[2])}"
            ),
        ),
        Problem(
            0,
            3,
            0,
            0,
            3,  # 3 integers: hours for Jacob, Greg’s adjustment, and Patrick’s adjustment
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]}, {male_names[1]}, and {male_names[2]} are all busy with their homework assignments!"
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[2]} has {ints[0]} hours left to finish his homework. "
                f"{male_names[1]} has {ints[0]} - {ints[1]} hours left to finish his homework, while "
                f"{male_names[0]} has {ints[2]} hours less than twice the time that {male_names[1]} has left. "
                f"How many hours do they all have left to finish their homework? {irrelevant_string}"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"If {male_names[2]} has {ints[0]} hours left to finish his homework, "
                f"{male_names[1]} has {ints[0]} - {ints[1]} = <<{ints[0]}-{ints[1]}={ints[0] - ints[1]}>>"
                f"{ints[0] - ints[1]} hours left to finish his homework. The total number of hours {male_names[2]} and {male_names[1]} "
                f"have left to finish their homework is {ints[0] - ints[1]} + {ints[0]} = <<{ints[0] - ints[1]}+{ints[0]}="
                f"{(ints[0] - ints[1]) + ints[0]}>>{(ints[0] - ints[1]) + ints[0]} hours. "
                f"{male_names[0]} has {ints[2]} hours less than twice the time {male_names[1]} has, meaning {male_names[0]} has "
                f"{ints[2]} hours less than {ints[0] - ints[1]} * 2 = <<{ints[0] - ints[1]}*2={2 * (ints[0] - ints[1])}>>"
                f"{2 * (ints[0] - ints[1])} hours left. "
                f"{male_names[0]} has {2 * (ints[0] - ints[1])} - {ints[2]} = <<{2 * (ints[0] - ints[1])}-{ints[2]}="
                f"{(2 * (ints[0] - ints[1])) - ints[2]}>>{(2 * (ints[0] - ints[1])) - ints[2]} hours left to finish his homework. "
                f"Altogether, they have {(ints[0] - ints[1]) + ints[0]} + {(2 * (ints[0] - ints[1])) - ints[2]} = "
                f"<<{(ints[0] - ints[1]) + ints[0]}+{(2 * (ints[0] - ints[1])) - ints[2]}="
                f"{(ints[0] - ints[1]) + ints[0] + (2 * (ints[0] - ints[1]) - ints[2])}>>"
                f"{(ints[0] - ints[1]) + ints[0] + (2 * (ints[0] - ints[1]) - ints[2])} hours left. #### "
                f"{(ints[0] - ints[1]) + ints[0] + (2 * (ints[0] - ints[1]) - ints[2])}"
            ),
        ),
        Problem(
            0,
            1,
            0,
            0,
            3,  # 3 integers: envelopes under 5 pounds, stamps per heavy envelope, additional stamps for positivity
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} was thinking of sending letters to many different countries, so he bought stamps in bulk."
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} bought envelopes to send, and depending on the weight of the envelope, he will need more stamps. "
                f"If an envelope weighs more than 5 pounds, he will need {ints[2]} stamps. If it weighs less than that, it will only need 2 stamps. "
                f"If he bought {(ints[1] * 2) + (ints[2] * 5)} stamps with {ints[1]} envelopes that weigh less than 5 pounds, "
                f"how many envelopes in total did {male_names[0]} need to buy? {irrelevant_string}"
            ),
            lambda female_names, male_names, male_relations, female_relations, ints: (
                f"{male_names[0]} had to buy {ints[1]} * 2 = <<{ints[1]}*2={ints[1] * 2}>>{ints[1] * 2} stamps for {ints[1]} envelopes less than 5 pounds. "
                f"He has {(ints[1] * 2) + (ints[2] * 5)} - {ints[1] * 2} = <<{(ints[1] * 2) + (ints[2] * 5)}-{ints[1] * 2}="
                f"{(ints[1] * 2) + (ints[2] * 5) - (ints[1] * 2)}>>{(ints[1] * 2) + (ints[2] * 5) - (ints[1] * 2)} more stamps available. "
                f"There are {(ints[1] * 2) + (ints[2] * 5) - (ints[1] * 2)} / {ints[2]} = "
                f"<<{(ints[1] * 2) + (ints[2] * 5) - (ints[1] * 2)}/{ints[2]}="
                f"{((ints[1] * 2) + (ints[2] * 5) - (ints[1] * 2)) // ints[2]}>>{((ints[1] * 2) + (ints[2] * 5) - (ints[1] * 2)) // ints[2]} envelopes that weigh more than 5 pounds. "
                f"{male_names[0]} needed to buy {((ints[1] * 2) + (ints[2] * 5) - (ints[1] * 2)) // ints[2]} + {ints[1]} = "
                f"<<{((ints[1] * 2) + (ints[2] * 5) - (ints[1] * 2)) // ints[2]}+{ints[1]}="
                f"{((ints[1] * 2) + (ints[2] * 5) - (ints[1] * 2)) // ints[2] + ints[1]}>>"
                f"{((ints[1] * 2) + (ints[2] * 5) - (ints[1] * 2)) // ints[2] + ints[1]} envelopes in total. "
                f"#### {((ints[1] * 2) + (ints[2] * 5) - (ints[1] * 2)) // ints[2] + ints[1]}"
            ),
        ),
        Problem(
            0,
            1,
            0,
            0,
            5,
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} has been experimenting with his water buckets to see how much he can fit into larger containers!"
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} has 5 buckets of water. One contains {ints[0]} ounces, one contains {ints[1]} ounces, one contains {ints[2]} ounces, "
                f"one contains {ints[3]} ounces, and one contains {ints[4]} ounces. He pours the {ints[4]}-ounce bucket into a bigger bucket, "
                f"along with one of the other four. The total in the bigger bucket is now {ints[4] + ints[1]} ounces. "
                f"He pours the remaining three buckets into a second large bucket. How many ounces does the second large bucket contain? "
                f"{irrelevant_string}"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} poured the {ints[1]}-ounce bucket into the first large bucket because {ints[4] + ints[1]} - {ints[4]} = "
                f"<<{ints[4] + ints[1]}-{ints[4]}={ints[1]}>>{ints[1]}. The remaining buckets are thus the {ints[0]}, {ints[2]}, and {ints[3]} ounce buckets. "
                f"The second large bucket contains {ints[0]} + {ints[2]} + {ints[3]} = "
                f"<<{ints[0]}+{ints[2]}+{ints[3]}={ints[0] + ints[2] + ints[3]}>>{ints[0] + ints[2] + ints[3]} ounces. #### {ints[0] + ints[2] + ints[3]}"
            ),
        ),
        Problem(
            0,
            1,
            0,
            0,
            4,  # 4 integers: apples eaten per child, apples sold, adjusted total apples left, and apples per bag
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"The farmer was known for his generous apple trees that bore plenty of apples each season."
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"A farmer living in the countryside has a certain number of children. One day, they followed him to the farm, "
                f"each one with a bag to collect harvested apples. At the end of the day, each bag was filled with {ints[3]} apples. "
                f"On their way back home, 2 of the children have eaten {ints[0]} apples each, and another child sold {ints[1]} of his apples. "
                f"If they had a total of {ints[2] + (ints[3] - ((2 * ints[0] + ints[1] + ints[2]) % ints[3]))} apples left by the time they got home, "
                f"how many children does the farmer have? {irrelevant_string}"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"2 children ate {ints[0]} apples each, which gives 2 * {ints[0]} = <<2*{ints[0]}={2 * ints[0]}>>{2 * ints[0]} apples. "
                f"Another child gave out an additional {ints[1]} apples, making {2 * ints[0]} + {ints[1]} = "
                f"<<{2 * ints[0]}+{ints[1]}={2 * ints[0] + ints[1]}>>{2 * ints[0] + ints[1]} apples removed from the total. "
                f"There were {ints[2] + (ints[3] - ((2 * ints[0] + ints[1] + ints[2]) % ints[3]))} apples left after these, so the original total must have been "
                f"{2 * ints[0] + ints[1]} + {ints[2] + (ints[3] - ((2 * ints[0] + ints[1] + ints[2]) % ints[3]))} = "
                f"<<{2 * ints[0] + ints[1]}+{ints[2] + (ints[3] - ((2 * ints[0] + ints[1] + ints[2]) % ints[3]))}="
                f"{(2 * ints[0] + ints[1]) + (ints[2] + (ints[3] - ((2 * ints[0] + ints[1] + ints[2]) % ints[3])))}>>"
                f"{(2 * ints[0] + ints[1]) + (ints[2] + (ints[3] - ((2 * ints[0] + ints[1] + ints[2]) % ints[3])))} apples. "
                f"Each child collected {ints[3]} apples, so there are {(2 * ints[0] + ints[1]) + (ints[2] + (ints[3] - ((2 * ints[0] + ints[1] + ints[2]) % ints[3])))} / {ints[3]} = "
                f"<<{(2 * ints[0] + ints[1]) + (ints[2] + (ints[3] - ((2 * ints[0] + ints[1] + ints[2]) % ints[3])))}/{ints[3]}="
                f"{((2 * ints[0] + ints[1]) + (ints[2] + (ints[3] - ((2 * ints[0] + ints[1] + ints[2]) % ints[3])))) // ints[3]}>>"
                f"{((2 * ints[0] + ints[1]) + (ints[2] + (ints[3] - ((2 * ints[0] + ints[1] + ints[2]) % ints[3])))) // ints[3]} children. "
                f"#### {((2 * ints[0] + ints[1]) + (ints[2] + (ints[3] - ((2 * ints[0] + ints[1] + ints[2]) % ints[3])))) // ints[3]}"
            ),
        ),
        Problem(
            0,
            1,
            0,
            0,
            4,  # 4 integers: side length of the cube, density of gold, cost per gram, and sale multiplier
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} recently got into gold trading and is interested in calculating potential profits."
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} constructs a cube of pure gold. The cube is {ints[0]} cm on each side. "
                f"The density of gold is {ints[1]} grams per cubic centimeter. He buys the gold for ${ints[2]} per gram. "
                f"He sells it for {ints[3]} times its gold value. What was the profit? {irrelevant_string}"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"The cube is {ints[0]}*{ints[0]}*{ints[0]}=<<{ints[0]}*{ints[0]}*{ints[0]}={ints[0]**3}>>{ints[0]**3} cubic cm. "
                f"So it has a mass of {ints[0]**3}*{ints[1]}=<<{ints[0]**3}*{ints[1]}={ints[0]**3 * ints[1]}>>{ints[0]**3 * ints[1]} grams. "
                f"Buying this amount of gold costs ${ints[2]}*{ints[0]**3 * ints[1]}=<<{ints[2]}*{ints[0]**3 * ints[1]}={ints[2] * ints[0]**3 * ints[1]}>>{ints[2] * ints[0]**3 * ints[1]}. "
                f"That means he sells it for {ints[2] * ints[0]**3 * ints[1]}*{ints[3]}=<<{ints[2] * ints[0]**3 * ints[1]}*{ints[3]}={ints[2] * ints[0]**3 * ints[1] * ints[3]}>>{ints[2] * ints[0]**3 * ints[1] * ints[3]}. "
                f"So he has a profit of {ints[2] * ints[0]**3 * ints[1] * ints[3]}-{ints[2] * ints[0]**3 * ints[1]}="
                f"<<{ints[2] * ints[0]**3 * ints[1] * ints[3]}-{ints[2] * ints[0]**3 * ints[1]}={ints[2] * ints[0]**3 * ints[1] * (ints[3] - 1)}>>"
                f"{ints[2] * ints[0]**3 * ints[1] * (ints[3] - 1)}. #### {ints[2] * ints[0]**3 * ints[1] * (ints[3] - 1)}"
            ),
        ),
        Problem(
            0,
            1,
            0,
            0,
            3,  # 3 integers: initial score, points reduced on the second try, and multiplier for the third try
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} loves playing Candy Crush and keeps track of his points to see his improvement."
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} scored {ints[0]} points on the first try in a Candy Crush game, "
                f"{min(ints[1], ints[0] - 1)} points fewer on the second try, "
                f"and {ints[2]} times the number of points he scored on the second try on the third try. "
                f"What's the total number of points that he scored in all tries? {irrelevant_string}"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"If {male_names[0]} scored {ints[0]} points on the first try, he scored {ints[0]}-{min(ints[1], ints[0] - 1)} = "
                f"<<{ints[0]}-{min(ints[1], ints[0] - 1)}={ints[0] - min(ints[1], ints[0] - 1)}>>{ints[0] - min(ints[1], ints[0] - 1)} points on the second try. "
                f"The total number of points that {male_names[0]} scored after two tries is {ints[0]}+{ints[0] - min(ints[1], ints[0] - 1)} = "
                f"<<{ints[0]}+{ints[0] - min(ints[1], ints[0] - 1)}={ints[0] + (ints[0] - min(ints[1], ints[0] - 1))}>>"
                f"{ints[0] + (ints[0] - min(ints[1], ints[0] - 1))}. "
                f"On the third try, {male_names[0]} scored {ints[2]} times the points scored on the second try, which is "
                f"{ints[2]}*{ints[0] - min(ints[1], ints[0] - 1)} = "
                f"<<{ints[2]}*{ints[0] - min(ints[1], ints[0] - 1)}={ints[2] * (ints[0] - min(ints[1], ints[0] - 1))}>>"
                f"{ints[2] * (ints[0] - min(ints[1], ints[0] - 1))} points. "
                f"In all the tries of the game, {male_names[0]} scored "
                f"{ints[2] * (ints[0] - min(ints[1], ints[0] - 1))}+{ints[0] + (ints[0] - min(ints[1], ints[0] - 1))} = "
                f"<<{ints[2] * (ints[0] - min(ints[1], ints[0] - 1))}+{ints[0] + (ints[0] - min(ints[1], ints[0] - 1))}="
                f"{ints[2] * (ints[0] - min(ints[1], ints[0] - 1)) + (ints[0] + (ints[0] - min(ints[1], ints[0] - 1)))}>>"
                f"{ints[2] * (ints[0] - min(ints[1], ints[0] - 1)) + (ints[0] + (ints[0] - min(ints[1], ints[0] - 1)))} points. "
                f"#### {ints[2] * (ints[0] - min(ints[1], ints[0] - 1)) + (ints[0] + (ints[0] - min(ints[1], ints[0] - 1)))}"
            ),
        ),
        Problem(
            0,
            1,
            0,
            0,
            4,  # 4 integers: initial lifting total, initial body weight, total gain percentage, and body weight gain
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{male_names[0]} is preparing for his strength phase training and wants to measure his improvement."
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"Before {male_names[0]} starts the strength phase training of his cycle, he has a powerlifting total of {ints[0]} pounds "
                f"at a bodyweight of {ints[1]} pounds. He manages to gain {ints[2]}% on his total and {ints[3]} pounds of body weight. "
                f"What is the ratio of his lifting total to bodyweight? {irrelevant_string}"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"He added {ints[0]}*{ints[2] / 100} = <<{ints[0]}*{ints[2] / 100}={ints[0] * (ints[2] / 100)}>>{ints[0] * (ints[2] / 100)} "
                f"pounds to his total. That means his new total is {ints[0]} + {ints[0] * (ints[2] / 100)} = "
                f"<<{ints[0]}+{ints[0] * (ints[2] / 100)}={ints[0] + ints[0] * (ints[2] / 100)}>>{ints[0] + ints[0] * (ints[2] / 100)} "
                f"pounds. His new body weight is {ints[1]} + {ints[3]} = <<{ints[1]}+{ints[3]}={ints[1] + ints[3]}>>{ints[1] + ints[3]} "
                f"pounds. So he has {ints[0] + ints[0] * (ints[2] / 100)} / {ints[1] + ints[3]} = "
                f"<<{ints[0] + ints[0] * (ints[2] / 100)}/{ints[1] + ints[3]}="
                f"{(ints[0] + ints[0] * (ints[2] / 100)) / (ints[1] + ints[3])}>>"
                f"{(ints[0] + ints[0] * (ints[2] / 100)) / (ints[1] + ints[3])} for his ratio. "
                f"#### {(ints[0] + ints[0] * (ints[2] / 100)) / (ints[1] + ints[3])}"
            ),
        ),
        Problem(
            2,  # 2 female names (e.g., Christine and Janice)
            0,
            0,
            0,
            5,  # 5 integers: Christine's first throw, Janice's reduction on her first throw, Christine's second throw increase, Christine's third throw increase, and Janice's multiplier for the second throw
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"{female_names[0]} and {female_names[1]} are having a contest to see who can throw a ball the highest."
            ),
            lambda irrelevant_string, female_names, male_names, female_relations, male_relations, ints: (
                f"They each get three throws. On her first throw, {female_names[0]} throws it {ints[0]} feet high. "
                f"{female_names[1]}'s throw is {ints[1]} feet lower than {female_names[0]}'s. "
                f"On their second throw, {female_names[0]} throws it {ints[2]} feet higher than her first throw, and "
                f"{female_names[1]} throws it {ints[4]} times as high as her first throw. "
                f"On the final throw, {female_names[0]} throws it {ints[3]} feet higher than her 2nd throw, while "
                f"{female_names[1]} throws it {ints[3] + ints[0] - ints[1]} feet higher than {female_names[0]}'s first throw. "
                f"What is the height of the highest throw? {irrelevant_string}"
            ),
            lambda female_names, male_names, female_relations, male_relations, ints: (
                f"We know {female_names[0]}'s second throw was {ints[0]} + {ints[2]} = "
                f"<<{ints[0]}+{ints[2]}={ints[0] + ints[2]}>>{ints[0] + ints[2]} feet. "
                f"We know {female_names[0]}'s third throw was {ints[0] + ints[2]} + {ints[3]} = "
                f"<<{ints[0] + ints[2]}+{ints[3]}={ints[0] + ints[2] + ints[3]}>>{ints[0] + ints[2] + ints[3]} feet. "
                f"{female_names[1]}'s first throw was {ints[0]} - {ints[1]} = <<{ints[0]}-{ints[1]}={ints[0] - ints[1]}>>{ints[0] - ints[1]} feet. "
                f"{female_names[1]}'s second throw was {ints[0] - ints[1]} * {ints[4]} = "
                f"<<{ints[0] - ints[1]}*{ints[4]}={(ints[0] - ints[1]) * ints[4]}>>{(ints[0] - ints[1]) * ints[4]} feet. "
                f"{female_names[1]}'s final throw was {ints[0]} + {ints[3] + ints[0] - ints[1]} = "
                f"<<{ints[0]}+{ints[3] + ints[0] - ints[1]}={ints[0] + ints[3] + ints[0] - ints[1]}>>"
                f"{ints[0] + ints[3] + ints[0] - ints[1]} feet. "
                f"The highest throw was {max([ints[0] + ints[2] + ints[3], (ints[0] - ints[1]) * ints[4], ints[0] + ints[3] + ints[0] - ints[1]])} feet. "
                f"#### {max([ints[0] + ints[2] + ints[3], (ints[0] - ints[1]) * ints[4], ints[0] + ints[3] + ints[0] - ints[1]])}"
            ),
        ),
    ]
    return templates


def main():
    my_list = get_problem_templates()

    # Use this to experiement and check templates.
    for problem in my_list:
        print("----------------------------------------------------------------------")
        question, irrelevant_question, answer = problem.generate_problem()
        print("Original Question: \n", question, "\n")
        print("Question with Irrelevant Information: \n", irrelevant_question, "\n")
        print("Answer: \n", answer, "\n")
    print(f"I have {len(my_list)} questions")


if __name__ == "__main__":
    main()
