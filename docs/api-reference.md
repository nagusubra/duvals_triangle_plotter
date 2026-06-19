# API Reference

The library exposes two primary functions and one internal layout helper.

## `get_duval_points_traces()`

Build a Plotly `scatterternary` trace dict from gas concentration data. Each
call produces one trace representing a group of samples.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `methane_points_list` | `list[float]` | CH<sub>4</sub> concentrations in ppm for each sample |
| `acetylene_points_list` | `list[float]` | C<sub>2</sub>H<sub>2</sub> concentrations in ppm for each sample |
| `ethylene_points_list` | `list[float]` | C<sub>2</sub>H<sub>4</sub> concentrations in ppm for each sample |
| `date` | `str` | Label or date for the sample set (shown in legend and hover tooltip) |

### Returns

| Type | Description |
|------|-------------|
| `dict` | A Plotly `scatterternary` trace dictionary with marker styling and hover template |

### Example

```python
trace = dtp.get_duval_points_traces(
    [0.09, 0.15],
    [0.0, 0.02],
    [0.91, 0.83],
    "Transformer A"
)
```

## `get_duvals_triangle_plot()`

Generate a complete Duval's Triangle Plotly figure with the seven standard
fault regions and one or more data traces overlaid.

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `duval_points_list` | `list[dict]` | — | List of trace dicts from `get_duval_points_traces` |
| `show_plot` | `bool` | `False` | If `True`, display the figure immediately |
| `equipment_name` | `str` | `"General Site"` | Transformer or site name displayed in the plot title |

### Returns

| Type | Description |
|------|-------------|
| `plotly.graph_objects.Figure` | A Plotly Figure with seven fault region traces and data traces |

### Example

```python
trace = dtp.get_duval_points_traces(
    [0.09], [0.0], [0.91], "2000-08-16"
)
fig = dtp.get_duvals_triangle_plot(
    [trace],
    show_plot=True,
    equipment_name="Site 1"
)
```

## `get_layout()` (internal)

Build the plot layout configuration including ternary axis titles, margins,
and title text. Called internally by `get_duvals_triangle_plot`. Not typically
needed for end-user code.

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `equipment_name` | `str` | Name of the transformer or equipment displayed in the plot title |

### Returns

| Type | Description |
|------|-------------|
| `dict` | Plotly layout dictionary with axis configuration, size, and title |

### Layout details

- Ternary axes are labelled **CH<sub>4</sub> (Methane)**,
  **C<sub>2</sub>H<sub>2</sub> (Acetylene)**,
  and **C<sub>2</sub>H<sub>4</sub> (Ethylene)**
- Axis range is 0.01% to 100% with tick suffix "%"
- Plotly's `autosize` is enabled for responsive sizing
- Title format: **Duval's Triangle (Dissolved Gas Analysis) for : &lt;equipment_name&gt;**
