# Decision Support Dashboard — Streamlit Template

A SEADOTs branded multi-page Streamlit dashboard template for demo case leaders to adapt. The template is designed to be customised with your own content, scenarios, and models.

## Quick start

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Pages

| File | Purpose |
|------|---------|
| `app.py` | Home — welcome text, how-to guide, and about section |
| `pages/1_Case_Social_Ecological_System.py` | Overview of your case SES with description and diagram |
| `pages/2_Scenario_initialization.py` | Define what-if scenarios |
| `pages/3_Scenario_evaluation.py` | Evaluate and compare scenario outcomes with maps and interpretations provided by subject matter experts |
| `pages/4_Explore_more.py` | Links and further resources for your demonstrator |

---

## Adapting the template to your demonstrator

### 1. Branding

Update the sidebar title and tagline in every page file:

```python
sidebar_brand("Your dashboard title", "Your demonstrator name", logo_path="assets/seadots_logo.svg")
```

Replace `assets/seadots_logo.svg` with your own logo file.

Colours are defined in **two places that must stay in sync**:
- `components/styles.py` — Python constants (`NAVY`, `GOLD`, `CYAN`, …) and CSS variables
- `.streamlit/config.toml` — Streamlit theme colours

### 2. Home page (`app.py`)

- **Welcome text** — edit the `page_header(...)` call to describe your dashboard.
- **How to use** — update the four steps in the "How to use this dashboard" card to match what you want for your demo. 
- **About card** — replace the placeholder text with information about your demonstrator. The card also links to the Case SES page.

### 3. Case Social Ecological System (`pages/1_Case_Social_Ecological_System.py`)

- Replace the placeholder text in the description card with a brief overview of your SES context.
- Replace `assets/SES_example.png` with your own diagram or image. The image is displayed below the description card.

### 4. Scenario initialization (`pages/2_Scenario_initialization.py`)

The page is structured in two main sections:

**Top section — framing the scenarios**
- **Context card** — full-width card at the top. Replace the placeholder text with a description of the what-if scenario space for your case.
- **Model visualisation card** — shown alongside the interactive map. Add a diagram of your model (e.g. IBM, FCM, hydrodynamic model) here.
- **Map** — edit the `AREAS` list to set your study area locations (name, latitude, longitude).

**Bottom section — initialising scenarios**
- **Scenario cards** — four cards (01–04) with placeholder descriptions. The descriptions update dynamically to reflect the slider values the user has set for each scenario.
- **Scenario profile sliders** — rename "Offshore wind spatial configuration", "Fisheries access", "Other category", and "Another category" to the parameters relevant to your case. Each slider accepts Low / Medium / High and feeds directly into the scenario description text via f-string interpolation — update the sentence in `scenario_description()` to reflect your domain language.

### 5. Scenario evaluation (`pages/3_Scenario_evaluation.py`)

- **Comparison set** — four cards that automatically pull the scenario descriptions defined in Scenario initialization. No changes needed here unless you want to adjust the layout.
- **Spatial evaluation view** — edit the `POLYGONS` list to define the spatial zones relevant to your case (label, colour, and coordinate bounds).
- **Key outcome indicators** — update the `indicator_row(...)` call with the metrics and values relevant to your case.
- **Scenario interpretation** — update the f-string logic in `pos_text`, `neg_text`, and `interp_text` to reflect your domain. The yellow disclaimer card at the bottom is intentional and should be kept.
- **Uncertainty, limitations, and assumptions** — replace the placeholder text with content specific to your case and the parameter values selected.

### 6. Explore more (`pages/4_Explore_more.py`)

Add links to publications, datasets, VR experiences, or project pages relevant to your demonstrator.

### 7. Adding a new page

1. Create `pages/5_My_page.py` — Streamlit picks it up automatically.
2. Copy the boilerplate from an existing page (sys.path guard, `set_page_config`, imports, `inject_styles`, `sidebar_brand`, `sidebar_nav`).
3. Add a `st.sidebar.page_link` entry for the new file inside `sidebar_nav()` in `components/cards.py`.

---

## Component reference

All reusable UI components live in `components/`. Import from the package root:

```python
from components import inject_styles, page_header, branded_divider, indicator_row, \
    SectionCard, badge, badge_row, sidebar_brand, sidebar_nav, page_footer, info_strip
```

| Component | Description |
|-----------|-------------|
| `inject_styles()` | Call once per page — injects global CSS and Google Fonts |
| `page_header(title, subtitle)` | Styled page title with optional subtitle |
| `branded_divider()` | Navy → Cyan → Gold gradient rule |
| `indicator_card(label, value, delta, …)` | Single KPI tile with optional delta indicator |
| `indicator_row([{…}])` | Row of indicator tiles |
| `SectionCard(title)` | Context manager — wraps native Streamlit widgets in a styled card |
| `badge(text, variant)` | Inline pill — navy / gold / cyan / green / red |
| `badge_row([(text, variant)])` | Row of badges |
| `sidebar_brand(name, tagline, logo_path)` | Logo and title block at the top of the sidebar |
| `sidebar_nav()` | Navigation links in the sidebar — edit this to add or reorder pages |
| `page_footer()` | Footer with EU logo at the bottom of the main content area |
| `info_strip(message, variant)` | Full-width info or alert strip |

---

## Brand palette

| Token | Hex | Usage |
|-------|-----|-------|
| Navy | `#355A80` | Primary colour, headings, accents |
| Gold | `#FFB906` | Highlights, step indicators |
| Cyan | `#1FCFF8` | Secondary accent, chart traces |
| BG | `#FDFDFD` | Page background |
