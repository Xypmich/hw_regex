from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
new_contacts_list = []
regex_match_pattern = r"(\+7|8)?\s*\(*(\d{3})\)*\W*(\d{3})-*(\d{2})-*(\d{2})(\s*)\(*([а-яё]*\.*)\s*(\d*)\)*"
regex_subst_pattern = r"+7(\2)\3-\4-\5\6\7\8"
for employee in contacts_list:
    a = 0
    if ' ' in employee[0] and len(employee[0].split()) == 3:
        emp_split = employee[0].split()
        employee[0] = emp_split[0]
        employee[1] = emp_split[1]
        employee[2] = emp_split[2]
    elif ' ' in employee[0] and len(employee[0].split()) == 2:
        emp_split = employee[0].split()
        employee[0] = emp_split[0]
        employee[1] = emp_split[1]
    elif ' ' in employee[1]:
        emp_split = employee[1].split()
        employee[1] = emp_split[0]
        employee[2] = emp_split[1]
    regex_subst_res = re.sub(regex_match_pattern, regex_subst_pattern, employee[5])
    employee[5] = regex_subst_res
    for val in new_contacts_list:
        if employee[0] == val[0]:
            iter_count = 0
            for value in val:
                if value == '':
                    val[iter_count] = employee[iter_count]
                iter_count += 1
            a = 1
    if a == 0:
        new_contacts_list.append(employee)
pprint(new_contacts_list)

#TODO 2: сохраните получившиеся данные в другой файл
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
    datawriter.writerows(new_contacts_list)
