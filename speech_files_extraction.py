import requests
import os
from urllib.parse import urlparse

# List with urls
list_of_doc_urls = []
with open('links/b_doc_links.txt') as file:
    while line := file.readline().rstrip():
        list_of_doc_urls.append(str(line))

for url in list_of_doc_urls:
    # Take url and request the file
    r = requests.get(url, stream=True)

    # Find name of the file
    file_name = os.path.basename(urlparse(url).path)

    # Save the file
    with open("files/" + file_name, "wb") as doc:
        for chunk in r.iter_content(chunk_size=1024):
            # writing one chunk at a time to word file
            if chunk:
                doc.write(chunk)
