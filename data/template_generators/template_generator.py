# This script is used to generate the problems from templates.

import csv
import wes_templates
import will_templates
import edmund_templates
import tin_templates

from problem import Problem

def get_problem_templates():
    wes_templates.get_problem_templates()
    templates = sum([wes_templates.get_problem_templates(), will_templates.get_problem_templates(), edmund_templates.get_problem_templates(), tin_templates.get_problem_templates()], [])
    return templates


def get_problem_variants():
    templates = get_problem_templates()
    problems = [template.generate_problem() for template in templates for _ in range(50)]
    return problems


def save_problem_variants():
    with open("../variants_data.csv", 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(get_problem_variants())

save_problem_variants()

