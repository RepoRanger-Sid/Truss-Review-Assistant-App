def get_input_data(
        design_roof_dead_load=21,
        design_floor_dead_load=18,
        design_roof_live_load_more_slope=16,
        design_roof_live_load_less_slope=20,
        design_floor_live_load=40,
        actual_truss_spacing=2,
        design_wind_standard='ASCE 7-16',
        design_wind_speed=115,
        design_risk_category='II',
        design_building_code='IRC 2018',
        design_roof_live_load_deflection_criteria=360,
        design_roof_total_load_deflection_criteria=240,
        design_floor_live_load_deflection_criteria=480,
        design_floor_total_load_deflection_criteria=360,
):
    """
    Collects design input parameters for truss review analysis.

    Parameters:
    - design_roof_dead_load (float): Dead load for the roof in psf.
    - design_floor_dead_load (float): Dead load for the floor in psf.
    - design_roof_live_load_more_slope (float): Live load for roof with more slope in psf.
    - design_roof_live_load_less_slope (float): Live load for roof with less slope in psf.
    - design_floor_live_load (float): Live load for the floor in psf.
    - actual_truss_spacing (float): Spacing between trusses in inches.
    - design_wind_standard (str): Wind design standard used.
    - design_wind_speed (float): Design wind speed in mph.
    - design_risk_category (str): Risk category of the building.
    - design_building_code (str): Building code used for design.
    - design_roof_live_load_deflection_criteria (int): Deflection criteria for live load on roof.
    - design_roof_total_load_deflection_criteria (int): Deflection criteria for total load on roof.
    - design_floor_live_load_deflection_criteria (int): Deflection criteria for live load on floor.
    - design_floor_total_load_deflection_criteria (int): Deflection criteria for total load on floor.

    Returns:
    dict: A dictionary containing all design parameters with their values.
    """
    
    return {
        "design_roof_dead_load": design_roof_dead_load,
        "design_floor_dead_load": design_floor_dead_load,
        "design_roof_live_load_more_slope": design_roof_live_load_more_slope,
        "design_roof_live_load_less_slope": design_roof_live_load_less_slope,
        "design_floor_live_load": design_floor_live_load,
        "actual_truss_spacing": actual_truss_spacing,
        "design_wind_standard": design_wind_standard,
        "design_wind_speed": design_wind_speed,
        "design_risk_category": design_risk_category,
        "design_building_code": design_building_code,
        "design_roof_live_load_deflection_criteria": design_roof_live_load_deflection_criteria,
        "design_roof_total_load_deflection_criteria": design_roof_total_load_deflection_criteria,
        "design_floor_live_load_deflection_criteria": design_floor_live_load_deflection_criteria,
        "design_floor_total_load_deflection_criteria": design_floor_total_load_deflection_criteria,
    }