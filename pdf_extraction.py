"""Code for extracting HDFC bank monthly statement pdf file data from first page"""
import pdfplumber

pdf_name = 'montly_statement.pdf'
with pdfplumber.open(pdf_name) as pdf:
    """Getting texts like Customer Name and Address"""
    page = pdf.pages[0]
    text = page.extract_text()
    # print(text)
    newtext = text.split('\n')
    # print(newtext)
    pin = newtext[15].split()
    pin = pin[0]
    print(f"Customer Name: {newtext[4]}\nAddress: {newtext[6]}, {newtext[10]}, {newtext[12]}, {pin} ")

    """Extracting first two Transactions with all details from table"""
    print('----First two Transactions-----')

    lst = []
    for i in page.extract_table():
        lst.append(i)

    for j in lst[1:3]:
        dict = {'Date': j[0],
                'Narration': j[1],
                'Chq/Ref No.': j[2],
                'Value Date': j[3],
                'Withdrawl Amt': j[4],
                'Deposit Amt': j[5],
                'Closing Balance': j[6]
                }
        print(dict)
