import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "TzRvaG-lSphKQKfphzP9cRqVoqqwIyi15I9SMSLar9FR6kw3lVablr001AVZ_BcekesA6Q-KKFH09GgzqBwm5COR3t4V5nQChV7A8PfRnAC1CY1nupS2rQwnGaBGYHYx"
headers = {
    "Authorization": "Bearer " + api_key
}

params = {
    "location": "NYC"   
}
response = requests.get(url, headers=headers, params=params)
print(response.text)  # see the details of what the server sent us
businesses = response.json()["businesses"]
print(businesses)

names = [business["name"] for business in businesses if business["rating"] > 4.5]
print(names)
#for business in businesses:
#    print(business["name"])