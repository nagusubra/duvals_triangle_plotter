# Examples

This page shows practical code examples for common use cases. All examples
assume the library is installed (`pip install duvals-triangle-plotter`) and
imported as `dtp`.

## Example 1: Single Sample Plot

Plot one DGA data point from a single transformer sample:

```python
import duvals_triangle_plotter as dtp

# Gas concentrations in ppm
methane   = [0.09]
acetylene = [0.0]
ethylene  = [0.91]
date      = "2000-08-16"

trace = dtp.get_duval_points_traces(
    methane, acetylene, ethylene, date
)

fig = dtp.get_duvals_triangle_plot(
    [trace],
    show_plot=True,
    equipment_name="Site 1"
)
```

This generates a figure with the seven fault regions and the sample point
plotted as a black diamond marker. The hover tooltip shows the sample date
and gas percentages.

## Example 2: Multiple Samples Overlaid

Compare multiple DGA samples on the same plot to track changes over time:

```python
import duvals_triangle_plotter as dtp

# Sample 1
trace1 = dtp.get_duval_points_traces(
    [0.09], [0.0], [0.91], "2000-08-16"
)
# Sample 2 (taken three months later)
trace2 = dtp.get_duval_points_traces(
    [0.12], [0.01], [0.87], "2000-11-22"
)
# Sample 3
trace3 = dtp.get_duval_points_traces(
    [0.05], [0.03], [0.92], "2001-02-14"
)

# Combine all traces
fig = dtp.get_duvals_triangle_plot(
    [trace1, trace2, trace3],
    show_plot=True,
    equipment_name="Transformer B - Trend"
)
```

Each sample appears as a separate trace in the legend, making it easy to
visualise how gas concentrations and fault classifications evolve over time.

## Example 3: Custom Equipment Name

Identify each plot with the specific transformer or site name:

```python
trace = dtp.get_duval_points_traces(
    [0.09], [0.0], [0.91], "TX-1001"
)

fig = dtp.get_duvals_triangle_plot(
    [trace],
    show_plot=True,
    equipment_name="TX-1001 / North Substation"
)
```

The equipment name appears in the plot title:
**Duval's Triangle (Dissolved Gas Analysis) for : TX-1001 / North Substation**.

## Example 4: Saving Figure to HTML

Export the plot as a standalone HTML file for sharing or embedding:

```python
trace = dtp.get_duval_points_traces(
    [0.09], [0.0], [0.91], "2000-08-16"
)

fig = dtp.get_duvals_triangle_plot(
    [trace], show_plot=False
)

# Save as interactive HTML
fig.write_html("duvals_triangle_plot.html")
```

Set `show_plot=False` when saving programmatically to avoid opening the figure
in a browser.

## Example 5: Using in a Jupyter Notebook

This library works natively in Jupyter notebooks. Simply call
`get_duvals_triangle_plot` with `show_plot=True` and the Plotly figure renders
inline:

```python
# In a Jupyter notebook cell:
import duvals_triangle_plotter as dtp

trace = dtp.get_duval_points_traces(
    [0.09], [0.0], [0.91], "2000-08-16"
)

fig = dtp.get_duvals_triangle_plot(
    [trace], show_plot=True
)
```

No special configuration or extensions are required. The interactive Plotly
figure supports zoom, pan, and hover inspection directly in the notebook.
