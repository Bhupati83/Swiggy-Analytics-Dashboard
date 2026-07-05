import pandas as pd
import numpy as np

print("=" * 55)
print("  SWIGGY BANGALORE - STEP 1: DATA CLEANING")
print("=" * 55)

# ── Load Data ──
df = pd.read_csv('data/Swiggy Bangalore.csv')

print(f"\n✅ Data Loaded Successfully!")
print(f"   Total Rows    : {df.shape[0]}")
print(f"   Total Columns : {df.shape[1]}")
print(f"\n📋 Column Names : {df.columns.tolist()}")

print(f"\n🔍 Null Values Before Cleaning:")
print(df.isnull().sum())

# ── Clean Rating ──
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df_clean = df.dropna(subset=['Rating']).copy()

# ── Remove Useless Columns ──
df_clean = df_clean.drop(columns=['Offer', 'URL'])

# ── New Columns ──
df_clean['Primary_Cuisine'] = df_clean['Category'].apply(
    lambda x: str(x).split(',')[0].strip()
)

df_clean['Price_Category'] = pd.cut(
    df_clean['Cost for Two (in Rupees)'],
    bins=[0, 200, 400, 700, 3500],
    labels=['Budget', 'Mid-Range', 'Premium', 'Luxury']
)

df_clean['Rating_Category'] = pd.cut(
    df_clean['Rating'],
    bins=[0, 3, 3.5, 4, 4.5, 5],
    labels=['Poor', 'Average', 'Good', 'Very Good', 'Excellent']
)

# ── Save Cleaned File ──
df_clean.to_csv('outputs/swiggy_cleaned.csv', index=False)

print(f"\n✅ Cleaning Done!")
print(f"   Rows After Cleaning : {df_clean.shape[0]}")
print(f"   Columns Now         : {df_clean.shape[1]}")
print(f"\n📊 Sample Data:")
print(df_clean.head(3))
print("\n✅ File Saved → outputs/swiggy_cleaned.csv")