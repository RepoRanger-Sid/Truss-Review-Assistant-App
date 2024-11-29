import re

# SCRIPT TO SET REGULAR EXPRESSION PATTERNS


regex_dict = {

    'truss_label_pattern' : re.compile(r'[0-9A-Z]+[0-9-]+[a-zA-Z0-9]*Truss Type'),
    'truss_layout_pattern' : re.compile('PLACEMENT DIAGRAM'),
    'page1_pattern' : re.compile(r'Page 1'),
    'design_load_pattern' : re.compile(r'BCDL[0-9.\n\s*]+'),
    'roof_slope_pattern' : re.compile(r'([0-9][.][0-9]{2}) 12[0-9\n]*[a-zA-Z]*'),
    'floor_slope_pattern' : re.compile(r'Unbalanced floor live'),
    'truss_spacing_pattern' : re.compile(r'Code[0-9-]+'),
    'wind_standard_pattern' : re.compile(r'Wind:[a-zA-Z0-9\s-]+'),
    'wind_speed_pattern' : re.compile(r'Vult=[a-zA-Z0-9]+'),
    'risk_category_pattern' : re.compile(r'Cat.\n[A-Z]+'),
    'building_code_pattern' : re.compile(r'I[B|R]C[0-9]+'),
    'max_member_stress_pattern' : re.compile(r'[\n0-9.]+DEFL'),
    'actual_deflection_pattern' : re.compile(r'defl[\n(.*>*\d*|n/r|n/a)]+'),
    'design_deflection_criteria_pattern' : re.compile(r'L/d\n[0-9]+\n[0-9]+'),
    'drag_load_pattern' : re.compile(r'[total|seismic] drag [a-zA-Z0-9\s]+'),
    'warning_pattern' : re.compile(r'WARNING: Required bearing'),

}