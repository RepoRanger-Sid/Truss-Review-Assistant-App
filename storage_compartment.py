import re
from pattern import regex_dict

def find_patterns(page, regex_dict):
    """
    Extracts all required patterns from a page using regex and returns a dictionary of matches.
    
    Parameters:
    - page (str): The text content of the page.
    - regex_dict (dict): The dictionary containing regex patterns.
    
    Returns:
    dict: A dictionary containing matches for each pattern.
    """
    return {
        'label_found': re.findall(regex_dict['truss_label_pattern'], page),
        'page1_pattern_found': re.findall(regex_dict['page1_pattern'], page),
        'truss_layout_pattern_found': re.findall(regex_dict['truss_layout_pattern'], page),
        'design_load_found': re.findall(regex_dict['design_load_pattern'], page),
        'roof_slope_found': re.findall(regex_dict['roof_slope_pattern'], page),
        'floor_slope_found': re.findall(regex_dict['floor_slope_pattern'], page),
        'truss_spacing_found': re.findall(regex_dict['truss_spacing_pattern'], page),
        'wind_standard_found': re.findall(regex_dict['wind_standard_pattern'], page),
        'wind_speed_found': re.findall(regex_dict['wind_speed_pattern'], page),
        'risk_category_found': re.findall(regex_dict['risk_category_pattern'], page),
        'building_code_found': re.findall(regex_dict['building_code_pattern'], page),
        'max_member_stress_found': re.findall(regex_dict['max_member_stress_pattern'], page),
        'actual_deflection_found': re.findall(regex_dict['actual_deflection_pattern'], page),
        'design_deflection_criteria_found': re.findall(regex_dict['design_deflection_criteria_pattern'], page),
        'drag_load_found': re.findall(regex_dict['drag_load_pattern'], page),
        'warning_found': re.findall(regex_dict['warning_pattern'], page),
    }

def extract_truss_label(page_patterns, truss_dictionary, truss_key):
    """Extracts and stores the truss label if found."""
    truss_dictionary[truss_key] = [truss_key]  # Initialize with the truss key

def extract_design_loads(page_patterns, truss_dictionary, truss_key):
    """Extracts design loads and appends them to the truss dictionary."""
    if page_patterns['design_load_found']:
        loads = [load.strip('BCDL *') for load in page_patterns['design_load_found'][0].split('\n')]
        truss_dictionary[truss_key].extend([loads[1], loads[3], loads[0], loads[2]])

def extract_slope(page_patterns, truss_dictionary, truss_key):
    """Extracts roof or floor slope and appends it to the truss dictionary."""
    if page_patterns['roof_slope_found']:
        truss_dictionary[truss_key].append(page_patterns['roof_slope_found'][0])
    else:
        truss_dictionary[truss_key].append('0.00')

def extract_spacing(page_patterns, truss_dictionary, truss_key):
    """Extracts truss spacing and appends it to the truss dictionary."""
    if page_patterns['truss_spacing_found']:
        truss_dictionary[truss_key].append(page_patterns['truss_spacing_found'][0].split('-')[0].strip('Code'))

def extract_wind_data(page_patterns, truss_dictionary, truss_key):
    """Extracts wind standard and wind speed, and appends them to the truss dictionary."""
    wind_standard = page_patterns['wind_standard_found'][0].strip('Wind: ') if page_patterns['wind_standard_found'] else 'NA'
    wind_speed = page_patterns['wind_speed_found'][0].strip('Vult= mph') if page_patterns['wind_speed_found'] else 'NA'
    truss_dictionary[truss_key].extend([wind_standard, wind_speed])

def extract_risk_category(page_patterns, truss_dictionary, truss_key):
    """Extracts risk category and appends it to the truss dictionary."""
    risk_category = page_patterns['risk_category_found'][0].strip('Cat.\n') if page_patterns['risk_category_found'] else 'NA'
    truss_dictionary[truss_key].append(risk_category)

def extract_building_code(page_patterns, truss_dictionary, truss_key):
    """Extracts building code and appends it to the truss dictionary."""
    if page_patterns['building_code_found']:
        code, year = '', ''
        for char in page_patterns['building_code_found'][0]:
            if char.isalpha():
                code += char
            elif char.isdigit():
                year += char
        truss_dictionary[truss_key].append(f"{code} {year}")

def extract_max_member_stress(page_patterns, truss_dictionary, truss_key):
    """Extracts max member stress values and appends them to the truss dictionary."""
    if page_patterns['max_member_stress_found']:
        stresses = [stress.strip('DEFL') for stress in page_patterns['max_member_stress_found'][0].split('\n')]
        truss_dictionary[truss_key].extend(stresses)

def extract_deflection_criteria(page_patterns, truss_dictionary, truss_key):
    """Extracts deflection criteria and appends them to the truss dictionary."""
    if page_patterns['design_deflection_criteria_found']:
        deflection_criteria = page_patterns['design_deflection_criteria_found'][0].split('\n')
        truss_dictionary[truss_key].extend([deflection_criteria[1], deflection_criteria[2]])
    else:
        truss_dictionary[truss_key].extend(['NA', 'NA'])

    if page_patterns['actual_deflection_found']:
        actual_deflection = [d.strip('><') for d in page_patterns['actual_deflection_found'][0].split('\n')]
        truss_dictionary[truss_key].extend([actual_deflection[1], actual_deflection[2]])

def extract_drag_load(page_patterns, page_storage, index, truss_dictionary, truss_key):
    """Extracts drag load and appends it to the truss dictionary, including checks on subsequent pages."""
    if page_patterns['drag_load_found']:
        for load in page_patterns['drag_load_found'][0].split(' '):
            if re.search(r'\d+', load):
                truss_dictionary[truss_key].append(load)
    elif index + 1 < len(page_storage):
        next_page_patterns = find_patterns(page_storage[index + 1], regex_dict)
        if next_page_patterns['drag_load_found'] and re.findall(r'Page 2', page_storage[index + 1]):
            for load in next_page_patterns['drag_load_found'][0].split(' '):
                if re.search(r'\d+', load):
                    truss_dictionary[truss_key].append(load)
        else:
            truss_dictionary[truss_key].append('-')
    else:
        truss_dictionary[truss_key].append('-')

def extract_warning(page_patterns, truss_dictionary, truss_key):
    """Extracts warning data and appends it to the truss dictionary."""
    warning = page_patterns['warning_found'][0].strip(': Required bearing') if page_patterns['warning_found'] else '-'
    truss_dictionary[truss_key].append(warning)

def compartmentalize_pdf(regex_dict, pdf_data):
    """
    Main function to process PDF pages and organize extracted data into a dictionary.
    """
    truss_dictionary = {}
    # page_storage = read_pdf('Wright Reviewed_24-1180s3b')
    page_storage = pdf_data

    for index, page in enumerate(page_storage):
        page_patterns = find_patterns(page, regex_dict)
        
        if page_patterns['label_found'] and page_patterns['page1_pattern_found'] and not page_patterns['truss_layout_pattern_found']:
            truss_key = page_patterns['label_found'][0].split('Truss')[0]
            
            if truss_key not in truss_dictionary:
                extract_truss_label(page_patterns, truss_dictionary, truss_key)

            extract_design_loads(page_patterns, truss_dictionary, truss_key)
            extract_slope(page_patterns, truss_dictionary, truss_key)
            extract_spacing(page_patterns, truss_dictionary, truss_key)
            extract_wind_data(page_patterns, truss_dictionary, truss_key)
            extract_risk_category(page_patterns, truss_dictionary, truss_key)
            extract_building_code(page_patterns, truss_dictionary, truss_key)
            extract_max_member_stress(page_patterns, truss_dictionary, truss_key)
            extract_deflection_criteria(page_patterns, truss_dictionary, truss_key)
            extract_drag_load(page_patterns, page_storage, index, truss_dictionary, truss_key)
            extract_warning(page_patterns, truss_dictionary, truss_key)

    return truss_dictionary