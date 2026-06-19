# Duval's Triangle Plotter

Python library for generating [Duval's Triangle](https://nagusubra.github.io/duvals-triangle-plotter) plots — a ternary diagnostic tool used in Dissolved Gas Analysis (DGA) for power transformer condition monitoring.

## Installation

```bash
pip install duvals-triangle-plotter
```

## Quick Start

```python
import duvals_triangle_plotter as dtp

trace = dtp.get_duval_points_traces(
    [0.09], [0.0], [0.91], "2000-08-16"
)
fig = dtp.get_duvals_triangle_plot([trace], show_plot=True)
```

## Documentation

Full documentation and API reference: [nagusubra.github.io/duvals-triangle-plotter](https://nagusubra.github.io/duvals-triangle-plotter)

## License

MIT
