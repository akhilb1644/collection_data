import plotly.graph_objects as go
import json

s = open('socotra.json')
data = json.load(s)

data = data["features"]
data = data[0]["geometry"]
data = data["coordinates"][0]

lats = list()
lons = list()

for coord in data:
    lats.append(coord[1])
    lons.append(coord[0])

fig = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = lons, lat = lats,
    marker = { 'size': 10, 'color': "#0000FF" }))

fig.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': 53.8237, 'lat': 12.4634 },
        'zoom': 7},
    showlegend = False)

fig.show()
fig.write_html('soqotra.html')
