import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import kaleido

file = "C:\\Users\\User\\Desktop\\Portfolio_Python\\projet_python_SQL\\data\\ecommerce_sales_data.csv"

# Ouvrir le fichier et analyser les en-têtes / Opening the file and analysing the headers
df = pd.read_csv(file)
print(df.head(10))
print(df.info())

# Établir la database et la connection / Establish both the database and the connection
conn = sqlite3.connect("ecommerce.db")

df.to_sql("ecommerce", conn, if_exists="replace", index=False)

ca_total = """
           SELECT SUM(Price*Quantity) AS Revenu
           FROM ecommerce
           """
df_results = pd.read_sql_query(ca_total, conn)
print(df_results)

ca_category = """
              SELECT ProductCategory,
              SUM(Price*Quantity) AS Revenu
              FROM ecommerce
              GROUP BY ProductCategory
              ORDER BY Revenu DESC
              """
df_category = pd.read_sql_query(ca_category, conn)

monthly_revenu = """
                 SELECT strftime('%Y-%m', TransactionDate) AS month,
                    SUM(Price*Quantity) AS Revenu
                 FROM ecommerce
                 GROUP BY strftime('%Y-%m', TransactionDate)
                 ORDER BY month ASC
                 """
df_month = pd.read_sql_query(monthly_revenu, conn)

# Vérifier le retour / Checking the output
print(df_category)

# Identifier le problème de septembre 2024 / Identifying the problem of Sept. 2024
print(df_month)

check = """
        SELECT MIN(TransactionDate), MAX(TransactionDate)
        FROM ecommerce
        WHERE strftime('%Y-%m', TransactionDate) = '2024-09'
        """
df_check = pd.read_sql_query(check, conn)
print(df_check)

# Fermer la connection / Closing the connection
conn.close()

# Faire les graphiques / Creating the graphs
fig = px.bar(
    df_category,
    x="ProductCategory",
    y="Revenu",
    title="Total Revenu by Category",
    labels={"ProductCategory": "Categories",
            "Revenu": "Revenu"},
    )
fig.show()

fig = px.pie(
    df_category,
    names="ProductCategory",
    values="Revenu",
    title="Distribution by Category",
    hole = 0.3
    )
fig.show()

fig = px.line(
    df_month,
    x="month",
    y="Revenu",
    title='Monthly Revenu Evolution',
    labels={"month": "Month", "Revenu": "Revenu"},
    markers=True
)

# Hover propre / A clean hover
fig.update_traces(hovertemplate="<b>%{x}</b><br>Revenue: %{y:,.0f} €")

# Layout propre / A clean Layout
fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Revenue (€)",
    template="plotly_dark"
)

# Annotation mois incomplet
fig.add_annotation(
    x="2024-09",
    y=df_month["Revenu"].iloc[-1],
    text="Incomplete month",
    showarrow=True,
    arrowhead=2
)
fig.show()

# Création du dashboard
fig = make_subplots(
    rows=2,
    cols=2,
    specs=[[{'colspan':2}, None],
           [{"type":"bar"}, {"type":"domain"}]],
    subplot_titles=(
        "Monthly Revenue Distribution",
        "Revenue by Category",
        "Category Distribution"
    )
)
fig.add_trace(
    go.Scatter(
        x=df_month["month"],
        y=df_month["Revenu"],
        mode="lines+markers",
        name="Revenue",
    ),
    row=1, col=1
)
fig.add_trace(
    go.Bar(
        x=df_category["ProductCategory"],
        y=df_category["Revenu"],
        name="Categories",
    ),
    row=2, col=1
)
fig.add_trace(
    go.Pie(
        labels=df_category["ProductCategory"],
        values=df_category["Revenu"],
        hole=0.3
    ),
    row=2, col=2
)
fig.update_layout(
    title="E-commerce Sales Dashboard",
    template="plotly_dark",
    height=700,
    showlegend=False
)
fig.add_annotation(
    x="2024-09",
    y=df_month["Revenu"].iloc[-1],
    text="Incomplete month",
    showarrow=True,
    row=1, col=1
)

fig.write_image("C:\\Users\\User\\Desktop\\Portfolio_Python\\projet_python_SQL\\images\\dashboard.png")