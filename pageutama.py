import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
import itertools
from itertools import groupby
from itertools import chain
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title="PERSENTASE MEROKOK",
    options=["Home", "JK", "Umur", "Tinggal", "Semua", "About"],
    icons=["house", "book", "envelope"],
    menu_icon="cast",
    orientation="horizontal",
    styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "10px"},
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
    )

excel_file = 'persentasemerokok.xlsx'
#df_semua = pd.read_excel(excel_file,
#                sheet_name='DATA',
#                usecols='A:H',
#                header=2)


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

jk = pd.read_excel(excel_file,
                    sheet_name='JK',
                    usecols='B:C',
                    header=2)
umur = pd.read_excel(excel_file,
                    sheet_name='Umur',
                    usecols='B:D',
                    header=2)
tinggal = pd.read_excel(excel_file,
                    sheet_name='Tinggal',
                    usecols='B:C',
                    header=2)

df_all = chain(jk, umur, tinggal)

df_gabg = pd.concat([df_JK, df_Umur, df_Tinggal]) #concat juga bisa disebut chain

if selected == "Home":
    st.title("Data Persentase Pengguna Rokok Di Indonesia")
    st.subheader("Data berdasarkan")
    #df_all.index=[''] * len(df_all)
    st.table(df_all)  

if selected == "JK":
    st.title("Data Persentase Pengguna Rokok Di Indonesia")
    st.subheader("Berdasarkan Jenis Kelamin")
    #st.dataframe(df_JK)
    
    chart_cowo = px.pie(df_JK, 
                    title="Bagan untuk Laki-Laki",
                    values='Laki-laki',
                    names='Tahun')

    st.plotly_chart(chart_cowo)
    
    chart_cewe = px.pie(df_JK, 
                    title="Bagan untuk Perempuan",
                    values='Perempuan',
                    names='Tahun')

    st.plotly_chart(chart_cewe)

    meancwo = df_JK['Laki-laki'].mean()
    st.write('Persentase Rata-Rata Laki-Laki: ', meancwo)
    meancwe = df_JK['Perempuan'].mean()
    st.write('Persentase Rata-Rata Perempuan: ', meancwe)
    meanJK = df_JK[['Laki-laki','Perempuan']].mean().mean()
    st.write('Persentase Rata-Rata Semua Jenis Kelamin: ', meanJK)
    
    df_JK.insert(2, 'Cek (L)', df_JK['Laki-laki'].apply(lambda x: '> Mean' if x >= meanJK else '< Mean'))
    df_JK.insert(4, 'Cek (P)', df_JK['Perempuan'].apply(lambda x: '> Mean' if x >= meanJK else '< Mean'))
    
    
    #st.dataframe(df_JK.to_string(index=False))
    df_JK.index=[''] * len(df_JK)
    st.table(df_JK.style)
    
    

if selected == "Umur":
    st.title("Data Persentase Pengguna Rokok Di Indonesia")
    st.subheader('Berdasarkan Umur')
    
    meanUm = df_Umur[['10-12 Tahun', '13-15 Tahun', '16-18 Tahun']].mean().mean()
    st.write('Persentase Rata-Rata Semua Jenis Kelamin: ', meanUm)
    
    #df.insert(1, 'status', df['nilai'].apply(lambda x: 'lulus' if x >= 85 else 'tidak lulus'))
    
    df_Umur.insert(2, 'Cek 10-12', df_Umur['10-12 Tahun'].apply(lambda x: '> Mean' if x >= meanUm else '< Mean'))
    df_Umur.insert(4, 'Cek 13-15', df_Umur['13-15 Tahun'].apply(lambda x: '> Mean' if x >= meanUm else '< Mean'))
    df_Umur.insert(6, 'Cek 16-18', df_Umur['16-18 Tahun'].apply(lambda x: '> Mean' if x >= meanUm else '< Mean'))
    
    df_Umur.index=[''] * len(df_Umur)
    st.table(df_Umur)
    
    

if selected == "Tinggal":
    st.title("Data Persentase Pengguna Rokok Di Indonesia")
    st.header('Berdasarkan Tempat Tinggal')
    
    #df_Tinggal.index=[''] * len(df_Tinggal)
    df_Tinggal = df_Tinggal.groupby(by='Tahun').mean().head()
    st.table(df_Tinggal)
    
    st.subheader("Data Persentase Kota")
    
    #barKota = px.bar(df_Tinggal,
    #                   x='Tahun',
    #                   y='Kota',
    #                   color_discrete_sequence=['#728FCE']*len(df_Tinggal),
    #                   template='plotly_white')
    #st.plotly_chart(barKota)
    
    st.subheader("Data Persentase Desa")
    #barDesa = px.bar(df_Tinggal,
    #                   x='Tahun',
    #                   y='Desa',
    #                   color_discrete_sequence=['#2B547E']*len(df_Tinggal),
    #                   template='plotly_white')
    #st.plotly_chart(barDesa)
    
if selected == "Semua":
    
    df_gabung = df_gabg.groupby('Tahun').mean().head()
    
    st.title("Data Persentase Pengguna Rokok Di Indonesia")
    st.subheader("Semua Data")
    
    st.table(df_gabung.style.hide_index())
    
    #df_group = df.groupby(by=['Tahun', 'Umur', 'Jenis Kelamin'])
    #st.dataframe(df_group)
    
    
if selected == "About":
    st.title("Hii, It's my first time using streamlit ^_^")
    st.text("Feel free to give me any advice to improve myself")
    st.header("Here's my identity")
    st.subheader("Amalia Suciati")
    st.text("NIM   : 21102069")
    st.text("Kelas : IF 09 M")

