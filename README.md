# Truss Review Assistant

A full-stack web application designed to automate and streamline the review process of truss design documents by analyzing PDF shop drawings and providing detailed parameter validation.

## Features

- **PDF Processing**: Extracts critical design parameters from uploaded truss shop drawings
- **Automated Validation**: Checks compliance with user-defined criteria for:
  - Load calculations (dead load, live load, truss spacing)
  - Design standards (wind speed, building codes, risk categories)
  - Structural integrity (member stress analysis)
  - Deflection requirements
  - Drag load conditions
  - Bearing requirements

## Technology Stack

- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend**: Python Flask
- **Libraries**:
  - PyPDF2: PDF processing
  - openpyxl: Excel file handling
  - Flask-CORS: Cross-origin resource sharing

## Key Components

1. **PDF Analysis**
   - Automated text extraction using regex patterns
   - Structured data organization for multiple truss configurations

2. **Data Processing**
   - Comprehensive parameter validation
   - Excel workbook generation with formatted results
   - Color-coded highlighting for non-compliant values

3. **User Interface**
   - Modern Microsoft-style design
   - Real-time form validation
   - Progress tracking for file processing
   - Interactive result review

## Installation

1. Clone the repository
2. Install required packages:
```sh
pip install -r [requirements.txt](http://_vscodecontentref_/1)
```
3. Run the Flask application:
```
python app.py
```

## Project Structure

```
├── app.py                  # Flask application entry point
├── data_checker.py         # Data validation logic
├── execute.py             # Main execution controller
├── pattern.py             # Regex pattern definitions
├── pdf_reader.py          # PDF processing utilities
├── storage_compartment.py # Data extraction and storage
├── workbook_creater.py    # Excel file generation
├── static/               # Static assets
├── templates/            # HTML templates
└── uploads/              # PDF upload directory
```

## Usage
1. Upload truss shop drawing PDF
2. Input design criteria:
    - Loading parameters
    - Deflection limits
    - Building code requirements
    - Wind design standards
3. Run analysis
4. Review color-coded Excel output for parameter compliance