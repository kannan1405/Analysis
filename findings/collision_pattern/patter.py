import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load your dataset into a pandas DataFrame (assuming it's in a CSV file)
data = pd.read_csv("C:/Users/kannan/Desktop/unnati_phase1_data_revised.csv")


# Convert the "Date" column to a datetime data type
data['Date'] = pd.to_datetime(data['Date'])

# Extract additional date-related information
data['Month'] = data['Date'].dt.month
data['DayOfWeek'] = data['Date'].dt.day_name()
data['Hour'] = pd.to_datetime(data['Time'], format='%H:%M:%S').dt.hour

# Temporal Analysis by Time of Day
hourly_collision_counts = data.groupby('Hour')['Alert'].count()

# Temporal Analysis by Day of the Week
day_of_week_collision_counts = data.groupby('DayOfWeek')['Alert'].count()

# Temporal Analysis by Month
monthly_collision_counts = data.groupby('Month')['Alert'].count()

# Plot the temporal analysis
plt.figure(figsize=(15, 8))


# Plotting Temporal Analysis by Time of Day
plt.subplot(2, 2, 1)
hourly_collision_counts.plot(kind='line', color='blue')
plt.xlabel('Hour of the Day')
plt.ylabel('Collision Count')
plt.title('Collision Trends by Time of Day')
plt.grid()

# Plotting Temporal Analysis by Day of the Week
plt.subplot(2, 2, 2)
day_of_week_collision_counts.plot(kind='bar', color='green')
plt.xlabel('Day of the Week')
plt.ylabel('Collision Count')
plt.title('Collision Trends by Day of the Week')
plt.xticks(rotation=45)

# Plotting Temporal Analysis by Month
plt.subplot(2, 2, 3)
monthly_collision_counts.plot(kind='bar', color='orange')
plt.xlabel('Month')
plt.ylabel('Collision Count')
plt.title('Collision Trends by Month')

plt.tight_layout()
plt.savefig("collision_Trends.png")
plt.show()
