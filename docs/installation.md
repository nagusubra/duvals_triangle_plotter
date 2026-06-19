# Installation

## Install with pip

The recommended way to install **duvals-triangle-plotter** is via pip from
PyPI:

```bash
pip install duvals-triangle-plotter
```

## Python Version Support

This library supports Python 3.6 and later, including Python 3.7, 3.8, 3.9,
3.10, 3.11, and 3.12.

## Dependencies

The only required dependency is **Plotly** 5.0 or higher, which is installed
automatically with the package:

```bash
# Plotly is pulled in automatically
pip install duvals-triangle-plotter
```

Plotly provides the interactive plotting backend used to render Duval's
Triangle figures in Jupyter notebooks, browsers, and standalone scripts.

## Verify Installation

Run the following Python code to confirm the package installed correctly:

```python
import duvals_triangle_plotter as dtp
print(dtp.__version__)
```

## Upgrading

To upgrade to the latest version:

```bash
pip install --upgrade duvals-triangle-plotter
```

## Troubleshooting

**Permission errors.** If you encounter permission errors on Linux or macOS,
try installing in a virtual environment or use:

```bash
pip install --user duvals-triangle-plotter
```

**Plotly not found.** If Plotly is missing despite installation, install it
explicitly:

```bash
pip install "plotly>=5.0"
```

**Virtual environment recommended.** We recommend installing in a Python
virtual environment to avoid conflicts with other packages:

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS / Linux:
# source venv/bin/activate
pip install duvals-triangle-plotter
```
