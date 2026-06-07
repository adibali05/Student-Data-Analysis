import numpy as np
import pandas as pd

# 1. Set seed for reproducibility (so you get the same data every time)
np.random.seed(42)
num_students = 500

# 2. Generate Independent Variables
student_ids = range(10001, 10001 + num_students)

genders = np.random.choice(["Male", "Female", "Non-binary"], size=num_students, p=[0.48, 0.48, 0.04])

# Attendance rates centered around 85% using a normal distribution
attendance = np.random.normal(loc=85, scale=8, size=num_students)
attendance = np.clip(attendance, 50, 100).round(1)  # Keep within realistic limits

# Study hours (skewed: more students study less hours, fewer study massive hours)
study_hours = np.random.randint(2, 28, size=num_students)

extracurriculars = np.random.choice(["Yes", "No"], size=num_students, p=[0.4, 0.6])

sleep_hours = np.random.choice([5, 6, 7, 8, 9], size=num_students, p=[0.15, 0.25, 0.35, 0.20, 0.05])

# 3. Create the Base DataFrame
df = pd.DataFrame({
    "Student_ID": student_ids,
    "Gender": genders,
    "Attendance_Rate": attendance,
    "Study_Hours_Per_Week": study_hours,
    "Extracurricular_Activities": extracurriculars,
    "Sleep_Hours_Per_Night": sleep_hours
})

# 4. Inject Realistic Logic for the "Final_Grade" (The Target Variable)
# Grade = (Attendance weight) + (Study weight) + (Sleep weight) + Random Noise
noise = np.random.normal(loc=0, scale=4, size=num_students)  # Adds realistic randomness

df["Final_Grade"] = (
    (df["Attendance_Rate"] * 0.45) + 
    (df["Study_Hours_Per_Week"] * 1.2) + 
    (df["Sleep_Hours_Per_Night"] * 1.5) + 
    noise
)

# Scale grades to a standard 0-100 max scale and round
df["Final_Grade"] = np.clip(df["Final_Grade"], 0, 100).round(1)

# 5. Export to a CSV file
df.to_csv("student_performance_dataset.csv", index=False)

print("Success! 'student_performance_dataset.csv' has been created with 500 records.")
print(df.head())