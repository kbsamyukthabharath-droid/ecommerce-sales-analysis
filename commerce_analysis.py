import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# LOAD DATASET

df = pd.read_csv("ecommerce.csv")

print("Original Dataset:")
print(df.head())


# CHECK & HANDLE MISSING VALUES

print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numeric values with column mean
numeric_cols = ["Quantity", "Unit_Price", "Total_Sales", "Delivery_Days", "Customer_Rating"]
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# Fill missing categorical values with mode
categorical_cols = ["Region", "Payment_Method"]
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# REMOVE DUPLICATES

print("\nNumber of Duplicate Rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("Dataset Shape After Removing Duplicates:", df.shape)

# DETECT & HANDLE OUTLIERS

plt.figure(figsize=(6,4))
sns.boxplot(y=df["Total_Sales"])
plt.title("Total Sales Outlier Detection")
plt.show()

# Remove extreme outliers (sales > 100000)
df = df[df["Total_Sales"] <= 100000]
print("Dataset Shape After Removing Outliers:", df.shape)


# BASIC STATISTICS

print("\nStatistical Summary:")
print(df.describe())


# VISUALIZATIONS


#1. Average Sales by Product Category
plt.figure(figsize=(8,4))
df.groupby("Product_Category")["Total_Sales"].mean().plot(kind="bar", color="#4c72b0")
plt.title("Average Sales by Product Category")
plt.ylabel("Average Sales")
plt.xticks(rotation=45)
plt.show()

#2. Payment Method Distribution
plt.figure(figsize=(6,4))
df["Payment_Method"].value_counts().plot(kind="pie", autopct="%1.1f%%", colors=sns.color_palette("Set2"))
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.show()

#3. Region-wise Total Sales
plt.figure(figsize=(8,4))
sns.barplot(data=df, x="Region", y="Total_Sales", estimator=sum, ci=None, palette="muted")
plt.title("Region-wise Total Sales")
plt.show()

#4. Delivery Days vs Customer Rating
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="Delivery_Days", y="Customer_Rating", hue="Region", palette="Set1")
plt.title("Delivery Days vs Customer Rating")
plt.show()

#5. Top 10 Customers by Sales
top_customers = df.groupby("Customer_Name")["Total_Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,4))
top_customers.plot(kind="bar", color="#55a868")
plt.title("Top 10 Customers by Sales")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()


# INSIGHTS

print("\n========== PROJECT INSIGHTS ==========")

print("\nHighest Sales Order:", df.loc[df["Total_Sales"].idxmax(), "Order_ID"])
print("Highest Sales Value:", round(df["Total_Sales"].max(), 2))

print("\nAverage Order Value:", round(df["Total_Sales"].mean(), 2))
print("Average Delivery Days:", round(df["Delivery_Days"].mean(), 2))
print("Average Customer Rating:", round(df["Customer_Rating"].mean(), 2))

print("\nMost Popular Payment Method:", df["Payment_Method"].mode()[0])
print("Region with Highest Sales:", df.groupby("Region")["Total_Sales"].sum().idxmax())

print("\nProject Completed Successfully!")
