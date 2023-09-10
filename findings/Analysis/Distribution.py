import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# Calculate the frequency of each vehicle type
vehicle_type_counts = data['Vehicle'].value_counts()
print("Vehicle Type Counts:")
print(vehicle_type_counts)

# Plot a pie chart to visualize the distribution of vehicle types
plt.figure(figsize=(8, 8))
plt.pie(vehicle_type_counts, labels=vehicle_type_counts.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular.
plt.title('Distribution of Vehicle Types')
plt.savefig("Distribution of VehicalType")
plt.show()
