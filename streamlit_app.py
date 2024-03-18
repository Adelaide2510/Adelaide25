import streamlit as st
import pandas as pd
import numpy as np
voc=pd.nead_csv('lien')
st.dataframe(voc)
l=voc.shape[o]
i=hp.random.choice(range(l))
word_fr=voc['Définition'].values[i]
word_chi=voc['?'].values[i]
st.write(word_frt"hanzi"+word_chi)
st.button("refresh")