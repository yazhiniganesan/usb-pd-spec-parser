import os
import sys
import pandas as pd
from pdf_parsing.pdf_reader import PDFDocReader
from pdf_parsing.toc_extractor import TOCExtractor
from jsonl_schemas.toc_schema import save_jsonl as save_toc_jsonl
from jsonl_schemas.section_schema import save_jsonl as save_sections_jsonl
from validation.report_generator import ValidationReport
from pdf_parsing.report_utils import combine_excel_reports


def jsonl_to_excel(jsonl_path, excel_path):
    df = pd.read_json(jsonl_path, lines=True)
    df.to_excel(excel_path, index=False)
    print(f"Converted {jsonl_path} to {excel_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <usb_pd_spec_pdf>")
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.normpath(os.path.join(script_dir, sys.argv[1]))

    print(f"Opening PDF: {pdf_path}")
    reader = PDFDocReader(pdf_path)
    toc_text = reader.extract_toc_pages()

    toc_entries = TOCExtractor.extract(toc_text)
    print(f"Extracted {len(toc_entries)} TOC entries.")

    os.makedirs("outputs", exist_ok=True)

    # Save JSONL files
    toc_jsonl_path = os.path.join("outputs", "usb_pd_toc.jsonl")
    save_toc_jsonl(toc_jsonl_path, toc_entries)
    print(f"Saved TOC JSONL to {toc_jsonl_path}")

    sections_jsonl_path = os.path.join("outputs", "usb_pd_spec.jsonl")
    save_sections_jsonl(sections_jsonl_path, toc_entries)
    print(f"Saved Sections JSONL to {sections_jsonl_path}")

    metadata = [{
        "doc_title": "USB PD Specification Rev X",
        "total_toc_sections": len(toc_entries),
        "total_sections": len(toc_entries),
    }]
    metadata_jsonl_path = os.path.join("outputs", "usb_pd_metadata.jsonl")
    save_toc_jsonl(metadata_jsonl_path, metadata)
    print(f"Saved Metadata JSONL to {metadata_jsonl_path}")

    # Generate Validation Excel Report
    validation_report_path = os.path.join("outputs", "validation_report.xlsx")
    report = ValidationReport(toc_entries)
    report.generate(validation_report_path)
    print(f"Validation report saved to {validation_report_path}")

    reader.close()
    print("Parsing and validation complete.")

    # Convert JSONL files to Excel
    jsonl_to_excel(toc_jsonl_path, "outputs/usb_pd_toc_with_content.xlsx")
    jsonl_to_excel(sections_jsonl_path, "outputs/usb_pd_section_with_content.xlsx")
    jsonl_to_excel(metadata_jsonl_path, "outputs/usb_pd_full_sections.xlsx")

    # Combine Excel files into single workbook
    combine_excel_reports()
    print("Combined Excel report generated.")


if __name__ == "__main__":
    main()
