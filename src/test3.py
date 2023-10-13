import spacy

nlp = spacy.load("en_core_web_sm")
text = "During the interview, Elon Musk discussed SpaceX and Tesla, Inc., which are both innovative companies."
doc = nlp(text)

for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")

