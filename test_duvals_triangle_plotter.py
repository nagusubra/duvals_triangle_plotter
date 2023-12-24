import plotly.graph_objects as go
from duvals_triangle_plotter.duvals_triangle_plotter import get_duval_points_traces, get_duvals_triangle_plot

# step 1: install pytest (pip install pytest)
# step 2: run pytest test_duval_plot.py in the command prompt to test the package

def test_get_duvals_triangle_plot():
    # Sample data for testing
    methane_points_list = [0.09] # units = ppm
    acetylene_points_list = [0.0] # units = ppm
    ethylene_points_list = [0.91] # units = ppm
    date = "2000-08-16"

    # Call the function to get Duval's Triangle traces
    duval_trace = get_duval_points_traces(methane_points_list, acetylene_points_list, ethylene_points_list, date)

    # Call the function to get Duval's Triangle plot
    fig = get_duvals_triangle_plot([duval_trace])

    # Check if the returned object is a Plotly Figure
    assert isinstance(fig, go.Figure)

    # Optional: Add more specific assertions based on your requirements
    # For example, you can check if certain properties are set correctly in the layout.

    # Uncomment the following lines if you want to add more specific assertions
    # assert fig.layout.title.text == "<b>Duval's Triangle (Dissolved Gas Analysis) for : General Site</b>"
    # assert fig.layout.ternary.sum == 100

if __name__ == "__main__":
    test_get_duvals_triangle_plot()
