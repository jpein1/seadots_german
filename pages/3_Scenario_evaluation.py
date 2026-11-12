"""
pages/3_Scenario_evaluation.py  –  Scenario comparison and evaluation
"""
import sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st
st.set_page_config(page_title="Scenario evaluation · Dashboard", layout="wide")

import plotly.graph_objects as go

from components import (
    inject_styles, page_header, branded_divider,
    indicator_row, sidebar_brand, sidebar_nav, page_footer,
)
from components.styles import NAVY, GOLD, CYAN
from scenarios_data import SCENARIOS, SCENARIO_IDS

inject_styles()
sidebar_brand("Decision support dashboard", "German bight ", logo_path="assets/seadots_logo.svg")
sidebar_nav()

# ── Page header ───────────────────────────────────────────────────────────────
page_header(
    "Scenario evaluation",
    "Select a scenario below to explore its spatial footprint, outcome indicators, "
    "and interpretation. Results are shown for comparison only — the tool does not rank, "
    "score or recommend an optimal scenario.",
)

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

# ── Comparison set: all four scenarios at a glance ────────────────────────────
with st.container(border=True):
    st.markdown('<div class="section-title">Comparison set</div>', unsafe_allow_html=True)
    btn_cols = st.columns(4)
    for col, sid in zip(btn_cols, SCENARIO_IDS):
        sc = SCENARIOS[sid]
        with col:
            st.markdown(
                f"""
                <div style="background:#355A80;color:#fff;border-radius:8px;
                            padding:10px 14px;font-family:'DM Sans',sans-serif;
                            font-size:.85rem;line-height:1.5;">
                    <div style="font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;
                                color:rgba(255,255,255,.65);margin-bottom:3px;">{sid} Scenario</div>
                    <strong>{sc['title']}</strong><br>
                    Wind: {sc['sliders']['Wind']} &nbsp;·&nbsp; Aquaculture: {sc['sliders']['Aquaculture']}<br>
                    Regulations: {sc['sliders']['Regulatory Conditions']} &nbsp;·&nbsp; Another: {sc['sliders']['another']}
                </div>
                """,
                unsafe_allow_html=True,
            )

branded_divider()

# ── Scenario selector ─────────────────────────────────────────────────────────
selected = st.radio(
    "Select scenario to evaluate:",
    SCENARIO_IDS,
    format_func=lambda s: f"{s} — {SCENARIOS[s]['title']}",
    horizontal=True,
    key="eval_scenario",
)

sc = SCENARIOS[selected]

branded_divider()

# ── Spatial evaluation view ───────────────────────────────────────────────────
# [CASE LEADERS] The polygons shown here come from scenarios_data.py → SCENARIOS[id]["polygons"].
# Each polygon dict needs: label (str), color (hex str), lats (list[float]), lons (list[float]).
# Replace the placeholder coordinates in scenarios_data.py with the real spatial footprint
# for each scenario. Add or remove polygon dicts per scenario as needed.

def hex_to_rgba(hex_color: str, alpha: float = 0.3) -> str:
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"

fig_spatial = go.Figure()
for poly in sc["polygons"]:
    fig_spatial.add_trace(go.Scattermap(
        lat=poly["lats"],
        lon=poly["lons"],
        mode="lines",
        fill="toself",
        fillcolor=hex_to_rgba(poly["color"], alpha=0.3),
        line=dict(color=poly["color"], width=2),
        name=poly["label"],
        hovertemplate=f"<b>{poly['label']}</b><extra></extra>",
    ))

fig_spatial.update_layout(
    map=dict(style="open-street-map", center=dict(lat=57.5, lon=10), zoom=3),
    height=480,
    margin=dict(l=0, r=0, t=0, b=0),
    paper_bgcolor="rgba(0,0,0,0)",
    legend=dict(
        orientation="h", y=0.01, x=0.01,
        bgcolor="rgba(255,255,255,0.8)",
        font=dict(family="DM Sans, sans-serif"),
    ),
)

with st.container(border=True):
    st.markdown(
        f'<div class="section-title">Spatial evaluation view — {selected} {sc["title"]}</div>',
        unsafe_allow_html=True,
    )
    st.plotly_chart(fig_spatial, key=f"spatial_map_{selected}")

branded_divider()

# ── Key outcome indicators ────────────────────────────────────────────────────
# [CASE LEADERS] Indicator values come from scenarios_data.py → SCENARIOS[id]["indicators"].
# Each indicator dict needs: label, value, delta, delta_direction ("up"/"down"/"flat"), accent.
# Replace placeholder values with real modelled outcomes for each scenario.

st.markdown(
    f'<div class="section-title" style="margin-bottom:12px;">Key outcome indicators — {selected} {sc["title"]}</div>',
    unsafe_allow_html=True,
)
indicator_row(sc["indicators"])

branded_divider()

# ── Scenario interpretation ───────────────────────────────────────────────────
# [CASE LEADERS] Interpretation text comes from scenarios_data.py → SCENARIOS[id]["interpretation"].
# Keys: positives, negatives, main. Replace placeholder text with scenario-specific content.

with st.container(border=True):
    st.markdown(
        f'<div class="section-title">Scenario interpretation — {selected} {sc["title"]}</div>',
        unsafe_allow_html=True,
    )

    pos_col, neg_col = st.columns(2)
    with pos_col:
        st.markdown(
            f"""
            <div class="section-card">
                <div class="section-title">Potential positives</div>
                <p>{sc['interpretation']['positives']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with neg_col:
        st.markdown(
            f"""
            <div class="section-card">
                <div class="section-title">Potential negatives</div>
                <p>{sc['interpretation']['negatives']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div style="background:#355A80;color:#fff;border-radius:8px;padding:16px 20px;
                    font-family:'DM Sans',sans-serif;font-size:.9rem;line-height:1.6;margin-top:8px;">
            <div style="font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;
                        color:rgba(255,255,255,.65);margin-bottom:6px;">Main interpretation</div>
            {sc['interpretation']['main']}
        </div>
        <div style="background:rgba(255,185,6,0.15);border:1px solid rgba(255,185,6,0.4);
                    border-radius:8px;padding:14px 18px;margin-top:10px;
                    font-family:'DM Sans',sans-serif;font-size:.875rem;line-height:1.6;
                    color:var(--navy);">
            No automatic recommendation is provided. The dashboard supports comparison and
            interpretation, but the decision remains with the user / decision-making process.
        </div>
        """,
        unsafe_allow_html=True,
    )

branded_divider()

# ── Uncertainty, limitations, and assumptions ─────────────────────────────────
# [CASE LEADERS] Uncertainty text comes from scenarios_data.py → SCENARIOS[id]["uncertainty"].
# Replace placeholder text with scenario-specific content.


# Want to implement plots about Mussel harvest, and relevant indicators for
# AQ within the OWF. The plots show then the advantages and risks 
# for each scenario.
st.markdown(
    f"""
    <div class="section-card">
        <div class="section-title">Uncertainty, limitations, and assumptions — {selected} {sc['title']}</div>
        <p>{sc['uncertainty']}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

page_footer()
