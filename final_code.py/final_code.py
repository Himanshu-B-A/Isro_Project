import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv(r"data.txt", 
                 delim_whitespace=True, header=None, 
                 names=['Date_Time', 'Agency', 'Event', 'a', 'b', 'c', 'd', 'e'])


df["Date_Time"] = df["Date_Time"].astype(str)
df.sort_values(by="Date_Time", inplace=True)


event_types = df["Event"].unique()
event_colors = {event: px.colors.qualitative.Set1[i % len(px.colors.qualitative.Set1)]
                for i, event in enumerate(event_types)}

days = [f"2024-{168 + i}" for i in range(8)]
day_data = {day: df[df["Date_Time"].str.contains(day)] for day in days}


fig = make_subplots(rows=8, cols=1, shared_xaxes=False, 
                    subplot_titles=[f"Day {i+1}" for i in range(8)], 
                    vertical_spacing=0.1)

for i, (day, data) in enumerate(day_data.items()):
    
    if len(data) > 1:
        x_values = [(j / (len(data)-1)) * 24 for j in range(len(data))]
    else:
        x_values = [0] 
    
    fig.add_trace(
        go.Bar(
            x=x_values, 
            y=[1] * len(data),
            marker=dict(color=[event_colors[event] for event in data["Event"]]),
            name=data["Event"].iloc[0] if not data.empty else "Unknown",
            hovertext=[f"Event: {row['Event']}<br>Date: {row['Date_Time']}<br>Count: 1<br>Agency: {row['Agency']}"
                       for _, row in data.iterrows()],
            hoverinfo="text"
        ),
        row=i+1, col=1
    )
    

    fig.update_xaxes(
        tickmode="array",
        tickvals=list(range(25)),  # Positions 0,1,...,24
        ticktext=[f"{h:02d}:00" for h in range(25)],
        row=i+1, col=1
    )
fig.update_layout(
    title="Event-Based Graphs for 8 Days (Mapped to 24-Hour Timeline)",
    height=4500, width=1200,
    showlegend=True
)

fig.show()
