# -*- coding: utf-8 -*-
"""StreamLit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XCD3ndTE52BU1kmMB6Yq7Cq0C29uKXMV
"""

import streamlit as st
st.write("""Max of three numbers""")
n1=st.number_input("Number1")
n2=st.number_input("Number2")
n3=st.number_input("Number3")
if st.button("Run"):
  st.write(max(n1,n2,n3))
