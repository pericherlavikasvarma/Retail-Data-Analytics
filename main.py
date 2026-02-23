import pandas as pd
import datetime as dt

# Load dataset (Replace with your local path)
df = pd.read_xlsx(Datascienceencoding="ISO-8859-1")

# 1. Drop rows without CustomerID
df = df.dropna(subset=['CustomerID'])

# 2. Filter out returns (Quantity > 0) and UnitPrice > 0
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# 3. Create 'TotalSum' column
df['TotalSum'] = df['Quantity'] * df['UnitPrice']

# 4. Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# 5. Define a 'Snapshot Date' (1 day after the last transaction in the data)
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)