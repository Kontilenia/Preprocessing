import docx
import csv
import os
import codecs

with codecs.open('unprocessed_text.csv', 'a', 'utf-8') as f:
    header = ['name', 'text']
    # create the csv writer
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()

for filename in os.listdir("files"):
    document = docx.Document("files/" + filename)
    list_all = []
    for paragraph in document.paragraphs:
        for continues_text_with_same_fond in paragraph.runs:
            if continues_text_with_same_fond.bold:
                list_all.append([0, continues_text_with_same_fond.text])
                # print("Bold: " + continues_text_with_same_fond.text)
            else:
                list_all.append([1, continues_text_with_same_fond.text])
                # print("Text: " + continues_text_with_same_fond.text)

    # open the file in the append mode
    with codecs.open('unprocessed_text.csv', 'a', 'utf-8') as f:
        # create the csv writer
        writer = csv.writer(f)

        # Find the first bold text
        position = 0
        for i in range(len(list_all)):
            if list_all[i][0] == 0:
                position = i
                break
        text = ""
        name = ""
        for i in range(position, len(list_all)):
            # If text is bold then append the name list
            if list_all[i][0] == 0:
                name += list_all[i][1]
            # Else the text is not bold, so it is the speech part
            else:
                text += list_all[i][1]
                # If next text is bold
                if i+1 < len(list_all)-1 and list_all[i + 1][0] == 0:
                    # If next text is not only spaces
                    if not list_all[i + 1][1].replace(" ", "") == "":
                        # write a row to the csv file
                        writer.writerow([name, text])
                        name = ""
                        text = ""
                    else:
                        text += " "
        f.close()
