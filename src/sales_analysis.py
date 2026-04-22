
import pandas as pd
import numpy as np


def main():
    # ==============================
    # STEP 1: CREATE DATA
    # ==============================
    print("=" * 60)
    print("📊 SALES DATA ANALYSIS PROJECT")
    print("=" * 60)

    data = {
        "Product": ["Phone", "Laptop", "Tablet", "Phone", None, "Laptop", "Tablet"],
        "Price": [1200, 2500, 900, 1300, 800, None, 950],
        "Quantity": [5, 3, 8, 2, None, 4, 3],
        "Region": ["Accra", "Kumasi", "Accra", "Tamale", "Kumasi", "Accra", "Tamale"]
    }

    df = pd.DataFrame(data)

    print("\n📋 ORIGINAL DATASET:")
    print(df)

    # ==============================
    # STEP 2: DATA CLEANING
    # ==============================
    print("\n🔧 DATA CLEANING...")

    df = df.drop_duplicates()

    # Handle missing values
    df["Product"] = df["Product"].fillna("Unknown")
    df["Region"] = df["Region"].str.strip()

    price_mean = df["Price"].mean()
    df["Price"] = df["Price"].fillna(price_mean)

    quantity_median = df["Quantity"].median()
    df["Quantity"] = df["Quantity"].fillna(quantity_median).astype(int)

    print("\n✅ CLEANED DATASET:")
    print(df)

    # ==============================
    # STEP 3: FEATURE ENGINEERING
    # ==============================
    df["Revenue"] = df["Price"] * df["Quantity"]

    print("\n📊 DATASET WITH REVENUE:")
    print(df)

    # ==============================
    # STEP 4: DATA VALIDATION
    # ==============================
    print("\n🔍 DATA VALIDATION:")
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nData Types:")
    print(df.dtypes)

    # ==============================
    # STEP 5: SUMMARY STATISTICS
    # ==============================
    print("\n📈 SUMMARY STATISTICS:")
    print(df.describe())

    # ==============================
    # STEP 6: ANALYSIS
    # ==============================
    print("\n" + "=" * 60)
    print("🔍 SALES ANALYSIS RESULTS")
    print("=" * 60)

    total_revenue = df["Revenue"].sum()
    print(f"\n💰 Total Revenue: ${total_revenue:,.2f}")

    # Revenue by Product
    revenue_by_product = (
        df.groupby("Product")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )
    print("\n📦 Revenue by Product:")
    print(revenue_by_product)

    # Revenue by Region
    revenue_by_region = (
        df.groupby("Region")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )
    print("\n🌍 Revenue by Region:")
    print(revenue_by_region)

    # Top performers
    top_product = revenue_by_product.idxmax()
    top_product_revenue = revenue_by_product.max()

    top_region = revenue_by_region.idxmax()
    top_region_revenue = revenue_by_region.max()

    # Top transaction
    top_transaction = df.loc[df["Revenue"].idxmax()]
    print("\n🏆 TOP PERFORMING TRANSACTION:")
    print(f"Product: {top_transaction['Product']}")
    print(f"Region: {top_transaction['Region']}")
    print(f"Revenue: ${top_transaction['Revenue']:,.2f}")

    # ==============================
    # STEP 7: INSIGHTS
    # ==============================
    print("\n" + "=" * 60)
    print("💡 BUSINESS INSIGHTS")
    print("=" * 60)

    print(f"\n🏆 Top Product: {top_product} (${top_product_revenue:,.2f})")
    print(f"📍 Top Region: {top_region} (${top_region_revenue:,.2f})")
    print(f"💰 Total Revenue: ${total_revenue:,.2f}")
    print(f"📊 Average Transaction: ${df['Revenue'].mean():,.2f}")
    print(f"⭐ Number of Transactions: {len(df)}")

    print(f"\n💡 Insight: {top_product} is the main revenue driver and should be prioritized.")

    # ==============================
    # STEP 8: MARKET SHARE
    # ==============================
    print("\n📊 MARKET SHARE BY PRODUCT:")
    for product, revenue in revenue_by_product.items():
        share = (revenue / total_revenue) * 100
        bar = "█" * int(share / 2)
        print(f"{product:10}: {bar} {share:.1f}% (${revenue:,.0f})")

    # ==============================
    # STEP 9: EXPORT RESULTS
    # ==============================
    print("\n💾 EXPORTING RESULTS...")

    revenue_by_product.reset_index().to_csv("product_summary.csv", index=False)
    revenue_by_region.reset_index().to_csv("region_summary.csv", index=False)
    df.to_csv("cleaned_sales_data.csv", index=False)

    print("✅ Files saved:")
    print("   - product_summary.csv")
    print("   - region_summary.csv")
    print("   - cleaned_sales_data.csv")

    print("\n" + "=" * 60)
    print("🎉 PROJECT COMPLETED SUCCESSFULLY!")
    print("=" * 60)


# Run the script
if __name__ == "__main__":
    main()
