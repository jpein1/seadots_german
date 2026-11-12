"""
app.py  –  Main entry point
Run with:  streamlit run app.py
"""
import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st

st.set_page_config(
    page_title="Decision support dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

from components import (
    inject_styles,
    page_header,
    branded_divider,
    sidebar_brand,
    sidebar_nav,
    page_footer,
)

inject_styles()

sidebar_brand("Decision support dashboard", "German bight", logo_path="assets/seadots_logo.svg")
sidebar_nav()

# ── Home page content ─────────────────────────────────────────────────────────
page_header(
    "Welcome!",
    "This is the dashboard of the German Bight case.",
)

st.markdown(
    """
    <div class="section-card">
        <div class="section-title">How to use this dashboard</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:0.75rem;">
            <div>
                <span style="font-size:1.5rem;font-weight:700;color:var(--gold);margin-right:0.5rem;">1</span>
                <strong>Understand the case</strong>
                <p style="margin:0.4rem 0 0 2rem;color:var(--muted);font-size:.9rem;">
                    Read about the social-ecological system in the <strong>Case SES</strong> page.
                </p>
            </div>
            <div>
                <span style="font-size:1.5rem;font-weight:700;color:var(--gold);margin-right:0.5rem;">2</span>
                <strong>Initialize scenarios</strong>
                <p style="margin:0.4rem 0 0 2rem;color:var(--muted);font-size:.9rem;">
                    Go to <strong>Scenario initialization</strong> and configure your input parameters
                    to define the conditions you want to explore.
                </p>
            </div>
            <div>
                <span style="font-size:1.5rem;font-weight:700;color:var(--gold);margin-right:0.5rem;">3</span>
                <strong>Evaluate scenarios</strong>
                <p style="margin:0.4rem 0 0 2rem;color:var(--muted);font-size:.9rem;">
                    Open <strong>Scenario evaluation</strong> to review outcomes, compare scenarios,
                    and draw conclusions for your decision.
                </p>
            </div>
            <div>
                <span style="font-size:1.5rem;font-weight:700;color:var(--gold);margin-right:0.5rem;">4</span>
                <strong>Explore more</strong>
                <p style="margin:0.4rem 0 0 2rem;color:var(--muted);font-size:.9rem;">
                    Links to more information
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

branded_divider()

st.markdown("""
<style>
[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--bg) !important;
    border-color: #E2EAF2 !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 8px rgba(53,90,128,.06) !important;
}
</style>
""", unsafe_allow_html=True)
with st.container(border=True):
    st.markdown('<div class="section-title">About</div>', unsafe_allow_html=True)
    st.markdown("<p style='color:var(--muted);margin:0 0 0.75rem 0;'>Here you can provide information on your demonstrator.</p>", unsafe_allow_html=True)
    st.page_link(
        "pages/1_Case_Social_Ecological_System.py",
        label="Case Social Ecological System →",
    )

page_footer()
