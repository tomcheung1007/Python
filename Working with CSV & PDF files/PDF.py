# In general, PDFs aren't the best way to amend documents. .txt or word doc is better suited
import PyPDF2

file = "/Users/tomcheung/Python/Working with CSV & PDF files/Working_Business_Proposal.pdf"
# 1. OPEN FILE
work_business_proposal = open(file, "rb")
# 2. USE PyPDF to access pdf file
pdf_reader = PyPDF2.PdfFileReader(work_business_proposal)

# print(pdf_reader.numPages) >>> 5

# 3. CREATE PAGE OBJECT
page_one = pdf_reader.getPage(0)
# 4. USE .EXTRACTTEXT
page_one_text = page_one.extractText()
print(page_one_text)
# 5. Can now use python fundamentals to achieve objective as text is now accessible

work_business_proposal.close()

# EXAMPLE - Get phone number from PDF file

import PyPDF2
import re

file = "/Users/tomcheung/Python/Working with CSV & PDF files/Find_the_Phone_Number.pdf"

pfd_doc = open(file, "rb")
pdf_reader = PyPDF2.PdfFileReader(pfd_doc)

pdf_text = []

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))
    (\.|\s|-)?
    (\d{3}|\(\d{3}\))
    (\.|\s|-)?
    (\d{4}|\(\d{4}\))  
)''', re.VERBOSE)

for group in re.findall(phone_regex, str(pdf_text)):
    phone_num = " ".join([group[1], group[3], group[5]])
    print(phone_num)