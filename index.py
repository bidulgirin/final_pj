import altair as alt
import streamlit as st

class SetMain():
    def __init__(self):
        st.set_page_config(
            page_title="와 진짜 신기하다",
            page_icon="💥",
            layout="wide",
            initial_sidebar_state="auto"
        )
        alt.themes.enable("dark")
        
    def render(self):
        st.title("멋진 타이틀")
        st.sidebar.success("이거 메뉴임?")

def main():
    app = SetMain()
    app.render()
  
    
if __name__ == "__main__":
    main()