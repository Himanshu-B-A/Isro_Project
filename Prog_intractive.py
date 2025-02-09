import pandas as pd


df = pd.read_csv(r"C:\Users\himub\OneDrive\Desktop\ISRO internship project\trial\data_rel.txt", 
                 delim_whitespace=True, header=None, 
                 names=['Date_Time', 'Agency', 'Event', 'a', 'b', 'c', 'd', 'e'])


df['Pay lode operation'] = df[['a', 'b', 'c', 'd', 'e']].astype(str).agg(' '.join, axis=1)


df.drop(columns=['a', 'b', 'c', 'd', 'e'], inplace=True)

print('''Enter the Operation 
1. To display the Entire Data 
2. To show the bar graph 
3. To get the Any graph''')
main_option =  int(input("Enter your choice :"))
if (main_option == 1):
    print(df)

elif (main_option == 2):
    print('''Enter the operation 
          1: To Show the entire Box plot 
          2: To Show the Bar Graph according to Day wise 
          3: To display manual the day''')
    second_option = int(input("Enter your Choice  :"))
    if (second_option == 1):
        print("This is the Box Plot...........")
    elif(second_option==2):
        print("Drawing the Graph:............ ")
    elif(second_option ==3):
        print('''Enter which Day graph u want to see: 
              1: Day 1
              2: Day 2
              3: Day 3
              4: Day 4
              5: Day 5
              6: Day 6
              7: Day 7
              8: Day 8 ''')
        day_wise_option=int(input("Enter the which Day Graph u want to see : "))
        if (day_wise_option == 1):
            print("Opening the Day 1 Box Graph ....................")
        elif (day_wise_option == 2):
            print("Opening the Day 2 Box Graph ....................")
        elif (day_wise_option == 3):
            print("Opening the Day 3 Box Graph ....................")
        elif (day_wise_option == 4):
            print("Opening the Day 4 Box Graph ....................")
        elif (day_wise_option == 5):
            print("Opening the Day 5 Box Graph ....................")
        elif (day_wise_option == 6):
            print("Opening the Day 6 Box Graph ....................")
        elif (day_wise_option == 7):
            print("Opening the Day 7 Box Graph ....................")
        elif (day_wise_option == 8):
            print("Opening the Day 8 Box Graph ....................")
        else:
            print(f"There is no data for :{day_wise_option}")
    else:
        print("Invalid Option")
elif(main_option == 3):
    print(''' Type name 
Basic Charts
Line Chart (line)
Bar Chart (bar)
Scatter Plot (scatter)
Pie Chart (pie)
Histogram (histogram)
Statistical Charts
Box Plot (box)
Violin Plot (violin)
Density Heatmap (density_heatmap)
ECDF (Empirical CDF) Plot (px.ecdf)
3D Charts
3D Scatter Plot (Scatter3d)
3D Line Plot (Scatter3d)
3D Surface Plot (Surface)
Geospatial Charts
Choropleth Map (choropleth)
Scatter Geo Plot (scatter_geo)
Density Mapbox (density_mapbox)
Heatmaps & Matrix
Heatmap (imshow)
Correlation Matrix Heatmap (Heatmap)
''')
else:
    print("Invalid Choice")
    