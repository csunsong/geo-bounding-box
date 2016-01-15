import requests 
import json

GMAPS_GEOCODE_API_ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s'

class GeoJsonApi(object): 
	
	def __init__(self, key=''):
		self.key = key

	def location_data(self, location):
		data = self._query(location)	
		return data

	def geo_bounds(self, location): 
		response = self._query(location)
		if response != None: 
			return self._query(location)['geometry']['bounds']
		else: 
			return response

	def viewport_bounds(self, location):
		
		coords = self._query(location)['geometry']['viewport']
		return coords

	def coordinates(self, location):
		bounds = self._query(location)['geometry']['location']
		return bounds

	def location_type(self, location):
		location_type = self._query(location)['types']
		return location_type	

	def _filter_response(self, response):
		if len(response) > 2:	
			options = [ response[i]['formatted_address'] for i in range(0, len(response))]
			print("\n Response too large: Please narrow your location query to one of the following: \n", options)
			response = None
		else: 
			response = response[0]
		return response 

	def _query(self, location): 
		url = GMAPS_GEOCODE_API_ENDPOINT % location
		response = json.loads(requests.get(url).text)['results']			
		return self._filter_response(response)
		


if __name__ == "__main__":
    geojson = GeoJsonApi()
    geojson.main()
