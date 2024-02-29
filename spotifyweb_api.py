import requests
from urllib3.util import url


def search_spotify_tracks(query):
    api_token = 'your api token'
    headers = {'Authorization': f'Bearer {api_token}'}
    url = f'https://api.spotify.com/v1/search?q={query}&type=track'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for track in data['tracks']['items']:
            print(f"Name: {track['name']}")
            print(f"Artist: {track['artists'][0]['name']}")
            print()
        else:
            print("Failed to search tracks on Spotify.")


search_query = input("Enter track name: ")
search_spotify_tracks(search_query)
