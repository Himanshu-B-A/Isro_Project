import pandas as pd
import plotly.express as px

# Load data with updated separator for whitespace
df = pd.read_csv(r"C:\Users\himub\OneDrive\Desktop\ISRO internship project\trial\6-12-25\data_rel.txt", 
                 sep='\s+', header=None, 
                 names=['Date_Time', 'Agency', 'Event','a','b','c','d','e']) 

# ✅ Convert Date_Time to datetime with explicit format
df['Date_Time'] = pd.to_datetime(df['Date_Time'], format='%Y-%m-%dT%H:%M:%S', errors='coerce')

# ✅ Group by Date_Time and Event, then count occurrences
df_counts = df.groupby(['Date_Time', 'Event']).size().reset_index(name='Event_Count')

# ✅ Sort by Date_Time
df_counts.sort_values(by='Date_Time', inplace=True)

# ✅ Create a correctly ordered vertical bar chart
fig = px.bar(df_counts, 
             x='Date_Time',  
             y='Event_Count',  
             color='Event',  
             title="Event Frequency Over Time",
             labels={'Event_Count': 'Number of Events', 'Date_Time': 'Timestamp'},
             barmode='group',
             category_orders={'Date_Time': df_counts['Date_Time'].astype(str).tolist()})  # Forces Date Order

# ✅ Rotate x-axis labels for better readability
fig.update_layout(xaxis=dict(tickangle=-45))

# Show the graph
fig.show()

print('''
Enter 1: To Show Entire Data
Enter 2: To Show Entire Date in Box Plot
Enter 3: To Show Day 1 Operations of Box plot
Enter 4: To Show Day 2 Operations of Box plot
Enter 5: To Show Day 3 Operations of Box plot
Enter 6: To Show Day 4 Operations of Box plot
Enter 7: To Show Day 5 Operations of Box plot
Enter 8: To Show Day 6 Operations of Box plot
Enter 9: To Show Day 7 Operations of Box plot
Enter 10: To Show Day 8 Operations of Box plot
Enter 11: To To Show All 8 Days Operations of Box plot
Enter 12: To Show Entire Date in Scatter Plot
Enter 13: To Show Day 1 Operations of Scatter plot
Enter 14: To Show Day 2 Operations of Scatter plot
Enter 15: To Show Day 3 Operations of Scatter plot
Enter 16: To Show Day 4 Operations of Scatter plot
Enter 17: To Show Day 5 Operations of Scatter plot
Enter 18: To Show Day 6 Operations of Scatter plot
Enter 19: To Show Day 7 Operations of Scatter plot
Enter 20: To Show Day 8 Operations of Scatter plot
Enter 21: To Show All 8 Days Operations of Scatter plot
      ''')
option = int(input("Enter the option ::"))
if (option == 1):
    print("Here is data :")
elif(option==2):
    print("Opening Graph..............")
elif(option==3):
    print("Opening Graph..............")
elif(option==4):
    print("Opening Graph..............")
elif(option==5):
    print("Opening Graph..............")
elif(option==6):
    print("Opening Graph..............")
elif(option==7):
    print("Opening Graph..............")
elif(option==8):
    print("Opening Graph..............")
elif(option==9):
    print("Opening Graph..............")
elif(option==10):
    print("Opening Graph..............")
elif(option==11):
    print("Opening Graph..............")
elif(option==12):
    print("Opening Graph..............")
elif(option==13):
    print("Opening Graph..............")
elif(option==14):
    print("Opening Graph..............")
elif(option==15):
    print("Opening Graph..............")
elif(option==16):
    print("Opening Graph..............")
elif(option==17):
    print("Opening Graph..............")
elif(option==18):
    print("Opening Graph..............")
elif(option==19):
    print("Opening Graph..............")
elif(option==20):
    print("Opening Graph..............")
elif(option==21):
    print("Opening Graph..............")
else:
    print("Invalid Option")