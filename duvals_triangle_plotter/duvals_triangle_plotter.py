import plotly.graph_objects as go
from duvals_triangle_plotter.constants import pd_region, d1_region, d2_region, dt_region, t1_region, t2_region, t3_region


def get_layout(equipment_name: str):
    """Build a layout dictionary for the Duval's Triangle ternary plot.

    Parameters
    ----------
    equipment_name : str
        Name of the transformer or equipment displayed in the plot title.

    Returns
    -------
    dict
        Plotly layout configuration with ternary axes, margins, and title.

    Examples
    --------
    >>> layout = get_layout("Transformer A")
    >>> layout["title"]
    "<b>Duval's Triangle (Dissolved Gas Analysis) for : Transformer A</b>"
    """
    layout = {
                "title": "<b>Duval's Triangle (Dissolved Gas Analysis) for : {0}</b>".format(equipment_name),
                "width": 1044*1.8,
                "height": 545*1.8,
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
    """Create a Plotly scatterternary trace from gas concentration data.

    Parameters
    ----------
    methane_points_list : list of float
        Concentration of methane (CH4) for each sample, in ppm.
    acetylene_points_list : list of float
        Concentration of acetylene (C2H2) for each sample, in ppm.
    ethylene_points_list : list of float
        Concentration of ethylene (C2H4) for each sample, in ppm.
    date : str
        Label or date associated with the samples (displayed in legend and hover).

    Returns
    -------
    dict
        A dict representing a Plotly ``scatterternary`` trace, ready to be
        passed to ``get_duvals_triangle_plot``.

    Examples
    --------
    >>> trace = get_duval_points_traces([0.09], [0.0], [0.91], "2000-08-16")
    >>> trace["type"]
    'scatterternary'
    """
    duval_points =  {
                    "a": methane_points_list,
                    "b": acetylene_points_list,
                    "c": ethylene_points_list,
                    "mode": "markers",
                    "type": "scatterternary",
                    "marker":   {
                                    "size": 18,
                                    "color": "black",
                                    "symbol": 217,
                                },
                    "cliponaxis": True,
                    "hovertemplate":  "Sample Date: {0}<br>".format(date) + "Methane (CH4): %{a:.2f}%<br>" + "Acetylene (C2H2): %{b:.2f}%<br>" + "Ethylene (C2H4): %{c:.2f}%<br>",
                    "name": "Sample Date: {0}<br>".format(date)
                }

    return duval_points


def get_duvals_triangle_plot(duval_points_list: list, show_plot:bool = False, equipment_name:str = "General Site"):
    """Generate a complete Duval's Triangle Plotly Figure.

    The figure overlays the seven standard fault regions (PD, D1, D2, DT, T1,
    T2, T3) with the user-supplied data traces.

    Parameters
    ----------
    duval_points_list : list of dict
        One or more scatterternary trace dicts, typically created by
        ``get_duval_points_traces``.
    show_plot : bool, optional
        If True, display the figure immediately in the browser (default False).
    equipment_name : str, optional
        Name of the equipment shown in the plot title (default "General Site").

    Returns
    -------
    go.Figure
        A Plotly Figure containing the Duval's Triangle plot with fault
        regions and data points.

    Examples
    --------
    >>> trace = get_duval_points_traces([0.09], [0.0], [0.91], "2000-08-16")
    >>> fig = get_duvals_triangle_plot([trace], show_plot=False)
    >>> isinstance(fig, go.Figure)
    True
    """
    data = [pd_region, d1_region, d2_region, dt_region, t1_region, t2_region, t3_region]
    data.extend(duval_points_list)

    fig = go.Figure(data=data, layout = get_layout(equipment_name))
    fig.update_layout(get_layout(equipment_name))

    if show_plot:
        fig.show()

    return fig
