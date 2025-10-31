import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('India.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0,'India')

st.markdown(
    "<h1 style='text-align: center;'>India Data Visualization</h1>",
    unsafe_allow_html=True
)

st.text('*Size Represents Primary Parameter')
st.text('* Color Represents Secondary Parameter')


st.sidebar.title('India Data Visualization')

selected_state = st.sidebar.selectbox('Select a State',list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    if selected_state == 'India':
     fig = px.scatter_map(df, lat='Latitude',lon='Longitude',size=primary,color=secondary,zoom=3.5,size_max=35,map_style='carto-positron',width=1200,height=700,hover_name='District')
     st.plotly_chart(fig,use_container_width=True)
    else:
     state_df = df[df['State'] == selected_state]
     fig = px.scatter_map(state_df, lat='Latitude',lon='Longitude',size=primary,color=secondary,zoom=6,size_max=35,map_style='carto-positron',width=1200,height=700,hover_name='District')
     st.plotly_chart(fig,use_container_width=True)