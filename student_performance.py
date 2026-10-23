

import pandas as pd

# Read student data
df = pd.read_csv("students.csv")

# Calculate total and average
subjects = ["Maths", "Science", "English"]

df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1).round(2)

# Calculate pass or fail
df["Result"] = df[subjects].ge(40).all(axis=1)
df["Result"] = df["Result"].map({
    True: "Pass",
    False: "Fail"
})

# Display complete report
print("\nSTUDENT PERFORMANCE REPORT")
print(df.to_string(index=False))

# Find top performer
top_index = df["Average"].idxmax()
print("\nTop Performer:", df.loc[top_index, "Name"])
print("Highest Average:", df["Average"].max())

# Calculate class average
print("Class Average:", round(df["Average"].mean(), 2))

# Subject-wise averages
print("\nSUBJECT-WISE AVERAGES")
print(df[subjects].mean().round(2))

# Save analyzed data
df.to_csv("student_analysis_report.csv", index=False)

print("\nReport saved successfully!")

import matplotlib.pyplot as plt

# Student average marks chart
plt.bar(df["Name"], df["Average"])

plt.title("Student Performance Analysis")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")

plt.ylim(0, 100)
plt.tight_layout()
plt.show()




