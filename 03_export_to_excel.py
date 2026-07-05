import pandas as pd

print("=" * 55)
print("  SWIGGY BANGALORE - STEP 3: EXPORT TO EXCEL")
print("=" * 55)

# ── Load Cleaned Data ──
df = pd.read_csv('outputs/swiggy_cleaned.csv')

writer = pd.ExcelWriter('outputs/swiggy_report.xlsx', engine='openpyxl')

# Sheet 1: Cleaned Data
df.to_excel(writer, sheet_name='Cleaned Data', index=False)
print("✅ Sheet 1 → Cleaned Data")

# Sheet 2: Area Summary
area_summary = df.groupby('Area').agg(
    Total_Restaurants=('Restaurant Name', 'count'),
    Avg_Rating=('Rating', 'mean'),
    Avg_Cost=('Cost for Two (in Rupees)', 'mean'),
    Top_Cuisine=('Primary_Cuisine', lambda x: x.value_counts().index[0])
).round(2).sort_values('Avg_Rating', ascending=False).reset_index()
area_summary.to_excel(writer, sheet_name='Area Summary', index=False)
print("✅ Sheet 2 → Area Summary")

# Sheet 3: Cuisine Summary
cuisine_summary = df.groupby('Primary_Cuisine').agg(
    Count=('Restaurant Name', 'count'),
    Avg_Rating=('Rating', 'mean'),
    Avg_Cost=('Cost for Two (in Rupees)', 'mean')
).round(2).sort_values('Count', ascending=False).head(20).reset_index()
cuisine_summary.to_excel(writer, sheet_name='Cuisine Summary', index=False)
print("✅ Sheet 3 → Cuisine Summary")

# Sheet 4: Price Segment Analysis
price_summary = df.groupby('Price_Category').agg(
    Count=('Restaurant Name', 'count'),
    Avg_Rating=('Rating', 'mean'),
    Avg_Cost=('Cost for Two (in Rupees)', 'mean')
).round(2).reset_index()
price_summary.to_excel(writer, sheet_name='Price Analysis', index=False)
print("✅ Sheet 4 → Price Analysis")

# Sheet 5: KPI Summary
kpi_data = {
    'Metric': [
        'Total Restaurants',
        'Total Areas',
        'Average Rating',
        'Avg Cost for Two (₹)',
        'Top Cuisine',
        'Best Rated Area',
        'Most Restaurants Area',
        'Budget Restaurants',
        'Luxury Restaurants'
    ],
    'Value': [
        len(df),
        df['Area'].nunique(),
        round(df['Rating'].mean(), 2),
        int(df['Cost for Two (in Rupees)'].mean()),
        df['Primary_Cuisine'].value_counts().index[0],
        df.groupby('Area')['Rating'].mean().idxmax(),
        df['Area'].value_counts().index[0],
        len(df[df['Price_Category'] == 'Budget']),
        len(df[df['Price_Category'] == 'Luxury'])
    ]
}
pd.DataFrame(kpi_data).to_excel(writer, sheet_name='KPI Summary', index=False)
print("✅ Sheet 5 → KPI Summary")

writer.close()

print("\n🎉 Excel file saved → outputs/swiggy_report.xlsx")
print("   5 Sheets ready for Power BI!")

print("=" * 55)
print("  SWIGGY BANGALORE - STEP 3: EXPORT TO EXCEL")
print("=" * 55)

# ── Load Cleaned Data ──
df = pd.read_csv('outputs/swiggy_cleaned.csv')

writer = pd.ExcelWriter('outputs/swiggy_report.xlsx', engine='openpyxl')

# Sheet 1: Cleaned Data
df.to_excel(writer, sheet_name='Cleaned Data', index=False)
print("✅ Sheet 1 → Cleaned Data")

# Sheet 2: Area Summary
area_summary = df.groupby('Area').agg(
    Total_Restaurants=('Restaurant Name', 'count'),
    Avg_Rating=('Rating', 'mean'),
    Avg_Cost=('Cost for Two (in Rupees)', 'mean'),
    Top_Cuisine=('Primary_Cuisine', lambda x: x.value_counts().index[0])
).round(2).sort_values('Avg_Rating', ascending=False).reset_index()
area_summary.to_excel(writer, sheet_name='Area Summary', index=False)
print("✅ Sheet 2 → Area Summary")

# Sheet 3: Cuisine Summary
cuisine_summary = df.groupby('Primary_Cuisine').agg(
    Count=('Restaurant Name', 'count'),
    Avg_Rating=('Rating', 'mean'),
    Avg_Cost=('Cost for Two (in Rupees)', 'mean')
).round(2).sort_values('Count', ascending=False).head(20).reset_index()
cuisine_summary.to_excel(writer, sheet_name='Cuisine Summary', index=False)
print("✅ Sheet 3 → Cuisine Summary")

# Sheet 4: Price Segment Analysis
price_summary = df.groupby('Price_Category').agg(
    Count=('Restaurant Name', 'count'),
    Avg_Rating=('Rating', 'mean'),
    Avg_Cost=('Cost for Two (in Rupees)', 'mean')
).round(2).reset_index()
price_summary.to_excel(writer, sheet_name='Price Analysis', index=False)
print("✅ Sheet 4 → Price Analysis")

# Sheet 5: KPI Summary
kpi_data = {
    'Metric': [
        'Total Restaurants',
        'Total Areas',
        'Average Rating',
        'Avg Cost for Two (₹)',
        'Top Cuisine',
        'Best Rated Area',
        'Most Restaurants Area',
        'Budget Restaurants',
        'Luxury Restaurants'
    ],
    'Value': [
        len(df),
        df['Area'].nunique(),
        round(df['Rating'].mean(), 2),
        int(df['Cost for Two (in Rupees)'].mean()),
        df['Primary_Cuisine'].value_counts().index[0],
        df.groupby('Area')['Rating'].mean().idxmax(),
        df['Area'].value_counts().index[0],
        len(df[df['Price_Category'] == 'Budget']),
        len(df[df['Price_Category'] == 'Luxury'])
    ]
}
pd.DataFrame(kpi_data).to_excel(writer, sheet_name='KPI Summary', index=False)
print("✅ Sheet 5 → KPI Summary")

writer.close()

print("\n🎉 Excel file saved → Output/swiggy_report.xlsx")
print("   5 Sheets ready for Power BI!")