# Quick Start

This guide walks through a minimal working example. By the end you will have
generated an interactive Duval's Triangle plot from DGA data.

## Prerequisites

Make sure the library is installed:

```bash
pip install duvals-triangle-plotter
```

## Step 1: Import the library

```python
import duvals_triangle_plotter as dtp
```

## Step 2: Prepare gas concentration data

Provide methane (CH<sub>4</sub>), acetylene (C<sub>2</sub>H<sub>2</sub>), and
ethylene (C<sub>2</sub>H<sub>4</sub>) concentrations in ppm. Each parameter
is a list so you can plot multiple samples at once.

```python
methane   = [0.09]
acetylene = [0.0]
ethylene  = [0.91]
date      = "2000-08-16"
```

## Step 3: Create a scatterternary trace

`get_duval_points_traces` builds a Plotly `scatterternary` trace dict from the
concentration data:

```python
trace = dtp.get_duval_points_traces(
    methane, acetylene, ethylene, date
)
```

## Step 4: Generate the figure

`get_duvals_triangle_plot` combines fault region polygons with the data trace
and returns a Plotly Figure:

```python
fig = dtp.get_duvals_triangle_plot(
    [trace], show_plot=True
)
```

Set `show_plot=True` to display the figure immediately. Set it to `False`
when saving or further customising the figure.

## Understanding the output

The resulting figure shows:

- Seven shaded fault regions (PD, D1, D2, DT, T1, T2, T3)
- Your data point plotted as a marker within the ternary axes
- Axis labels for CH<sub>4</sub>, C<sub>2</sub>H<sub>2</sub>, and
  C<sub>2</sub>H<sub>4</sub> percentages
- A title with the equipment name and the Duval's Triangle label
- Hover information showing sample date and gas concentrations

## Using in Jupyter notebooks

This library works natively in Jupyter notebooks. When `show_plot=True`, the
Plotly figure renders inline. No special configuration is needed.

## Full example

```python
import duvals_triangle_plotter as dtp

methane   = [0.09]
acetylene = [0.0]
ethylene  = [0.91]
date      = "2000-08-16"

trace = dtp.get_duval_points_traces(
    methane, acetylene, ethylene, date
)

fig = dtp.get_duvals_triangle_plot(
    [trace], show_plot=True,
    equipment_name="Site 1"
)
```
