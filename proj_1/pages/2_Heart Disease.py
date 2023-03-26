import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import colors, figure
import streamlit as st
import pandas as pd
from PIL import Image

st.title('Heart Disease')
st.header(':blue[The number of deaths due to heart attacks in India has remained consistently over 25,000 in the last four years, and over 28,000 in the last three year.]')

im=Image.open("heart.jpg")
st.image(im, caption='Heart Disease')
data = pd.read_csv("C:/Users/Shilpi Rani/Downloads/heart.csv") 
st.write ("This is the dataset of heart disease")
st.write(data)

st.subheader("Shape of the data is ")
st.write(data.shape)

st.subheader('Description of the data is')
st.write(data.describe())

st.subheader('Name of columns of the data is')
st.write(data.columns)

st.subheader("Attributes information")
st.subheader(":blue[1.age, 2.sex, 3.chest pain type (4 values), 4.resting blood pressure, 5.serum cholestoral in mg/dl, 6.fasting blood sugar > 120 mg/dl, 7.resting electrocardiographic results (values 0,1,2), 8.maximum heart rate achieved, 9.exercise induced angina, 10.oldpeak = ST depression induced by exercise relative to rest, 11.the slope of the peak exercise ST segment, 12.number of major vessels (0-3) colored by flourosopy, 13.thal: 0 = normal; 1 = fixed defect; 2 = reversable defect (The names and social security numbers of the patients were recently removed from the database, replaced with dummy values).]")

st.subheader("Correlation")
corr=data.corr()
plt.subplots(figsize=(9,6))
sns.heatmap(corr,annot=True)
st.pyplot(fig=None, clear_figure=None)

st.subheader("Histogram plot")
data.hist(bins=20,figsize=(20,15))
st.pyplot(fig=None, clear_figure=None)

st.subheader("Bar plot")
plt.bar(x=data['sex'],height=data['age'])
plt.xlabel("Sex")
plt.ylabel("Age")
st.pyplot(fig=None, clear_figure=None)

st.subheader("Bar plot of output")
sns.barplot(data['output'])
st.pyplot(fig=None, clear_figure=None)

st.subheader("Box plot")
data.plot(kind='box',y=['age','sex','cp','rest bp','chol','fbs','restecg','max H.R','exng','oldpeak','slp','M.V no.','thall','output'],figsize=(10,10));
st.pyplot(fig=None, clear_figure=None)

st.set_option('deprecation.showPyplotGlobalUse', False)
