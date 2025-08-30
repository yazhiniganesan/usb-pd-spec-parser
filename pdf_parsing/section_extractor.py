class SectionExtractor:
    @staticmethod
    def extract(doc_reader, toc):
        pages = doc_reader.extract_full_text()
        spec_sections = []
        for toc_entry in toc:
            page = toc_entry["page"] - 1
            section_text = pages[page] if 0 <= page < len(pages) else ""
            # Could add more extraction logic per section/subsection
            entry = dict(toc_entry)
            entry["section_text"] = section_text
            spec_sections.append(entry)
        return spec_sections
