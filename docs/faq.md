# Frequently Asked Questions

## What is Duval's Triangle?

Duval's Triangle is a graphical method for interpreting Dissolved Gas
Analysis (DGA) data in power transformers. It plots three hydrocarbon gases
(methane, acetylene, ethylene) on a ternary diagram to classify faults into
seven regions: PD, D1, D2, DT, T1, T2, and T3.

## How do I install the Duval's Triangle Plotter library?

Run `pip install duvals-triangle-plotter`. The library requires Python 3.6 or
higher and Plotly 5 or higher (installed automatically as a dependency). See
the [Installation page](installation.md) for details.

## What inputs does the library expect?

The library expects three lists of gas concentrations (methane, acetylene,
ethylene) in ppm, plus a date or label string for each sample group. See the
[Quick Start](quickstart.md) guide for a working example.

## What does the library output?

It returns a Plotly Figure object with seven shaded fault regions and the
user's data points plotted as markers. The figure can be displayed
(`show_plot=True`), saved as HTML (`fig.write_html()`), or exported as an
image.

## What do PD, D1, D2, DT, T1, T2, and T3 mean?

These are the seven fault regions in Duval's Triangle:

- **PD** — Corona / Partial Discharges
- **D1** — Low-Energy Discharges (sparking)
- **D2** — High-Energy Discharges (arcing)
- **DT** — Mixed Electrical and Thermal Fault
- **T1** — Thermal Fault under 300°C
- **T2** — Thermal Fault 300–700°C
- **T3** — Thermal Fault over 700°C

See the [Fault Regions](fault-regions.md) page for detailed explanations.

## Does this library work in Jupyter notebooks?

Yes, the library works natively in Jupyter notebooks. Plotly figures render
inline when `show_plot=True`. No special extensions or configuration are
required.

## Why Plotly instead of matplotlib?

Plotly provides interactive, zoomable figures that work in Jupyter notebooks
and browsers without plugins. Figures can be saved as standalone HTML files,
making them easy to share with colleagues who may not have Python installed.

## Why use this library instead of manual plotting?

Manual plotting requires calculating gas ratios, defining fault region polygon
coordinates, configuring ternary axes, and colouring each region. This library
automates all of that — provide gas concentrations and receive a
publication-ready figure with all seven fault regions correctly shaded and
labelled.

## How is Duval's Triangle different from other DGA methods?

Unlike ratio-based methods (IEC, Roger's Ratio), Duval's Triangle provides a
visual representation of DGA data that is intuitive to interpret. Unlike the
Key Gas method, it uses standardised region boundaries, making results
consistent across analysts and laboratories. The
[Duval's Triangle Explained](duvals-triangle-explained.md) page has a
comparison table.

## Can I use this library in scripts and web applications?

Yes. Use `show_plot=False` to get the Figure object without displaying it,
then save as HTML with `fig.write_html()` or embed it in a Dash, Flask, or
other web application. Plotly figures are fully interactive when embedded.

## Is this library suitable for automated reporting pipelines?

Yes. The library's programmatic API makes it ideal for automated reporting.
You can generate plots for multiple transformers in a loop, customise
equipment names, and export figures as HTML or PNG for inclusion in condition
monitoring reports.

## How should someone interpret the plot?

Look at which fault region the data point falls in. The region label (PD, D1,
D2, DT, T1, T2, or T3) indicates the most likely fault type. Points near
region boundaries may indicate mixed fault conditions and should be
interpreted alongside additional DGA methods and diagnostic tests for a
comprehensive assessment.

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "What is Duval's Triangle?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Duval's Triangle is a graphical method for interpreting Dissolved Gas Analysis (DGA) data in power transformers. It plots three hydrocarbon gases (methane, acetylene, ethylene) on a ternary diagram to classify faults into seven regions: PD, D1, D2, DT, T1, T2, and T3."
            }
        },
        {
            "@type": "Question",
            "name": "How do I install the Duval's Triangle Plotter library?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Run 'pip install duvals-triangle-plotter'. Requires Python 3.6+ and Plotly 5+ (installed automatically)."
            }
        },
        {
            "@type": "Question",
            "name": "What inputs does the library expect?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "The library expects three lists of gas concentrations (methane, acetylene, ethylene) in ppm, plus a date or label string for each sample group."
            }
        },
        {
            "@type": "Question",
            "name": "What does the library output?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "It returns a Plotly Figure object with seven shaded fault regions and the user's data points plotted as markers. The figure can be displayed, saved as HTML, or exported as an image."
            }
        },
        {
            "@type": "Question",
            "name": "What do PD, D1, D2, DT, T1, T2, and T3 mean?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "PD = Corona/Partial Discharges, D1 = Low-Energy Discharges (sparking), D2 = High-Energy Discharges (arcing), DT = Mixed Electrical and Thermal Fault, T1 = Thermal Fault under 300°C, T2 = Thermal Fault 300-700°C, T3 = Thermal Fault over 700°C."
            }
        },
        {
            "@type": "Question",
            "name": "Does this library work in Jupyter notebooks?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes, the library works natively in Jupyter notebooks. Plotly figures render inline when show_plot=True. No special extensions are required."
            }
        },
        {
            "@type": "Question",
            "name": "Why Plotly instead of matplotlib?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Plotly provides interactive, zoomable figures that work in Jupyter notebooks and browsers without plugins. Figures can be saved as standalone HTML files, making them easy to share with colleagues who may not have Python installed."
            }
        },
        {
            "@type": "Question",
            "name": "Why use this library instead of manual plotting?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Manual plotting requires calculating gas ratios, defining fault region polygons, and configuring ternary axes. This library automates all of that — provide gas concentrations and receive a publication-ready figure with all seven fault regions correctly shaded and labelled."
            }
        },
        {
            "@type": "Question",
            "name": "How is Duval's Triangle different from other DGA methods?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Unlike ratio-based methods (IEC, Roger's), Duval's Triangle provides a visual representation of DGA data. Unlike the Key Gas method, it uses standardised region boundaries, making results consistent across analysts."
            }
        },
        {
            "@type": "Question",
            "name": "Can I use this library in scripts and web applications?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Use show_plot=False to get the Figure object without displaying it, then save as HTML with fig.write_html() or embed in a Dash or Flask application."
            }
        },
        {
            "@type": "Question",
            "name": "Is this library suitable for automated reporting pipelines?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. The library's programmatic API makes it ideal for automated reporting. You can generate plots for multiple transformers in a loop and export them as HTML or PNG for inclusion in reports."
            }
        },
        {
            "@type": "Question",
            "name": "How should someone interpret the plot?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Look at which fault region the data point falls in. The region label (PD, D1, D2, DT, T1, T2, or T3) indicates the most likely fault type. Points near region boundaries may indicate mixed fault conditions and should be interpreted with additional DGA methods."
            }
        }
    ]
}
</script>
