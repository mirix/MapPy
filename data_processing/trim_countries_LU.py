#!/usr/bin/env python3

import pandas as pd

import os
cwd = os.getcwd()

df_all = pd.read_csv(cwd + '/countries_lu.csv', na_filter = False)

df_all = df_all[['Land','Landcode','Haaptstad','Numm vun der Persoun','Adjektiv','Währung','Kontinent','Faarf']]

df_all.to_csv("countries_lu_trim.csv", sep=',', index=False)
