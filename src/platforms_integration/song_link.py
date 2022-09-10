import requests
import urllib

SONGLINK_ENDPOINT = "https://api.song.link/v1-alpha.1/links"

SELECTED_PLATFORMS = {
    "amazonMusic",
    "deezer",
    "appleMusic",
    "spotify",
    "tidal",
    "yandex",
    "youtube",
    "youtubeMusic",
    "soundcloud"
}

def get_songlink_url(song_url: str) -> dict:
    response_dict = {}
    encoded_url = urllib.parse.quote(song_url)
    response = requests.get(
        url=SONGLINK_ENDPOINT,
        params={
            "url": encoded_url
        }
    )
    api_response_dict = response.json()
    links_by_platform = api_response_dict['linksByPlatform']
    for platform, properties in links_by_platform.items():
        if platform in SELECTED_PLATFORMS:
            response_dict[platform] = properties['url']
    return response_dict

def get_multiple_songlink_urls(urls: list[str]) -> list[dict]:
    return [get_songlink_url(url) for url in urls]