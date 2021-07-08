"""Code for extracting HDFC bank monthly statement pdf file data from first page"""
import pdfplumber

pdf_name = 'montly_statement.pdf'
with pdfplumber.open(pdf_name) as pdf:
    """Getting texts like Customer Name and Address"""
    page = pdf.pages[0]
    cust_details = page.extract_text()
    # print(text)
    cust_details = cust_details.split('\n')
    # print(newtext)
    pin_code = cust_details[15].split()
    pin_code = pin_code[0]
    print(f"Customer Name: {cust_details[4]}\nAddress: {cust_details[6]}, {cust_details[10]}, {cust_details[12]}, {pin_code}")

    """Extracting first two Transactions with all details from table"""
    print('----First two Transactions-----')

    transaction_lst = []
    for i in page.extract_table():
        transaction_lst.append(i)

    for j in transaction_lst[1:3]:
        transactions = {'Date': j[0],
                        'Narration': j[1],
                        'Chq/Ref No.': j[2],
                        'Value Date': j[3],
                        'Withdrawl Amt': j[4],
                        'Deposit Amt': j[5],
                        'Closing Balance': j[6]}
        print(transactions)
