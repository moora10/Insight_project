#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:22:20 2020

@author: annahmoore
"""


import streamlit as st
import pandas as pd

st.write("""
         # Amyloid Augury
         **_Personalized_** risk profiling for the earliest pathological marker of Alzheimer's disease
""")

st.subheader('Demographics')
age = st.slider('Age', 54, 90, 78, 1)
gender = st.selectbox('Biological Sex', ('Male', 'Female'))
# code gender as 1 for male and 2 for female for model input
PTGENDER = 1
if gender == 'Male':
    PTGENDER == 1
else: 
    PTGENDER == 2
    
PTEDUCAT = st.slider('Years of education', 6, 20, 12, 1)
st.subheader('Genetic Profile')
apoe_count = st.selectbox('APOE4 Allele Count', ('0', '1', '2'), 1)
superPGRSATN_kunkle = st.slider('Genetic Risk Score', -1.3, 1.3, 1.2, 0.1)

st.subheader('Serum Protein Concentrations')
Eotaxin = st.slider('Eotaxin.3 (pg/mL)', 1.5, 3.3, 3.0, 0.1)
Apolipoprotein = st.slider('Apolipoprotein E (μg/mL)', 0.8, 2.7, 2.3, 0.1)
BNP = st.slider('Brain Natriuretic Peptide (pg/mL)', 1.9, 4.1, 3.5, 0.1)
PAI1 = st.slider('Plasminogen Activator Inhibitor 1 (ng/mL)', 0.9, 2.7, 2.2, 0.1)
PeptideYY = st.slider('Peptide YY (pg/mL)', 1.3, 3.1, 2.3, 0.1)
Adiponectin = st.slider('Adiponectin (μg/mL)', 0.2, 1.5, 0.5)
Leptin = st.slider('Leptin (ng/mL)', 0.2, 2.0, 1.7)
Insulin = st.slider('Insulin like growth factor binding protein (ng/mL)', 1.5, 2.5, 1.7, 0.1)
CD5 = st.slider('CD5 (ng/mL)', 3.1, 4.0, 3.8)

#import model 
import pickle
filename = 'logistic_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

X_test = {'PTGENDER': PTGENDER, 'PTEDUCAT': PTEDUCAT, 'apoe_count': apoe_count, 
     'age': age, 'superPGRSATN_kunkle': superPGRSATN_kunkle,'Eotaxin': Eotaxin,
        'Apolipoprotein': Apolipoprotein, 'BNP': BNP, 'PAI1': PAI1, 
         'PeptideYY': PeptideYY,'Adiponectin': Adiponectin, 'Leptin': Leptin,
         'Insulin': Insulin, 'CD5': CD5}
print(X_test)
#X_test = X_test.to_frame()
X_test = pd.DataFrame.from_dict(X_test, orient='index')
#transpose
X_test_input = X_test.T

out = loaded_model.predict(X_test_input)
#print(y_pred)
if out == 0:
    st.title('high amyloid risk')
else: 
    st.title('low amyloid risk')
    
st.write("Disclaimer: Model is ~79% accurate")



