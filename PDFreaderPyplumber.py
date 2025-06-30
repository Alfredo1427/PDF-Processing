import pdfplumber
import pandas as pd
import os


pdf_path = "C:\\Users\\aperez\\.spyder-py3\\PDFReader\\1.pdf"

pdf_pages = pdfplumber.open(pdf_path)

page = pdf_pages.pages[0]
text = page.extract_text()
text_list = text.split("\n")

invoice_text_data = {
    "invoice_number": text_list[0].replace("Invoice Number: ", ""),
    "invoice_date": text_list[2].replace("Invoice Date: ", ""),
    "due_date": text_list[5].replace("Due Date: ", ""),
    "client_name": text_list[3],
    "payment_terms": text_list[35],
    "client_address": text_list[4],
}

tables = page.extract_tables()

#print(invoice_text_data)

invoice_text_df = pd.DataFrame([invoice_text_data])

invoice_data = pd.concat([invoice_text_df], ignore_index=True)
invoice_data = pd.concat([invoice_data], axis=1)

data = invoice_data

data.to_excel("C:\\Users\\aperez\\.spyder-py3\\PDFReader\\invoice_data.xlsx", index=False)


