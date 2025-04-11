import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def load_data():
    # Connect to the PostgreSQL database using the same connection details as used in your project
    engine = create_engine('postgresql://postgres:secret@localhost:5432/finance_db')
    # Load data from the staging fact model created by dbt (or directly from the seed, based on your project)
    # Here we use the staging model "stg_fact_financial_transactions"
    query = "SELECT * FROM public.stg_fact_financial_transactions"
    df = pd.read_sql(query, engine)
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])

    # Calculate additional metrics: profit = amount - cost
    if 'profit' not in df.columns:
        df['profit'] = df['amount'] - df['cost']

    # Add a 'month' column for grouping purposes
    df['month'] = df['transaction_date'].dt.to_period('M').astype(str)
    return df

def plot_monthly_revenue(df):
    monthly_revenue = df.groupby('month', as_index=False)['amount'].sum()
    fig = px.line(monthly_revenue, x='month', y='amount',
                  title='Monthly Revenue from Financial Transactions',
                  labels={'amount': 'Total Revenue', 'month': 'Month'})
    st.plotly_chart(fig)

def plot_monthly_profit(df):
    monthly_profit = df.groupby('month', as_index=False)['profit'].sum()
    fig = px.line(monthly_profit, x='month', y='profit',
                  title='Monthly Profit from Financial Transactions',
                  labels={'profit': 'Total Profit', 'month': 'Month'})
    st.plotly_chart(fig)

def plot_department_analysis(df):
    # Calculate average profit per transaction and transaction volume by department
    dept_summary = df.groupby('department_id', as_index=False).agg({
        'profit': 'mean',
        'transaction_id': 'count'
    })
    dept_summary.rename(columns={'transaction_id': 'transaction_volume', 'profit': 'avg_profit'}, inplace=True)
    fig = px.bar(dept_summary, x='department_id', y='avg_profit',
                 title='Average Profit per Transaction by Department',
                 labels={'department_id': 'Department', 'avg_profit': 'Average Profit'})
    st.plotly_chart(fig)

def main():
    st.title("Financial Dashboard")

    # Display an overview of the data
    st.subheader("Data Overview")
    df = load_data()
    st.write(df.head())

    # Visualize monthly revenue
    st.subheader("Monthly Revenue Trend")
    plot_monthly_revenue(df)

    # Visualize monthly profit
    st.subheader("Monthly Profit Trend")
    plot_monthly_profit(df)

    # Visualize departmental performance
    st.subheader("Department Performance")
    plot_department_analysis(df)

if __name__ == "__main__":
    main()
