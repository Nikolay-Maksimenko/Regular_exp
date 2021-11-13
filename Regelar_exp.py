from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)
pattern_for_phone = r"(\+7|8)\s?\(?(\d{3})\)?\s?-?(\d{3})-?(\d{2})-?(\d{2})\s?\(?(\w{3}\.)?\s?(\d+)?\)?"
substitution_phone = r"+7(\2)\3-\4-\5 \6\7"

def fix_contact_list(contacts_list):
  new_contacts_list = []
  for contact in contacts_list:
    full_name = ' '.join(contact[:3]).split(' ')
    new_contact = [full_name[0], full_name[1], full_name[2], contact[3], contact[4], re.sub(pattern_for_phone, substitution_phone, contact[5]), contact[6]]
    new_contacts_list.append(new_contact)
  return new_contacts_list

def delete_duplicate(contacts_list):
    for contact in contacts_list:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in contacts_list:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "":
                    contact[2] = new_contact[2]
                if contact[3] == "":
                    contact[3] = new_contact[3]
                if contact[4] == "":
                    contact[4] = new_contact[4]
                if contact[5] == "":
                    contact[5] = new_contact[5]
                if contact[6] == "":
                    contact[6] = new_contact[6]
    result_list = list()
    for i in contacts_list:
        if i not in result_list:
            result_list.append(i)
    return result_list

x = fix_contact_list(contacts_list)
pprint(delete_duplicate(x))


# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(delete_duplicate(x))