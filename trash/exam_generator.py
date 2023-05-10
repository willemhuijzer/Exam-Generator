import PyPDF2

def pdf_to_text(input_pdf):
    with open(input_pdf, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)
        extracted_text = ''

        for page_num in range(total_pages):
            pdf_page = pdf_reader.pages[page_num]
            extracted_text += pdf_page.extract_text()

    return extracted_text

