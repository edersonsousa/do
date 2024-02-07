from pypdf import PdfReader


pdf = "./20231229EXEC1.pdf"


reader = PdfReader("20240129EXEC1.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[2]
text = page.extract_text()
print(text)
