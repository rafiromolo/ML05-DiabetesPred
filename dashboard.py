import streamlit as st
import numpy as np
import pickle

# -- Load the trained model --
filename = 'diabetespred_model.sav'
model = pickle.load(open(filename, 'rb'))

st.title('Prediksi Diagnosa Diabetes')
st.text(
    """
    Program Prediksi Diagnosa Diabetes ini dilakukan menggunakan algoritma machine 
    learning yang didasarkan dari dataset 'Diabetes prediction dataset' di Kaggle.
    """
)

st.subheader('Masukkan Data')

# -- Data --
gender = st.selectbox(label='Jenis Kelamin', options=('Perempuan', 'Laki-laki', 'Lainnya'))
if gender == 'Perempuan':
    gender = 0
elif gender == 'Laki-laki':
    gender = 1
else:
    gender = 2

gender_scaled = (gender - 0) / (2 - 0)

age = st.number_input(label='Usia')
age_scaled = (age - 0.08) / (80.0 - 0.08)

hypertension = st.radio(label='Hipertensi', options=('Tidak', 'Iya'), horizontal=False)
if hypertension == 'Tidak':
    hypertension = 0
else:
    hypertension = 1

hypertension_scaled = (hypertension - 0) / (1 - 0)

heart = st.radio(label='Penyakit Jantung', options=('Tidak', 'Iya'), horizontal=False)
if heart == 'Tidak':
    heart = 0
else:
    heart =1

heart_scaled = (heart - 0) / (1 - 0)

smoking = st.radio(label='Catatan Merokok', options=('Sedang tidak', 'Mantan perokok', 'Tidak ada informasi', 'Perokok aktif', 'Tidak Pernah', 'Pernah'))
if smoking == 'Sedang tidak':
    smoking = 0
elif smoking == 'Mantan perokok':
    smoking = 1
elif smoking == 'Tidak ada informasi':
    smoking = 2
elif smoking == 'Perokok aktif':
    smoking = 3
elif smoking == 'Tidak Pernah':
    smoking = 4
else:
    smoking = 5

smoking_scaled = (smoking - 0) / (5 - 0)

bmi = st.number_input(label='Body Mass Index')
bmi_scaled = (bmi - 10.01) / (95.69 - 10.01)

hemoglobin = st.number_input(label='Hemoglobin A1c')
hemoglobin_scaled = (hemoglobin - 3.5) / (9.0 - 3.5)

blood = st.number_input(label='Gula darah')
blood_scaled = (blood - 80.0) / (300.0 - 80.0)

predict = st.button("Predict", type="primary")

if predict:
    data = [[gender_scaled, age_scaled, hypertension_scaled, heart_scaled,
             smoking_scaled, bmi_scaled, hemoglobin_scaled, blood_scaled]]
    
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.write('Terindikasi Diabetes')
    else:
        st.write('Tidak Terindikasi Diabetes')

