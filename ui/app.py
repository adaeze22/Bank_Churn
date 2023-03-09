#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:04:40 2023

@author: ada-eze
"""

import numpy as np 
import pandas as pd
from joblib import load
import streamlit as st 

model = load('../model/log_model.joblib')

### This is the function/method that handles the prediction
def prediction(Balance, IsActiveMember, EstimatedSalary, HasCrCard):
    prediction = model.predict(np.array([[Balance, IsActiveMember, EstimatedSalary, HasCrCard]]))
    
    return prediction


# function to create the ui
def main():
    st.title("Bank Customer Churn Model")
    
    Balance = st.number_input('Enter your balance: ')
    IsActiveMember = st.selectbox('Are you an active member? : ', ['yes', 'no'])
    EstimatedSalary = st.number_input('What is your Estimated Salary?: ')
    HasCrCard = st.selectbox('Do you have a Credit Card?: ', ['yes', 'no'])
    
    button = st.button('Predict')
    

    
    if IsActiveMember.lower() == 'yes':
        IsActiveMember = 1
        
    else:
        IsActiveMember = 0
    

    if HasCrCard.lower() == 'yes':
        HasCrCard = 1
        
    else:
        HasCrCard = 0
        
        
    result = ''
    
    if (button):
        result = prediction(Balance, IsActiveMember, EstimatedSalary, HasCrCard)
        st.write('predicting....')
        if result == 0:
            st.success('This user would not exit')
            
        else:
            st.success('This user would exit')
    
if __name__ == '__main__':
    main()