## LIBRARY IMPORTS ##
import streamlit as st
import streamlit.components.v1 as components

import pandas as pd
import numpy as np

import plotly as ply
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from PIL import Image
import datetime

# import matplotlib.pyplot as plt
# import seaborn as sns
# import dash as dash
# from dash import dash_table
# from dash import dcc
# from dash import html
# from dash.dependencies import Input, Output
# from dash.exceptions import PreventUpdate
# import dash_bootstrap_components as dbc

# import scipy.stats as stats
# import statistics

#%%
## DIRECTORY CONFIGURATION ##
current_path = r'https://raw.githubusercontent.com/nehat312/fantasy-football-2022/main'
basic_path = 'https://raw.githubusercontent.com/nehat312/fantasy-football-2022/main'
overview_path = current_path + '/data/2022-FF-Overview.csv'
overall_path = current_path + '/data/2022-FF-Overall.csv'
qb_path = current_path + '/data/2022-FF-QB.csv'
rb_path = current_path + '/data/2022-FF-RB.csv'
wr_path = current_path + '/data/2022-FF-WR.csv'
te_path = current_path + '/data/2022-FF-TE.csv'
idp_path = current_path + '/data/2022-FF-IDP.csv'
k_path = current_path + '/data/2022-FF-K.csv'
# dst_path = current_path + '/data/2022-FF-DST.csv'

#%%
## TIME INTERVALS ##
today = datetime.date.today()
before = today - datetime.timedelta(days=1095) #700
start_date = '2000-01-01'
end_date = today

#%%
## DATA IMPORT ##
nfl_overview = pd.read_csv(overview_path, header=0, index_col='RK')
overall_rankings = pd.read_csv(overall_path, header=0, index_col='RK')
qb_rankings = pd.read_csv(qb_path, header=0, index_col='RK')
rb_rankings = pd.read_csv(rb_path, header=0, index_col='RK')
wr_rankings = pd.read_csv(wr_path, header=0, index_col='RK')
te_rankings = pd.read_csv(te_path, header=0, index_col='RK')
idp_rankings = pd.read_csv(idp_path, header=0, index_col='RK')
k_rankings = pd.read_csv(k_path, header=0, index_col='RK')
# dst_rankings = pd.read_csv(dst_path, header=0, index_col='RK')

# print(qb_rankings.info())
# print(qb_rankings.columns)

#%%
all_cols = ['CODE', 'PLAYER', 'TEAM', 'BYE',
            'PPL TEAM', 'SALARY', 'TAG',
            '2022 PROJ', '2021 TTL',
            'BEST', 'WORST', 'AVG']

output_cols = ['CODE', 'PLAYER', 'TEAM', 'BYE',
               '2021 TTL', #'2022 PROJ', 
               'BEST', 'WORST', 'AVG']

overview_dash = nfl_overview
overall_rankings = overall_rankings[output_cols]
qb_rankings = qb_rankings[output_cols]
rb_rankings = rb_rankings[output_cols]
wr_rankings = wr_rankings[output_cols]
te_rankings = te_rankings[output_cols]
idp_rankings = idp_rankings[output_cols]
k_rankings = k_rankings[output_cols]


## IMAGE IMPORT ##
NFL_logo = Image.open('images/NFL-Logo.png')
AFC_logo = Image.open('images/AFC-Logo.png')
NFC_logo = Image.open('images/NFC-Logo.png')

DAL_logo = Image.open('images/DAL-Cowboys.png')
PHI_logo = Image.open('images/PHI-Eagles.png')
NYG_logo = Image.open('images/NYG-Giants.png')
WAS_logo = Image.open('images/WAS-Commanders.png')

MIN_logo = Image.open('images/MIN-Vikings.png')
GBP_logo = Image.open('images/GBP-Packers.png')
DET_logo = Image.open('images/DET-Lions.png')
CHI_logo = Image.open('images/CHI-Bears.png')

LAR_logo = Image.open('images/LAR-Rams.png')
ARI_logo = Image.open('images/ARI-Cardinals.png')
SEA_logo = Image.open('images/SEA-Seahawks.png')
SFO_logo = Image.open('images/SFO-49ers.png')

NOS_logo = Image.open('images/NOS-Saints.png')
TBB_logo = Image.open('images/TBB-Buccaneers.png')
ATL_logo = Image.open('images/ATL-Falcons.png')
CAR_logo = Image.open('images/CAR-Panthers.png')

NEP_logo = Image.open('images/NEP-Patriots.png')
MIA_logo = Image.open('images/MIA-Dolphins.png')
BUF_logo = Image.open('images/BUF-Bills.png')
NYJ_logo = Image.open('images/NYJ-Jets.png')

IND_logo = Image.open('images/IND-Colts.png')
JAC_logo = Image.open('images/JAC-Jaguars.png')
HOU_logo = Image.open('images/HOU-Texans.png')
TEN_logo = Image.open('images/TEN-Titans.png')

CIN_logo = Image.open('images/CIN-Bengals.png')
PIT_logo = Image.open('images/PIT-Steelers.png')
BAL_logo = Image.open('images/BAL-Ravens.png')
CLE_logo = Image.open('images/CLE-Browns.png')

KCC_logo = Image.open('images/KCC-Chiefs.png')
LVR_logo = Image.open('images/LVR-Raiders.png')
LAC_logo = Image.open('images/LAC-Chargers.png')
DEN_logo = Image.open('images/DEN-Broncos.png')

## FORMAT / STYLE ##

## COLOR SCALES ##
YlOrRd = px.colors.sequential.YlOrRd
Mint = px.colors.sequential.Mint
Electric = px.colors.sequential.Electric
Sunsetdark = px.colors.sequential.Sunsetdark
Sunset = px.colors.sequential.Sunset
Tropic = px.colors.diverging.Tropic
Temps = px.colors.diverging.Temps
Tealrose = px.colors.diverging.Tealrose
Blackbody = px.colors.sequential.Blackbody
Ice = px.colors.sequential.ice
Ice_r = px.colors.sequential.ice_r
Dense = px.colors.sequential.dense

## VISUALIATION LABELS ##

# chart_labels = {'pl_name':'PL. NAME',
#                 }


## FEATURE VARIABLES ##


## VISUALIZATIONS ##


#%%
#####################
### STREAMLIT APP ###
#####################

## CONFIGURATION ##
st.set_page_config(page_title='FANTASY FOOTBALL DRAFT KIT', layout='wide', initial_sidebar_state='auto') #, page_icon=":smirk:"

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)

## CSS LAYOUT CUSTOMIZATION ##

th_props = [('font-size', '12px'),
            ('text-align', 'center'),
            ('font-weight', 'bold'),
            ('color', '#EBEDE9'), #6d6d6d #29609C
            ('background-color', '#29609C') #f7f7f9
            ]

td_props = [('font-size', '12px'),
            # ('text-align', 'center'),
            # ('font-weight', 'bold'),
            # ('color', '#EBEDE9'), #6d6d6d #29609C
            # ('background-color', '#29609C') #f7f7f9
            ]

df_styles = [dict(selector="th", props=th_props),
             dict(selector="td", props=td_props)]


col_format_dict = {'BYE': "{:,}",
                   '2022 PROJ': "{:,}",
                   '2021 TTL': "{:,}",
                   'BEST': "{:,}",
                   'WORST': "{:,}",
                   'AVG': "{:,}",
                   'WINS': "{:,}",
                   'O-LINE-RK': "{:,}",
                   'D-LINE-RK': "{:,}",
                   'OFFENSE-RK': "{:,}",
                   'DST-RK': "{:,}",
                   # 'DE-RK': "{:,}",
                   # 'SALARY': "${:.2}", #"${:,}"
                   # #: "{:.1%}", #:"{:.1}x",
                   }

## SIDEBAR ##
# st.sidebar.xyz

# sidebar_header = st.sidebar.subheader('VISUALIZATION TIMEFRAME:')
# sidebar_start = st.sidebar.date_input('START DATE', before)
# sidebar_end = st.sidebar.date_input('END DATE', today)
# if sidebar_start < sidebar_end:
#     st.sidebar.success('START DATE: `%s`\n\nEND DATE: `%s`' % (sidebar_start, sidebar_end))
# else:
#     st.sidebar.error('ERROR: END DATE BEFORE START DATE')

## HEADER ##
st.container()
st.title('2022-2023 FANTASY FOOTBALL DRAFT KIT')

## NFC LOGOS ##
NFCEast_col_1, NFCEast_col_2, NFCEast_col_3, NFCEast_col_4,\
NFCWest_col_1, NFCWest_col_2, NFCWest_col_3, NFCWest_col_4, \
NFCSouth_col_1, NFCSouth_col_2, NFCSouth_col_3, NFCSouth_col_4,\
NFCNorth_col_1, NFCNorth_col_2, NFCNorth_col_3, NFCNorth_col_4 = st.columns(16)
NFCEast_col_1.image(WAS_logo, caption='WAS', width=45)
NFCEast_col_2.image(PHI_logo, caption='PHI', width=45)
NFCEast_col_3.image(DAL_logo, caption='DAL', width=45)
NFCEast_col_4.image(NYG_logo, caption='NYG', width=45)
NFCWest_col_1.image(LAR_logo, caption='LAR', width=45)
NFCWest_col_2.image(SFO_logo, caption='SFO', width=45)
NFCWest_col_3.image(SEA_logo, caption='SEA', width=45)
NFCWest_col_4.image(ARI_logo, caption='ARI', width=45)
NFCSouth_col_1.image(TBB_logo, caption='TBB', width=45)
NFCSouth_col_2.image(NOS_logo, caption='NOS', width=45)
NFCSouth_col_3.image(ATL_logo, caption='ATL', width=45)
NFCSouth_col_4.image(CAR_logo, caption='CAR', width=45)
NFCNorth_col_1.image(GBP_logo, caption='GBP', width=45)
NFCNorth_col_2.image(MIN_logo, caption='MIN', width=45)
NFCNorth_col_3.image(DET_logo, caption='DET', width=45)
NFCNorth_col_4.image(CHI_logo, caption='CHI', width=45)

## AFC LOGOS ##
AFCEast_col_1, AFCEast_col_2, AFCEast_col_3, AFCEast_col_4,\
AFCWest_col_1, AFCWest_col_2, AFCWest_col_3, AFCWest_col_4, \
AFCSouth_col_1, AFCSouth_col_2, AFCSouth_col_3, AFCSouth_col_4,\
AFCNorth_col_1, AFCNorth_col_2, AFCNorth_col_3, AFCNorth_col_4 = st.columns(16)
AFCEast_col_1.image(BUF_logo, caption='BUF', width=45)
AFCEast_col_2.image(MIA_logo, caption='MIA', width=45)
AFCEast_col_3.image(NEP_logo, caption='NEP', width=45)
AFCEast_col_4.image(NYJ_logo, caption='NYJ', width=45)
AFCWest_col_1.image(KCC_logo, caption='KCC', width=45)
AFCWest_col_2.image(LAC_logo, caption='LAC', width=45)
AFCWest_col_3.image(LVR_logo, caption='LVR', width=45)
AFCWest_col_4.image(DEN_logo, caption='DEN', width=45)
AFCSouth_col_1.image(IND_logo, caption='IND', width=45)
AFCSouth_col_2.image(TEN_logo, caption='TEN', width=45)
AFCSouth_col_3.image(HOU_logo, caption='HOU', width=45)
AFCSouth_col_4.image(JAC_logo, caption='JAC', width=45)
AFCNorth_col_1.image(BAL_logo, caption='BAL', width=45)
AFCNorth_col_2.image(CIN_logo, caption='CIN', width=45)
AFCNorth_col_3.image(CLE_logo, caption='CLE', width=45)
AFCNorth_col_4.image(PIT_logo, caption='PIT', width=45)


## SECTOR TABS ##
tab_0, tab_1, tab_2, tab_3, tab_4, tab_5, tab_6, tab_7, tab_8\
    = st.tabs(['NFL', 'OVERALL', 'QB', 'RB', 'WR', 'TE', 'K', 'IDP', 'DST'])

with tab_0:
    st.subheader('NFL OVERVIEW')
    st.dataframe(overview_dash.style.format(col_format_dict).set_table_styles(df_styles))

with tab_1:
    st.subheader('OVERALL RANKINGS')
    st.dataframe(overall_rankings.style.format(col_format_dict).set_table_styles(df_styles))

with tab_2:
    st.subheader('QUARTERBACK [QB] RANKINGS')
    st.dataframe(qb_rankings.style.format(col_format_dict).set_table_styles(df_styles))

with tab_3:
    st.subheader('RUNNINGBACK [RB] RANKINGS')
    st.dataframe(rb_rankings.style.format(col_format_dict).set_table_styles(df_styles))

with tab_4:
    st.subheader('WIDE RECEIVER [WR] RANKINGS')
    st.dataframe(wr_rankings.style.format(col_format_dict).set_table_styles(df_styles))

with tab_5:
    st.subheader('TIGHT END [TE] RANKINGS')
    st.dataframe(te_rankings.style.format(col_format_dict).set_table_styles(df_styles))

with tab_6:
    st.subheader('KICKER [K] RANKINGS')
    # st.dataframe(k_rankings.style.format(col_format_dict).set_table_styles(df_styles))

with tab_7:
    st.subheader('DEFENSIVE PLAYERS [IDP] RANKINGS')
    st.dataframe(idp_rankings.style.format(col_format_dict).set_table_styles(df_styles))

with tab_8:
    st.subheader('DEFENSE / SPECIAL TEAMS [DST]')


## SCATTER MATRIX ##
# left_col_1, right_col_1 = st.columns(2)
# left_col_1.plotly_chart(exo_matrix_1, use_container_width=False, sharing="streamlit")
# right_col_1.plotly_chart(star_matrix_1, use_container_width=False, sharing="streamlit")


## LEAGUE LOGOS ##
afc_col_1, nfl_col_2, nfc_col_3 = st.columns(3)
afc_col_1.image(AFC_logo, width=300) #
nfl_col_2.image(NFL_logo, width=300) # caption='NATIONAL FOOTBALL LEAGUE'
nfc_col_3.image(NFC_logo, width=300) # caption='NATIONAL FOOTBALL LEAGUE'

## EXTERNAL LINKS ##
github_link = '[GITHUB REPOSITORY](https://github.com/nehat312/exoplanet-explorer/)'
tbu_link1 = '[TBU](<TBU>)'
tbu_link2 = '[TBU](<TBU>)'

link_col_1, link_col_2, link_col_3 = st.columns(3)
ext_link_1 = link_col_1.markdown(github_link, unsafe_allow_html=True)
ext_link_2 = link_col_2.markdown(tbu_link1, unsafe_allow_html=True)
ext_link_3 = link_col_3.markdown(tbu_link2, unsafe_allow_html=True)


## SCRIPT TERMINATION ##
st.stop()



### INTERPRETATION ###




### SCRATCH NOTES ###

## LOGOS BY DIVISION ##
# NFCEast_col_1, NFCEast_col_2, NFCEast_col_3, NFCEast_col_4 = st.columns(4)
# NFCEast_col_1.image(WAS_logo, caption='WASHINGTON COMMANDERS', width=250)
# NFCEast_col_2.image(PHI_logo, caption='PHILADELPHIA EAGLES', width=250)
# NFCEast_col_3.image(DAL_logo, caption='DALLAS COWBOYS', width=250)
# NFCEast_col_4.image(NYG_logo, caption='NEW YORK GIANTS', width=250)
#
# NFCWest_col_1, NFCWest_col_2, NFCWest_col_3, NFCWest_col_4 = st.columns(4)
# NFCWest_col_1.image(LAR_logo, caption='LOS ANGELES RAMS', width=250)
# NFCWest_col_2.image(SFO_logo, caption='SAN FRANCISCO 49ERS', width=250)
# NFCWest_col_3.image(SEA_logo, caption='SEATTLE SEAHAWKS', width=250)
# NFCWest_col_4.image(ARI_logo, caption='ARIZONA CARDINALS', width=250)
#
# NFCSouth_col_1, NFCSouth_col_2, NFCSouth_col_3, NFCSouth_col_4 = st.columns(4)
# NFCSouth_col_1.image(TBB_logo, caption='TAMPA BAY BUCCANEERS', width=250)
# NFCSouth_col_2.image(NOS_logo, caption='NEW ORLEANS SAINTS', width=250)
# NFCSouth_col_3.image(ATL_logo, caption='ATLANTA FALCONS', width=250)
# NFCSouth_col_4.image(CAR_logo, caption='CAROLINA PANTHERS', width=250)
#
# NFCNorth_col_1, NFCNorth_col_2, NFCNorth_col_3, NFCNorth_col_4 = st.columns(4)
# NFCNorth_col_1.image(GBP_logo, caption='GREEN BAY PACKERS', width=250)
# NFCNorth_col_2.image(MIN_logo, caption='MINNESOTA VIKINGS', width=250)
# NFCNorth_col_3.image(DET_logo, caption='DETROIT LIONS', width=250)
# NFCNorth_col_4.image(CHI_logo, caption='CHICAGO BEARS', width=250)

## CACHE MODEL ##
# @st.cache(persist=True, allow_output_mutation=True, suppress_st_warning=True)



## FONTS ##

# t = st.radio("Toggle to see font change", [True, False])
#
# if t:
#     st.markdown(
#         """
#         <style>
# @font-face {
#   font-family: 'Tangerine';
#   font-style: normal;
#   font-weight: 400;
#   src: url(https://fonts.gstatic.com/s/tangerine/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
#   unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
# }
#
#     html, body, [class*="css"]  {
#     font-family: 'Tangerine';
#     font-size: 48px;
#     }
#     </style>
#
#     """,
#         unsafe_allow_html=True,
#     )
#
# "# Hello"
#
# """This font will look different, based on your choice of radio button"""

# CONFIG TEMPLATE
    # st.set_page_config(page_title="CSS hacks", page_icon=":smirk:")
    #
    # c1 = st.container()
    # st.markdown("---")
    # c2 = st.container()
    # with c1:
    #     st.markdown("Hello")
    #     st.slider("World", 0, 10, key="1")
    # with c2:
    #     st.markdown("Hello")
    #     st.slider("World", 0, 10, key="2")

# STYLE WITH CSS THROUGH MARKDOWN
    # st.markdown("""
    # <style>
    # div[data-testid="stBlock"] {
    #     padding: 1em 0;
    #     border: thick double #32a1ce;
    # }
    # </style>
    # """, unsafe_allow_html=True)


# STYLE WITH JS THROUGH HTML IFRAME
    # components.html("""
    # <script>
    # const elements = window.parent.document.querySelectorAll('div[data-testid="stBlock"]')
    # console.log(elements)
    # elements[0].style.backgroundColor = 'paleturquoise'
    # elements[1].style.backgroundColor = 'lightgreen'
    # </script>
    # """, height=0, width=0)


# st.markdown("""
#             <style>
#             div[data-testid="stBlock"] {padding: 1em 0; border: thick double #32a1ce; color: blue}
#             </style>
#             """,
#             unsafe_allow_html=True)

# style={'textAlign': 'Center', 'backgroundColor': 'rgb(223,187,133)',
#                                            'color': 'black', 'fontWeight': 'bold', 'fontSize': '24px',
#                                            'border': '4px solid black', 'font-family': 'Arial'}),

#pattern_shape = "nation", pattern_shape_sequence = [".", "x", "+"]

            # fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group", facet_row="time", facet_col="day",
            #        category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})

            # fig = px.scatter_matrix(df, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], color="species")

            # fig = px.parallel_categories(df, color="size", color_continuous_scale=px.colors.sequential.Inferno)

            # fig = px.parallel_coordinates(df, color="species_id", labels={"species_id": "Species",
            #                   "sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
            #                   "petal_width": "Petal Width", "petal_length": "Petal Length", },
            #                     color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
