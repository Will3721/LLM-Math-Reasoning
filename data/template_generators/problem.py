# This script defines the template used to define problems.

import random

class Problem:
    def __init__(self, num_female_names, num_male_names, num_female_relations, num_male_relations, num_ints, irrelevant_string_generator, question_generator, answer_generator, condition=None, modification=None):
        self.num_female_names = num_female_names
        self.num_male_names = num_male_names
        self.num_female_relations = num_female_relations
        self.num_male_relations = num_male_relations
        self.num_ints = num_ints
        self.irrelevant_string_generator = irrelevant_string_generator
        self.question_generator = question_generator
        self.answer_generator = answer_generator
        self.condition = condition
        self.modification = modification

    def generate_problem(self):
        female_names = random.sample(["Olivia", "Emma", "Charlotte", "Amelia", "Sophia", "Mia", "Isabella", "Ava"], self.num_female_names)
        male_names = random.sample(["Liam", "Noah", "Oliver", "James", "Elijah", "Mateo", "Lucas", "William"], self.num_male_names)
        female_relations = random.sample(["grandmother", "mother", "aunt", "sister", "niece", "daughter"], self.num_female_relations)
        male_relations = random.sample(["grandfather", "father", "uncle", "brother", "nephew", "son"], self.num_male_relations)
        ints = random.sample([i for i in range(10, 100)], self.num_ints)
        params = (female_names, male_names, female_relations, male_relations, ints)

        if self.condition is not None and not self.condition(*params):
            if self.modification is None:
                return self.generate_problem()
            else:
                self.modification(*params)
        
        irrelevant_string = self.irrelevant_string_generator(*params)

        return self.question_generator("", *params), self.question_generator(irrelevant_string, *params), self.answer_generator(*params)

