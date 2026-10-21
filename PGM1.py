import spacy

nlp = spacy.load("en_core_web_sm")
text = input("Enter a sentence: ")

doc = nlp(text)

print("POS Tagging:")
for token in doc:
    print(token.text, token.pos_)

print("\nNamed Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)