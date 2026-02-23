# Customer Segmentation Analysis (RFM)

## 📌 Project Overview
This project focuses on transforming raw transactional data into actionable business intelligence. Using **RFM (Recency, Frequency, Monetary) Analysis**, I segmented a customer base of over 4,000 users into distinct groups to help a business understand purchasing behavior and optimize marketing strategies.



## 🛠️ Tools & Technologies
* **Language:** Python 3.x
* **Libraries:** Pandas (Data Manipulation), Matplotlib/Seaborn (Static Visualization), Plotly (Interactive 3D Visualization), Scikit-learn (Preprocessing)
* **Environment:** Jupyter Notebook / VS Code

## 🚀 Key Features & Workflow

### 1. Data Cleaning & Preprocessing
* Handled missing values in `CustomerID` to ensure data integrity.
* Filtered out "Return" transactions and zero-price entries to reflect actual revenue.
* Engineered a `TotalSum` feature for monetary calculations.

### 2. RFM Feature Engineering
* **Recency (R):** Days since the last purchase.
* **Frequency (F):** Number of unique transactions.
* **Monetary (M):** Total lifetime spend per customer.

### 3. Customer Segmentation Logic
Applied a quartile-based scoring system (1-4) to categorize customers:
* **Champions:** Recent, frequent, and high-spending customers.
* **Loyal/Potential:** Active customers with growth potential.
* **At-Risk/Hibernating:** Customers who haven't purchased in a long time and are likely to churn.

## 📊 Visualizations
* **Snake Plot:** A standardized line chart comparing the average R, F, and M values across segments.
* **3D Interactive Cluster:** An interactive Plotly scatter plot (log-scaled) demonstrating how customers naturally group together in 3D space.



## 📈 Business Insights & Recommendations
* **Champions:** Implement a loyalty program or early access to new products.
* **At-Risk:** Trigger automated "We Miss You" email campaigns with personalized discounts to prevent churn.
* **Potential Loyalists:** Use upsell strategies to increase their average order value.

## 📂 How to View
Due to GitHub's static rendering, the interactive 3D charts may not play directly. Please use [nbviewer](https://nbviewer.org/) and paste this repo's link to see the full interactive experience.
