#!/usr/bin/env python

import urllib2
import json

locu_api = '0db6690436828ac595096df808e7222e979259da'

#url = 'https://api.locu.com/v1_0/venue/search/?radius=5000&locality=santa%20monica&category=restaurant&api_key=0db6690436828ac595096df808e7222e979259da'

# Function to create URL to search from locu API
def locu_search(query):
	api_key = locu_api
	# Attach api key to base URL
	url = 'https://api.locu.com/v1_0/venue/search/?radius=5000'
	# Replace the spaces of the query variable with %20 to insert into the final URL
	locality = query.replace(' ', '%20')
	final_url = url + "&locality=" + locality + "&category=restaurant" + "&api_key=" + api_key
	json_obj = urllib2.urlopen(final_url)
	data = json.load(json_obj)
	
	for business in data['objects']:
		print business['name'], business['phone']