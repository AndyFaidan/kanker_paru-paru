import pickle
import numpy as np
import streamlit as st
from PIL import Image



## load save model
model = pickle.load(open('kanker-paru.sav', 'rb'))

##import data
image = Image.open("kanker.jpg")
st.image(image, use_column_width=True)

## judul web
st.title('Prediksi Kanker Paru-Paru')
st.text('(andy sofyan guspriyanto 191351112)')

## atribut
col1, col2, col3 = st.columns(3)

with col1:    
                index = st.number_input('index')

with col2:
                Age  = st.number_input('Umur')

with col3:
                Gender   = st.number_input('Jenis Kelamin')

with col1:
                Air_Pollution  = st.number_input('Polusi Udara')

with col2:
                Alcohol_use  = st.number_input('Penggunaan Alkohol')

with col3:
                 Dust_Allergy  = st.number_input('Alergi Debu')

with col1:
                OccuPational_Hazards = st.number_input('Resiko Genetik')

with col2:
                Genetic_Risk  = st.number_input('Penyakit Paru Paru Kronis')

with col3:
                 chronic_Lung_Disease  = st.number_input('Induksi Angina')

with col1:
                 Balanced_Diet  = st.number_input('Diet Seimbang')

with col2:
                 Obesity  = st.number_input('obesitas')

with col3:
                 Smoking = st.number_input('Merokok')

with col1:
                Passive_Smoker  = st.number_input('Perokok Pasif')

with col2:
                Chest_Pain   = st.number_input('Nyeri Dada')

with col3:
                 Coughing_of_Blood   = st.number_input('Batuk Darah')

with col1:
                Fatigue = st.number_input('Kelelahan')

with col2:
                Weight_Loss  = st.number_input('Penurunan Berat Badan')

with col3:
                Shortness_of_Breath= st.number_input('Sesak Nafas')

with col1:
                Wheezing    = st.number_input('Suara Nafas Mengi')

with col2:
                Swallowing_Difficulty    = st.number_input('Kesulitan Menelan')

with col3:
                Clubbing_of_Finger_Nails    = st.number_input('Tabuh Kuku Jari')

with col1:
                Frequent_Cold   = st.number_input('Flu')

with col2:
                Dry_Cough = st.number_input('Batuk Kering')

with col3:
                Snoring    = st.number_input('Mendengkur')


# code for prediction
kanker_diagnosis =''

## membuat tombol prediksi
if st.button('Prediksi Kanker Paru - Paru'):
    kanker_prediction = model.predict([[index, Age, Gender, Air_Pollution, Alcohol_use, Dust_Allergy, OccuPational_Hazards, Genetic_Risk, chronic_Lung_Disease, Balanced_Diet, Obesity, Smoking, Passive_Smoker, Chest_Pain, Coughing_of_Blood, Fatigue, Weight_Loss, Shortness_of_Breath, Wheezing, Swallowing_Difficulty, Clubbing_of_Finger_Nails, Frequent_Cold, Dry_Cough, Snoring]])

    if (kanker_prediction[0]==2):
        kanker_diagnosis = 'Pasien Terkena Kanker Paru-Paru (High)'
    elif(kanker_prediction[0]==1):
        kanker_diagnosis = 'pasien terkena kanker paru paru (Medium)'
    else:
        kanker_diagnosis = 'Pasien Tidak Terkena Kanker Paru-Paru'
st.success(kanker_diagnosis)

