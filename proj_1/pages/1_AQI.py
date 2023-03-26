import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors, figure
import streamlit as st
import pandas as pd
from PIL import Image

st.title("Air Quality Index")
st.header(':blue[According to the recent study, statistics of the world health organization say that out of ten people, nine breathe unhealthy air that is not fit for human health. This is responsible for death over 7 million annually. Now, if we look in terms of air pollution in case of India, national quality standards of air is much low with compared to the guidelines given by WHO. Here, we can see the percentage of poor air quality from 2020 to 2022.]')

im=Image.open("aqi_con.png")
st.image(im, caption='Labels of AQI')
image = Image.open('who2021.png')
st.image(image, caption='WHO Guidelines')
data = pd.read_csv("C:/Users/Shilpi Rani/Downloads/AQI dataset 2020-22.csv") 
st.write ("This is the dataset of AQI from 2020 to 2022 of Delhi and Indore ")
st.write(data)
st.subheader("Shape of the data is ")
st.write(data.shape)

st.subheader('Description of the data is')
st.write(data.describe())

st.subheader('Name of columns of the data is')
st.write(data.columns)

st.subheader("Correlation")
corr=data.corr()
plt.subplots(figsize=(9,6))
sns.heatmap(corr,annot=True)
st.pyplot(fig=None, clear_figure=None)

st.subheader("Histogram plot")
data.hist(bins=20,figsize=(20,15))
st.pyplot(fig=None, clear_figure=None)

st.subheader("Box plot")
data.plot(kind='box',y=['PM2.5','PM10','NO2','NH3','SO2','CO','O3','AQI'],figsize=(10,10));
st.pyplot(fig=None, clear_figure=None)

st.subheader("Pie plot")
change_satis = {"AQI_Bucket": { "satisfactory": "Satisfactory"}}
data=data.replace(change_satis)
data.groupby(['AQI_Bucket']).sum().plot(kind='pie', y='PM2.5',autopct='%1.0f%%',figsize=(10,10))
st.pyplot(fig=None, clear_figure=None)

st.set_option('deprecation.showPyplotGlobalUse', False)