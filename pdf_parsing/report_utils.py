import os
import pandas as pd

def combine_excel_reports():
    file_paths = {
        "usb_pd_full_sections": "outputs/usb_pd_full_sections.xlsx",
        "usb_pd_section_with_content": "outputs/usb_pd_section_with_content.xlsx",
        "usb_pd_toc_with_content": "outputs/usb_pd_toc_with_content.xlsx"
    }
    output_file = "outputs/combined_usb_pd_report.xlsx"

    with pd.ExcelWriter(output_file) as writer:
        for sheet_name, file_path in file_paths.items():
            if os.path.exists(file_path):
                df = pd.read_excel(file_path)
                df.to_excel(writer, sheet_name=sheet_name, index=False)
            else:
                print(f"Warning: File {file_path} not found. Skipping sheet {sheet_name}.")

    print(f"Combined Excel report created at {output_file}")
