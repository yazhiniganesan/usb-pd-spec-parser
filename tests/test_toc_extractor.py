from pdf_parsing.toc_extractor import TOCExtractor

def test_toc_extractor_parse():
    sample_toc = "1. Introduction ........ 5\n1.1 Details ........ 7"
    entries = TOCExtractor.extract(sample_toc)
    assert isinstance(entries, list)
    assert len(entries) >= 1
    assert "section_id" in entries[0]
