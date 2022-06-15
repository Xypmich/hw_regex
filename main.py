from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
new_contacts_list = []
iter_count = 0
for employee in contacts_list:
    for value in new_contacts_list:
        if ' ' in employee[0] and len(employee[0].split()) == 3:
            emp_split = employee[0].split()
            employee[0] = emp_split[0]
            employee[1] = emp_split[1]
            employee[2] = emp_split[2]
        elif ' ' in employee[1]:
            emp_split = employee[1].split()
            employee[1] = emp_split[0]
            employee[2] = emp_split[1]
        elif employee[0] == value[0]:
            n = 0
            while n <= len(employee) - 1:
                if value[n] == '':
                    new_contacts_list[iter_count - 1][n] = employee[n]
                n += 1
            continue
    new_contacts_list.append(employee)
    iter_count += 1
regex_match_pattern = r"(\+7|8)\s*\(*(\d{3})\)*\W*(\d{3})-*(\d{2})-*(\d{2})(\s*)\(*(\w*\.*)\s*(\d*)"
regex_subst_pattern = r"+7(\2)\3-\4-\5\6\7\8"
for val in new_contacts_list:
    regex_subst_res = re.sub(regex_match_pattern, regex_subst_pattern, val[5])
    val[5] = regex_subst_res
pprint(new_contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#     datawriter.writerows(contacts_list)
