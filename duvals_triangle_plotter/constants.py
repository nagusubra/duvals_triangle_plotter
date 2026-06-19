"""
Region definitions for Duval's Triangle.

Each constant is a Plotly ``scatterternary`` trace that fills a polygon
corresponding to a specific fault type identified by Dissolved Gas Analysis.

The seven standard regions defined here are used by
``get_duvals_triangle_plot`` to render the diagnostic zones on the ternary
plot.  Coordinates represent relative percentages of methane (a-axis),
acetylene (b-axis), and ethylene (c-axis) after normalising the three gas
concentrations to 100 %.
"""

pd_region = {
    # PD — Corona / Partial Discharges.
    # Low-energy electrical discharges within gas-filled cavities in the
    # insulation.  Typically the first sign of insulation aging.
    "uid": "pd_region",
    "a": [98, 1, 98],
    "b": [0, 0, 2],
    "c": [2, 0, 0],
    "fill": "toself",
    "line": {"color": "#444"},
    "mode": "lines",
    "text": "PD",
    "type": "scatterternary",
    "fillcolor": "#b3de69",
    "name": "PD - Corona Partial Discharges"
}

d1_region = {
    # D1 — Electrical Discharges of Low Energy.
    # Low-energy sparking or arcing, often associated with poor connections or
    # floating-potential components.
    "uid": "d1_region",
    "a": [0, 0, 64, 87],
    "b": [1, 77, 13, 13],
    "c": [0, 23, 23, 0],
    "fill": "toself",
    "line": {"color": "#444"},
    "mode": "lines",
    "text": "D1",
    "type": "scatterternary",
    "fillcolor": "#ffffb3",
    "name": "D1 - Electrical Discharges of Low Energy"
}

d2_region = {
    # D2 — Electrical Discharges of High Energy.
    # High-energy arcing capable of producing significant volumes of fault gas
    # and causing rapid insulation degradation.
    "uid": "d2_region",
    "a": [0, 0, 31, 47, 64],
    "b": [77, 29, 29, 13, 13],
    "c": [23, 71, 40, 40, 23],
    "fill": "toself",
    "line": {"color": "#444"},
    "mode": "lines",
    "text": "D2",
    "type": "scatterternary",
    "fillcolor": "#bebada",
    "name": "D2 - Electrical Discharges of High Energy"
}

dt_region = {
    # DT — Electrical and Thermal Fault (Mixed).
    # A mixed-fault zone where both electrical discharges and thermal
    # decomposition contribute to the gas profile.
    "uid": "dt_region",
    "a": [0, 0, 35, 46, 96, 87, 47, 31],
    "b": [29, 15, 15, 4, 4, 13, 13, 29],
    "c": [71, 85, 50, 50, 0, 0, 40, 40],
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
    # T1 — Thermal Faults, T < 300 C.
    # Low-temperature thermal faults, typically from prolonged overload or
    # inadequate cooling.
    "uid": "t1_region",
    "a": [76, 80, 98, 98, 96],
    "b": [4, 0, 0, 2, 4],
    "c": [20, 20, 2, 0, 0],
    "fill": "toself",
    "line": {"color": "#444"},
    "mode": "lines",
    "text": "T1",
    "type": "scatterternary",
    "fillcolor": "#80b1d3",
    "name": "T1 - Thermal Faults, T<300C"
}

t2_region = {
    # T2 — Thermal Faults, 300 C < T < 700 C.
    # Medium-temperature thermal faults, often from localised hot spots in the
    # core or windings.
    "uid": "t2_region",
    "a": [46, 50, 80, 76],
    "b": [4, 0, 0, 4],
    "c": [50, 50, 20, 20],
    "fill": "toself",
    "line": {"color": "#444"},
    "mode": "lines",
    "text": "T2",
    "type": "scatterternary",
    "fillcolor": "#fdb462",
    "name": "T2 - Thermal Faults, 300C<T<700C"
}

t3_region = {
    # T3 — Thermal Faults, T > 700 C.
    # High-temperature thermal faults, typically from sustained arcing or
    # severe core overheating.
    "uid": "t3_region",
    "a": [0, 0, 50, 35],
    "b": [15, 0, 0, 15],
    "c": [85, 1, 50, 50],
    "fill": "toself",
    "line": {"color": "#444"},
    "mode": "lines",
    "text": "T3",
    "type": "scatterternary",
    "fillcolor": "#8dd3c7",
    "name": "T3 - Thermal Faults, T>700C"
}
