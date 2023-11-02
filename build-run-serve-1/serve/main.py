import streamlit as st
from streamlit.logger import get_logger
from streamlit_autorefresh import st_autorefresh

LOGGER = get_logger(__name__)

def run():
    st.set_page_config(
        page_title="BuildRunServe",
        page_icon="👋",
    )

    count = st_autorefresh(interval=2000, limit=None, key="counter")

    st.write("# Built Run and Served by LLM-GitOps 👋")
    st.write(f"Count: {count}")

if __name__ == "__main__":
    run()
