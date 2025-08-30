import re

class TOCExtractor:
    @staticmethod
    def extract(toc_text):
        pattern = re.compile(
            r'^(?P<section_id>\d+(\.\d+)*)\s+(?P<title>.*?)(?:\.+|\s+)(?P<page>\d+)$',
            re.MULTILINE
        )
        entries = []
        for match in pattern.finditer(toc_text):
            section_id = match.group('section_id')
            title = match.group('title').strip()
            page = int(match.group('page'))
            level = section_id.count('.') + 1
            parent_id = '.'.join(section_id.split('.')[:-1]) if '.' in section_id else None
            entry = {
                "doc_title": "USB PD Specification Rev X",
                "section_id": section_id,
                "title": title,
                "full_path": f"{section_id} {title}",
                "page": page,
                "level": level,
                "parent_id": parent_id,
                "tags": []
            }
            entries.append(entry)
        return entries
