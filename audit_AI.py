# Uvoz librarya

import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import plotly.express as px
from benfordslaw import benfordslaw
import seaborn as sns

## Glavni program

def main():
	slika = Image.open('tesseract_AI_logo.png')
	st.image(slika)
	st.markdown("EKSPLORATORNA ANALIZA PODATAKA I FORENZIČKI TESTOVI ZA REVIZIJSKE POSTUPKE")
	password = st.text_input("Password", type='password')
	if password != "kofidenca123":
		st.write("Pogrešan password, pokušajte ponovno!")
		st.stop()
	else: 
		st.write("Uspješan login!")

	meni = ["Početna stranica", "Analiza podataka", "Forenzički testovi", "O nama"]
	izbor = st.sidebar.selectbox("Izbor", meni)

	if izbor == "Početna stranica":
		st.subheader("Iz izbornika lijevo odaberite željenu opciju")

	elif izbor == "Analiza podataka":
		st.write("Za analizu podataka o izlaznim računima pripremite Excel datoteku u potrebnom formatu!")
		excel_file_0 = st.file_uploader("Molimo uplodajte Excel file!", type=['xlsx', 'xls'])
		if excel_file_0 is not None:
			df0 = pd.read_excel(excel_file_0)
			st.write("1) Prikaz podataka iz knjige IRA:")
			st.write(df0)
			st.write("2) Deskriptivna statistika knjige IRA:")
			df0.describe()
			st.write(df0.describe())
			st.write("3) Vizualizacija Distribucije, potraga za outlierima:")
			fig,ax = plt.subplots()
			ax.boxplot(df0['Iznos'])
			st.pyplot(fig)
			st.write("Prema ovim podacima potrebno je posebnu pažnju u reviziji posvetiti ekstremnim vrijednostima")
			st.write("4) Top 10 najvećih kupaca, po ukupnim iznosima izdanih računa:")
			a = df0.groupby(by='Kupac').sum().sort_values(by='Iznos', ascending=False).head(10)
			st.write(a)
			st.write("4a) Interaktivni grafički prikaz najznačajnijih kupaca")
			figura = px.bar(a, y='Iznos', width=900, height=500)
			st.plotly_chart(figura)

	elif izbor == "Forenzički testovi":
		st.write("Za forenzički test podvrgavanja Benfordovom zakonu pripremite Excel datoteku u potrebnom formatu!")
		excel_file_1 = st.file_uploader("Molimo uplodajte Excel file!", type=['xlsx', 'xls'])
		if excel_file_1 is not None:
			df1 = pd.read_excel(excel_file_1)
			bl = benfordslaw(alpha=0.05)
			X = df1['Iznos'].values
			results = bl.fit(X)
			st.set_option('deprecation.showPyplotGlobalUse', False)
			bl.plot()
			st.pyplot()
			st.write("Na gornjem grafikonu treba obratiti pažnju koliko se dobro empirijska distribucija iz naše datotetke poklapa s Benfordovom.")
			st.write("Ukoliko je P vrijednost veća od 0.05, poklapanje je dovoljno dobro.")

	else:
		st.subheader("Kofidenca d.o.o. & Tesseract AI")
		slika2 = Image.open('kofidenca_logo.png')
		st.image(slika2)

if __name__ == '__main__':
	main()