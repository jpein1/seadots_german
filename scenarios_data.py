"""
scenarios_data.py — Static scenario definitions shared across Scenario initialization
and Scenario evaluation pages.

HOW TO UPDATE FOR CASE LEADERS
================================
Edit the SCENARIOS dict below. Each key ("01"–"04") maps to one scenario dict with:

  title        — short display name
  sliders      — fixed parameter values shown on the initialization page (Low/Medium/High)
  polygons     — list of map polygon dicts; each needs label, color, lats, lons
                 Replace placeholder coordinates with the real spatial footprint for your case.
  indicators   — list of outcome indicator dicts (label, value, delta, delta_direction, accent)
                 delta_direction: "up" | "down" | "flat"
  interpretation — dict with keys: positives, negatives, main  (all plain text / safe HTML)
  uncertainty  — plain text / safe HTML for the uncertainty, limitations, and assumptions section
  scenario_image - image of the AQ configuration within the OWF
"""

# NOTE: This module is imported AFTER the page has already added ROOT to sys.path,
# so the components import below is safe.
from components.styles import NAVY, GOLD, CYAN
import streamlit as st

SCENARIO_IDS = ["01", "02", "03", "04"]

SCENARIOS = {
    "01": {
        "title": "Business as usual",
        "sliders": {
            "Wind":      "High",
            "Aquaculture": "Low",
            "Regulatory Conditions":     "High",
            "another":   "Low",
        },
        # [CASE LEADERS] Replace lat/lon coordinates below with the real spatial footprint
        # for Scenario 01. Add or remove polygon dicts as needed.
        "polygons": [
            {
                "label": "Offshore wind (small)",
                "color": NAVY,
                "lats":  [54.0, 54.0, 55.5, 55.5, 54.0],
                "lons":  [4.5,  6.0,  6.0,  4.5,  4.5],
            },
            {
                "label": "Fisheries (large)",
                "color": GOLD,
                "lats":  [58.0, 58.0, 61.0, 61.0, 58.0],
                "lons":  [2.0,  6.5,  6.5,  2.0,  2.0],
            },
        ],
        # [CASE LEADERS] Replace value/delta strings below with real indicator outcomes
        # for Scenario 01.
        "indicators": [
            {"label": "Energy production potential", "value": "Higher",  "delta": "Higher",  "delta_direction": "up", "accent": NAVY},
            {"label": "Aquaculture production potential", "value": "Lower",  "delta": "Lower",  "delta_direction": "down", "accent": GOLD},
         #   {"label": "Fisheries performance",       "value": "Higher", "delta": "Higher", "delta_direction": "up",   "accent": CYAN},
        ],
        # [CASE LEADERS] Replace interpretation text below with scenario-specific content.
        "interpretation": {
            "positives": (
                "Offshore wind can be produced without any disturbances and has easy "
                "access to the monopiles for maintenance."
            ),
            "negatives": (
                "The aquaculture farmer has no high revenue, due to a small area for aquaculture. "
                "He still needs to go out to maintain lines and has therefore high vessel costs compared to the yield from the mussels."
            ),
            "main": (
                "Scenario 01 represents a business-as-usual trajectory with low aquaculture expansion. "
                "Offshore wind effort remains largely undisturbed, but the opportunity to scale mussel production "
                "is constrained."
            ),
        },
        # [CASE LEADERS] Replace uncertainty text below with scenario-specific content.
        "uncertainty": (
            "Key uncertainties include baseline aquaculture data quality and the extent to which current "
            "access patterns will persist under unchanged policy conditions. Assumes no new maritime "
            "spatial planning interventions are introduced within the scenario horizon."
        ),
        "scenario_image": "assets/WiS1.jpg",
        "description": (" This senario describes the situation right now. The OWF is operating at full fullest capacity. There are only small setups of aqua culture "
                        "at the corner of the wind farm grid. It is a test setup for the aquaculture, it tests the feasibilty and potential of aquaculture to gather "
                        " information both for the aqua culture farmer and scientist. The access to the monopiles for maintenance is not compromised."),
            
    },

    "02": {
        "title": "Moderate expansion",
        "sliders": {
            "Wind":      "High",
            "Aquaculture": "Medium",
            "Regulatory Conditions":     "Medium",
            "another":   "Medium",
        },
        # [CASE LEADERS] Replace lat/lon coordinates below with the real spatial footprint
        # for Scenario 02.
        "polygons": [
            {
                "label": "Offshore wind (medium)",
                "color": NAVY,
                "lats":  [53.5, 53.5, 56.5, 56.5, 53.5],
                "lons":  [4.0,  7.5,  7.5,  4.0,  4.0],
            },
            {
                "label": "Aquaculture",
                "color": CYAN,
                "lats":  [56.5, 56.5, 58.0, 58.0, 56.5],
                "lons":  [17.5, 20.0, 20.0, 17.5, 17.5],
            },
        ],
        # [CASE LEADERS] Replace indicator values for Scenario 02.
        "indicators": [
            {"label": "Energy production potential", "value": "Higher", "delta": "Higher", "delta_direction": "flat", "accent": NAVY},
            {"label": "Aquaculture production potential", "value": "Medium", "delta": "Medium", "delta_direction": "flat", "accent": GOLD},
         #   {"label": "Fisheries performance",       "value": "Medium", "delta": "Medium", "delta_direction": "flat", "accent": CYAN},
        ],
        # [CASE LEADERS] Replace interpretation text for Scenario 02.
        "interpretation": {
            "positives": (
                "Balanced expansion provides moderate aquaculture gains while maintaining "
                "aquaculture access through co-existence zones."
            ),
            "negatives": (
                "Neither objective is fully achieved: aquaculture goals remain partially unmet "
                "and for the OWF the access to the monopiles might be compromised`."
            ),
            "main": (
                "Scenario 02 explores a middle path with medium offshore wind expansion and "
                "negotiated aquaculture access. Trade-offs are distributed across sectors rather "
                "than concentrated in one area."
            ),
        },
        # [CASE LEADERS] Replace uncertainty text for Scenario 02.
        "uncertainty": (
            "Uncertainty is highest around co-existence zone management effectiveness and how "
            "aquaculture will adapt to medium-level displacement. "
        ),
        "scenario_image": "assets/WiS2.jpg",
        "description": (" The aquaculture long lines are all placed together in the center of the OWF, where they are best sheltered from waves and where they "
                        "easy accessable for the farmer. This scenario is ideal for the aquaculture farmer if the laws are quite regulativ, but they are allowed"
                        " to exploid aquaculture in one area of the OWF. Another advantage of the area in the middle is distance between the monopiles and that "
                        "are no powerlines directly under the long lines. The OWF operator has still good access to all the monopiles."),
    },

    "03": {
        "title": "High aquaculture priority",
        "sliders": {
            "Wind":      "Medium",
            "Aquaculture": "High",
            "Regulatory Conditions":     "Low",
            "another":   "Medium",
        },
        # [CASE LEADERS] Replace lat/lon coordinates below with the real spatial footprint
        # for Scenario 03.
        "polygons": [
            {
                "label": "Offshore wind (large)",
                "color": NAVY,
                "lats":  [53.0, 53.0, 57.5, 57.5, 53.0],
                "lons":  [3.5,  8.5,  8.5,  3.5,  3.5],
            },
            {
                "label": "Aquaculture",
                "color": CYAN,
                "lats":  [56.0, 56.0, 59.0, 59.0, 56.0],
                "lons":  [16.5, 21.0, 21.0, 16.5, 16.5],
            },
        ],
        # [CASE LEADERS] Replace indicator values for Scenario 03.
        "indicators": [
            {"label": "Energy production potential", "value": "Medium", "delta": "Medium", "delta_direction": "flat",   "accent": NAVY},
            {"label": "Aquaculture production potential", "value": "Higher", "delta": "Higher", "delta_direction": "up",   "accent": GOLD},
          #  {"label": "Fisheries performance",       "value": "Lower",  "delta": "Lower",  "delta_direction": "down", "accent": CYAN},
        ],
        # [CASE LEADERS] Replace interpretation text for Scenario 03.
        "interpretation": {
            "positives": (
                "Large-scale aquaculture deployment has a high potential for high mussels production."
                "and positive socio-economic impact on the aquaculture sector."
            ),
            "negatives": (
                "Significant restriction of fisheries access leads to substantial displacement "
                "and potential socio-economic impacts on fishing communities."
            ),
            "main": (
                "Scenario 03 prioritises energy transition over fisheries access. High renewable "
                "energy gains are achieved at the cost of considerable fishing effort displacement "
                "and reduced fisheries performance."
            ),
        },
        # [CASE LEADERS] Replace uncertainty text for Scenario 03.
        "uncertainty": (
            "Significant uncertainty around the impacts of the aquaculture on the OWF "
            "and the feasibility of full-scale aquaculture deployment within the planning horizon. "
            "Assumes strong political will."
        ),
        "scenario_image": "assets/WiS3.jpg",
        "description": ("This scenrio exploides every possible location for the aquaculture within the windfarm grid. The operation of the wind farm might be "
                        "compromised, due to more difficilty in reaching the monopiles. Lose regulations for the aquaculture are an important condition for this "
                        " scenario. The long lines are placed in such a way, that they are not above the power lines of the OWF grid."),
    },

    "04": {
        "title": "Integrated management",
        "sliders": {
            "Wind":      "High",
            "Aquaculture": "High",
            "Regulatory Conditions":     "Low",
            "another":   "High",
        },
        # [CASE LEADERS] Replace lat/lon coordinates below with the real spatial footprint
        # for Scenario 04.
        "polygons": [
            {
                "label": "Offshore wind (large)",
                "color": NAVY,
                "lats":  [53.5, 53.5, 57.5, 57.5, 53.5],
                "lons":  [4.5,  8.5,  8.5,  4.5,  4.5],
            },
            {
                "label": "Aquaculture (expanded)",
                "color": CYAN,
                "lats":  [56.0, 56.0, 59.5, 59.5, 56.0],
                "lons":  [16.0, 21.5, 21.5, 16.0, 16.0],
            },
        ],
        # [CASE LEADERS] Replace indicator values for Scenario 04.
        "indicators": [
            {"label": "Energy production potential", "value": "Higher", "delta": "Higher", "delta_direction": "up",   "accent": NAVY},
            {"label": "Aquaculture production potential", "value": "Lower",  "delta": "Lower",  "delta_direction": "down", "accent": GOLD},
         #   {"label": "Fisheries performance",       "value": "Higher", "delta": "Higher", "delta_direction": "up",   "accent": CYAN},
        ],
        # [CASE LEADERS] Replace interpretation text for Scenario 04.
        "interpretation": {
            "positives": (
                "Integrated multi-use zone management enables high wind energy output and maintained "
                "fisheries access through deliberate co-location design."
            ),
            "negatives": (
                "Implementation requires complex coordination between sectors and sustained governance "
                "investment; may not be feasible in all jurisdictions or within short timescales."
            ),
            "main": (
                "Scenario 04 explores ambitious integrated management where high wind energy deployment "
                "and high fisheries access are achieved simultaneously through spatial co-existence "
                "planning and adaptive management."
            ),
        },
        # [CASE LEADERS] Replace uncertainty text for Scenario 04.
        "uncertainty": (
            "High uncertainty around the practical feasibility of multi-use zones at scale and the "
            "long-term ecological effects of co-located uses. Assumes advanced monitoring capacity, "
            "adaptive management frameworks, and cross-sector institutional cooperation."
        ),
        "scenario_image": "assets/WiS1.jpg",
        "description": (" "),
    },
}
