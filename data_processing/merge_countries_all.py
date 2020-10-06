#!/usr/bin/env python3

import pandas as pd

import fuzzymatcher

import os
cwd = os.getcwd()

continent = pd.read_csv(cwd + '/country-and-continent-codes-list-csv_csv.csv', na_filter = False)

df_cont = pd.read_csv(cwd + '/country-and-continent-codes-list-csv_csv.csv', usecols=[0,3], names=['Continent', 'CountryCode'])

languages = {
	'en' : ['Country','Code','Capital','Demonym','Adjective','Currency'],
	'de' : ['Land','Ländercode','Hauptstadt','Personenbezeichnung','Adjektiv','Währung'],
	'fr' : ['Pays','Code2','Capitale','Gentilé','Adjectif','Monnaie'],
	'pt' : ['País','Código','Capital','Gentílico','Adjetivo','Moeda'],
	'sk' : ['Krajina','Kód','Hlavné mesto','Obyvateľské meno','Prídavné meno','Mena'],
	}

colours = {
	'Oceania' : '1',
	'Europe' : '2',
	'North America' : '3',
	'South America' : '4',
	'Africa' : '5',
	'Asia' : '6',
	'Antarctica' : '7'
	}

for lang in languages:

	link = 'https://publications.europa.eu/code/' + lang + '/' + lang + '-5000500.htm'
	df = pd.read_html(link, header=0)[1]
	
	if lang == 'fr':
		df = df.iloc[:,[1,4,5,6,7,8]]
	else:
		df = df.iloc[:,[1,3,4,5,6,7]]
	
	df.columns = languages[lang]
	
	for (columnName, columnData) in df.iteritems():
		df[columnName] = df[columnName].str.replace(r"\([^()]*\)","").str.strip()
	
	coden = languages[lang][1]
	df = df[df[coden].str.len() == 2]
	
	df_wc = fuzzymatcher.fuzzy_left_join(df, df_cont, left_on = coden, right_on = 'CountryCode')
	
	df_wc['Colour'] = df_wc['Continent'].map(colours)
	
	df_wc.drop(df_wc.columns[[0, 1, 2, 10]], axis = 1, inplace = True) 
	
	df_wc.to_csv('countries_' + lang + '.csv', sep=',', index=False)
	

