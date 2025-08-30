from pdf_parsing.pdf_reader import PDFDocReader

def test_pdf_reader_extract_toc_pages():
    reader = PDFDocReader("usb_pd_spec.pdf")
    toc_text = reader.extract_toc_pages()
    assert isinstance(toc_text, str)
    assert len(toc_text) > 0
    reader.close()
