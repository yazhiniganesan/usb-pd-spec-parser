import pandas as pd

class ValidationReport:
    def __init__(self, toc_entries):
        self.toc_entries = toc_entries

    def generate(self, out_filepath):
        rows = []
        for i, entry in enumerate(self.toc_entries):
            valid_order = True
            if i > 0:
                prev_page = self.toc_entries[i-1]['page']
                if entry['page'] < prev_page:
                    valid_order = False
            rows.append({
                "section_id": entry["section_id"],
                "title": entry["title"],
                "page": entry["page"],
                "valid_order": valid_order
            })
        df = pd.DataFrame(rows)
        try:
            df.to_excel(out_filepath, index=False)
        except PermissionError:
            print(f"Permission denied when writing to {out_filepath}.")
            print("Please close the Excel file if it is open and try running the script again.")
