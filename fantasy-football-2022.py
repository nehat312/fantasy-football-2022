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
overall_path = current_path + '/data/2022-FF-Overall.csv'
qb_path = current_path + '/data/2022-FF-QB.csv'
rb_path = current_path + '/data/2022-FF-RB.csv'
wr_path = current_path + '/data/2022-FF-WR.csv'
te_path = current_path + '/data/2022-FF-TE.csv'

#%%

## DATA IMPORT ##
overall_rankings = pd.read_csv(overall_path, header=0, index_col='RK') #, header=0, index_col='pl_name'#,
qb_rankings = pd.read_csv(qb_path, header=0, index_col='RK') #, header=0, index_col='pl_name'#,
rb_rankings = pd.read_csv(rb_path, header=0, index_col='RK') #, header=0, index_col='pl_name'#,
wr_rankings = pd.read_csv(wr_path, header=0, index_col='RK') #, header=0, index_col='pl_name'#,
te_rankings = pd.read_csv(te_path, header=0, index_col='RK') #, header=0, index_col='pl_name'#,

# qb_rankings.sort_values(by='disc_year', inplace=True)
#%%
print(qb_rankings.info())
print(qb_rankings.columns)


#%%
gen_cols = ['CODE', 'PLAYER', 'TEAM', 'BYE', 'PPL TEAM', 'SALARY', 'TAG',
       '2022 PROJ', ''21 TTL', 'BEST', 'WORST', 'AVG']

#%%
## IMAGE IMPORT ##
# jwst_tele_img_1 = Image.open('images/JWST-2.jpg')

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
#
#                 }

## FEATURE VARIABLES ##




## VISUALIZATIONS ##


#%%
#####################
### STREAMLIT APP ###
#####################

## CONFIGURATION ##
st.set_page_config(page_title='2022 FANTASY FOOTBALL DRAFT KIT', layout='wide', initial_sidebar_state='auto') #, page_icon=":smirk:"

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """

st.markdown(hide_menu_style, unsafe_allow_html=True)


## SIDEBAR ##
# st.sidebar.xyz


## HEADER ##
st.container()

## EXTERNAL LINKS ##

github_link = '[GITHUB REPOSITORY](https://github.com/nehat312/exoplanet-explorer/)'
tbu_link1 = '[TBU](<TBU>)'
tbu_link2 = '[TBU](<TBU>)'

link_col_1, link_col_2, link_col_3 = st.columns(3)
ext_link_1 = link_col_1.markdown(github_link, unsafe_allow_html=True)
ext_link_2 = link_col_2.markdown(tbu_link1, unsafe_allow_html=True)
ext_link_3 = link_col_3.markdown(tbu_link2, unsafe_allow_html=True)

st.title('2022 FANTASY FOOTBALL DRAFT KIT')

## TELESCOPE IMAGES ##
# qb_col_1, rb_col_2, wr_col_3, te_col_4 = st.columns(4)
# qb_col_1.image(jwst_tele_img_1, caption='JAMES WEBB SPACE TELESCOPE (JWST)', width=250)
# rb_col_2.image(jwst_tele_img_1, caption='TRANSITING EXOPLANET SURVEY SATELLITE (TESS)', width=250)
# wr_col_3.image(jwst_tele_img_1, caption='KEPLER SPACE TELESCOPE', width=250)
# te_col_4.image(jwst_tele_img_1, caption='HUBBLE SPACE TELESCOPE', width=250)

## 3D SCATTER ##
# st.plotly_chart(scatter_3d_1, use_container_width=False, sharing="streamlit")

## SELECTION FORM ##
# exo_drop_cols = ['pl_controv_flag', 'pl_bmassprov', 'ttv_flag',
#                  'st_temp_eff_k1', 'st_temp_eff_k2',
#                  'decstr', 'rastr',
#                  'sy_vmag', 'sy_kmag', 'sy_gaiamag']


## EXOPLANET SELECTION ##
# @st.cache(persist=True, allow_output_mutation=True, suppress_st_warning=True)

# def display_sector_comps(df):
#     st.dataframe(df.style.set_table_styles(df_styles))

# def display_ticker_stats(ticker_input):
#     display_ticker_df = ticker_output_df.loc[ticker_output_df['ticker'] == ticker_input]
#     st.dataframe(display_ticker_df.style.format(col_format_dict).set_table_styles(df_styles))

# with st.form('EXOPLANET SELECTION'):
#     exoplanet_prompt = st.subheader('SELECT AN EXOPLANET:')
#     exo_input = st.selectbox('', (exo_planet_list)) #'EXOPLANETS:'
#     exo_submit = st.form_submit_button('EXO-STATS')
#     if exo_submit:
        # display_planet_stats(exo_input)


## SECTOR TABS ##
tab_0, tab_1, tab_2, tab_3, tab_4, tab_5, tab_6, tab_7, tab_8 = st.tabs(['NFL', 'OVERALL', 'QB', 'RB', 'WR', 'TE', 'K', 'IDP', 'DST'])

with tab_0:
    st.subheader('NFL OVERVIEW')


with tab_1:
    st.subheader('OVERALL')
    st.dataframe(overall_rankings)

with tab_2:
    st.subheader('QUARTERBACK [QB]')
    st.dataframe(qb_rankings)

with tab_3:
    st.subheader('RUNNINGBACK [RB]')
    st.dataframe(rb_rankings)

with tab_4:
    st.subheader('WIDE RECEIVER [WR]')

with tab_5:
    st.subheader('TIGHT END [TE]')

with tab_6:
    st.subheader('KICKER [K]')

with tab_7:
    st.subheader('DEFENSIVE PLAYERS [IDP]')

with tab_8:
    st.subheader('DEFENSE / SPECIAL TEAMS [DST]')


## SCATTER MATRIX ##
# left_col_1, right_col_1 = st.columns(2)
# left_col_1.plotly_chart(exo_matrix_1, use_container_width=False, sharing="streamlit")
# right_col_1.plotly_chart(star_matrix_1, use_container_width=False, sharing="streamlit")

## GALAXY IMAGES ##
# img_col_1, img_col_2, img_col_3 = st.columns(3)
# img_col_1.image(jwst_carina_img_1, caption='CARINA NEBULA (JWST)', width=400)
# img_col_2.image(jwst_phantom_img_1, caption='PHANTOM GALAXY (JWST)', width=400)
# img_col_3.image(jwst_infra_img_1, caption='INFRARED PANORAMIC (JWST)', width=400)


## SCRIPT TERMINATION ##
st.stop()



### INTERPRETATION ###





### SCRATCH NOTES ###






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
