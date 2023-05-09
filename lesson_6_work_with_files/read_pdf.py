from PyPDF2 import PdfReader

reader = PdfReader('resources/AByteofPythonRussian-2.02.pdf')
print(len(reader.pages))

page = reader.pages[2]

text = page.extract_text()
print(text)
