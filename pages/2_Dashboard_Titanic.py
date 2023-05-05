import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

st.title("Dashboard - Titanic Data")

IMAGE_PATH = r'resources\\images\\titanic.jpg'
DATA_PATH = r'resources\\data\\titanic.csv'

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

analysis_type = st.sidebar.selectbox('Select Analysis Type', ('Univariate', 'Bivariate'))

if analysis_type=="Univariate":
    with st.container():
      variable = st.selectbox('Select Variable', ('pclass','age','fare'))
      tab1,tab2=st.tabs(["Male","Female"])
      with tab1:
        col1,col2=st.columns(2)
        fig_1 = px.histogram(df[df['sex'] == 'male'], x=variable)
        col1.plotly_chart(fig_1, use_container_width=True)

        fig_2 = px.box(df[df['sex'] == 'male'], x=variable)
        col2.plotly_chart(fig_2, use_container_width=True)
      with tab2:
        col1,col2=st.columns(2)
        fig_3 = px.histogram(df[df['sex'] == 'female'], x=variable)
        col1.plotly_chart(fig_3, use_container_width=True)

        fig_4 = px.box(df[df['sex'] == 'female'], x=variable)
        col2.plotly_chart(fig_4, use_container_width=True)

if analysis_type=="Bivariate":
    with st.container():
        variable_x = st.selectbox('Select X Variable', df.columns)
        variable_y = st.selectbox('Select Y Variable', df.columns)
        tab1,tab2,tab3=st.tabs(["Numerical vs Numerical"," Categorical vs Numerical","Categorical vs Categorical"])
        with tab1:
            fig_1 = px.scatter(df, x=variable_x,y=variable_y)
            st.plotly_chart(fig_1, use_container_width=True)
        with tab2:
           fig_2 = px.box(df, x=variable_x,y=variable_y)
           st.plotly_chart(fig_2, use_container_width=True)
        with tab3:
           fig_3=px.bar(df,x=variable_x,y=variable_y,color='sex',barmode='stack')
           st.plotly_chart(fig_3, use_container_width=True)

           
        
    
    
    

