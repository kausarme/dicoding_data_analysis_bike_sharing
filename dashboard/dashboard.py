import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Judul Dashboard
st.title('Dashboard Analisis Data: Bike Sharing Dataset')

st.header('Proyek Analisis Data: Bike Sharing Dataset')
st.write('**Nama:** Kausar Meutuwah')
st.write('**Email:** kausar.meutuwah@gmail.com')
st.write('**ID Dicoding:** kausarme')


# Membaca data
@st.cache_data
def load_data():
    day_df = pd.read_csv('./day.csv')
    hour_df = pd.read_csv('./hour.csv')
    return day_df, hour_df


day_df, hour_df = load_data()

# Pertanyaan 1
st.header('1. Pola perilaku penggunaan sepeda antara pengguna terdaftar dan pengguna kasual')
day_df['type_day'] = 'Hari Kerja'
day_df.loc[day_df['holiday'] == 1, 'type_day'] = 'Hari Libur'
day_df.loc[(day_df['weekday'] == 0) | (day_df['weekday'] == 6), 'type_day'] = 'Akhir Pekan'
fig, ax = plt.subplots(1, 2, figsize=(14, 6))
sns.boxplot(data=day_df, x='type_day', y='registered', order=["Hari Kerja", "Akhir Pekan", "Hari Libur"], ax=ax[0])
ax[0].set_title('Pengguna Terdaftar')
sns.boxplot(data=day_df, x='type_day', y='casual', order=["Hari Kerja", "Akhir Pekan", "Hari Libur"], ax=ax[1])
ax[1].set_title('Pengguna Kasual')
st.pyplot(fig)

# Pertanyaan 2
st.header('2. Pengaruh kondisi cuaca pada jumlah penggunaan sepeda')
fig, ax = plt.subplots(1, 2, figsize=(14, 6))
sns.boxplot(data=day_df, x='weathersit', y='registered', ax=ax[0])
ax[0].set_title('Pengguna Terdaftar vs Kondisi Cuaca')
sns.boxplot(data=day_df, x='weathersit', y='casual', ax=ax[1])
ax[1].set_title('Pengguna Kasual vs Kondisi Cuaca')
st.pyplot(fig)

# Pertanyaan 3
st.header('3. Tren penggunaan rental sepeda berdasarkan waktu')
fig, ax = plt.subplots(figsize=(14, 6))
sns.barplot(data=hour_df, x='hr', y='cnt', estimator=sum, ci=None, ax=ax)
ax.set_title('Total Penggunaan Sepeda Berdasarkan Jam')
st.pyplot(fig)

# Referensi
st.markdown('### Referensi Dataset')
st.markdown('[Kaggle Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)')
