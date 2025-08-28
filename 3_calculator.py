import streamlit as st  # Import Streamlit library for building web apps
from app_pages.multi_page import MultiPage  # Import MultiPage class for multi-page support
from app_pages.page_calculator import calculator_body  # Import calculator page function

# Create an instance of MultiPage with the app name
app = MultiPage(app_name ="Calculator App")

# Add the calculator page to the app
app.add_page("Calculator", calculator_body)

# Run the Streamlit app
app.run()

