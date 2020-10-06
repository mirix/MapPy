#!/usr/bin/env python3

import pandas as pd

import os
cwd = os.getcwd()

link = "https://lb.wikipedia.org/wiki/L%C3%ABscht_vun_de_Staate_vun_der_Welt"
df_lu = pd.read_html(link, header=0)[0]

df_lu = df_lu[['Land', 'Haaptstad']]

df_lu = df_lu.rename(columns={'Land':'CountryName_LU'})
df_lu = df_lu.rename(columns={'Haaptstad':'CapitalName_LU'})

import fuzzymatcher

world_data = pd.read_csv(cwd + '/countries_lu.txt', na_filter = False)

df_all = fuzzymatcher.fuzzy_left_join(world_data, df_lu, left_on = 'Land', right_on = 'CountryName_LU')

df_all.to_csv("countries_lu_text.csv", sep=',', index=False)

df_all = df_all[['Land','CountryName_LU','Landcode','Haaptstad', 'CapitalName_LU', 'Numm vun der Persoun', 'Adjektiv', 'Währung', 'Kontinent', 'Faarf']]

df_all.to_csv("countries_lu.csv", sep=',', index=False)
