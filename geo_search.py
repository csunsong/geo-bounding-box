import requests
import json

GMAPS_GEOCODE_API_ENDPOINT = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'


class GeoJsonApi(object):

    def __init__(self, key=''):
        self.key = key

    def location_data(self, location):
        data = self._query(location)
        return data

    def geo_bounds(self, location):
        data = self._query(location)
        if data != None:
            return data['geometry']['bounds']
        else:
            return data

    def viewport_bounds(self, location):
        data = self._query(location)
        if data != None:
            return data['geometry']['viewport']
        else:
            return data

    def coordinates(self, location):
        data = self._query(location)
        if data != None:
            return data['geometry']['location']
        else:
            return data

    def location_type(self, location):
        data = self._query(location)
        if data != None:
            return data['types']
        else:
            return data

    def formatted_address(self, location):
        data = self._query(location)
        if data != None:
            return data['formatted_address']
        else:
            return data

    def _validate_request(self, response):
        if 'error_message' in response:
            print(response['error_message'])
        elif len(response['results']) == 0:
            print('\n No Results Found; Please re-check your location.')

    def _filter_response(self, response):
        results = response['results']
        if len(results) > 2:
            options = [results[i]['formatted_address']
                       for i in range(0, len(results))]
            print("\n Response too large: Please narrow your location query to one of the following: \n",
                  options)
            response = None
        elif len(results) < 1:
            self._validate_request(response)
            response = None
        else:
            response = results[0]
        return response

    def _query(self, location):
        url = GMAPS_GEOCODE_API_ENDPOINT % (location, self.key)
        response = json.loads(requests.get(url).text)
        return self._filter_response(response)
