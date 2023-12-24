# Duval's Triangle Plotter

Duval's Triangle Plotter is a Python library for generating Duval's Triangle plots, which are commonly used in Dissolved Gas Analysis (DGA) for monitoring power transformers.

## Introduction

Duval's Triangle is a graphical representation used in DGA to analyze the concentration levels of different gases, such as methane, acetylene, and ethylene, dissolved in transformer oil. This project provides a Python library that allows users to easily create Duval's Triangle plots for their DGA data.

## Features

- Generate Duval's Triangle plots with customizable configurations.
- Plot various regions on Duval's Triangle, such as PD (Partial Discharges), D1, D2, DT, T1, T2, and T3.
- Customize layout, colors, and symbols for better visualization.

## Getting Started

### Installation
```bash
pip install duvals-triangle-plotter
```

### Usage
```python
import duvals_triangle_plotter as dtp

duval_points = [
    dtp.get_duval_points_traces([0.09], [0.0], [0.91], "2000-08-16")
]

dtp.get_duvals_triangle_plot(duval_points, show_plot=True)
```