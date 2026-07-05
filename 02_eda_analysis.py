import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 55)
print("  SWIGGY BANGALORE - STEP 2: EDA ANALYSIS")
print("=" * 55)

# ── Load Cleaned Data ──
df = pd.read_csv('outputs/swiggy_cleaned.csv')

print(f"\n✅ Cleaned Data Loaded!")
print(f"   Total Rows : {len(df):,}")

# ── Key Stats ──
print(f"\n📊 KEY STATISTICS:")
print(f"   Total Restaurants : {len(df):,}")
print(f"   Total Areas       : {df['Area'].nunique()}")
print(f"   Avg Rating        : {df['Rating'].mean():.2f}")
print(f"   Avg Cost/Two      : ₹{int(df['Cost for Two (in Rupees)'].mean())}")
print(f"   Top Cuisine       : {df['Primary_Cuisine'].value_counts().index[0]}")
print(f"   Best Rated Area   : {df.groupby('Area')['Rating'].mean().idxmax()}")

# ── Plots ──
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('Swiggy Bangalore — EDA Dashboard',
             fontsize=16, fontweight='bold')

# Plot 1: Top 10 Areas by Restaurant Count
area_count = df['Area'].value_counts().head(10)
axes[0,0].barh(area_count.index[::-1], area_count.values[::-1], color='#FC5A03')
axes[0,0].set_title('Top 10 Areas by Restaurant Count')
axes[0,0].set_xlabel('Number of Restaurants')

# Plot 2: Rating Distribution
axes[0,1].hist(df['Rating'], bins=20, color='#2196F3', edgecolor='white')
axes[0,1].axvline(df['Rating'].mean(), color='red', linestyle='--',
                   label=f"Mean: {df['Rating'].mean():.2f}")
axes[0,1].set_title('Rating Distribution')
axes[0,1].set_xlabel('Rating')
axes[0,1].legend()

# Plot 3: Top 10 Cuisines
top_cuisines = df['Primary_Cuisine'].value_counts().head(10)
axes[0,2].bar(top_cuisines.index, top_cuisines.values, color='#9C27B0')
axes[0,2].set_title('Top 10 Cuisines')
axes[0,2].tick_params(axis='x', rotation=45)

# Plot 4: Price Segment Distribution
price_dist = df['Price_Category'].value_counts()
axes[1,0].bar(price_dist.index, price_dist.values,
              color=['#4CAF50', '#2196F3', '#FF8C42', '#E74C3C'])
axes[1,0].set_title('Price Segment Distribution')
axes[1,0].set_ylabel('Count')

# Plot 5: Top 10 Areas by Avg Rating
avg_rating = df.groupby('Area')['Rating'].mean().sort_values(
             ascending=False).head(10)
axes[1,1].barh(avg_rating.index[::-1], avg_rating.values[::-1], color='#E91E63')
axes[1,1].set_title('Top 10 Areas by Avg Rating')
axes[1,1].set_xlim(3.5, 4.5)

# Plot 6: Cost vs Rating Scatter
sample = df[df['Cost for Two (in Rupees)'] < 1000].sample(500, random_state=42)
axes[1,2].scatter(sample['Cost for Two (in Rupees)'], sample['Rating'],
                   alpha=0.3, color='#FC5A03', s=20)
axes[1,2].set_title('Cost vs Rating')
axes[1,2].set_xlabel('Cost for Two (₹)')
axes[1,2].set_ylabel('Rating')

plt.tight_layout()
plt.savefig('outputs/eda_dashboard.png', dpi=150, bbox_inches='tight')
plt.show()
print("\n✅ Chart saved → outputs/eda_dashboard.png")