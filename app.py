# importing the libraries
import streamlit as st
from apps import home, visualizations, conclusion
from multiapp import multiapp

# init
app = multiapp()

# apps
app.add_app('Intro',home.app)
app.add_app('Visualizations',visualizations.app)
app.add_app('Conclusions',conclusion.app)

# running the app
app.run()