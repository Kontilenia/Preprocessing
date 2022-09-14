import pandas as pd

# Read the file and load all text data to pandas dataframe
df = pd.read_csv('total_data.csv')

# Keep rows that have more than 100 letters in text column
df = df[df['text'].map(len) > 100]

# Remove parentheses and the context between them
df['text'] = df['text'].str.replace("[\(\[].*?[\)\]]", " ", regex=True)
df['name'] = df['name'].str.replace("[\(\[].*?[\)\]]", " ", regex=True)

# Replace unnecessary symbols and delete spaces
df['name'] = df['name'].str.replace(":", "")
df['name'] = df['name'].str.replace("   ", " ")
df['name'] = df['name'].str.replace("  ", " ")
df['name'] = df['name'].str.replace(r" - ", "-", regex=True)
df['name'] = df['name'].str.replace(r" – ", "-", regex=True)
df['name'] = df['name'].str.replace(" -", "-", regex=False)
df['name'] = df['name'].str.replace("- ", "-", regex=False)
df['name'] = df['name'].str.replace("A", "Α")
df['name'] = df['name'].str.replace("ς", "Σ")
df['name'] = df['name'].str.replace("Ί", "Ι")
df['name'] = df['name'].str.replace("ϊ", "Ϊ")
df['name'] = df['name'].str.replace("Ό", "Ο")

# Replace misspelled words
df['name'] = df['name'].str.replace("ΕΦΗ", "ΕΥΤΥΧΙΑ")
df['name'] = df['name'].str.replace("ΚΩΝΣΤΑΝΤΙΝΟΣ ΑΧ. ΚΑΡΑΜΑΝΛΗΣ", "ΚΩΝΣΤΑΝΤΙΝΟΣ ΚΑΡΑΜΑΝΛΗΣ", regex=False)
df['name'] = df['name'].str.replace("ΒΑΣΙΛΕΙΟ Σ-ΝΙΚΟΛΑΟΣ ΥΨΗΛΑΝΤΗΣ", "ΒΑΣΙΛΕΙΟΣ-ΝΙΚΟΛΑΟΣ ΥΨΗΛΑΝΤΗΣ")
df['name'] = df['name'].str.replace("ΓΕΝΝΗΜΑΤΑ ΦΩΦΗ", "ΦΩΦΗ ΓΕΝΝΗΜΑΤΑ")
df['name'] = df['name'].str.replace("ΦΩΤΕΙΝΗ ΓΕΝΝΗΜΑΤΑ", "ΦΩΦΗ ΓΕΝΝΗΜΑΤΑ")
df['name'] = df['name'].str.replace("ΚΕΓΚΕΡΓΛΟΥ", "ΚΕΓΚΕΡΟΓΛΟΥ")
df['name'] = df['name'].str.replace("ΚΩΝΣΑΝΤΙΝΟΣ", "ΚΩΝΣΤΑΝΤΙΝΟΣ")
df['name'] = df['name'].str.replace("ΣΠΥΡΙΔΩΝ ΠΝΕΥΜΑΤΙΚΟΣ", "ΣΠΥΡΙΔΩΝΑΣ ΠΝΕΥΜΑΤΙΚΟΣ")
df['name'] = df['name'].str.replace("ΑΛΕΞΑΝΔΡΟΣ ΧΑΡΙΤΣΗΣ", "ΑΛΕΞΗΣ ΧΑΡΙΤΣΗΣ")
df['name'] = df['name'].str.replace("ΑΝΝΑ-ΜΑΝΗ ΠΑΠΑΔΗΜΗΤΡΙΟΥ", "ΑΝΝΑ ΜΑΝΗ-ΠΑΠΑΔΗΜΗΤΡΙΟΥ")
df['name'] = df['name'].str.replace("ΑΣΗΜΑΚΟΠΟΥΛΟΥ ΣΟΦΙΑ-ΧΑΙΔΩ", "ΣΟΦΙΑ-ΧΑΪΔΩ ΑΣΗΜΑΚΟΠΟΥΛΟΥ")
df['name'] = df['name'].str.replace("ΧΑΙΔΩ", "ΧΑΪΔΩ")
df['name'] = df['name'].str.replace("ΑΧΜΕΤ ΙΛΧΑΝ", "ΙΛΧΑΝ ΑΧΜΕΤ")
df['name'] = df['name'].str.replace("ΔΙΟΝΥΣΙΟΣ ΚΑΛΑΜΑΤΙΑΝΟΣ", "ΔΙΟΝΥΣΙΟΣ-ΧΑΡΑΛΑΜΠΟΣ ΚΑΛΑΜΑΤΙΑΝΟΣ")
df['name'] = df['name'].str.replace("ΖΕΪΜΠΕΚ ΧΟΥΣΕΪΝ", "ΧΟΥΣΕΪΝ ΖΕΪΜΠΕΚ")
df['name'] = df['name'].str.replace("ΚΑΡΑΓΙΑΝΝΗΣ ΓΕΩΡΓΙΟΣ", "ΓΕΩΡΓΙΟΣ ΚΑΡΑΓΙΑΝΝΗΣ")
df['name'] = df['name'].str.replace("ΖΟΥΡΑΡΙΣ", "ΖΟΥΡΑΡΗΣ")
df['name'] = df['name'].str.replace("ΠΟΥΛΟΥ ΠΑΝΑΓΙΟΥ", "ΠΑΝΑΓΙΟΥ ΠΟΥΛΟΥ")
df['name'] = df['name'].str.replace("ΚΩΝΤΣΑΝΤΙΝΟΣ", "ΚΩΝΣΤΑΝΤΙΝΟΣ")
df['name'] = df['name'].str.replace("ΜΙΧΑΛΗΣ ΠΑΠΑΔΟΠΟΥΛΟΣ", "ΜΙΧΑΗΛ ΠΑΠΑΔΟΠΟΥΛΟΣ")
df['name'] = df['name'].str.replace("ΜΠΑΡΑΝ ΜΠΟΥΡΧΑΝ", "ΜΠΟΥΡΧΑΝ ΜΠΑΡΑΝ")
df['name'] = df['name'].str.replace("ΤΣΑΚΛΟΓΟΥ", "ΤΣΑΚΛΟΓΛΟΥ")
df['name'] = df['name'].str.replace("ΝΟΤΗΣ ΜΗΤΑΡΑΚΗΣ", "ΠΑΝΑΓΙΩΤΗΣ ΜΗΤΑΡΑΚΗΣ")
df['name'] = df['name'].str.replace("ΣΤΑΙΚΟΥΡΑΣ", "ΣΤΑΪΚΟΥΡΑΣ")
df['name'] = df['name'].str.replace("ΧΑΛΑΡΑΜΠΟΣ", "ΧΑΡΑΛΑΜΠΟΣ")

# Delete useless rows
df = df.drop(11048)
df = df.drop(15382)

# Read the file and load all political party names to pandas dataframe
df2 = pd.read_csv('political_party_names.csv')

# Remove parentheses and the context between them
df2['name'] = df2['name'].str.replace("[\(\[].*?[\)\]]", " ", regex=True)

# Replace unnecessary symbols and delete spaces
df2['name'] = df2['name'].str.replace(" - ", "-", regex=False)

# Convert lower letters  to upper letters
df2['name'] = df2['name'].str.upper()

# Remove father name
df2['name'] = df2['name'].str.split().str.get(2) + " " + df2['name'].str.split().str.get(0)

# Replace unnecessary symbols and delete spaces
df2['name'] = df2['name'].str.replace("Ά", "Α")
df2['name'] = df2['name'].str.replace("Έ", "Ε")
df2['name'] = df2['name'].str.replace("Ί", "Ι")
df2['name'] = df2['name'].str.replace("Ή", "Η")
df2['name'] = df2['name'].str.replace("Ό", "Ο")
df2['name'] = df2['name'].str.replace("Ύ", "Υ")
df2['name'] = df2['name'].str.replace("Ώ", "Ω")
df2['name'] = df2['name'].str.replace("΄", "")

# Replace misspelled words
df2['name'] = df2['name'].str.replace("ΑΛΕΞΑΝΔΡΟΣ ΧΑΡΙΤΣΗΣ", "ΑΛΕΞΗΣ ΧΑΡΙΤΣΗΣ")
df2['name'] = df2['name'].str.replace("ΖΩΗ ΜΑΚΡΗ", "ΖΕΤΤΑ ΜΑΚΡΗ")
df2['name'] = df2['name'].str.replace("ΧΡΙΣΤΟΦΟΡΟΣ-ΕΜΜΑΝΟΥΗΛ ΜΠΟΥΤΣΙΚΑΚΗΣ", "ΜΠΟΥΤΣΙΚΑΚΗΣ")
df2['name'] = df2['name'].str.replace("ΧΑΙΔΩ", "ΧΑΪΔΩ")
df2['name'] = df2['name'].str.replace("ΑΘΑΝΑΣΙΟΣ ΜΩΡΑΪ́ΤΗΣ", "ΑΘΑΝΑΣΙΟΣ ΜΩΡΑΪΤΗΣ")
df2['name'] = df2['name'].str.replace("ΑΛΕΞΙΟΣ ΤΣΙΠΡΑΣ", "ΑΛΕΞΗΣ ΤΣΙΠΡΑΣ")
df2['name'] = df2['name'].str.replace("ΜΙΧΑΛΗΣ ΠΑΠΑΔΟΠΟΥΛΟΣ", "ΜΙΧΑΗΛ ΠΑΠΑΔΟΠΟΥΛΟΣ")
df2['name'] = df2['name'].str.replace("ΙΑΣΩΝ ΦΩΤΗΛΑΣ", "ΙΑΣΟΝΑΣ ΦΩΤΗΛΑΣ")
df2['name'] = df2['name'].str.replace("ΣΥΜΕΩΝ ΚΕΔΙΚΟΓΛΟΥ", "ΣΙΜΟΣ ΚΕΔΙΚΟΓΛΟΥ")
df2['name'] = df2['name'].str.replace("ΕΙΡΗΝΗ ΚΑΣΙΜΑΤΗ", "ΝΙΝΑ ΚΑΣΙΜΑΤΗ")
df2['name'] = df2['name'].str.replace("ΜΑΡΙΑ-ΕΛΙΖΑ ΞΕΝΟΓΙΑΝΝΑΚΟΠΟΥΛΟΥ", "ΜΑΡΙΛΙΖΑ ΞΕΝΟΓΙΑΝΝΑΚΟΠΟΥΛΟΥ")
df2['name'] = df2['name'].str.replace("ΣΠΥΡΙΔΩΝ-ΠΑΝΑΓΙΩΤΗΣ ΛΙΒΑΝΟΣ", "ΛΙΒΑΝΟΣ")
df2['name'] = df2['name'].str.replace("ΜΙΧΑΗΛ ΧΡΥΣΟΧΟΪ́ΔΗΣ", "ΜΙΧΑΗΛ ΧΡΥΣΟΧΟΪΔΗΣ")
df2['name'] = df2['name'].str.replace("ΓΑΡΥΦΑΛΛΙΑ ΚΑΝΕΛΛΗ", "ΛΙΑΝΑ ΚΑΝΕΛΛΗ")
df2['name'] = df2['name'].str.replace("ΣΠΥΡΙΔΩΝ ΛΑΠΠΑΣ", "ΣΠΥΡΙΔΩΝΑΣ ΛΑΠΠΑΣ")
df2['name'] = df2['name'].str.replace("ΑΠΟΣΤΟΛΟΣ ΒΕΣΥΡΟΠΟΥΛΟΣ", "ΒΕΣΥΡΟΠΟΥΛΟΣ")
df2.loc[233, 'name'] = "ΑΝΝΑ ΒΑΓΕΝΑ-ΚΗΛΑΗΔΟΝΗ"
df2.loc[217, 'name'] = "ΚΑΛΛΙΟΠΗ ΒΕΤΤΑ"
df['political_party'] = ""

# Match political party name to text data
for index in df2.index:
    df.loc[df['name'].str.contains(str(df2.loc[index, 'name'])), 'political_party'] = df2.loc[index, 'political_party']

# Remove text that doesn't belong to a political party
df = df.loc[df['political_party'] != "ΑΝΕΞΑΡΤΗΤΟΙ"]

# Reset index
df.reset_index(drop=True, inplace=True)

seq_len = [len(i.split()) for i in df['text']]
print(sorted(seq_len))

seq_len = [len(i.split()) for i in df['text']]
print(sorted(seq_len))

# Count of text for every political_party
print(df.groupby(by='political_party').agg('count'))

# Save final dataset to a new file
df.to_csv('final_dataset.csv', index=False)
