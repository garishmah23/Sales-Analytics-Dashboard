import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv("sales_data.csv")

# Convert Date column
data['Date'] = pd.to_datetime(data['Date'])

# Create Month column
data['Month'] = data['Date'].dt.month

# Total Sales and Profit
total_sales = data['Sales'].sum()
total_profit = data['Profit'].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

# Group data
product_sales = data.groupby('Product')['Sales'].sum()
product_profit = data.groupby('Product')['Profit'].sum()
monthly_sales = data.groupby('Month')['Sales'].sum()

# Create Dashboard
plt.figure(figsize=(12, 5))

# Chart 1 - Sales by Product
plt.subplot(1, 3, 1)
product_sales.plot(kind='bar')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

# Chart 2 - Profit Distribution
plt.subplot(1, 3, 2)
product_profit.plot(kind='pie', autopct='%1.1f%%')
plt.title("Profit Distribution")
plt.ylabel("")

# Chart 3 - Monthly Sales Trend
plt.subplot(1, 3, 3)
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Adjust layout
plt.tight_layout()

# SAVE dashboard image file
plt.savefig("dashboard_output.png")

# Show dashboard
plt.show()

#saved data
with open("output.txt", "w") as file:
    file.write("SALES DASHBOARD REPORT\n")
    file.write("======================\n\n")

    file.write(f"Total Sales: {total_sales}\n")
    file.write(f"Total Profit: {total_profit}\n\n")

    file.write("Sales by Product:\n")
    file.write(str(product_sales))
    file.write("\n\n")

    file.write("Profit by Product:\n")
    file.write(str(product_profit))
    file.write("\n\n")

    file.write("Monthly Sales Trend:\n")
    file.write(str(monthly_sales))


# Create summary dataframe
summary = pd.DataFrame({
    'Metric': ['Total Sales', 'Total Profit'],
    'Value': [total_sales, total_profit]
})

# Save summary CSV
summary.to_csv("sales_summary.csv", index=False)

print("Dashboard saved as dashboard_output.png")
print("Summary saved as sales_summary.csv")