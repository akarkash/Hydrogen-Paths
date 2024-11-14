#Data Analysis 
#%%
import pandas as pd
import numpy as np
import math 
#%%
filename1= 'CuH_1.csv'
filename2= 'CuH_2.csv'

df1 = pd.read_csv(filename1)
df2 = pd.read_csv(filename2)

deltaX=list(df1['x']-df2['x'])
deltaY=list(df1['y']-df2['y'])
deltaZ=list(df1['z']-df2['z'])

#%%
# Inter atomic distance in XY-Plane
d_XY = []
frames = []
for i in range(0,len(deltaX)):
    d2 = math.pow(deltaX[i],2)+math.pow(deltaY[i],2)
    d =  math.sqrt(d2)
    d_XY.append(d)
    frames.append(i)
#%%
#Inter atomic distance in XYZ spac
r_XYZ = []
for i in range(0,len(deltaX)):
    r2 = math.pow(deltaX[i],2)+math.pow(deltaY[i],2) + math.pow(deltaZ[i],2)
    r =  math.sqrt(r2)
    r_XYZ.append(r)
#%%
# Exporting the data to csv files: 
    
# Create a dictionary with the column names and corresponding data
data = {'index': frames, 'xy': d_XY, 'xyz': r_XYZ}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Specify the output CSV file path
output_file = 'Total_Cu.csv'

# Export the DataFrame to a CSV file
df.to_csv(output_file, index=False)  # Set index=False to exclude row numbers

    
    
