from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from user_input import get_input_data
from execute import execute
from pattern import regex_dict
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Handle file upload
        if 'fileInput' not in request.files:
            return jsonify({'success': False, 'message': 'No file uploaded'})
        
        file = request.files['fileInput']
        if file.filename == '':
            return jsonify({'success': False, 'message': 'No file selected'})
            
        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
        
        # Get form data and create input_data dictionary
        input_data = get_input_data(
            design_roof_dead_load=float(request.form.get('roofDeadLoad', 21)),
            design_floor_dead_load=float(request.form.get('floorDeadLoad', 18)),
            design_roof_live_load_more_slope=float(request.form.get('roofLiveLoadSteep', 16)),
            design_roof_live_load_less_slope=float(request.form.get('roofLiveLoadShallow', 20)),
            design_floor_live_load=float(request.form.get('floorLiveLoad', 40)),
            actual_truss_spacing=float(request.form.get('trussSpacing', 2)),
            design_wind_standard=request.form.get('windStandard', 'ASCE 7-16'),
            design_wind_speed=float(request.form.get('windSpeed', 115)),
            design_risk_category=request.form.get('riskCategory', 'II'),
            design_building_code=request.form.get('buildingCode', 'IRC 2018'),
            design_roof_live_load_deflection_criteria=int(request.form.get('roofLiveDeflection', 'L/360').split('/')[1]),
            design_roof_total_load_deflection_criteria=int(request.form.get('roofTotalDeflection', 'L/240').split('/')[1]),
            design_floor_live_load_deflection_criteria=int(request.form.get('floorLiveDeflection', 'L/360').split('/')[1]),
            design_floor_total_load_deflection_criteria=int(request.form.get('floorTotalDeflection', 'L/240').split('/')[1])
        )

        # Execute analysis
        execute(input_data, filepath, regex_dict)
        
        # Get the output file path
        output_file = f'Truss Review Results_{os.path.splitext(os.path.basename(filepath))[0]}.xlsx'
        output_path = os.path.abspath(output_file)
        
        return jsonify({
            'success': True, 
            'message': 'Analysis completed successfully',
            'output_path': output_path
        })

    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True)