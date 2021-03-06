import requests
import json

###
# Get Dictionary of temperature by given list of cities
# {"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":300,"main":"Drizzle","description":"light intensity drizzle","icon":"09d"}],"base":"stations","main":{"temp":280.32,"pressure":1012,"humidity":81,"temp_min":279.15,"temp_max":281.15},"visibility":10000,"wind":{"speed":4.1,"deg":80},"clouds":{"all":90},"dt":1485789600,"sys":{"type":1,"id":5091,"message":0.0103,"country":"GB","sunrise":1485762037,"sunset":1485794875},"id":2643743,"name":"London","cod":200}
# ###
def get_city_temperature(city):
    headers = {
    }
    jobs = []
    payload = {}
    current_temp = 0.0
    url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}'
    api_key = '032c9d4cb09efa7db81656c33d1a636e'
    city_url = url.format(city,api_key)
    #Get the json data from Rest IP
    response = requests.request("GET", city_url, headers=headers, data=payload)
    data = json.loads(response.text.encode('utf8'))
    #the data is given by kelvin so we need to move it to celsius
    kelvin_temp = float(data['main']['temp'])
    current_temp = kelvin_temp - 273.15
    return current_temp
###
# Print the list in order of temperature from cold to hot
# we sort the array by the value
# ###
def Print_sorted_list_from_coldest_to_warmest_city(cities):
    temp_list = {}
    for city in cities:
        current_temp = get_city_temperature(city)
        temp_list[city] = current_temp
    #sort the dictionary by value
    sorted_temp_list = sorted(temp_list.items(), key=lambda kv: kv[1])

    print('sorted list from coldest to warmest city')
    print('----------------------------------------')
    for city,temperature in sorted_temp_list:
        print('{0} - {1:5.2f}'.format(city,temperature))


cities = ['London,GB','Sydney,AU','Tokyo,JP','Madrid,ES','Addis Ababa,ET']
Print_sorted_list_from_coldest_to_warmest_city(cities)

