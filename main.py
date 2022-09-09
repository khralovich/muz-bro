from ytmusicapi import YTMusic
from src.platforms_integration.youtube_music import get_artist_songs, get_songs_urls
from src.platforms_integration.song_link import get_multiple_songlink_urls
def main():
    ytmusic = YTMusic()
    ytmusic_songs = get_artist_songs(
        youtube_music_client=ytmusic,
        artist_name="BRUTTO",
        n_songs=1
    )
    ytmusic_urls = get_songs_urls(ytmusic_songs)
    songlink_urls = get_multiple_songlink_urls(urls=ytmusic_urls)
    for key, value in songlink_urls[0].items():
        print(f"Platform: {key}, URL: {value}")
        print("\n")

if __name__ == '__main__':
    main()