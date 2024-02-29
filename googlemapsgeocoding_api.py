import requests

def geocode_address(address):
    api_key = 'your api key'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location = data['results'][0]['geometry']['location']
        print(f"Latitude: {location['lat']}, Longitude: {location['lng']}")
    else:
        print("Failed to geocode address.")

address = input("Enter address: ")
geocode_address(address)