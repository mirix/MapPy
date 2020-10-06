#!/usr/bin/env python3

import os
cwd = os.getcwd()

import pandas as pd

# Import latitude and longitude

import folium

world_geo = os.path.join(cwd , 'CNTR_RG_60M_2020_4326.geojson')

languages = {
	'en' : ['Country','Code','Capital','Demonym','Adjective','Currency','Continent','Colour','CapitalLatitude','CapitalLongitude'],
	'de' : ['Land','Ländercode','Hauptstadt','Personenbezeichnung','Adjektiv','Währung','Continent','Colour','CapitalLatitude','CapitalLongitude'],
	'fr' : ['Pays','Code2','Capitale','Gentilé','Adjectif','Monnaie','Continent','Colour','CapitalLatitude','CapitalLongitude'],
	'pt' : ['País','Código','Capital','Gentílico','Adjetivo','Moeda','Continent','Colour','CapitalLatitude','CapitalLongitude'],
	'sk' : ['Krajina','Kód','Hlavné mesto','Obyvateľské meno','Prídavné meno','Mena','Continent','Colour','CapitalLatitude','CapitalLongitude'],
	}

for lang in languages:
 
	world_data = pd.read_csv(cwd + '/countries_' + lang + '_coord.csv', na_filter = False)
	
	country = languages[lang][0]
	coden = languages[lang][1]
	capital = languages[lang][2]
	demonym = languages[lang][3]
	adjective = languages[lang][4]
	currency = languages[lang][5]
 
	# Initialize the map:
	m = folium.Map(location=[25, 5], zoom_start=3, tiles='http://tile.stamen.com/terrain-background/{z}/{x}/{y}.png', attr="terrain-bcg")
	 
	# Add the color for the chloropleth:
	choropleth = folium.Choropleth(
		geo_data=world_geo,
		name='choropleth',
		data=world_data,
		columns=[coden, 'Colour'],
		key_on='feature.id',
		highlight=True,
		fill_color='Set1',
		fill_opacity=0.3,
		line_color='white',
		line_weight=2,
	).add_to(m)
	
	for key in choropleth._children:
	    if key.startswith('color_map'):
	        del(choropleth._children[key])
	
	for i in range(0,len(world_data)):
		icon = folium.features.CustomIcon('png/' + world_data.iloc[i][coden] + '.PNG',icon_size=(40, 30))
		folium.Marker([world_data.iloc[i]['CapitalLatitude'], world_data.iloc[i]['CapitalLongitude']],
		popup = folium.Popup(folium.Html("""
		{Capital} : <b>{cap}</b> <br> {Country}: <b>{cou}</b> <br> {Demonym} : <b>{dem}</b> <br> {Adjective} : <b>{adj}</b> <br> {Currency} : <b>{cur}</b> </b>
		""".format(Capital = capital, cap = world_data.iloc[i][capital], 
		Country = country, cou = world_data.iloc[i][country], 
		Demonym = demonym, dem = world_data.iloc[i][demonym], 
		Adjective = adjective, adj = world_data.iloc[i][adjective], 
		Currency = currency, cur = world_data.iloc[i][currency]), script=True), max_width=256),
		icon = icon
		).add_to(m)
	
	# Save to html
	m.save(cwd + '/countries_' + lang + '.html')
	
