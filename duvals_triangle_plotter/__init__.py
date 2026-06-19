"""
duvals_triangle_plotter — Python library for generating Duval's Triangle plots.

Duval's Triangle is a ternary plot used in Dissolved Gas Analysis (DGA) to
diagnose faults in power transformers based on relative concentrations of
methane (CH4), acetylene (C2H2), and ethylene (C2H4).

Public API
----------
get_duval_points_traces(methane_points_list, acetylene_points_list,
                        ethylene_points_list, date)
    Build a scatterternary trace dict from gas concentration data.

get_duvals_triangle_plot(duval_points_list, show_plot=False,
                         equipment_name="General Site")
    Generate a complete Plotly Figure with fault regions and data traces.
"""

from .duvals_triangle_plotter import get_duval_points_traces, get_duvals_triangle_plot
