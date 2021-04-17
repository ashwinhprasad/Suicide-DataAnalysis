# importing the libraries
import streamlit as st

# multi app class
class multiapp:

    # init empty list for apps
    def __init__(self):
        self.apps = []

    # adding apps to object
    def add_app(self, title, func):
        self.apps.append({
            "title":title,
            "function":func
        })

    # running the instance
    def run(self):
        app = st.selectbox(
            'Navigation',
            self.apps,
            format_func=lambda app:app['title']
        )

        app['function']()