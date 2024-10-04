import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca dataset
day_df = pd.read_csv('Data/day.csv')

# Mengganti nama kolom
day_df.rename(columns={
    "mnth": "bulan",
    "season": "musim",
    "yr": "tahun",
    "cnt": "total"
}, inplace=True)

# Mengganti nilai kolom musim dan tahun
day_df["musim"] = day_df["musim"].replace({1: "Semi", 2: "Panas", 3: "Gugur", 4: "Dingin"})
day_df["bulan"] = day_df["bulan"].replace({1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"})
day_df["tahun"] = day_df["tahun"].replace({0: "2011", 1: "2012"})

# Judul untuk dashboard
st.title('Dashboard Bike Sharing Data Analysis')

# Visualisasi pertama: Total penyewaan per musim
st.header('Total Penyewaan Per Musim')

# Menghitung total penyewaan per musim
data_musim = day_df.groupby(by="musim").total.sum().sort_values(ascending=False).reset_index()

# Membuat grafik bar
fig, ax = plt.subplots()
ax.bar(data_musim['musim'], data_musim['total'] / 2)
ax.set_title('Total Penyewaan per Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Total Penyewaan')
st.pyplot(fig)

# Insight musim
st.write('Insight: Musim dengan tingkat penyewaan terendah terjadi pada musim semi.')

# Visualisasi kedua: Tren penyewaan pada tahun 2011
st.header('Tren Penyewaan Sepeda di Tahun 2011')

# Filter data untuk tahun 2011
day_df_2011 = day_df[day_df["tahun"] == "2011"]

# Menghitung total penyewaan per bulan di tahun 2011
data_bulan = day_df_2011.groupby(by="bulan").total.sum().reset_index()

# Mengurutkan bulan sesuai urutan kalender
bulan_order = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 
               'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']

data_bulan['bulan'] = pd.Categorical(data_bulan['bulan'], categories=bulan_order, ordered=True)
data_bulan = data_bulan.sort_values('bulan')

# Membuat grafik line chart
fig, ax = plt.subplots()
ax.plot(data_bulan['bulan'], data_bulan['total'])
ax.set_title('Total Penyewaan per Bulan di Tahun 2011')
ax.set_xlabel('Bulan')
ax.set_ylabel('Total Penyewaan')
plt.xticks(rotation=45)
st.pyplot(fig)

# Insight tahun 2011
st.write('Insight: Pada tahun 2011, terjadi peningkatan dari Januari hingga Juni, lalu menurun hingga Desember.')

# Kesimpulan
st.header('Conclusion')
st.write("""
Conclusion pertanyaan 1
- Musim dengan tingkat Penyewaan terendah terjadi pada musim semi, dengan total penyewaan yang paling rendah dibandingkan musim yang lain. Perbedaan yang sangat signifikan terjadi karena kemungkinan orang eropa banyak yang alergi pada musim semi dan faktor - faktor lainnya. Untuk meningkatkan penyewaan di musim semi, harus meningkatkan strategi pemasaran yang lebih efektif, seperti promosi dan penyusuaian produk.

Conclusion pertanyaan 2
- Terjadi peningkatan yang signifikan dalam penyewaan dari bulan januari hingga juni, dengan puncaknya terjadi dibulan juni. Ini menunjukan adanya tren penjualan yang kuat diparuh pertama tahun. Setelah mencapai puncak pada bulan juni, penyewaan mulai menurun dari bulan juli hingga desember. Penurunan ini mungkin disebabkan pengaruh musiman yang menyebabkan penurunan penyewaan.
""")
