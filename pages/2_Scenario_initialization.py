"""
pages/2_Scenario_initialization.py  –  Scenario configuration and interactive visualisation
"""
import sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st
st.set_page_config(page_title="Scenario initialization · Dashboard", layout="wide")

import plotly.graph_objects as go

from components import (
    inject_styles, page_header, branded_divider,
    sidebar_brand, sidebar_nav, page_footer,
)
from components.styles import NAVY, GOLD, CYAN
from scenarios_data import SCENARIOS, SCENARIO_IDS

inject_styles()
sidebar_brand("Decision support dashboard", "German bight demonstrator", logo_path="assets/seadots_logo.svg")
sidebar_nav()

# ── Page header ───────────────────────────────────────────────────────────────
page_header(
    "Scenario initialization",
    "Four what-if scenarios are defined below. Each scenario has fixed parameter values — "
    "select a scenario to inspect its configuration, then proceed to Scenario evaluation to "
    "compare outcomes.",
)

AREAS = [
    {"name": "Utsira",       "lat": 59.31, "lon":  4.87},
    {"name": "German Bight", "lat": 54.65, "lon":  7.80},
    {"name": "Gotland",      "lat": 57.50, "lon": 18.55},
]
fig_map = go.Figure(go.Scattermap(
    lat=[a["lat"] for a in AREAS],
    lon=[a["lon"] for a in AREAS],
    mode="markers+text",
    marker=dict(size=20, color=[NAVY, GOLD, CYAN], opacity=0.9),
    text=[a["name"] for a in AREAS],
    textposition="top center",
    textfont=dict(size=13, family="DM Sans, sans-serif"),
    hovertemplate="<b>%{text}</b><extra></extra>",
    name="",
))
fig_map.update_layout(
    map=dict(style="open-street-map", center=dict(lat=57.5, lon=10), zoom=4),
    height=420,
    margin=dict(l=0, r=0, t=0, b=30),
    paper_bgcolor="rgba(0,0,0,0)",
    showlegend=False,
)

# ── Context ───────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="section-card">
        <div class="section-title">Context</div>
        <p>The What-if scenarios are different options for the use of aquaculture within the OWF. They differ in location and amount of aquaculture.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Model visualisation + map ─────────────────────────────────────────────────
col_model, col_map = st.columns([1, 2])

with col_model:
    st.markdown(
        """
        <div class="section-card" style="height:100%;">
            <div class="section-title">Model visualisation</div>
            <p>Add a visualisation of your model here (e.g. IBM, FCM, hydrodynamic model diagram).</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_map:
    st.plotly_chart(fig_map, key="area_map")

branded_divider()

# ── Scenario overview cards ───────────────────────────────────────────────────
st.markdown(
    """
    <div class="section-card">
        <div class="section-title">What-if scenarios</div>
        <p>Four scenarios are pre-defined for this case. Select a scenario below to inspect
        its parameter values. Slider values are fixed and cannot be changed — they represent
        the conditions as defined for this case.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

sc1, sc2, sc3, sc4 = st.columns(4)
for col, sid in zip([sc1, sc2, sc3, sc4], SCENARIO_IDS):
    sc = SCENARIOS[sid]
    with col:
        st.markdown(
            f"""
            <div class="section-card">
                <div class="section-title">{sid} — {sc['title']}</div>
                <p>Wind: <strong>{sc['sliders']['Wind']}</strong> &nbsp;·&nbsp;
                   Fisheries: <strong>{sc['sliders']['Aquaculture']}</strong></br>
                   Regulations: <strong>{sc['sliders']['Regulatory Conditions']}</strong> &nbsp;·&nbsp;
                   Another: <strong>{sc['sliders']['another']}</strong></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Scenario profile (read-only) ──────────────────────────────────────────────
branded_divider()

st.markdown("""
<style>
[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--bg) !important;
    border-color: #E2EAF2 !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 8px rgba(53,90,128,.06) !important;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

active = st.radio(
    "Inspect scenario:",
    SCENARIO_IDS,
    format_func=lambda s: f"{s} — {SCENARIOS[s]['title']}",
    horizontal=True,
    key="active_scenario",
)

sc = SCENARIOS[active]

with st.container(border=True):
    st.markdown(
        f'<div class="section-title">Scenario profile — {active} {sc["title"]}</div>',
        unsafe_allow_html=True,
    )
    st.caption("Parameter values for this scenario are fixed and shown for reference only.")

    sp1, sp2 = st.columns(2)
    with sp1:
        st.select_slider(
            "Offshore wind spatial configuration",
            options=["Low", "Medium", "High"],
            value=sc["sliders"]["Wind"],
            disabled=True,
            key=f"wind_{active}",
        )
        st.select_slider(
            "Regulations",
            options=["Low", "Medium", "High"],
            value=sc["sliders"]["Regulatory Conditions"],
            disabled=True,
            key=f"other_{active}",
        )
    with sp2:
        st.select_slider(
            "Fisheries access",
            options=["Low", "Medium", "High"],
            value=sc["sliders"]["Aquaculture"],
            disabled=True,
            key=f"fisheries_{active}",
        )
        st.select_slider(
            "Another category",
            options=["Low", "Medium", "High"],
            value=sc["sliders"]["another"],
            disabled=True,
            key=f"another_{active}",
        )
        
        
st.markdown(
    f"""
            <div class="section-card">
                <div class="section-title"> {sc['title']}</div>

       <p> {sc['description']}</p>
    </div>
""",
    unsafe_allow_html=True,
)


st.image(sc["scenario_image"], width="stretch")

page_footer()
