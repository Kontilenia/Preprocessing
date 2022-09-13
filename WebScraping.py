import requests
from bs4 import BeautifulSoup

# List with urls
list_of_doc_urls = []
# For every page on a particular part
for page in range(1, 21):
    # Request page
    # 3rd part -> range(1,19)
    # get_page = requests.get('https://www.hellenicparliament.gr/Praktika/Synedriaseis-Olomeleias?search=on'
    #                        '&SessionPeriod=d1e63fbc-9e29-4a80-9986-adb70123628e&pageNo='+str(page))

    # 2nd part -> range(1,21)
    get_page = requests.get('https://www.hellenicparliament.gr/Praktika/Synedriaseis-Olomeleias?search=on'
                            '&SessionPeriod=5cf4f254-eee1-4264-9258-ac4b00b1ca69&pageNo='+str(page))

    # 1rst part -> range(1, 23)
    # get_page = requests.get('https://www.hellenicparliament.gr/Praktika/Synedriaseis-Olomeleias?search=on'
    #                        '&SessionPeriod=1d81f25b-0dfd-4649-8dab-aa8d00a81852&pageNo=1'+str(page))

    # For every one of the ten html elements that contain links in the current page
    for i in range(1,11):
        get_page_soup = BeautifulSoup(get_page.text, 'html.parser')
        number = str(i)
        if i <= 9:
            number = '0' + str(i)
        # Take html element that contains the url of the doc
        all_id_elements = get_page_soup.findAll('a', {'id': 'ctl00_ContentPlaceHolder1_rr_repSearchResults_ctl'+number
                                                            + '_lnkTxt'})
        # Get the link
        for el in all_id_elements:
            if el.get('href'):
                list_of_doc_urls.append(el.get('href'))

# Save links in a txt file
with open('links/b_doc_links.txt', 'a') as f:
    for elem in list_of_doc_urls:
        f.write(str(elem)+'\n')
