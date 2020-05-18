import pdftotext


def main(pdf):
  with open(pdf, "rb") as f:
    pdf = pdftotext.PDF(f)
  
  text = "\n\n".join(pdf)

  print(text)


if __name__ == '__main__':
  import plac; plac.call(main)
