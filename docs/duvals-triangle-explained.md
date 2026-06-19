# What is Duval's Triangle?

Duval's Triangle is a graphical method for interpreting Dissolved Gas
Analysis (DGA) data in power transformers. It plots three hydrocarbon gases
as relative percentages on a ternary diagram and classifies the transformer's
operating condition based on which region the data point falls in.

## What is Dissolved Gas Analysis (DGA)?

Dissolved Gas Analysis is a diagnostic technique that measures the
concentrations of gases dissolved in transformer insulating oil. When a
transformer experiences a fault — electrical or thermal — the oil and paper
insulation decompose, releasing characteristic gases. By analysing the types
and quantities of these gases, engineers can identify the nature and severity
of the fault without taking the transformer offline.

## The Three Gases

Duval's Triangle specifically uses three hydrocarbon gases:

| Gas | Formula | Primary Indicator Of |
|-----|---------|---------------------|
| Methane | CH<sub>4</sub> | Low-temperature thermal faults and partial discharges |
| Acetylene | C<sub>2</sub>H<sub>2</sub> | Electrical discharges (arcing and sparking) |
| Ethylene | C<sub>2</sub>H<sub>4</sub> | High-temperature thermal faults |

## How the Triangle Works

1. **Normalise concentrations.** The three gas concentrations are converted to
   relative percentages that sum to 100%.
2. **Plot the point.** The normalised values are plotted on a ternary
   (triangular) plot where each corner represents 100% of one gas.
3. **Identify the fault region.** The location of the data point on the
   triangle determines the fault classification based on empirically defined
   region boundaries.

## Why Duval's Triangle?

Duval's Triangle is one of the most widely used DGA interpretation methods
globally. It is recommended by major standards organisations and transformer
manufacturers for several reasons:

| Method | Visual | Standardised | Easy to automate |
|--------|--------|-------------|-----------------|
| Duval's Triangle | Yes | Yes | Yes |
| IEC Ratio Method | No | Yes | Yes |
| Key Gas Method | Yes | No | No |
| Roger's Ratio | No | Yes | Yes |

The visual nature of Duval's Triangle makes it particularly useful for
communicating findings to non-specialist stakeholders, while standardised
region boundaries ensure consistent results across analysts and laboratories.

## Why Plotly for Duval's Triangle?

This library uses Plotly as its plotting backend because:

- **Interactivity.** Plotly figures are zoomable, hover-enabled, and support
  real-time panning — ideal for examining dense data points.
- **Notebook support.** Plotly renders natively in Jupyter notebooks without
  additional plugins.
- **Web export.** Figures can be saved as standalone HTML files, embedded in
  web pages, or exported as PNG/SVG images.
- **Programmatic control.** Every aspect of the plot can be customised through
  Python code, making it suitable for automated reporting pipelines.

## Relationship to Transformer Diagnostics

Duval's Triangle is part of a broader DGA workflow. It is typically used
alongside other diagnostic methods such as gas ratio analysis, key gas
analysis, and furan analysis to build a comprehensive picture of transformer
health. Regular DGA monitoring using Duval's Triangle can detect developing
faults months or years before they lead to failure, enabling condition-based
maintenance and reducing unplanned outages.

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "What is Duval's Triangle? — DGA Method for Transformer Fault Diagnosis",
    "description": "Duval's Triangle is a ternary plot method for Dissolved Gas Analysis (DGA). It classifies power transformer faults using relative concentrations of methane, acetylene, and ethylene.",
    "author": { "@type": "Person", "name": "Subramanian Narayanan" }
}
</script>
