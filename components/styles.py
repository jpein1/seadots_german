import streamlit as st

# ── Brand palette ────────────────────────────────────────────────────────────
NAVY    = "#355A80"
GOLD    = "#FFB906"
CYAN    = "#1FCFF8"
BG      = "#FDFDFD"
SURFACE = "#F0F4F8"
TEXT    = "#1A2733"
MUTED   = "#6B8299"


def inject_styles() -> None:
    """Inject global CSS + Google Fonts into the Streamlit app."""
    st.markdown(
        f"""
        <style>
        /* ── Google Fonts ───────────────────────────────────────────── */
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,700;1,9..40,300&family=DM+Mono:wght@400;500&display=swap');

        /* ── CSS Variables ──────────────────────────────────────────── */
        :root {{
            --navy:    {NAVY};
            --gold:    {GOLD};
            --cyan:    {CYAN};
            --bg:      {BG};
            --surface: {SURFACE};
            --text:    {TEXT};
            --muted:   {MUTED};
            --radius:  12px;
            --shadow:  0 2px 16px rgba(53,90,128,.10);
            --shadow-hover: 0 6px 28px rgba(53,90,128,.18);
        }}

        /* ── Global reset ───────────────────────────────────────────── */
        html, body, [class*="css"] {{
            font-family: 'DM Sans', sans-serif !important;
            background-color: var(--bg) !important;
            color: var(--text) !important;
        }}

        /* ── Streamlit chrome ───────────────────────────────────────── */
        #MainMenu, footer, header {{ visibility: hidden; }}

        /* ── Hide ALL sidebar collapse/expand controls ──────────────── */
        [data-testid="collapsedControl"],
        button[kind="header"],
        [data-testid="stSidebarCollapseButton"] {{
            display: none !important;
            visibility: hidden !important;
            pointer-events: none !important;
        }}

        /* ── Hide Streamlit's auto-generated page nav ───────────────── */
        [data-testid="stSidebarNav"] {{
            display: none !important;
        }}


        /* ── Top page header ────────────────────────────────────────── */
        .page-header {{
            padding: 8px 0 28px 0;
            border-bottom: 2px solid var(--surface);
            margin-bottom: 28px;
        }}
        .page-header h1 {{
            font-size: 1.9rem;
            font-weight: 700;
            color: var(--navy);
            margin: 0 0 4px 0;
            letter-spacing: -.02em;
        }}
        .page-header p {{
            color: var(--muted);
            margin: 0;
            font-size: .92rem;
        }}

        /* ── Indicator card ───────────────────────────────────────────── */
        .indicator-card {{
            background: var(--bg);
            border: 1px solid #E2EAF2;
            border-radius: var(--radius);
            padding: 20px 22px 16px;
            box-shadow: var(--shadow);
            transition: box-shadow .25s, transform .25s;
            position: relative;
            overflow: hidden;
        }}
        .indicator-card:hover {{
            box-shadow: var(--shadow-hover);
            transform: translateY(-2px);
        }}
        .indicator-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 3px;
            background: var(--accent-color, var(--navy));
        }}
        .indicator-label {{
            font-size: .72rem;
            text-transform: uppercase;
            letter-spacing: .10em;
            color: var(--muted);
            margin-bottom: 8px;
            font-weight: 500;
        }}
        .indicator-value {{
            font-size: 2rem;
            font-weight: 700;
            color: var(--navy);
            line-height: 1;
            margin-bottom: 6px;
            font-family: 'DM Mono', monospace;
        }}
        .indicator-delta {{
            font-size: .78rem;
            font-weight: 500;
        }}
        .indicator-delta.up   {{ color: #18A06A; }}
        .indicator-delta.down {{ color: #D94F4F; }}
        .indicator-delta.flat {{ color: var(--muted); }}

        /* ── Section card (generic container) ───────────────────────── */
        .section-card {{
            background: var(--bg);
            border: 1px solid #E2EAF2;
            border-radius: var(--radius);
            padding: 24px 26px;
            box-shadow: var(--shadow);
            margin-bottom: 20px;
        }}
        .section-title {{
            font-size: .78rem;
            text-transform: uppercase;
            letter-spacing: .10em;
            color: var(--muted);
            margin-bottom: 16px;
            font-weight: 500;
        }}

        /* ── Badge ──────────────────────────────────────────────────── */
        .badge {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: .70rem;
            font-weight: 600;
            letter-spacing: .04em;
            text-transform: uppercase;
        }}
        .badge-navy  {{ background: rgba(53,90,128,.12); color: var(--navy); }}
        .badge-gold  {{ background: rgba(255,185,6,.15);  color: #9A6E00;    }}
        .badge-cyan  {{ background: rgba(31,207,248,.15); color: #0B8FAD;    }}
        .badge-green {{ background: rgba(24,160,106,.12); color: #18A06A;    }}
        .badge-red   {{ background: rgba(217,79,79,.12);  color: #D94F4F;    }}

        /* ── Tag row ────────────────────────────────────────────────── */
        .tag-row {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 12px;
        }}

        /* ── Divider ────────────────────────────────────────────────── */
        .branded-divider {{
            height: 2px;
            background: linear-gradient(90deg, var(--navy), var(--cyan), var(--gold));
            border: none;
            border-radius: 2px;
            margin: 24px 0;
        }}

        /* ── Streamlit native widget tweaks ─────────────────────────── */
        .stButton > button {{
            background: var(--navy) !important;
            color: #fff !important;
            border: none !important;
            border-radius: 8px !important;
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
            padding: 8px 20px !important;
            transition: opacity .2s !important;
        }}
        .stButton > button:hover {{ opacity: .85 !important; }}

        .stDownloadButton > button {{
            background: var(--gold) !important;
            color: var(--navy) !important;
        }}

        div[data-baseweb="select"] > div {{
            border-color: #D0DDE8 !important;
            border-radius: 8px !important;
        }}

        .stDataFrame thead tr th {{
            background: var(--navy) !important;
            color: #fff !important;
        }}

        /* ── Plotly chart background fix ─────────────────────────────── */
        .js-plotly-plot .plotly .bg {{
            fill: transparent !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = "") -> None:
    """Render a styled page header."""
    sub_html = f"<p>{subtitle}</p>" if subtitle else ""
    st.markdown(
        f'<div class="page-header"><h1>{title}</h1>{sub_html}</div>',
        unsafe_allow_html=True,
    )


def branded_divider() -> None:
    st.markdown('<hr class="branded-divider">', unsafe_allow_html=True)
