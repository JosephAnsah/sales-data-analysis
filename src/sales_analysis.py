# Sales Analysis Script

import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
data = pd.read_csv('sales_data.csv')

# Display the first few rows of the data
print(data.head())

# Function to analyze sales by product

def analyze_sales_by_product(data):
    sales_summary = data.groupby('product')['sales'].sum()
    return sales_summary

# Function to plot sales data

def plot_sales(sales_summary):
    sales_summary.plot(kind='bar')
    plt.title('Sales Analysis by Product')
    plt.xlabel('Product')
    plt.ylabel('Total Sales')
    plt.show()

# Main execution
if __name__ == '__main__':
    sales_summary = analyze_sales_by_product(data)
    print(sales_summary)
    plot_sales(sales_summary)