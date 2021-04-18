import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


@st.cache
def fetch_data():
    df0 = pd.read_csv("./data/master.csv")
    df1 = pd.read_csv("./data/df1.csv")
    df2 = pd.read_csv("./data/df2.csv")
    df3 = pd.read_csv("./data/df3.csv")
    df4 = pd.read_csv("./data/df4.csv")
    df5 = pd.read_csv("./data/df5.csv")
    return (df0,df1,df2,df3,df4,df5)

df = fetch_data()

def suicide_rates():
    st.title("Sucide Rate per Country Each Year")
    
    # plot
    fig = px.scatter(df[1],x='Country',y='Suicides per 100k',animation_frame='Year',size='Suicides per 100k',color='Country')
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
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df[2]['year'],y=df[2]['deaths'],marker={'color':'red'},mode='lines+markers',hovertext=df[2]['year'],hoverinfo='text'))
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
    malecount = df[0].groupby('sex').get_group('male')['suicides_no'].sum()
    femalecount = df[0].groupby('sex').get_group('female')['suicides_no'].sum()
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
    fig = px.pie(df[3],values='deaths',names='generations')
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
    # plot
    fig = px.scatter(df[4],x='gdp',y='suicides')
    fig.update_layout(
        title="GDP vs Suicide Rates",
        xaxis_title="Gdp",
        yaxis_title="Suicide rates"
    )
    st.plotly_chart(fig)

def country_best():
    st.header("Countries that have done a great Job in controlling suicide rates")
    st.write("""\n\n\n\n\n
    """)
    st.write("\n",df[5].reset_index(drop=True))

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

    
    country_best()
