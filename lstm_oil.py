# To jest wersja 2 nowej strony - gdzie modele mają opisy i parametry i jest ich więcej

import streamlit as st
from streamlit import set_page_config
import pandas as pd
import numpy as np
import datetime as dt
from datetime import datetime, timedelta, date
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
import appdirs as ad
CACHE_DIR = ".cache"
# Force appdirs to say that the cache dir is .cache
ad.user_cache_dir = lambda *args: CACHE_DIR
# Create the cache dir if it doesn't exist
Path(CACHE_DIR).mkdir(exist_ok=True)


# Set page configuration for full width
set_page_config(layout="wide")
# Definicje
today = date.today()

st.title('Crude Oil (NYSE) LSTM D+1 prediction model')
st.divider()
val_OIL = pd.read_excel('LSTM_mv.xlsx', sheet_name='D1_OIL')
val_OILD1 = val_OIL[['Date','OIL-NYSE','Day + 1 Prediction']].iloc[:-1]
day_s = val_OILD1.shape[0]

st.subheader(f'Predictions for the last {day_s} days')

fig_val = px.line(val_OILD1, x='Date', y=['OIL-NYSE','Day + 1 Prediction'],color_discrete_map={
                 'OIL-NYSE':'black','Day + 1 Prediction':'red'}, width=1200, height=600 ) 

fig_val.update_layout(plot_bgcolor='white',showlegend=True,xaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='Lightgrey'),
                      yaxis=dict(showgrid=True, gridwidth=0.5, gridcolor='Lightgrey'))
   
st.plotly_chart(fig_val, use_container_width=True)  