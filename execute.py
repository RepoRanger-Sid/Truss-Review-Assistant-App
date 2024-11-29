import os
import glob
from pdf_reader import read_pdf
from storage_compartment import compartmentalize_pdf
from pattern import regex_dict
from workbook_creater import create_workbook, unpack_and_store_values
from data_checker import assess
from user_input import get_input_data


def execute(input_data, pdf_file_path, regex_dict):
    # Extract the base name of the PDF file without the extension
    pdf_file_name = os.path.splitext(os.path.basename(pdf_file_path))[0]
    
    # Read the PDF
    pdf_data = read_pdf(pdf_file_path)
    if pdf_data is None:
        print(f"Error: The file '{pdf_file_path}' was not found.")
        return
    
    # Compartmentalize the PDF data
    compartmentalized_data = compartmentalize_pdf(regex_dict, pdf_data)
    
    # Create a workbook
    workbook = create_workbook(pdf_file_name, compartmentalized_data)
    
    # Unpack and store values in the workbook
    unpack_and_store_values(workbook, compartmentalized_data)
    
    # Run the main data checker function
    assess(pdf_file_name, input_data)