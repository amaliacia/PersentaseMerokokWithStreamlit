import pandas as pd
import streamlit as st
import plotly.express as px
#from PIL import Image
from itertools import chain
from streamlit_option_menu import option_menu

# membuat navigation bar
selected = option_menu(
    menu_title="PERSENTASE MEROKOK",
    options=["Home", "Gender", "Age", "Place", "All Data", "About"],
    icons=["house", "gender-ambiguous", "activity", "building", "bullseye", "info-circle"],
    menu_icon="caret-right-square-fill",
    orientation="horizontal",
    styles={
                "container": {"padding": "0!important", "background-color": "black"},
                "icon": {"color": "white", "font-size": "10px"},
                "nav-link": {
                    "font-size": "15px",
                    "font-colour": "white",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#eeeee",
                },
                "nav-link-selected": {"background-color": "#696666"},
            },
    )


# Membaca file excel
excel_file = 'persentasemerokok.xlsx'

# membuat dataframe dari file excel
df_JK = pd.read_excel(excel_file,
                    sheet_name='JK', # nama sheet
                    usecols='A:C', # kolom yang dibaca
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


#### ----- SECTION HOME ---- ####
if selected == "Home":
    st.title("Data Persentase Pengguna Rokok Di Indonesia")
    st.subheader("Data berdasarkan")
    
    # menggabungkan nama nama kolom 
    df_all = chain(jk, umur, tinggal)
    
    # mengubah ke dataframe
    df_all = pd.DataFrame(df_all)
    
    # merename index
    #df_all.rename(columns={0: 'List'}, index={0: '->', 1: '->', 2: '->', 3: '->', 4:'->', 5:'->', 6:'->'}, inplace=True)
    df_all.rename(columns={0: 'Spesifik'}, index=lambda x: 'Gender' if 0<=x<2 else ('Age' if 1<x<5  else 'Place'), inplace=True)
    
    
    # menampilkan dataframe dalam tabel streamlit
    st.table(df_all)  


#### ----- SECTION GENDER ---- ####
if selected == "Gender":
    st.title("Data Persentase Pengguna Rokok Di Indonesia")
    st.subheader("Berdasarkan Jenis Kelamin")
    #st.dataframe(df_JK)
    
    chart_cowo = px.pie(df_JK, 
                    title="Bagan untuk Laki-Laki",
                    values='Laki-laki',
                    names='Tahun')

    # menampilkan pada streamlit
    st.plotly_chart(chart_cowo)
    
    chart_cewe = px.pie(df_JK, 
                    title="Bagan untuk Perempuan",
                    values='Perempuan',
                    names='Tahun')

    # menampilkan pada streamlit
    st.plotly_chart(chart_cewe)

    meancwo = df_JK['Laki-laki'].mean()
    st.write('Persentase Rata-Rata Laki-Laki: ', meancwo)
    
    meancwe = df_JK['Perempuan'].mean()
    st.write('Persentase Rata-Rata Perempuan: ', meancwe)
    
    meanJK = df_JK[['Laki-laki','Perempuan']].mean().mean()
    st.write('Persentase Rata-Rata Semua Jenis Kelamin: ', meanJK)
    
    df_JK.insert(2, 'Cek (L)', df_JK['Laki-laki'].apply(lambda x: '> Mean' if x >= meanJK else '< Mean'))
    df_JK.insert(4, 'Cek (P)', df_JK['Perempuan'].apply(lambda x: '> Mean' if x >= meanJK else '< Mean'))
    
    # ubah nama indeks
    df_JK.rename(index={0: '1', 1: '2', 2: '3', 3: '4'}, inplace=True)
    
    # mengubah warna value dengan kondisi
    df_JK = df_JK.style.applymap(lambda y: 'color : red' if  y == '> Mean' else 'color : default')
    
    # menampilkan dataframe dalam tabel streamlit
    st.table(df_JK)


#### ----- SECTION AGE ---- ####
if selected == "Age":
    st.title("Data Persentase Pengguna Rokok Di Indonesia")
    st.subheader('Berdasarkan Umur')
    
    st.line_chart(df_Umur, x="Tahun", y=["10-12 Tahun", "13-15 Tahun", "16-18 Tahun"])
    
    meanUm = df_Umur[['10-12 Tahun', '13-15 Tahun', '16-18 Tahun']].mean().mean()
    st.write('Persentase Rata-Rata Semua Umur (< 18 tahun): ', meanUm)
    
    df_Umur.insert(2, 'Cek 10-12', df_Umur['10-12 Tahun'].apply(lambda x: '> Mean' if x >= meanUm else '< Mean'))
    df_Umur.insert(4, 'Cek 13-15', df_Umur['13-15 Tahun'].apply(lambda x: '> Mean' if x >= meanUm else '< Mean'))
    df_Umur.insert(6, 'Cek 16-18', df_Umur['16-18 Tahun'].apply(lambda x: '> Mean' if x >= meanUm else '< Mean'))
    
    #df_Umur.index=[''] * len(df_Umur)
    df_Umur.rename(index={0: '1', 1: '2', 2: '3', 3: '4'}, inplace=True)
   
    # mengubah warna value dengan kondisi
    df_Umur = df_Umur.style.applymap(lambda y: 'color : red' if  y == '> Mean' else 'color : default')

    # menampilkan dataframe dalam tabel streamlit
    st.table(df_Umur)


#### ----- SECTION PLACE ---- ####
if selected == "Place":
    st.title("Data Persentase Pengguna Rokok Di Indonesia")
    st.header('Berdasarkan Tempat Tinggal')
    
    fig = px.bar(df_Tinggal, x='Tahun', y=['Kota', 'Desa'], 
                 barmode='group', 
                 height=400)

    fig.update_layout(title_text='Barchart untuk Persentase Kota dan Desa')

    st.plotly_chart(fig)
    
    st.subheader("Data Tabel")
    #df_Tinggal.index=[''] * len(df_Tinggal)
    df_Tinggal = df_Tinggal.groupby('Tahun').mean().head()
    df_Tinggal = df_Tinggal.style.set_properties(**{'background-color': 'black',
                           'color': 'white'})
    st.table(df_Tinggal)
    

#### ----- SECTION ALL DATA ---- ####
if selected == "All Data":
    st.title("Data Persentase Pengguna Rokok Di Indonesia")
    st.subheader("Semua Data")
    
    # menggabungkan 3 dataframe menjadi satu dataframe
    #df_gabung = pd.concat([df_JK, df_Umur, df_Tinggal]) #concat sm spt chain
    
    df_gab = pd.merge(df_JK, df_Umur, how='outer')
    df_gabung = pd.merge(df_gab, df_Tinggal, how='outer')
  
    st.line_chart(df_gabung, 
                  x="Tahun", 
                  y=["Laki-laki", "Perempuan",
                     "10-12 Tahun", "13-15 Tahun", 
                     "16-18 Tahun", "Kota", "Desa"]
                  )
    
    # menggabungkan dengan kolom Tahun sebagai acuan
    df_gabung = df_gabung.groupby('Tahun').mean().head()
   
    st.subheader("Data Tabel")
    
    df_gabung = df_gabung.style.set_properties(**{'background-color': 'black',
                           'color': 'white'})
    
    st.table(df_gabung)


#### ----- SECTION ABOUT ---- ####
if selected == "About":
    st.header("Hii, It's my first time using streamlit ^_^")
    st.caption("Feel free to give me any advice to improve myself")
    st.write("Here's my identity :")
    st.subheader("Amalia Suciati")
    st.write("NIM   : 21102069")
    st.write("Kelas : IF 09 M")
    st.caption("Tugas Besar Pemrograman Fungsional")
