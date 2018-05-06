from random import sample, choice, randint
import csv
import pandas as pd
from pprint import pprint



pos = 0
header = ["Province", "First_Name", "Last_Name", "Street", "City"]
letters = "abcdefghijklmnopqrstuvwxyz".upper()
data = []

while pos < len(header):
    file = pd.read_csv("data.csv")
    column = file.loc[:, header[pos]]
    data.append([row for row in column])
    pos += 1

province = data[0]
first_names = data[1]
last_names = data[2]
street_name = data[3]
city_name = data[4]

list_fake_dict = []

for _ in range(13):
    prov = choice(province)
    first = choice(first_names)
    last = choice(last_names)
    street = choice(street_name)
    street_num = randint(100, 999)
    city = choice(city_name)

    phone_number = f"514-{randint(100, 999)}-{randint(1000, 9999)}"
    email = f"{first.lower()}_{last.lower()}@company.com"
    address = f"{street_num} {street}"
    postal_code = f"{choice(letters)}{randint(0, 9)}{choice(letters)} " \
                      f"{choice(letters)}{randint(0, 9)}{choice(letters)}"

    fake_dict_list = {
                "first name": first,
                 "last name": last,
                 "address": address,
                 "city": city,
                 "phone": phone_number,
                 "email": email,
                 "province": prov,
                 "postal code": postal_code}

    list_fake_dict.append(fake_dict_list)


