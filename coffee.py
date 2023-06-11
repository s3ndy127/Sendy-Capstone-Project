import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
from PIL import Image

st.set_page_config(
    page_title="Industri Kopi Dunia",
    page_icon=":coffee:",
    layout="wide"

)

# baca dataset: 
coffee_import = pd.read_csv('archive_4/Coffee_import.csv')
coffee_importers_consumption = pd.read_csv('archive_4/Coffee_importers_consumption.csv')
coffee_production = pd.read_csv('archive_4/Coffee_production.csv')
coffee_export = pd.read_csv('archive_4/Coffee_export.csv')
coffee_domestic_consumption = pd.read_csv('archive_4/Coffee_domestic_consumption.csv')

# Sidebar
image= Image.open('archive_4/kopi.png')
st.markdown("""
    <style>
        [data-testid=stSidebar] {
            background-color: #CA9E7B;
        }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.write("")
    with col2:
        st.image(image)
    with col3:
        st.write("")
    st.markdown('<div style="text-align: center;font-size:40px;font-weight:bold;color:black;">Capstone Project</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:20px;color:black;">Sendy Saputra</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:15px;color:black;">sendy.saputra10@gmail.com</div>', unsafe_allow_html=True)
    with st.expander("Data Source"):
        st.write("Data yang digunakan berasal dari dua sumber yaitu https://www.ico.org/new_historical.asp untuk data industri kopi dunia tahun 1990-2020")

# Titles
_, center, _ = st.columns([1,2,1])

with center:
    st.markdown('<div style="text-align: center;font-size:40px;font-weight:bold;color:black;">Perkembangan Industri Kopi Dunia Tahun 1990-2020</div>', unsafe_allow_html=True)
    st.image('https://ecs7.tokopedia.net/blog-tokopedia-com/uploads/2017/10/Blog_Judul-Blog19.jpg')
st.write('Kopi adalah salah satu minuman yang paling populer dan mendunia. Dikenal dengan rasa uniknya dan efek stimulasi kafein yang memberikan energi, kopi telah menjadi favorit bagi jutaan orang di berbagai belahan dunia. \
    Lebih dari sekadar minuman, kopi juga memiliki sejarah panjang dan telah menjadi bagian tak terpisahkan dari budaya dan industri di seluruh dunia. \
        Dalam periode tahun 1990 hingga 2020, industri kopi mengalami evolusi yang mengagumkan, didukung oleh data dan analisis yang disediakan oleh International Coffee Organization (ICO). \
            Tren dan inovasi dalam produksi, konsumsi, serta preferensi konsumen telah memberikan dampak signifikan pada industri kopi secara global. \Dalam analisis berikut, akan dipaparkan perkembangan industri kopi dari tahun 1990 hingga 2020.')

st.write("***")
st.title('Total Ekspor dan Impor Kopi di Dunia dari tahun 1990-2020')

################################################################
# Main Menu
################################################################

col1, col2 = st.columns(2)
with col1:
    top_export = coffee_export[['Country', 'Total_export']].sort_values(by=['Total_export'], ascending=False).head(10)
    fig = px.bar(top_export, x='Country', y='Total_export',labels={
                "Country": "Countries",
                "Total_export": "Total Export"
                },title='10 Negara dengan Total Ekspor Tertinggi:')
    st.plotly_chart(fig)
    st.write("Berdasarkan grafik diatas, Indonesia menempati peringkat ke-4 dibawah negara seperti Brazil, Viet Nam, dan Colombia\
         dalam hal ekspor kopi dengan total jumlah ekspor sebanyak 10,607,940,000 kg atau 10.6jt ton selama periode 1990-2020.")

with col2:
    top_import = coffee_import[['Country', 'Total_import']].sort_values(by=['Total_import'], ascending=False).head(10)
    fig = px.bar(top_import, x='Country', y='Total_import',labels={
                "Country": "Countries",
                "Total_import": "Total import"
                },title='10 Negara dengan Total Impor Tertinggi:')
    st.plotly_chart(fig)
    st.write("Dari grafik diatas, menunjukan bahwa negara USA menjadi negara importir kopi paling banyak dunia\
        yaitu sebanyak 42,507,660,000 kg atau 42.5jt ton selama periode 1990-2020, disusul oleh negara seperti Jerman, Italy dan Jepang")

st.write('***')

col1, col2 = st.columns(2)
with col1:
    st.metric('Total Ekspor 1990-2020', sum(coffee_export['Total_export']))
    st.metric('Total Ekspor Periode 2019-2020', sum(coffee_export['2019']))
with col2:
    st.metric('Total Impor 1990-2020', sum(coffee_import['Total_import']))
    st.metric('Total Impor Periode 2019-2020', sum(coffee_import['2019']))
st.write('***')

################################################################
production_country = coffee_production[['Country','Total_production']]
top_production = production_country.sort_values('Total_production',ascending=False).head(10)
top_prod = production_country.set_index('Country').sort_values('Total_production',ascending=False).head(20)

tab1, tab2, tab3 = st.tabs(["📈 Grafik Bar","📈 Grafik Perbandingan","📈 Grafik Pie"])
tab1.subheader("Grafik produksi kopi dunia")
tab2.subheader("Grafik Perbandingan 4 Negara produsen kopi di dunia")
tab3.subheader("Data Negara Produksi Kopi Dunia")

fig = px.bar(top_production, x='Country', y='Total_production',labels={
                "Country": "Countries",
                "Total_production": "Total Production"
                },title='10 Negara dengan Total Produksi Tertinggi:', width=1300)
tab1.plotly_chart(fig)

countries = ['Brazil', 'Colombia', 'Viet Nam', 'Indonesia']

fig = plt.figure(figsize=(10, 5))
plt.xticks(rotation=90)

for country in countries:
    data = coffee_production[coffee_production['Country'] == country]
    sns.lineplot(data=data.iloc[0, 2:len(data.columns) - 1], label=country)

plt.xlabel('Time')
plt.ylabel('Production')
plt.legend()

tab2.pyplot(fig)
tab2.write("Dari grafik diatas kita bisa tau bahwa negara Brazil selalu menjadi\
    menjadi negara dengan produksi kopi tertinggi di dunia selama periode 1990-2020\
        disisi lain negara produksi kopi di Vietnam setiap tahunnya terus meningkat\
            hingga pada akhirnya menjadi negara produsen kopi tertinggi kedua di dunia\
                sedangkan Indonesia dan Colombia cukup stagnant dalam produksi kopi di dunia bahkan\
                    disusul jauh dari negara vietnam dari tahun 1998")

fig = px.pie(production_country, values='Total_production', names='Country', title='Persentase Produksi kopi dunia', width=1300, height=600)
tab3.plotly_chart(fig)
tab3.write("Selama periode tahun 1990-2020, Brazil menguasai produksi kopi di dunia\
    dengan 33.3% disusul dengan negara Vietnam sebanyak 12.8%, negara Colombia dengan\
        9.57%. Sedangkan Indonesia sendiri hanya sebanyak 6.28% dari total keseluruhan produksi kopi dunia. Dengan\
            kata lain, sekitar 61.95% dari total keseluruhan produksi kopi dikuasai oleh ke-4 negara-negara tersebut")
st.write("***")

top_domestic_consumption = coffee_domestic_consumption[['Country', 'Total_domestic_consumption']].sort_values(by=['Total_domestic_consumption'], ascending=False).head(20)
top_domestic_consumption.head(10)

fig = px.bar(top_domestic_consumption, x='Country', y='Total_domestic_consumption', labels={
                     "Country": "Countries",
                     "Total_domestic_consumption": "Total Consumption"
                 },title='Negara dengan Konsumsi Kopi Domestic Tertinggi', width=1300, height=600)
st.plotly_chart(fig)
st.write('Dari data konsumsi kopi domestik diatas menunjukan bahwa negara Brazil memiliki angka konsumsi kopi tertinggi dibanding dengan\
    negara negara produsen kopi lainnya yaitu sebanyak 27.824.700.000 kg atau 27,8jt ton selama periode 1990-2020, disusul oleh negara seperti Indonesia, Ethopia, dan Mexico.')

top_import_consumption = coffee_importers_consumption[['Country', 'Total_import_consumption']].sort_values(by=['Total_import_consumption'], ascending=False).head(20)
top_import_consumption.head(10)

fig = px.bar(top_import_consumption, x='Country', y='Total_import_consumption', labels={
                     "Country": "Countries",
                     "Total_import_consumption": "Total Consumption"
                 },title='Negara dengan Konsumsi Kopi Import Tertinggi', width=1300, height=600)
st.plotly_chart(fig)
st.write('Disisi lain, Negara USA menempati peringkat pertama sebagai negara Importir kopi dengan tingkat konsumsi tertinggi di dunia\
    yaitu sebanyak 37.816.800.000 kg atau 37.8jt ton selama periode 1990-2020, disusul oleh Jerman dan Jepang')

st.markdown('<div style="text-align: center;font-size:40px;font-weight:bold;color:black;">Kesimpulan</div>', unsafe_allow_html=True)
_, col, _ = st.columns([1,2,1])

with col:
    st.write("Berdasarkan analisis yang telah dilakukan dapat diambil beberapa point penting")
    st.write("1. Negara Brazil merupakan Negara peringkat 1 dalam ekspor,konsumsi,dan produksi (menguasai 1/3 dari produksi kopi) di dunia")
    st.write("2. Negara Vietnam menduduki peringkat 2 setelah brazil dalam produksi dan ekspor namun peringkat ke-9 dalam konsumsi kopi dunia")
    st.write("3. Negara USA menduduki sebagai negara importir kopi, dan konsumsi kopi import terbesar di dunia")
    st.write("4. Negara Indonesia menduduki peringkat 4 dalam produksi kopi dunia dengan total 12.8% dari total produksi kopi dunia periode 1990-2020\
        ,untuk peringkat konsumsi Indonesia ada di peringkat ke-2 setelah Brazil")







