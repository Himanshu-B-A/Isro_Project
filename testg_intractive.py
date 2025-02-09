import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load Data (Fixed Delimiter Warning)
df = pd.read_csv(r"C:\Users\himub\OneDrive\Desktop\ISRO internship project\trial\data_rel.txt", 
                 sep=r'\s+', header=None, 
                 names=['Date_Time', 'Agency', 'Event', 'a', 'b', 'c', 'd', 'e'])

# Convert Date_Time to proper datetime format (Specify format)
df['Date_Time'] = pd.to_datetime(df['Date_Time'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Combine columns a-e into 'Payload Operation' & drop them
df['Payload Operation'] = df[['a', 'b', 'c', 'd', 'e']].astype(str).agg(' '.join, axis=1)
df.drop(columns=['a', 'b', 'c', 'd', 'e'], inplace=True)

# User options
print("Choose an operation:")
print("""
1. Display the entire dataset
2. Show a bar graph
3. Select any type of graph
""")

main_option = int(input("Enter your choice: "))

if main_option == 1:
    print(df)

elif main_option == 2:
    print("""
Select a graph type:
1. Display the entire box plot
2. Show a bar graph by day
3. Manually select a specific day's graph
""")
    second_option = int(input("Enter your choice: "))

    if second_option == 1:
        fig = px.box(df, x='Agency', y='Event', title="Box Plot of Events per Agency")
        fig.show()
    elif second_option == 2:
        fig = px.bar(df, x='Date_Time', y='Event', color='Agency', 
                     title="Bar Graph of Events per Day")
        fig.show()
    elif second_option == 3:
        day_wise_option = int(input("Enter the day number (1-8): "))
        if 1 <= day_wise_option <= 8:
            selected_date = df['Date_Time'].dt.date.unique()[day_wise_option - 1]
            df_day = df[df['Date_Time'].dt.date == selected_date]
            fig = px.box(df_day, x='Agency', y='Event', title=f"Box Plot for {selected_date}")
            fig.show()
        else:
            print(f"No data available for Day {day_wise_option}.")
    else:
        print("Invalid choice. Please select a valid option.")

elif main_option == 3:
    print("""
Choose a type of graph:

**Basic Charts**  
- Line Chart (`line`)  
- Bar Chart (`bar`)  
- Scatter Plot (`scatter`)  
- Pie Chart (`pie`)  
- Histogram (`histogram`)  

**Statistical Charts**  
- Box Plot (`box`)  
- Violin Plot (`violin`)  
- Density Heatmap (`density_heatmap`)  
- ECDF Plot (`ecdf`)  

**3D Charts**  
- 3D Scatter Plot (`scatter_3d`)  
- 3D Line Plot (`line_3d`)  
- 3D Surface Plot (`surface`)  

**Geospatial Charts**  
- Choropleth Map (`choropleth`)  
- Scatter Geo Plot (`scatter_geo`)  
- Density Mapbox (`density_mapbox`)  

**Heatmaps & Matrices**  
- Heatmap (`imshow`)  
- Correlation Matrix Heatmap (`heatmap`)  
""")

    graph_type = input("Enter the type of graph you want to draw: ").strip().lower()
    
    # Define supported graphs
    graph_functions = {
        "line": px.line,
        "bar": px.bar,
        "scatter": px.scatter,
        "pie": px.pie,
        "histogram": px.histogram,
        "box": px.box,
        "violin": px.violin,
        "density_heatmap": px.density_heatmap,
        "ecdf": px.ecdf,
        "scatter_3d": px.scatter_3d,
        "line_3d": px.line_3d,
        "choropleth": px.choropleth,
        "scatter_geo": px.scatter_geo,
        "density_mapbox": px.density_mapbox,
        "imshow": px.imshow,
        "heatmap": px.imshow  # Alternative name
    }

    if graph_type == "surface":
        df['Numeric_Column'] = range(len(df))
        fig = go.Figure(data=[go.Surface(z=df[['Numeric_Column']].values)])
        fig.update_layout(title="3D Surface Plot", autosize=True)
        fig.show()

    elif graph_type in graph_functions:
        if graph_type == "pie":
            fig = px.pie(df, names='Agency', title="Pie Chart of Agencies")
        else:
            fig = graph_functions[graph_type](
                df, x='Date_Time', color='Event', 
                title=f"{graph_type.capitalize()} Graph"
            )
        fig.show()

    else:
        print("Invalid graph type. Please enter a valid option.")

else:
    print("Invalid Option")
