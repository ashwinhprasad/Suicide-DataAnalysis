# importing the libraries
import streamlit as st
from apps import home
from multiapp import multiapp

# init
app = multiapp()

# apps
app.add_app('Home',home.app)

# running the app
app.run()