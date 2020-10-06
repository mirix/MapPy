#!/usr/bin/env python3

import pandas as pd

import fuzzymatcher

import os
cwd = os.getcwd()

coordinates = pd.read_csv(cwd + '/concap.csv', na_filter = False)
coordinates = coordinates[['CapitalLatitude','CapitalLongitude','CountryCode']]

languages = {
	'en' : ['Country','Code','Capital','Demonym','Adjective','Currency'],
	'de' : ['Land','Ländercode','Hauptstadt','Personenbezeichnung','Adjektiv','Währung'],
	'fr' : ['Pays','Code2','Capitale','Gentilé','Adjectif','Monnaie'],
	'pt' : ['País','Código','Capital','Gentílico','Adjetivo','Moeda'],
	'sk' : ['Krajina','Kód','Hlavné mesto','Obyvateľské meno','Prídavné meno','Mena'],
	}

for lang in languages:

	df = pd.read_csv(cwd + '/countries_' + lang + '.csv', na_filter = False)
	
	coden = languages[lang][1]
	df_wc = fuzzymatcher.fuzzy_left_join(df, coordinates, left_on = coden, right_on = 'CountryCode')
	
	df_wc.drop(df_wc.columns[[0, 1, 2, 13]], axis = 1, inplace = True) 
	
	df_wc.to_csv('countries_' + lang + '_coord.csv', sep=',', index=False)
	

