# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 15:21:35 2022

@author: SRC
"""

import streamlit as st
import pandas as pd




def main():
    st.title('Air Passengers Analysis')
    data = pd.read_csv('AirPassengers.csv')
    month = st.selectbox("Month",list(data['Month'].unique()))
    st.table(data[data['Month']==month])
    #st.table(data)
    
    
    
    
    
    
    
    
if __name__=='__main__':
    main()
