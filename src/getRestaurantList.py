import json

def getRestaurants(lat:float, lon:float)->list:
	'''takes latitude and longtitude as geolocation and 
	return a list of restaurants in that area'''
	req = requests.get(self._BaseURL, params=self.param, headers=self.headers)
	req.write()

def 


def main():
	apiKey = input("Please enter Apikey")
	lat = input 
	outputFile = open("restaurants.json","w")
	json.dum(inputDict, outputFile)

#main()