import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

# Database Connection
def get_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="115176",
        database="abes_dashboard"
    )
    query = "SELECT * FROM students"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Sidebar Filters

def sidebar_filters(df):
    st.sidebar.header("Filter Data")
    branches = st.sidebar.multiselect("Branch", options=df['branch'].unique(), default=df['branch'].unique())
    years = st.sidebar.multiselect("Year", options=df['year'].unique(), default=df['year'].unique())
    return df[(df['branch'].isin(branches)) & (df['year'].isin(years))]

# Main Dashboard

def main():
    st.title(" Arpit's Institute - BTech Student Analytics Dashboard")

    df = get_data()
    filtered_df = sidebar_filters(df)

    st.subheader("General Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", len(filtered_df))
    col2.metric("Avg CGPA", round(filtered_df['cgpa'].mean(), 2))
    col3.metric("Placement Rate", f"{round(filtered_df['placed'].mean() * 100, 2)}%")

    st.subheader("CGPA Distribution")
    st.plotly_chart(px.histogram(filtered_df, x="cgpa", nbins=20, color="branch"))

    st.subheader("Placement Overview")
    st.plotly_chart(px.pie(filtered_df, names='placed', title='Placed vs Not Placed'))

    st.subheader("Top Recruiters")
    top_companies = filtered_df[filtered_df['placed'] == 1]['company'].value_counts().reset_index()
    top_companies.columns = ['Company', 'Students']
    st.plotly_chart(px.bar(top_companies, x='Company', y='Students'))

    st.subheader("Attendance vs CGPA")
    st.plotly_chart(px.scatter(filtered_df, x='attendance_percent', y='cgpa', color='branch'))

    st.subheader("Raw Data")
    st.dataframe(filtered_df)

if __name__ == '__main__':
    main()
