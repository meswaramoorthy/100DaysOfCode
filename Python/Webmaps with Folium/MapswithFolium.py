import folium
import pandas

def colorSelect(elevation):
    if elevation > 0 and elevation < 1000:
        return "green"
    elif elevation < 2000:
        return "orange"
    else:
        return "red"

data = pandas.read_csv("Volcanoes_USA.txt")
# print(data)
latitude = data["LAT"]
longitude = data["LON"]
name = data["NAME"]
elevations = data["ELEV"]
# print(name)
# print(latitude)
# print(longitude)
# print (zip(latitude,longitude, name))
map = folium.Map(location=(38, -100), zoom_start= 6,)
map.save("map2.html")

featureGroup = folium.FeatureGroup(name="Volcanoes in USA")


# for lat, long in zip(latitude,longitude):
#
#     featureGroup.add_child(folium.Marker(location=[lat, long], popup="Hi I m a popup", tooltip="Hi I m a tooltip",
#                                      icon = folium.Icon(color='blue')))
for lat, long, n, el in zip(latitude,longitude, name, elevations):

    # print(type(n))
    # featureGroup.add_child(folium.Marker(location=[lat, long],
    #                                      popup=folium.Popup(n + " " + str(el) + " m", parse_html=True),
    #                                      # tooltip=folium.Tooltip(n, style="str"),
    #                                      icon=folium.Icon(color=colorSelect(el))))
    color=colorSelect(el)
    featureGroup.add_child(folium.CircleMarker(location=[lat, long], radius=6,
                                               popup=folium.Popup(n + " " + str(el) + " m", parse_html=True),
                                               fill=True, fill_color=color, color=color, fill_opacity=0.7))


map.add_child(featureGroup)

map.save("map3.html")

featureGroup1 = folium.FeatureGroup("Population Layer")
featureGroup1.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
                                       style_function=lambda x: {'fillColor':' green' if x['properties']['POP2005'] < 10000000
                                                                  else 'yellow' if x['properties']['POP2005'] < 20000000
                                                                  else 'red'}))

map.add_child(featureGroup1)
map.add_child(folium.LayerControl())

map.save("map4.html")