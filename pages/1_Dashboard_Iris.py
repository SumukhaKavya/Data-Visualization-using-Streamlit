import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

IMAGE_PATH = 'resources\images\iris.jpg'
DATA_PATH = 'resources\data\iris.csv'

st.title("Dashboard - Iris Data")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

species = st.selectbox("Select the Species:", df['Species'].unique())

with st.container():
    col1, col2,col3 = st.columns(3)

    fig_1 = px.histogram(df[df['Species'] == species], x="SepalLengthCm")
    col1.plotly_chart(fig_1, use_container_width=True)

    fig_2 = px.box(df[df['Species'] == species], y="SepalLengthCm")
    col2.plotly_chart(fig_2, use_container_width=True)

    fig_3=px.bar(df['Species'])
    col3.plotly_chart(fig_3, use_container_width=True)

with st.container():
    st.write("Multivariate Analysis")
    col_name=st.selectbox("Select the column name:",("SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"))

    fig_1=px.scatter(df[df['Species'] == species],x="SepalLengthCm",y=col_name,width=800, height=400)

    st.plotly_chart(fig_1)

fig_2 = px.box(df,x="Species",y=col_name)
st.plotly_chart(fig_2, use_container_width=True)

    

    
