# python-SQL-ecommerce-insights
Analyze e-commerce sales data with Python, SQLite3, and Plotly to create an interactive dashboard for revenue insights and category trends.

# E-commerce Sales Dashboard

## Project Overview
This project focuses on analyzing e-commerce sales data using Python, SQL, and data visualization tools.  
The objective is to extract meaningful insights from raw transactional data and present them through a clear and interactive dashboard.

## Technologies Used
- Python
- Pandas
- SQLite
- Plotly

## Dataset Description
The dataset contains 100,000 transactions with the following key features:  
- ProductCategory  
- Quantity  
- Price  
- TransactionDate  
- CustomerLocation  
- PaymentMethod  
- Customer demographics (age, gender, income group, loyalty score)  

## Data Processing
- Data loaded from CSV using Pandas  
- Stored in a SQLite database for querying  
- SQL used to compute:  
  - Total revenue  
  - Revenue by product category  
  - Monthly revenue trends  

## Dashboard Features
The dashboard includes:  
1. **Monthly Revenue Evolution**  
   - Line chart showing revenue trends over time  
   - Helps identify patterns and anomalies  
2. **Revenue by Category**  
   - Bar chart ranking product categories by revenue  
3. **Category Distribution**  
   - Donut chart showing revenue share by category  

## Data Insight
A significant drop is observed in September 2024.  
This is not due to a business decline but to incomplete data, as only the first two days of the month are present in the dataset.  
This data point is intentionally kept in the visualization and clearly annotated to ensure transparency and accurate interpretation.

## Key Learnings
- Writing SQL queries for aggregation and analysis  
- Handling and identifying incomplete data  
- Building interactive dashboards with Plotly  
- Applying data storytelling principles


Future Improvements
Add interactive filters (by category, location, or payment method)
Enhance dashboard design and UX
Perform deeper customer segmentation analysis

Author

Valentin Viault
