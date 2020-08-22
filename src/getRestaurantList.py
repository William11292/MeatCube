import json
import requests
import csv

def getDiners(lat:float, lon:float, apikey)->list:
	'''takes latitude and longtitude as geolocation and 
	return a list of restaurants in that area'''
	request_url = "https://api.yelp.com/v3/businesses/search"
	parameters = {'term': 'restaurant', 'latitude': lat, 'longitude': lon, 'limit':50 }
	header = {'Authorization': 'Bearer '+str(apikey)}
	req = requests.get(request_url, params = parameters, headers =header)
	retval = json.loads(req.text)
	return retval["businesses"]

def parseDiners()->dict:
	'''Process data from '''

def writeDictToCSV(toCSV)->None:
	'''writes dict to csv'''
	keys = toCSV[0].keys()
	with open('output.csv', 'w', encoding='utf8', newline='') as output_file:
		fc = csv.DictWriter(output_file, fieldnames=toCSV[0].keys())
		fc.writeheader()
		fc.writerows(toCSV)
	return


def main():
	#takes api parameters here
	apiKey = input("Please enter Apikey")
	lat = 25.041766#input("Enter Latitude")
	lon = 121.543849#input("Enter Logntitudes")
	# outputFile = open("restaurants.json","w")
	# json.dum(inputDict, outputFile)
	
	dinersList = getDiners(lat, lon, apiKey)
	writeDictToCSV(dinersList)
	#print()

#1wEFcbPTtRQ-Ztc-E0nIjyAVGGLCwXKkL0hE9vETEyXyAotZXV-RysNLFIEq761vocfNH-S0wHLZGsNYNnOukqgu38vXVeVVfElml9qm1PNmAOOwaIoTHSU-iLgyX3Yx
#25.041766, 121.543849
main()
