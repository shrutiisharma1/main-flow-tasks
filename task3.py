import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as cns 
data=pd.read_csv(r"C:\Users\sharm\OneDrive\Desktop\GETTING STARTED\householdtask3.csv")
print(data)











#Scatter plot with YEAR against OWN 
plt.scatter(data['year'],data['own'])
#Adding a title to the plot
plt.title("Scatter plot")
#Setting the x and y lables
plt.xlabel('year')
plt.ylabel('own')
#Showing the result
plt.show()










#Line Chart with YEAR against OWN
