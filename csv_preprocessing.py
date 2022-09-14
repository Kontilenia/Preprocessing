import pandas as pd

# Read the file and load it to pandas dataframe
df = pd.read_csv('unprocessed_text.csv')

# Reformat of dataframe for minor changes that are needed to be done first
for index in df.index:
    if str(df.loc[index, 'name'])[0] == ")" and len(str(df.loc[index, 'name']).replace(" ", "")) > 1:
        df.loc[index - 1, 'text'] = str(df.loc[index - 1, 'text'] + ')')
        df.loc[index, 'name'] = df.loc[index, 'name'][1:]
    elif len(str(df.loc[index, 'name']).replace(" ", "")) == 0:
        df.loc[index, 'text'] = "-"
        df.loc[index, 'name'] = "-"
    elif len(str(df.loc[index, 'text']).replace(" ", "")) > 1 and str(df.loc[index, 'text'])[0] == ")" \
            and str(df.loc[index, 'text'])[1] == ":":
        df.loc[index, 'name'] = str(df.loc[index, 'name'] + '):')
        df.loc[index, 'text'] = df.loc[index, 'text'][2:]
    elif len(str(df.loc[index, 'text']).replace(" ", "")) > 0 and str(df.loc[index, 'text'])[0] == ":":
        df.loc[index, 'name'] = str(df.loc[index, 'name'] + ':')
        df.loc[index, 'text'] = df.loc[index, 'text'][1:]
    if len(str(df.loc[index, 'text']).replace(" ", "")) > 0 and str(df.loc[index, 'text'])[0] == " ":
        df.loc[index, 'text'] = df.loc[index, 'text'][1:]
    if len(str(df.loc[index, 'name']).replace(" ", "")) > 0 and str(df.loc[index, 'name'])[0] == " ":
        df.loc[index, 'name'] = df.loc[index, 'name'][1:]
    elif len(str(df.loc[index, 'name']).replace(" ", "")) > 0 and str(df.loc[index, 'name'])[0] == "  ":
        df.loc[index, 'name'] = df.loc[index, 'name'][2:]
    if "\t" in df.loc[index, 'text']:
        str(df.loc[index, 'text']).replace("\t", "")
    if "\t" in df.loc[index, 'name']:
        str(df.loc[index, 'name']).replace("\t", "")
    if "\xa0" in df.loc[index, 'text']:
        str(df.loc[index, 'text']).replace("\xa0", " ")
    if "\xa0" in df.loc[index, 'name']:
        str(df.loc[index, 'name']).replace("\xa0", " ")

# Second reformat of dataframe with bigger changes
for index in df.index:
    if (not ')' in df.loc[index, 'text'] and df.loc[index, 'name'] == "(") or \
            (str(df.loc[index, 'name']).replace(" ", "") == "(" and ')' in df.loc[index, 'text']
             and '(' in df.loc[index, 'text'] and not ')' in df.loc[index + 1, 'name']
             and ')' in df.loc[index + 1, 'text']):
        df.loc[index - 1, 'text'] = str(
            df.loc[index - 1, 'text'] + df.loc[index, 'name'] + df.loc[index, 'text'] + df.loc[
                index + 1, 'name'] + df.loc[index + 1, 'text'])
        df.loc[index, 'text'] = "-"
        df.loc[index, 'name'] = "-"
        df.loc[index + 1, 'text'] = "-"
        df.loc[index + 1, 'name'] = "-"
    elif (')' in df.loc[index, 'text'] and df.loc[index, 'name'] == "(") or str(df.loc[index, 'name']).replace(" ", "")[
        0] == '»' \
            or str(df.loc[index, 'name']).replace(" ", "")[0] == "." \
            or str(df.loc[index, 'name']).replace(" ", "")[0] == "," \
            or str(df.loc[index, 'name']).replace(" ", "")[0] == "/" \
            or str(df.loc[index, 'name']).replace(" ", "")[0] == "«" \
            or str(df.loc[index, 'name']).replace(" ", "")[0] == "΄":
        if not df.loc[index - 1, 'name'] == "-":
            df.loc[index - 1, 'text'] = str(df.loc[index - 1, 'text'] + df.loc[index, 'name'] + df.loc[index, 'text'])
            df.loc[index, 'text'] = "-"
            df.loc[index, 'name'] = "-"
        else:
            df.loc[index - 2, 'text'] = str(
                df.loc[index - 2, 'text'] + df.loc[index, 'name'] + df.loc[index, 'text'])
            df.loc[index, 'text'] = "-"
            df.loc[index, 'name'] = "-"
    if ("Στο σημείο αυτό την Προεδρική Έδρα" in df.loc[index, 'text'] or "Στο σημείο αυτό, την Προεδρική Έδρα" in
        df.loc[index, 'text']
        or "Στο σημείο αυτή την Προεδρική Έδρα" in df.loc[index, 'text'] or "Στο σημείο αυτό την προεδρική Έδρα" in
        df.loc[index, 'text']
        or "Στο σημείο αυτό την Προεδρική έδρα" in df.loc[index, 'text']
        or "Στο σημείο αυτό την Προεδρικής Έδρα" in df.loc[index, 'text']) \
            and ((str(df.loc[index + 1, 'text'])[0] == ")" and not "(" in df.loc[index + 1, 'name']) or (
            ")" in df.loc[index + 1, 'name'] and not "(" in df.loc[index + 1, 'name'])):
        df.loc[index, 'text'] = str(
            df.loc[index, 'text'] + df.loc[index + 1, 'name'] + df.loc[index + 1, 'text'])
        df.loc[index + 1, 'text'] = "-"
        df.loc[index + 1, 'name'] = "-"
    elif "Στο σημείο αυτό την Προεδρική Έδρα" in df.loc[index, 'text'] and not str(df.loc[index + 1, 'text'])[
                                                                                   0] == ")" and not "(" in df.loc[
        index + 1, 'name'] and str(df.loc[index + 2, 'text'])[0] == ")" and not "(" in df.loc[index + 2, 'name']:
        df.loc[index, 'text'] = str(
            df.loc[index, 'text'] + df.loc[index + 1, 'name'] + df.loc[index + 1, 'text'] + df.loc[index + 2, 'name'] +
            df.loc[index + 2, 'text'])
        df.loc[index + 1, 'text'] = "-"
        df.loc[index + 1, 'name'] = "-"
        df.loc[index + 2, 'text'] = "-"
        df.loc[index + 2, 'name'] = "-"
    if (len(str(df.loc[index, 'name']).split()) == 1 and str(df.loc[index, 'text']).replace(" ", "") == "" and len(
            str(df.loc[index + 1, 'name']).split()) == 1 and not str(df.loc[index + 1, 'text']).replace(" ", "") == "") \
            or (len(str(df.loc[index, 'name']).split()) >= 1 and str(df.loc[index, 'text']).replace(" ",
                                                                                                    "") == "" and "(" in
                df.loc[index + 1, 'name'] and ")" in df.loc[index + 1, 'name'] and not str(
                df.loc[index + 1, 'text']).replace(" ", "") == "") \
            or (
            "(" in df.loc[index, 'name'] and not ")" in df.loc[index, 'name'] and str(df.loc[index, 'text']).replace(
        " ", "") == "" and ")" in df.loc[index + 1, 'name'] and not str(df.loc[index + 1, 'text']).replace(" ",
                                                                                                           "") == ""):
        df.loc[index, 'name'] = str(
            df.loc[index, 'name'] + " " + df.loc[index + 1, 'name'])
        df.loc[index, 'text'] = str(df.loc[index, 'text'] + df.loc[index + 1, 'text'])
        df.loc[index + 1, 'name'] = "-"
        df.loc[index + 1, 'text'] = "-"
    elif not ":" in df.loc[index, 'name'] and not "(" in df.loc[index, 'name'] \
            and str(df.loc[index, 'text']).replace(" ", "") == "" \
            and len(str(df.loc[index + 1, 'name']).split()) > 1 and str(df.loc[index + 1, 'name'])[0] == "(" \
            and not ")" in df.loc[index + 1, 'name'] \
            and str(df.loc[index + 1, 'text']).replace(" ", "") == ")" \
            and str(df.loc[index + 2, 'name']).replace(" ", "") == ":":
        df.loc[index, 'name'] = str(
            df.loc[index, 'name'] + " " + df.loc[index + 1, 'name'] + "):")
        df.loc[index, 'text'] = str(df.loc[index + 2, 'text'])
        df.loc[index + 1, 'name'] = "-"
        df.loc[index + 1, 'text'] = "-"
        df.loc[index + 2, 'name'] = "-"
        df.loc[index + 2, 'text'] = "-"
    if ":" in str(df.loc[index, 'name']) and str(df.loc[index, 'name']).count(":") > 1:
        df.loc[index, 'name'] = "-"
        df.loc[index, 'text'] = "-"

# Delete all rows with garbage data
df = df[df["name"].str.contains(
    "ΠΡΟΕΔΡ|ΒΟΥΛΕΥΤ|ΔΙΑΤΑΞΗ|ΕΡΩΤΗΣΕΩΝ|ΕΡΓΑΣΙΑ|ΠΡΟΔΡΕΥΩΝ|ΠΡΟΕΔΡΕΥΩΝ|ΑΝΤΕΙΣΑΓΓΕΛΕΙΣ|ΑΕΡΟΠΑΓΙΤΕΣ|ΠΡΟΕΥΔΡΕΥΩΝ|ΠΡΟEΔΡΕΥΩΝ|ΠΡΟΔΕΡΕΥΩΝ|ΠΡΟΔΡΕΥΟΥΣΑ|ΠΡΟΕΔΕΥΩΝ|ΑΡΕΟΠΑΓΙΤΕΣ",
    regex=True) == False]
df['name'] = df['name'].str.replace("\t", "", True)
df.drop(df.index[df["text"] == '. '], inplace=True)
df.drop(df.index[df["text"] == ') '], inplace=True)
df.drop(df.index[df["text"] == '( '], inplace=True)
df.drop(df.index[df["name"] == '(  '], inplace=True)
df.drop(df.index[df["name"] == ''], inplace=True)
df.drop(df.index[df["name"] == ':'], inplace=True)
df.drop(df.index[df["name"] == 'Α'], inplace=True)
df.drop(df.index[df["name"] == '\xa0'], inplace=True)
df.drop(df.index[df["name"] == '\xa0\xa0'], inplace=True)
df.drop(df.index[df["name"] == '-'], inplace=True)
df.drop(df.index[df["text"] == '-'], inplace=True)
df.drop(df.index[df["text"] == ' '], inplace=True)
df.drop(df.index[df["name"] == 'ν'], inplace=True)

# Save the preprocessed dataframe to a new file
df.to_csv('total_data.csv', index=False)
