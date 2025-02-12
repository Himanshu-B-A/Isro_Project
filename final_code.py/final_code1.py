import pandas as pd
import plotly.express as px


df = pd.read_csv("data.txt", delim_whitespace=True, header=None, 
                 names=['Date_Time', 'Agency', 'Event', 'a', 'b', 'c', 'd', 'e'])

df.sort_values(by='Date_Time', inplace=True)


df[['Date', 'Time']] = df['Date_Time'].str.split('T', expand=True)


df['Date'] = df['Date'].apply(lambda x: pd.to_datetime(f"{x[:4]}-01-01") + pd.to_timedelta(int(x[5:]) - 1, unit='D'))


df['Date_Time'] = pd.to_datetime(df['Date'].astype(str) + " " + df['Time'])


df["Count"] = 1  


days = sorted(df["Date"].unique())[:8]
days_data = {day: df[df["Date"] == day] for day in days}


def create_bar_plot(df, title):

    df_unique = df.drop_duplicates(subset=["Date_Time"])  

    
    fig = px.bar(df_unique, 
                 x='Time',  
                 y='Count', 
                 color='Event',  
                 title=title,
                 hover_data=['Date_Time', 'Agency', 'Event'],
                 category_orders={'Time': sorted(df_unique['Time'].unique())})


    fig.update_layout(
        xaxis=dict(
            tickangle=-45,
            tickmode='auto',
            dtick=3600000, 
            showticklabels=True
        ),
        bargap=0.3,
        xaxis_title='Time (24-hour format)',
        yaxis_title='Operations',
        yaxis=dict(tickvals=[0, 1], ticktext=["", "1"]),  # Ensures y-axis never goes above 1
        width=1400,
        height=500
    )
    
    fig.show()


for i, (day, day_data) in enumerate(days_data.items(), 1):
    create_bar_plot(day_data, f"Day {i}")
