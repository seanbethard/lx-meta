import pdftotext
import spacy
import random

def main(pdf):

  nlp = spacy.load("de_core_news_md")
  
  with open(pdf, "rb") as f:
    pdf = pdftotext.PDF(f)

  # req: 1GB of temporary memory per 100,000 char
  text = "\n\n".join(pdf)[1000000:]
  
  doc = nlp(text)
  ents = {(e.text, e.label_) for e in doc.ents}

  print(random.sample(ents, 4))


if __name__ == '__main__':
  import plac; plac.call(main)
