# GeoSearchPy
A Python implementation of Gmaps geocode API, capable or returning viewport and geometric bounds. Simply pass in any city, region, or address as a string to retrieve Gmaps geocode data. 
Can be used to do viewport or Elasticsearch geo_bounding_box queries. 

<h3>Usage:</h3>

```python
from GeoSearchPy import GeoSearch
#API key is optional; You will need a key if you plan to do calls over daily quota; 
geo_search = GeoSearch(google_api_key)

#Retrieves full field of location data
location_data = geo_search.location_data(location)

viewport_bounds = geo_search.viewport_bounds(location)

geometric_bounds = geo_search.geo_bounds(location)

geo_coordinates = geo_search.coordinates(location)

location_type = geo_search.location_type(location)

#Helps disambiguate locations with similar names
formatted_address = geo_search.formatted_address(location)


```

