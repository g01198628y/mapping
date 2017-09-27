import folium
import pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])



map = folium.Map(location = [38.58,-99.09],zoom_start = 10)


fg = folium.FeatureGroup(name = "My Map")

for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup="Hi I am a marker",icon = folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")