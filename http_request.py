import requests


def get_response():
    params = {
        'access_key' : "d5188929370f953ab58b32a75d2d18b4",
        'query' : 'Montenegro'
    }

    api_result = requests.get('http://api.weatherstack.com/current',params)

    api_response = api_result.json()    
    return api_response


