import streamlit as st
import pickle
import numpy as np
import os
print(os.getcwd())
import time

def main():
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Personality Prediction </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write('To your answer')
    st.write('1.Not agree')
    st.write('2.Netural')
    st.write('3.Agree')
    a=[0,0,0]
    a[0] = st.slider('Ques 1. Do not like poetry.', 1, 3, 5)
    a[1] = st.slider('Ques 2. Have a vivid imagination.', 1, 3, 5)
    a[2] = st.slider('Ques 3. Have a rich vocabulary', 1, 3, 5)
   
    sum=0
    for i in a:
        sum = sum + i

    if st.button("Predict"):
        st.success('The probability of fire taking place is {}'.format(sum/3))

       

if __name__=='__main__':
    main()
