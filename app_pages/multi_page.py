import streamlit as st

class MultiPage:
    def __init__(self, app_name: str) -> None:
        self.app_name = app_name
        self.pages = []

        st.set_page_config(page_title=self.app_name, page_icon=":computer:")

    def add_page(self, title, func) -> None:
       self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio("Menu", self.pages, format_func=lambda page: page["title"])
        page["function"]()
