import pdftotext
import spacy
import random


def pdf2txt(pdf):
    with open(pdf, "rb") as f:
        pdf = pdftotext.PDF(f)
    txt = "\n\n".join(pdf)
    return txt


def main(pdf):
    nlp = spacy.load("de_core_news_md")
    doc = nlp(pdf2txt(pdf))
    ents = {(e.text, e.label_) for e in doc.ents}
    print(random.sample(ents, 4))


if __name__ == '__main__':
    import plac; plac.call(main)
