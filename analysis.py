import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# STEP 1: LOAD DATASET
# =========================
df = pd.read_csv("students.csv")

print("Original Dataset:")
print(df.head())

# =========================
# STEP 2: CHECK & HANDLE MISSING VALUES
# =========================
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with column mean
df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# =========================
# STEP 3: REMOVE DUPLICATES
# =========================
print("\nNumber of Duplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Dataset Shape After Removing Duplicates:", df.shape)


# DETECT & HANDLE OUTLIERS

plt.figure(figsize=(6,4))
sns.boxplot(y=df["Math"])
plt.title("Math Marks Outlier Detection")
plt.show()

# Remove impossible scores (>100 or <0)
df = df[(df["Math"] >= 0) & (df["Math"] <= 100)]
print("Dataset Shape After Removing Outliers:", df.shape)


# STEP 5: BASIC STATISTICS

print("\nStatistical Summary:")
print(df.describe())


# STEP 6: CREATE AVERAGE SCORE

df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)


# STEP 7: VISUALIZATIONS


# 1. Average Marks per Subject
plt.figure(figsize=(6,4))
df[["Math", "Science", "English"]].mean().plot(kind="bar", color=["#4c72b0","#55a868","#c44e52"])
plt.title("Average Marks by Subject")
plt.ylabel("Marks")
plt.xticks(rotation=0)
plt.show()

# 2. Attendance Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Attendance"], bins=6, color="#4c72b0", edgecolor="black")
plt.title("Attendance Distribution")
plt.xlabel("Attendance %")
plt.ylabel("Number of Students")
plt.show()

# 3. Hours Studied vs Math Marks
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="Hours_Studied", y="Math", hue="Gender", palette="Set2")
plt.title("Hours Studied vs Math Marks")
plt.show()

# 4. Gender-wise Average Marks
gender_avg = df.groupby("Gender")["Average"].mean()
plt.figure(figsize=(6,4))
gender_avg.plot(kind="bar", color="#55a868")
plt.title("Gender-wise Average Marks")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.show()

# 5. Top 5 Students
top5 = df.sort_values(by="Average", ascending=False).head(5)
plt.figure(figsize=(8,4))
sns.barplot(data=top5, x="Name", y="Average", palette="muted")
plt.title("Top 5 Students")
plt.ylabel("Average Marks")
plt.show()


# INSIGHTS

print("\n========== PROJECT INSIGHTS ==========")

print("\nHighest Scoring Student:", df.loc[df["Average"].idxmax(), "Name"])
print("Highest Average Score:", round(df["Average"].max(), 2))

print("\nClass Average:", round(df["Average"].mean(), 2))
print("Average Attendance:", round(df["Attendance"].mean(), 2), "%")
print("Average Hours Studied:", round(df["Hours_Studied"].mean(), 2), "hours/day")

print("\nMale Average Score:", round(df[df["Gender"] == "M"]["Average"].mean(), 2))
print("Female Average Score:", round(df[df["Gender"] == "F"]["Average"].mean(), 2))

print("\nProject Completed Successfully!")
