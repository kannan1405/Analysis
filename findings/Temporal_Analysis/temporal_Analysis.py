import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
# Load your dataset into a pandas DataFrame (assuming it's in a CSV file)
data = pd.read_csv("C:/Users/kannan/Desktop/unnati_phase1_data_revised.csv")

# Calculate the frequency of each type of collision
collision_counts = data['Alert'].value_counts()
print("Collision Type Counts:")
print(collision_counts)

# Plot a bar chart to visualize the collision type counts
plt.figure(figsize=(10, 6))
collision_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Collision Type')
plt.ylabel('Frequency')
plt.title('Collision Type Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Collision_Type_Freaquency.png')
plt.show()
