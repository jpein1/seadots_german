"""
components/cards.py
Reusable branded UI components for the dashboard.
"""
from __future__ import annotations
import streamlit as st
from components.styles import NAVY, GOLD, CYAN


# ── Indicator card ────────────────────────────────────────────────────────────

def indicator_card(
    label: str,
    value: str,
    delta: str | None = None,
    delta_direction: str = "up",   # "up" | "down" | "flat"
    accent: str = NAVY,
) -> None:
    delta_html = ""
    if delta:
        arrow = {"up": "↑", "down": "↓", "flat": "→"}.get(delta_direction, "→")
        delta_html = (
            f'<div class="indicator-delta {delta_direction}">{arrow} {delta}</div>'
        )

    st.markdown(
        f"""
        <div class="indicator-card" style="--accent-color:{accent}">
            <div class="indicator-label">{label}</div>
            <div class="indicator-value">{value}</div>
            {delta_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def indicator_row(metrics: list[dict]) -> None:
    """
    Render a horizontal row of indicator cards.

    Each dict in `metrics` should have keys:
        label, value, delta (opt), delta_direction (opt), accent (opt)
    """
    accents = [NAVY, GOLD, CYAN, "#1FCFF8"]
    cols = st.columns(len(metrics))
    for col, m, default_accent in zip(cols, metrics, accents):
        with col:
            indicator_card(
                label=m["label"],
                value=m["value"],
                delta=m.get("delta"),
                delta_direction=m.get("delta_direction", "flat"),
                accent=m.get("accent", default_accent),
            )


# ── Section / content card ────────────────────────────────────────────────────

class SectionCard:
    """
    Context-manager that wraps content in a styled section card.

    Usage
    -----
    with SectionCard("Sales Trend"):
        st.line_chart(df)
    """

    def __init__(self, title: str = "", padding: str = "24px 26px"):
        self.title = title
        self.padding = padding

    def __enter__(self):
        title_html = (
            f'<div class="section-title">{self.title}</div>' if self.title else ""
        )
        st.markdown(
            f'<div class="section-card" style="padding:{self.padding}">{title_html}',
            unsafe_allow_html=True,
        )
        return self

    def __exit__(self, *_):
        st.markdown("</div>", unsafe_allow_html=True)


# ── Badge helpers ─────────────────────────────────────────────────────────────

def badge(text: str, variant: str = "navy") -> str:
    """Return HTML for an inline badge. variant: navy | gold | cyan | green | red"""
    return f'<span class="badge badge-{variant}">{text}</span>'


def badge_row(items: list[tuple[str, str]]) -> None:
    """
    Render a row of badges.

    items : list of (text, variant) tuples
    """
    html = '<div class="tag-row">' + "".join(badge(t, v) for t, v in items) + "</div>"
    st.markdown(html, unsafe_allow_html=True)


# ── Sidebar branding ──────────────────────────────────────────────────────────

def sidebar_brand(
    name: str = "MyDash",
    tagline: str = "Analytics Platform",
    logo_path: str | None = None,
) -> None:
    from pathlib import Path

    if logo_path:
        root = Path(__file__).parent.parent
        abs_path = root / logo_path
        if abs_path.exists():
            st.sidebar.image(str(abs_path), width=150)

    st.sidebar.markdown(f"**{name}**  \n{tagline}")
    st.sidebar.divider()


def sidebar_nav() -> None:
    st.sidebar.markdown("#### Navigation")
    st.sidebar.page_link("app.py",                        label="🏠  Home")
    st.sidebar.page_link("pages/1_Case_Social_Ecological_System.py", label="🐟  Case SES")
    st.sidebar.page_link("pages/2_Scenario_initialization.py",       label="⚙️  Scenario initialization")
    st.sidebar.page_link("pages/3_Scenario_evaluation.py",           label="📊  Scenario evaluation")
    st.sidebar.page_link("pages/4_Explore_more.py",                  label="🔗  Explore more")
    st.sidebar.divider()


def page_footer() -> None:
    from pathlib import Path

    eu_logo = Path(__file__).parent.parent / "assets" / "eu_logo.jpg"
    if eu_logo.exists():
        st.markdown("---")
        st.image(str(eu_logo), width=120)


# ── Alert / info strip ────────────────────────────────────────────────────────

def info_strip(message: str, variant: str = "navy") -> None:
    """
    A slim full-width info strip.
    variant: navy | gold | cyan
    """
    colour_map = {
        "navy": (NAVY, "rgba(53,90,128,.08)"),
        "gold": (GOLD, "rgba(255,185,6,.10)"),
        "cyan": (CYAN, "rgba(31,207,248,.10)"),
    }
    border, bg = colour_map.get(variant, colour_map["navy"])
    st.markdown(
        f"""
        <div style="
            background:{bg};
            border-left:3px solid {border};
            border-radius:0 8px 8px 0;
            padding:10px 16px;
            font-size:.875rem;
            margin-bottom:16px;
        ">{message}</div>
        """,
        unsafe_allow_html=True,
    )
