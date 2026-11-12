"""
pages/4_Case_Social_Ecological_System.py  –  Case Social-Ecological System overview
"""
import sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st
st.set_page_config(page_title="Case SES · Dashboard", layout="wide")

from components import (
    inject_styles, page_header, sidebar_brand, sidebar_nav, page_footer,
)

inject_styles()
sidebar_brand("Decision support dashboard", "German Bight demonstrator", logo_path="assets/seadots_logo.svg")
sidebar_nav()

page_header(
    "Case Social Ecological System",
    "Overview of the social-ecological system context for this demonstrator.",
)

st.markdown(
    f"""
<div class="section-card" style="color: var(--text); font-family: 'DM Sans', sans-serif;">

<h2 style="color: var(--navy);">What is the social ecological systems (SES) framework?</h2>

<p>In SEADOTs, the SES framework is the foundation of the decision-support system (used in "Scenario initialization" and "Scenario evaluation").</p>

<p>The SES approach has been widely applied to describe and analyse diverse natural resource systems. 
The framework focuses on the components of, and linkages between, natural systems, human use, and ecosystem effects.</p>

<p>The framework splits social-ecological systems into four domains. 
<strong>Resource units</strong> (what we extract or use from the environment) are embedded in <strong>resource systems</strong> 
(spatially bounded areas where resource extraction and/or use takes place). 
<strong>Actors</strong> extract or use the resources in question; actors and their activities are governed by <strong>governance systems</strong> 
(institutions governing or influencing governance of the resource system and extractive/use activities). 
These four domains interact in varied ways, and result in outcomes like environmental and social sustainability. 
Lastly, the whole SES is influenced both by the larger ecosystems in which it is embedded and broader social, economic and political settings.</p>


</div>
""",
    unsafe_allow_html=True,
)

#[comment]: # img src="{ses_overview_img}" alt="SES overview diagram" style="width:100%; height:auto; display:block; margin-top:20px;" for the end of before </div>


st.markdown(
    f"""
<div class="section-card" style="color: var(--text); font-family: 'DM Sans', sans-serif;">

<h2 style="color: var(--navy);">The German Bight social ecological system</h2>

<h3 style="color: var(--navy);">System Definition and Social, economic and political settings</h3>

<p>In this study, the social–ecological system (SES) consists of an offshore wind farm in the southern North Sea and its potential for multi-use. 
The specific co-use option considered is the installation of low-trophic level aquaculture facilities within the offshore windfarm environment. 
The SES comprises the Meerwind Süd offshore wind farm and its potential co-use with offshore low-trophic aquaculture. 
The objective of the SES analysis is to identify the system components, interactions and governance structures that determine the subsequent construction of WiS. 
The case study focuses on the Meerwind Süd offshore wind farm, which has been in operation since 2015. 
While offshore wind energy is already commercially established in Germany, aquaculture is currently only operated onshore, 
with no active offshore installations. 
However, ongoing efforts involving scientists and aquaculture operators aim to assess the technical and economic feasibility of offshore aquaculture, 
indicating a transition phase in the socio-economic system.</p>

<h3 style="color: var(--navy);">Resource system</h3>

<p>The Meerwind Süd offshore wind farm is located approximately 23 km northwest of Helgoland in the German Bight. 
It consists of 80 monopile turbines, each with a capacity of 3.6 MW, resulting in a total installed capacity of 288 MW. 
The turbines are distributed over an area of approximately 43 km², with inter-turbine distances ranging between 1 and 1.5 km. 
The spatial extent of the wind farm defines the system boundaries of the SES. 
The potential integration of aquaculture introduces additional infrastructure within this bounded marine space, 
subject to safety and operational constraints.</p>

<h3 style="color: var(--navy);">Resource units</h3>

<p>The primary resource units are the monopile wind turbines and the prospective aquaculture installations. 
The turbines are bottom-fixed structures whose energy yield depends on wind conditions and maintenance requirements, 
with high economic value relative to aquaculture. Electricity prices and resulting profits are strongly influenced by market conditions and political frameworks. 
The potential aquaculture units comprise mussel longlines and shellfish towers. 
While mussel lines are established in nearshore environments, shellfish towers are still under development but have been tested offshore (e.g., in New Zealand). 
These systems are anchored to the seabed while remaining flexible in the water column. 
They represent a potential investment, with operational costs dominated by maintenance and logistics. 
Increasing demand for shellfish suggests growing economic potential for these resource units.</p>

<h3 style="color: var(--navy);">Actors</h3>

<p>The main actors are offshore wind farm operators, aquaculture developers, and the scientific community. 
Wind farm operators account for energy production and infrastructure maintenance, prioritising safety, accessibility, and operational efficiency. 
Aquaculture operators are interested in installing and managing offshore cultivation systems, with a focus on minimising operational 
costs and ensuring accessibility for maintenance and harvesting. Scientists play a key role in assessing feasibility, optimising system design, 
and providing advisory support, particularly given the absence of offshore aquaculture in Germany. 
Other potential actors, such as tourism, are acknowledged but not considered central to this analysis.</p>

<h3 style="color: var(--navy);">Governance system</h3>

<p>The governance framework is defined by national and European energy and maritime policies. 
Offshore wind energy is a key component of Germany’s energy strategy, with targets of 30 GW by 2030 and 70 GW by 2045. 
Marine spatial planning is managed by the Federal Maritime and Hydrographic Agency, which determines the location and scale of offshore wind developments. 
Existing regulations restrict activities such as fishing within offshore wind farm areas, 
while no comprehensive legal framework currently exists for aquaculture within these zones. 
Offshore wind projects are allocated through government tenders, and operators are required to construct and manage installations 
according to regulatory specifications. Within these constraints, operators may define additional rules governing co-use, 
which aquaculture developers must follow.</p>

<h3 style="color: var(--navy);">Related ecosystems</h3>

<p>The SES is influenced by environmental processes, particularly climate change and seasonal variability. 
Offshore wind energy production is affected by both wind wake effects within turbine arrays and long-term climate trends, 
with wake interactions exerting a stronger influence on yield reductions. 
Seasonal wind variability is expected to increase, with higher wind speeds in winter and lower speeds in summer. 
For aquaculture, seasonal dynamics are critical: growth depends on nutrient availability, which varies throughout the year, 
and harvest is typically limited to late summer and autumn, with negligible production in winter. 
These environmental factors define biophysical constraints for both energy production and aquaculture performance.</p>

<h3 style="color: var(--navy);">Interactions</h3>

<p>Interactions within the SES arise primarily from the co-location of offshore wind energy and aquaculture activities. 
Aquaculture installations must comply with safety regulations, including maintaining appropriate distances from 
turbine foundations and ensuring accessibility for maintenance operations. This creates a need for coordination between wind farm operators 
and aquaculture developers, including data exchange and joint planning. Both actors share an interest in efficient, safe, and economically viable operations. 
In addition, co-use may generate added value through improved public perception, 
as sustainability and resource efficiency are increasingly important in the Blue Economy, potentially supporting marketing and societal acceptance.</p>

<p>At the regional level, investment in Utsira Nord is an opportunity to compete for the industry necessary to enable large-scale floating offshore wind. 
Local and regional interactions also occur in the context of national- and international-level political agendas and lobbying, 
in the form of both decarbonization commitments and contestation over wind energy. 
Wind developers include economically powerful industry actors with deeply institutionalized ties to high-level political decision-makers.</p>

<h3 style="color: var(--navy);">Outcomes</h3>

<p>The primary outcomes of the SES include energy production and potential aquaculture yield. 
The wind farm features a nominal energy production of 288 MW, with relatively stable economic returns influenced by market demand and policy frameworks. 
Aquaculture outcomes are more variable, depending on environmental conditions, particularly nutrient availability and seasonal growth cycles. 
Operational costs, including vessel transit and maintenance, are influenced by the spatial configuration of installations within the wind farm, 
with factors such as travel distance affecting fuel consumption and overall profitability. 
Global crises and varying fuel prices can significantly affect operational costs. 
The economic viability of aquaculture is therefore strongly dependent on both environmental and 
logistical conditions as well as the global politics and energy context.</p>


</div>
""",
    unsafe_allow_html=True,
)
#<img src="{assets/SES_example.png}" alt="Utsira SES diagram" style="width:100%; height:auto; display:block; margin-top:20px;"> before </div>

st.image("assets/SES_example.png", width="stretch")

page_footer()
