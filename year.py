import streamlit as st
import pandas as pd

def year_analyse(df):
    name = df['name'].unique().shape[0]
    year = df['year founded'].unique().shape[0]
    industry = df['industry'].unique().shape[0]
    country = df['country'].unique().shape[0]
    employees = df['current employee estimate'].sum()

    st.title('Overall Statistics')
    col1, col2 = st.columns(2)
    with col1:
        st.header('Companies')
        st.title(name)
    with col2:
        st.header('Industry')
        st.title(industry)
    col3, col4 = st.columns(2)
    with col3:
        st.header('Country')
        st.title(country)
    with col4:
        st.header('Total Employees')
        st.title(employees)

def year_company(df):
    year_company = df[df['year founded'] != 0]['year founded'].value_counts().rename_axis('Year').reset_index(name='count').sort_values('Year')
    return year_company

def company_past_30_years(df):
    year_data = df.groupby('year founded', as_index=False)['name'].count()
    year_data = year_data.sort_values(by='year founded', ascending=False)[:30]
    year_data['count of companies'] = year_data['name']
    year_data.drop(columns=['name'], axis=1, inplace=True)
    return year_data

def top_country(df):
    country = df['country'].value_counts().rename_axis('country').reset_index(name='count')
    return country

def top_industry(df):
    industry = df['industry'].value_counts().rename_axis('industry').reset_index(name='count')
    return industry

