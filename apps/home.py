import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

@st.cache
def get_dataset():
    return pd.read_csv("./data/master.csv")

df = get_dataset()

def dataset():
    st.title('Dataset')
    st.write("""
    
        The dataset used for the analysis was downloaded from kaggle.

        Dataset Link: https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016
    """)
    
    st.write("Dataset Sample")
    st.write(df.head())

def missing():
    st.title('Dealing with Missing Values')
    st.write("""
        As we can see below, the 'HDI for year' column is filled with missing values
        and in this case, much information is not available about the significance of the column
        so, This column is dropped from the dataset
    """)
    fig = plt.figure(figsize=(12,6))
    sns.heatmap(df.isna(),yticklabels=0)
    st.pyplot(fig)

def correlation():
    st.title('Correlation Between Variables')
    st.write("""
        Obviously, we can see that the population has a linear relationshio with the 
        number of suicides. So, for further analysis, we could use the number of suicides per 100k
        people rather than the number of suicides column for comparison between different countries
    """)
    fig = plt.figure(figsize=(8,5))
    sns.heatmap(df.drop(['HDI for year'],axis=1).corr())
    st.pyplot(fig)


def app():
    st.title('Objective')
    st.write("""
        This project is for the analysis of suicide data for the past few years
        to gain appropriate inference and draw conclusions.
    """)

    # sample dataset
    dataset()

    # missing values and correlation
    missing()
    correlation()
    
