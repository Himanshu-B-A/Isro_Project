import pandas as pd
import plotly.express as px

# ✅ Read the file correctly
df = pd.read_csv(r"C:\Users\himub\OneDrive\Desktop\ISRO internship project\trial\data_rel.txt", 
                 sep=r'\s+', engine='python', header=None, 
                 names=['Date_Time', 'Agency', 'Event', 'a', 'b', 'c', 'd', 'e'])  

# ✅ Remove duplicates based on 'Date_Time'
df_unique = df.drop_duplicates(subset=['Date_Time'])

# ✅ Assign Y-axis to be 1 for each unique event
df_unique['Count'] = 1  # Adding a column for proper visualization

# ✅ Create a bar chart with correct ordering
fig = px.bar(df_unique, 
             x='Date_Time',
             y='Count',  
             color='Event',  
             title="Correctly Ordered Vertical Bar Graph",
             labels={'Count': 'Number of Events', 'Date_Time': 'Timestamp'},
             category_orders={'Date_Time': df_unique['Date_Time'].tolist()})  

# ✅ Rotate x-axis labels for better readability
fig.update_layout(xaxis=dict(tickangle=-45))

# Show the graph
fig.show()
