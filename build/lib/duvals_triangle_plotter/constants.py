"""
Constants for Duval's Triangle Plot Configuration
"""

pd_region = {
                # Get configuration for the PD (Partial Discharges) region in Duval's Triangle plot.
                
                "uid": "pd_region", 
                "a": [98, 1, 98], # methane
                "b": [0, 0, 2],   # acetylene
                "c": [2, 0, 0],   # ethylene
                "fill": "toself", 
                "line": {"color": "#444"}, 
                "mode": "lines", 
                "text": "PD", 
                "type": "scatterternary", 
                "fillcolor": "#b3de69",
                "name": "PD - Corona Partial Discharges"
            }

d1_region = {
            # Get configuration for the D1 (Electrical Discharges of Low Energy) region in Duval's Triangle plot.

            "uid": "d1_region", 
            "a": [0, 0, 64, 87],  # methane
            "b": [1, 77, 13, 13], # acetylene
            "c": [0, 23, 23, 0],  # ethylene
            "fill": "toself", 
            "line": {"color": "#444"}, 
            "mode": "lines", 
            "text": "D1", 
            "type": "scatterternary", 
            "fillcolor": "#ffffb3",
            "name": "D1 - Electrical Discharges of Low Energy"
        }

d2_region = {
            # Get configuration for the D2 (Electrical Discharges of High Energy) region in Duval's Triangle plot.
            "uid": "d2_region", 
            "a": [0, 0, 31, 47, 64],    # methane
            "b": [77, 29, 29, 13, 13],  # acetylene
            "c": [23, 71, 40, 40, 23],  # ethylene
            "fill": "toself", 
            "line": {"color": "#444"}, 
            "mode": "lines", 
            "text": "D2", 
            "type": "scatterternary", 
            "fillcolor": "#bebada",
            "name": "D2 - Electrical Discharges of High Energy"
        }

dt_region = {
            # Get configuration for the DT (Electrical and Thermal Fault) region in Duval's Triangle plot.

            "uid": "dt_region", 
            "a": [0, 0, 35, 46, 96, 87, 47, 31],    # methane
            "b": [29, 15, 15, 4, 4, 13, 13, 29],    # acetylene
            "c": [71, 85, 50, 50, 0, 0, 40, 40],    # ethylene
            "fill": "toself", 
            "line": {"color": "#444"}, 
            "mode": "lines", 
            "text": "DT",
            "hoverlabel": {"font": {"color": "black"}},
            "type": "scatterternary", 
            "fillcolor": "#fb8072",
            "name": "DT - Electrical and Thermal Fault"
        }

t1_region = {
            # Get configuration for the T1 (Thermal Faults, T<300 C) region in Duval's Triangle plot.
   
            "uid": "t1_region", 
            "a": [76, 80, 98, 98, 96],  # methane
            "b": [4, 0, 0, 2, 4],       # acetylene
            "c": [20, 20, 2, 0, 0],     # ethylene
            "fill": "toself", 
            "line": {"color": "#444"}, 
            "mode": "lines", 
            "text": "T1", 
            "type": "scatterternary", 
            "fillcolor": "#80b1d3",
            "name": "T1 - Thermal Faults, T<300C"
        }

t2_region = {
            # Get configuration for the T2 (Thermal Faults, 300 C<T<700 C) region in Duval's Triangle plot.
            "uid": "t2_region", 
            "a": [46, 50, 80, 76],      # methane
            "b": [4, 0, 0, 4],          # acetylene
            "c": [50, 50, 20, 20],      # ethylene
            "fill": "toself", 
            "line": {"color": "#444"}, 
            "mode": "lines", 
            "text": "T2", 
            "type": "scatterternary", 
            "fillcolor": "#fdb462",
            "name": "T2 - Thermal Faults, 300C<T<700C"
        }

t3_region = {
            # Get configuration for the T3 (Thermal Faults, T>700 C) region in Duval's Triangle plot.
            
            "uid": "t3_region", 
            "a": [0, 0, 50, 35],    # methane
            "b": [15, 0, 0, 15],    # acetylene
            "c": [85, 1, 50, 50],   # ethylene
            "fill": "toself", 
            "line": {"color": "#444"}, 
            "mode": "lines", 
            "text": "T3", 
            "type": "scatterternary",
            "fillcolor": "#8dd3c7",
            "name": "T3",
            "name": "T3 - Thermal Faults, T>700C"
        }
