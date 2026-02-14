# params.py
# parameters for Earth 

params = {
    # wavelength and R 
    "lambda": 4.3,  # [mü m]
    "R" : 6.371e6,      # distance from planet center [m] 
    
    # Planet mass and radius 
    "Mpl": 5.972e24,  # [kg]
    "Rpl": 6.371e6,   # [m]

    # Atmospheric properties
    "Tatm": 250.0,          # [K]
    "rho_surf": 2.5e25,     # surface number density [molecules/m^3]
    "mgas": 44.01e-3 / 6.022e23,  # CO2 molecule mass [kg]

    # Cross section file name 
    "cross_section_file": "CO2_mini-project_1.dat.txt" 
}
