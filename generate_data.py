# Import necessary libraries
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define a start date and create a list of dates (e.g., for 100 days)
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(100)]

# Generate synthetic data for the fact table
df = pd.DataFrame({
    'transaction_id': range(1, 101),
    'transaction_date': np.random.choice(dates, 100),
    'amount': np.random.uniform(100, 1000, 100).round(2),
    'cost': np.random.uniform(50, 500, 100).round(2),
    'department_id': np.random.choice([1, 2, 3], 100),
    'product_id': np.random.choice([101, 102, 103], 100)
})

# Save the data to a CSV file
df.to_csv('fact_financial_transactions.csv', index=False)
print("Synthetic data generated in fact_financial_transactions.csv")

