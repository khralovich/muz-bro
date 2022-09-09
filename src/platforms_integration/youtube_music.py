from ytmusicapi import YTMusic

youtube_url_format = "https://music.youtube.com/watch?v={}"

def get_artist_songs(youtube_music_client, artist_name: str, n_songs: int) -> list[dict]:
    songs = youtube_music_client.search(query=artist_name, filter="songs", limit=n_songs)
    return songs

def get_songs_urls(songs: list[dict]) -> list[str]:
    urls = [
        youtube_url_format.format(song['videoId'])
        for song
        in songs
    ]
    return urls