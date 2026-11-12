"""
pages/3_Explore_more.py  –  Links and further resources
"""
import sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st
st.set_page_config(page_title="Explore more · Dashboard", layout="wide")

from components import (
    inject_styles, page_header, sidebar_brand, sidebar_nav, page_footer,
)

inject_styles()
sidebar_brand("Decision support dashboard", "German bight demonstrator", logo_path="assets/seadots_logo.svg")
sidebar_nav()

page_header("Explore more", "Further reading and resources related to this demonstrator.")

st.markdown(
    """
    <div class="section-card">
        <div class="section-title">Resources</div>
        <p>More about the wider project, its other demonstrator cases and its
           publications is on the SEADOTs project website:
           <a href="https://seadots-project.eu/" target="_blank" rel="noopener">seadots-project.eu</a>.</p>
    </div>
    """,
    unsafe_allow_html=True,
)


page_footer()
