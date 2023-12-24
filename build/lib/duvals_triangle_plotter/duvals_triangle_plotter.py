import plotly.graph_objects as go
from duvals_triangle_plotter.constants import pd_region, d1_region, d2_region, dt_region, t1_region, t2_region, t3_region

def get_layout(equipment_name: str):

    """
    Generate layout configuration for Duval's Triangle plot.

    Parameters:
    - equipment_name (str): The name of the equipment for which the Duval's Triangle is plotted.

    Returns:
    dict: A dictionary containing layout configuration for the Duval's Triangle plot.
    """

    layout = {
                "title": "<b>Duval's Triangle (Dissolved Gas Analysis) for : {0}</b>".format(equipment_name), 
                "width": 1044*1.8,  # adjust respectively
                "height": 545*1.8,  # adjust respectively
                "ternary": {
                                "sum": 100, 
                                "aaxis": {
                                            "min": 0.01, 
                                            "ticks": "outside", 
                                            "title": "<b> CH4 (Methane) </b>", 
                                            "linewidth": 8, 
                                            "ticksuffix": "%",
                                        }, 
                                "baxis": {
                                            "min": 0.01, 
                                            "ticks": "outside", 
                                            "title": "<b> C2H2 (Acetylene) </b>", 
                                            "linewidth": 8, 
                                            "ticksuffix": "%"
                                        }, 
                                "caxis": {
                                            "min": 0.01, 
                                            "ticks": "outside", 
                                            "title": "<b> C2H4 (Ethylene) </b>", 
                                            "linewidth": 8, 
                                            "ticksuffix": "%"
                                        }
                }, 
                "autosize": True, 
                "showlegend": True,
                "margin": {"pad":100},
            }
    return layout

def get_duval_points_traces(methane_points_list: list, acetylene_points_list: list, ethylene_points_list: list, date: str):
    
    """
    Get traces for Duval's Triangle points.

    Parameters:
    - methane_points_list (list): List of methane points where each element is concentration level of methane in ppm.
    - acetylene_points_list (list): List of acetylene points where each element is concentration level of acetylene in ppm.
    - ethylene_points_list (list): List of ethylene points where each element is concentration level of ethylene in ppm.
    - date (str): Date associated with the samples.

    Returns:
    dict: A dictionary containing traces for Duval's Triangle points.
    """

    duval_points =  {
                    "a": methane_points_list,       # methane
                    "b": acetylene_points_list,     # acetylene
                    "c": ethylene_points_list,      # ethylene
                    "mode": "markers", 
                    "type": "scatterternary", 
                    "marker":   {
                                    "size": 18,     # adjust respectively
                                    "color": "black", 
                                    "symbol": 217,  # a different symbol number would give a different marker style
                                },
                    "cliponaxis": True,
                    "hovertemplate":  "Sample Date: {0}<br>".format(date) + "Methane (CH4): %{a:.2f}%<br>" + "Acetylene (C2H2): %{b:.2f}%<br>" + "Ethylene (C2H4): %{c:.2f}%<br>",
                    "name": "Sample Date: {0}<br>".format(date)
                }
    
    return duval_points

def get_duvals_triangle_plot(duval_points_list: list, show_plot:bool = False, equipment_name:str = "General Site"):
    
    """
    Generate Duval's Triangle plot.

    Parameters:
    - duval_points_list (list): List of Duval's Triangle points.
    - show_plot (bool): Flag to determine whether to display the plot.
    - equipment_name (str): Name of the equipment for which the plot is generated.

    Returns:
    go.Figure: A Plotly Figure containing Duval's Triangle plot.
    """
    
    # print("The data of recieved duval_points_list: ", duval_points_list)

    data = [pd_region, d1_region, d2_region, dt_region, t1_region, t2_region, t3_region]
    data.extend(duval_points_list)
    
    fig = go.Figure(data=data, layout = get_layout(equipment_name))
    fig.update_layout(get_layout(equipment_name))
    
    if show_plot:
        fig.show()
    
    return fig