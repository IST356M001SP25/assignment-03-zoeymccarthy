'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''

import streamlit as st

# Import the packaging module
import packaging

# Title
st.title('Package Data Input')
unparsedData = st.text_input('Enter one string of package data:')
if unparsedData:
    parsedData = packaging.parse_packaging(unparsedData)
    st.write('Package info:', parsedData)
    packageSize = packaging.calc_total_units(parsedData)
    st.write('Total package size:', packageSize)