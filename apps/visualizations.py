import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


@st.cache
def fetch_data():
    data = pd.read_csv("./data/master.csv")
    return data

@st.cache
def preprocess_data():
    data = pd.read_csv("./data/master.csv")

    country_list = list(data['country'].drop_duplicates())
    year_list = list(data['year'].drop_duplicates())
    year_list.sort()
    country = []
    year = []
    no_of_suicides = []
    for countryname in country_list:
        for yearname in year_list:
            country.append(countryname)
            year.append(yearname)
            try:
                no_of_suicides.append(data.groupby(['country','year']).get_group((countryname,yearname))['suicides/100k pop'].sum())
            except:
                no_of_suicides.append(0)
                
    # convertion to dataframe
    df1 = pd.DataFrame({
        'Country':country,
        'Year':year,
        'Suicides per 100k':no_of_suicides
    })
    return df1



df = fetch_data()
df1 = preprocess_data()

def suicide_rates():
    st.title("Sucide Rate per Country Each Year")
    
    # plot
    fig = px.scatter(df1,x='Country',y='Suicides per 100k',animation_frame='Year',size='Suicides per 100k',color='Country')
    fig.update_layout(
        xaxis={
            'showticklabels':False,
            'showgrid':False
        },
        title='Suicides Rate Each Year Per Country',
        yaxis_title='Number of Suicides per 100k'
    )

    st.plotly_chart(fig)


def timeseries():
    st.title("Number of Suicides over the Years")
    year_list = list(df['year'].drop_duplicates())
    year_list.sort()
    deaths_per_year = []
    for yearname in year_list:
        deaths_per_year.append(df.groupby('year').get_group(yearname)['suicides_no'].sum())

    df2 = pd.DataFrame({
        'year':year_list,
        'deaths':deaths_per_year
    })
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=year_list,y=deaths_per_year,marker={'color':'red'},mode='lines+markers',hovertext=year_list,hoverinfo='text'))
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Suicides',
        title='Suicides over the Years',
    )
    st.plotly_chart(fig)

def gender():

    st.write("""
        The number of males that have commited suicides have exceeded that of the
        females by a very large margin. Difference in the male and female population might
        have a slight contribution to this. But still, the difference is huge
    """)
    malecount = df.groupby('sex').get_group('male')['suicides_no'].sum()
    femalecount = df.groupby('sex').get_group('female')['suicides_no'].sum()
    fig = px.bar(x=['Male','Female'],y=[malecount,femalecount],color=[malecount,femalecount])
    fig.update_layout(
        title='Gender vs Suicides',
        xaxis_title='Gender',
        yaxis_title='Number of Suicides'
    )
    st.plotly_chart(fig)


def generations():
    st.write("""
        The Boomer Generation has suffered the most from this problem, followed by the Silent
        Generation.
    """)
    generationlist = list(df['generation'].drop_duplicates())
    generations = []
    deaths = []
    for generation in generationlist:
        generations.append(generation)
        deaths.append(df.groupby('generation').get_group(generation)['suicides_no'].sum())
    df3 = pd.DataFrame({
        'generations':generations,
        'deaths':deaths
    })
    fig = px.pie(df3,values='deaths',names='generations')
    fig.update_layout(
        title='Distribution of deaths over different generations'
    )
    st.plotly_chart(fig)

def gdp_per_capita():
    st.write("""
        Even thought we can't see a perfect negetive correlation between gdp and the rate
        of suicides, it can be seen that as the gdp increases, the suicide rate gradually
        decreases.
    """)
    country_year_list = list(df['country-year'].drop_duplicates())
    gdp = []
    suicides = []
    for countryyear in country_year_list:
        gdp.append(df[['country-year','gdp_per_capita ($)','suicides/100k pop']].groupby('country-year').get_group(countryyear)['gdp_per_capita ($)'].iloc[0])
        suicides.append(df[['country-year','gdp_per_capita ($)','suicides/100k pop']].groupby('country-year').get_group(countryyear)['suicides/100k pop'].sum())

    # plot
    fig = px.scatter(x=gdp,y=suicides)
    fig.update_layout(
        title="GDP vs Suicide Rates",
        xaxis_title="Gdp",
        yaxis_title="Suicide rates"
    )
    st.plotly_chart(fig)

def country_best():
    country_list = list(df['country'].drop_duplicates())
    country_deaths = []
    for country in country_list:
        country_deaths.append(df.groupby('country').get_group(country)['suicides/100k pop'].mean())

    st.write(pd.DataFrame({
    'country':country_list,
    'suicide_rate':country_deaths
    }).sort_values(by='suicide_rate').head())

def app():
    suicide_rates()
    timeseries()

    st.write("""
        From the above 2 graphs, It is evident that even though the number of suicides 
        have been increasing tremendously , the number of suicides per 100k population 
        for most of the contries in the plot is controlled to a certain extent and
        does not increase after a certain point in time. this is due to the increase in population in 
        the recent decades and the correlation between the population and the number of suicides
    """)

    opt1 = st.selectbox(
        "Analyse Suicide Rate with ?",
        ('Gender',"Generations","GDP Per Capita")
    )   

    if opt1 == "Gender":
        gender()
    elif opt1 == "Generations":
        generations()
    elif opt1 == "GDP Per Capita":
        gdp_per_capita()

    st.header("Countries that have done a great Job in controlling suicide rates")
    st.write("""\n\n
    """)
    country_best()
