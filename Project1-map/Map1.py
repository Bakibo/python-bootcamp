import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
home = [31.973046 , 34.774201]
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data['NAME'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
        
map = folium.Map(location = home , zoom_start = 3 , title = "Stamen Terrain")

fgm = folium.FeatureGroup(name = "Markers")
for lt , ln , el , na in zip(lat , lon , elev , name):
    fgm.add_child(folium.Marker(location = [lt , ln] , popup = na + '\n' + str(el)+" m" ,
     icon = folium.Icon(color = color_producer(el))))

fgm.add_child(folium.Marker(location = home , popup = 'Home' ,
 icon = folium.Icon(color = 'darkblue')))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = open('world.json' , 'r' , encoding = 'utf-8-sig').read() , 
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 100000000
 else 'orange' if 100000000 <= x['properties']['POP2005'] < 200000000 else 'red'} ,
  tooltip =  folium.features.GeoJsonTooltip(fields=['NAME','POP2005'] , aliases = ['Name: ' , 'Population: '] )) )

map.add_child(fgm)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")