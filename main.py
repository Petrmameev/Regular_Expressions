import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pattern_name = r"((^\w+))(\s|,)(\w+)(\s|,)(\w+)?,(,|\s*)(,|\s*)"
pattern_phone = r"(\+7|8)\s*(\(|\s*)(\d{3})(\)|s*)(-|s*)(\s*)(\d{3})(-|\s*)(\d\d)(-|\s*)(\d\d)(\W(\W|\s*)(доб.)\s(\d{4})\W)?"
replace_name = r"\2, \4, \6, "
replace_phone = r"+7(\3)\7-\9-\11 \14\15 "
new_contacts_list = list()
for contact in contacts_list:
    contact_string = ','.join(contact)
    phone_edit = re.sub(pattern_phone, replace_phone, contact_string)
    name_edit = re.sub(pattern_name, replace_name, phone_edit)
    contact = name_edit.split(',')
    new_contacts_list.append(contact)
a = [i or j for i, j in zip(new_contacts_list[7], new_contacts_list[8])]
b = [i or j for i, j in zip(new_contacts_list[2], new_contacts_list[4])]
new_contacts_list.append(a)
new_contacts_list.append(b)
del new_contacts_list[2]
del new_contacts_list[3]
del new_contacts_list[5:]
new_contacts_list.append(a)
new_contacts_list.append(b)

with open("phonebook.csv", 'w', encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_contacts_list)