import streamlit as st

def calculate_homa_ir(glucose, insulin):
    homa_ir = (glucose * insulin) / 405
    return homa_ir

st.title('HOMA-IR Calculator')

st.header('Patient Information')
fasting_glucose = st.number_input('Enter fasting glucose in mg/dL')
fasting_insulin = st.number_input('Enter fasting insulin in μU/mL')

if st.button('Calculate'):
    result = calculate_homa_ir(fasting_glucose, fasting_insulin)
    st.write('The HOMA-IR score is ', result)
