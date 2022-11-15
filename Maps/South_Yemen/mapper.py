"""
South Yemen's History summed up for optimal SLOC:

 - Some Muslim pirates decide to be bad boys, British get mad and take Aden, marking the beginning of the colonization of Yemen(in 1839)
 - Yemen(as a whole) partitioned between Ottomans and British(happened over couple of conferences)
 - World War 1 happens, and Ottoman Yemen becomes Mutawakkilite Kingdom
 - World War 2 happens, Britain is weak, and Mutawakkilite Kingdom becomes North Yemen(US ALLY & DEEPLY CONSERVATIVE)
 - FLOSY(Those who fight for South Yemen Independence) fights weak British, but originally lose but still hold ground. Then Harold Wilson gives up on colonies 
   East of Suez including South Yemen.
 - South Yemen becomes Communist☭☭☭☭(1967)
 - North and South fight a lot, eventually reuniting in 1990
 - Pro Socialist Revolt leading to 1994 civil war in Yemen, the North Yemen government(pretty much runs Yemen due to having more people) wins, crushing the rebels
 - Civil war in Yemen today is happening under borders similar to that of North and South Yemen during the Cold War
 
 - Parts I ignored: North Yemen is mostly Shia, while South Yemen is mostly Sunni. South Yemen also has lots of oil.
"""
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

# If you want to see the result, it will be called "result.png"
