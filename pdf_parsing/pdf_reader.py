import pdfplumber

class PDFDocReader:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.pdf = pdfplumber.open(pdf_path)
    def extract_toc_pages(self):
        toc_text = ""
        for i, page in enumerate(self.pdf.pages):
            if i > 0 and i % 1 == 0:
                print(f"╔════════════════╗")
                print(f"║ 📄 Processed {i} pages... ║")
                print(f"╚════════════════╝")

            try:
                page_text = page.extract_text_simple()
                if page_text:
                    toc_text += page_text + "\n"
                else:
                    print(f"Warning: No text on page {i+1}")
            except Exception as e:
                print(f"Error on page {i+1}: {e}")
        return toc_text


    def close(self):
        self.pdf.close()
