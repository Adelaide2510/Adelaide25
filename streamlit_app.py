import streamlit as st
import pandas as pd
import numpy as np
voc=pd.nead_csv(https://docs.google.com/spreadsheets/d/e/2PACX-1vSkifjjijhyCfiL_eySZW_xKo_ltheX-uvNH4IsK2DjuCPeQdqJqYAoLiJX0HVKFJUAImN1M8cRhl_N/pub?output=csv)
st.dataframe(voc)
l=voc.shape[o]
i=hp.random.choice(range(l))
word_fr=voc['Définition'].values[i]
word_chi=voc['?'].values[i]
st.write(word_frt"hanzi"+word_chi)
st.button("refresh")