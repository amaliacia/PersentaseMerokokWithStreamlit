import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from itertools import chain

st.set_page_config(page_title='Persentase Merokok')
st.header('Persentase Pengguna Rokok pada Umur < 18 Tahun')
st.subheader('coba')

#### --- Load Dataframe 
excel_file = 'persentasemerokok.xlsx'


df = pd.read_excel(excel_file,
                   sheet_name='DATA',
                   usecols='A:H',
                   header=2)


df_JK = pd.read_excel(excel_file,
                      sheet_name='JK',
                      usecols='A:C',
                      header=2)

df_Umur = pd.read_excel(excel_file,
                      sheet_name='Umur',
                      usecols='A:D',
                      header=2)

df_Tinggal = pd.read_excel(excel_file,
                      sheet_name='Tinggal',
                      usecols='A:C',
                      header=2)


df_all = chain(df_JK, df_Umur, df_Tinggal)

st.subheader('Persentase Berdasarkan :')
st.dataframe(df_all)
st.subheader('Berdasarkan Jenis Kelamin')
st.dataframe(df_JK)
st.subheader('Berdasarkan Umur')
st.dataframe(df_Umur)
st.subheader('Berdasarkan Tempat Tinggal')
st.dataframe(df_Tinggal)

pie_chart = px.pie(df_JK, 
                   title='Total',
                   values='Laki-laki',
                   names='Tahun')

st.plotly_chart(pie_chart)