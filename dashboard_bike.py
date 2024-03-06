import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def set_custom_palette(series, max_color='pink', other_color='lightgrey'):
    max_val = series.max()
    pal = []

    for item in series:
        if item == max_val:
            pal.append(max_color)
        else:
            pal.append(other_color)
    return pal

day_df = pd.read_csv("https://raw.githubusercontent.com/anaaputt/bike_sharing/main/Bike_Day_Clean.csv")
st.title("Dashboard Bike Sharing Dataset")

st.header("Peningkatan Jumlah Peminjam Sepeda Setiap Tahun")
count_year_df = day_df.groupby(by='year').agg({'count':'sum'}).sort_values(by='count',ascending=False).reset_index()
top_year = count_year_df['count'][0]
st.metric("Jumlah Peminjam Terbanyak", value=top_year)
fig, ax = plt.subplots(figsize=(16, 6))
palette = set_custom_palette(count_year_df['count'])

sns.barplot(data=count_year_df, x='year', y='count', palette=palette, ax=ax)
ax.set_title('Jumlah Peminjam Sepeda Per Tahun')
ax.set_xlabel('Tahun')
ax.set_ylabel('Jumlah')
st.pyplot(fig)

st.header("Hubungan Jumlah Peminjam Sepeda dengan Temperatur")
fig, ax = plt.subplots(figsize=(16, 6))

sns.regplot(data=day_df, x='count', y='temp', color='pink', ax=ax)

ax.set_title('Hubungan Jumlah Peminjam Sepeda dengan Temperatur')
ax.set_xlabel('Jumlah Peminjam Sepeda')
ax.set_ylabel('Temperatur')
st.pyplot(fig)

st.header("Hubungan Jumlah Peminjam Sepeda dengan Musim")
season_count = day_df.groupby(by='season').agg({'count':'sum'}).sort_values(by='count', ascending=False).reset_index()
top_season = season_count['count'][0]
st.metric("Jumlah Peminjam Terbanyak", value=top_season)
fig, ax = plt.subplots(figsize=(16, 6))

colors = ['orange', 'pink', 'red', 'blue']
explode = [0.1, 0, 0, 0]
ax.pie(season_count['count'], labels=season_count['season'], explode=explode, colors=colors, autopct='%.0f%%')
ax.set_title('Hubungan Jumlah Peminjam Sepeda dengan Musim')
st.pyplot(fig)

st.header("Hubungan Jumlah Peminjam Sepeda dengan Kecepatan Angin")
fig, ax = plt.subplots(figsize=(16, 6))

sns.regplot(data=day_df, x='count', y='windspeed', color='pink', ax=ax)

ax.set_title('Hubungan Jumlah Peminjam Sepeda dengan Kecepatan Angin')
ax.set_xlabel('Jumlah Peminjam Sepeda')
ax.set_ylabel('Kecepatan Angin')
st.pyplot(fig)

st.header("Hubungan Jumlah Peminjam Sepeda Per Hari")
count_day_df = day_df.groupby(by='weekday').agg({'count':'sum'}).sort_values(by='count',ascending=False).reset_index()
top_day = count_day_df['count'][0]
st.metric("Jumlah Peminjam Sepeda Terbanyak", value=top_day)
fig, ax = plt.subplots(figsize=(16, 6))
palette = set_custom_palette(count_day_df['count'])

sns.barplot(data=count_day_df, x='count', y='weekday', palette=palette, ax=ax)
ax.set_title('Jumlah Peminjam Sepeda Per Hari')
ax.set_xlabel('Jumlah')
ax.set_ylabel('Hari')
st.pyplot(fig)
