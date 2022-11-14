import json
import plotly.graph_objects as gos

sy = gos.Figure(gos.Scattermapbox(
  mode = "markers",
  lon = [45.0187],lat = [12.7855],
  marker = {'size': 20, 'color': ["cyan"]}
))

sY = open('southYemen.json')
coords = json.load(sY)

sy.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': { 'lon': 48, 'lat': 15},
        'zoom': 5, 'layers': [{
            'source': coords,
            'type': "fill", 'below': "traces", 'color': "royalblue"}]},
    margin = {'l':0, 'r':0, 'b':0, 't':0})

sy.show()
