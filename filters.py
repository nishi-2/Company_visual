import pandas as pd
import streamlit as st

def filter(df):
    df['year founded'] = df['year founded'].astype('int')
    years = df['year founded'].unique().tolist()
    years.sort()
    years.remove(0)
    years.insert(0, 'Overall')

    industry = df['industry'].unique().tolist()
    industry.sort()
    industry.insert(0, 'Overall')

    country = df['country'].unique().tolist()
    country.sort()
    country.insert(0, 'Overall')


    return years, industry, country


def apply_filter(df, year, industry, country):
    new_df = pd.DataFrame(
        {
            'name': df['name'],
            'year': df['year founded'],
            'industry': df['industry'],
            'country': df['country']
        }
    )

    if year == 'Overall' and industry == 'Overall' and country == 'Overall':
        temp = new_df

    if year == 'Overall' and industry != 'Overall' and country != 'Overall':
        temp = new_df[(new_df['industry'] == industry) & (new_df['country'] == country)]

    if industry == 'Overall' and year != 'Overall' and country != 'Overall':
        temp = new_df[(new_df['year'] == year) & (new_df['country'] == country)]

    if country == 'Overall' and industry != 'Overall' and year != 'Overall':
        temp = new_df[(new_df['year'] == year) & (new_df['industry'] == industry)]

    if year == 'Overall' and industry == 'Overall' and country != 'Overall':
        temp = new_df[new_df['country'] == country]

    if year == 'Overall' and country == 'Overall' and industry != 'Overall':
        temp = new_df[new_df['industry'] == industry]

    if year != 'Overall' and industry == 'Overall' and country == 'Overall':
        temp = new_df[new_df['year'] == year]

    if year != 'Overall' and industry != 'Overall' and country != 'Overall':
        temp = new_df[(new_df['industry'] == industry) & (new_df['country'] == country) & (new_df['year'] == year)]

    return(temp)
