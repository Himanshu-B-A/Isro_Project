import plotly.graph_objects as go
import numpy as np

# Event types and colors
event_types = ["MAP_ON", "JOINT", "POST_TAKE", "L_ONLY", "LOFS"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]  # Custom color palette

# Sample event data
events = [
    "MAP_ON", "JOINT", "MAP_ON", "JOINT", "POST_TAKE", "L_ONLY", "LOFS"
] * 20  # Repeated for a grid

# Grid size
num_rows = 10
num_cols = len(events) // num_rows

# Create X and Y coordinates
x = np.tile(np.arange(num_cols), num_rows)
y = np.repeat(np.arange(num_rows), num_cols)

# Assign colors based on events
color_map = {event: color for event, color in zip(event_types, colors)}
event_colors = [color_map.get(event, "#cccccc") for event in events]

# Create figure
fig = go.Figure(data=go.Scatter(
    x=x, y=-y,  # Flip y-axis for better visualization
    mode="markers",
    marker=dict(symbol="square", size=10, color=event_colors)
))

# Hide axes and layout settings
fig.update_layout(
    showlegend=False, plot_bgcolor="white",
    xaxis=dict(visible=False), yaxis=dict(visible=False),
    margin=dict(l=0, r=0, t=0, b=0)
)

# Show figure
fig.show()
