import requests
from bs4 import BeautifulSoup
import codecs
import csv

political_party = list()
person = list()

# For every page
for i in range(1, 31):
    response = requests.get(
        'https://www.hellenicparliament.gr/Organosi-kai-Leitourgia/Olomeleia/Synthesi-IH-Periodou/?pageNo='+str(i))

    count = 0
    # For every one of the ten html elements that contain names and political parties in the current page
    for tr in BeautifulSoup(response.text, 'html.parser').find("table").find("tbody").find_all("tr"):
        count+=1
        if count>10:
            break
        a_table = tr.find_all("a")
        political_party.append(str(a_table[0]).split('title="')[1].split('"')[0])
        person.append(a_table[1].text)

# Save political parties and names in a txt file
with codecs.open('political_party_names.csv', 'a', 'utf-8') as f:
    header = ['political_party', 'name']
    # create the csv writer
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()

with codecs.open('political_party_names.csv', 'a', 'utf-8') as f:
    # create the csv writer
    writer = csv.writer(f)
    for i in range(len(political_party)):
        writer.writerow([political_party[i], person[i]])
    f.close()

