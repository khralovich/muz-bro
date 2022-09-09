import requests
import urllib

songlink_endpoint = "https://api.song.link/v1-alpha.1/links"

def get_songlink_url(song_url: str) -> dict:
    response_dict = {}
    encoded_url = urllib.parse.quote(song_url)
    response = requests.get(
        url=songlink_endpoint,
        params={
            "url": encoded_url
        }
    )
    response_dict = response.json()
    links_by_platform = response_dict['linksByPlatform']
    for platform, properties in links_by_platform.items():
        response_dict[platform] = properties['url']
    return response_dict

def get_multiple_songlink_urls(urls: list[str]) -> list[dict]:
    return [get_songlink_url(url) for url in urls]