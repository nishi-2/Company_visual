import streamlit as st
import pandas as pd
import year, filters
import plotly.express as px
import matplotlib.pyplot as plt

#reading the dataset
df = pd.read_csv('filtered_file.csv')

#placing title on the selection sidebar
st.sidebar.title("Company Analysis")

#for selecting any one option from sidebar
side_option = st.sidebar.radio(
    'Choose an Option',
    ('Company Details', 'Charts')
)


#building the option for company details
if side_option == 'Company Details':
    # for creating filters on sidebar
    st.sidebar.title('Filters')
    year_val, industry, country = filters.filter(df)
    year_selected = st.sidebar.select_slider('Select years', year_val)
    industry_selected = st.sidebar.selectbox('Select Industry', industry)
    country_selected = st.sidebar.selectbox('Select Country', country)

    #company details changes as per the selection
    company_detail = filters.apply_filter(df, year_selected, industry_selected, country_selected)
    st.title('Details of Companies')
    st.dataframe(company_detail)

if side_option == 'Charts':
    val = year.year_analyse(df)

    # graph of companies all over the years
    year_company_graph = year.year_company(df)
    fig = px.line(year_company_graph, x='Year', y='count')
    st.title('Number of companies developed per year')
    st.plotly_chart(fig)

    #graph of companies past 30 years
    year_30_company = year.company_past_30_years(df)
    fig = px.bar(year_30_company, x='year founded', y='count of companies')
    st.title('Number of companies developed in last 30 years')
    st.plotly_chart(fig)

    #graph for top 20 countries as per number of companies
    top_20_country = year.top_country(df)
    fig = px.bar(top_20_country.nlargest(20, 'count').sort_values(by='count'), x='count', y='country', color = 'country')
    st.title('Top 20 countries as per number of companies')
    st.plotly_chart(fig)

    #graph for top 20 industries as per number of companies
    top_20_industry = year.top_industry(df)
    fig = px.bar(top_20_industry.nlargest(20, 'count').sort_values(by='count'), x='count', y='industry', color = 'industry')
    st.title('Top 20 industry as per number of companies')
    st.plotly_chart(fig)











