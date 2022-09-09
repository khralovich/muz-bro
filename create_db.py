from operator import index
from ytmusicapi import YTMusic
import pandas as pd
from src.platforms_integration.youtube_music import get_artist_songs, get_songs_titles_urls
from src.platforms_integration.song_link import get_multiple_songlink_urls

artists_list = ["Петля пристрастия", "relikt", "Ляпис трубецкой", "Akute"]
# artists_list = ["BRUTTO"]
csv_path = "./db.csv"


def save_top_10_songs(ytmusic_client, artist: str):
    ytmusic_songs = get_artist_songs(
        youtube_music_client=ytmusic_client,
        artist_name=artist,
        n_songs=10
    )
    ytmusic_titles, ytmusic_urls = get_songs_titles_urls(ytmusic_songs)
    songlink_urls = get_multiple_songlink_urls(urls=ytmusic_urls)
    new_df = pd.DataFrame.from_records(songlink_urls)
    new_df['artist'] = artist
    new_df['title'] = ytmusic_titles
    # If csv file already exists, add new records. Otherwise do nothing
    try:
        df = pd.read_csv(csv_path, index_col=0)
        new_df = pd.concat([new_df, df])
    except:
        pass
    new_df.to_csv(csv_path)
    print('done')
    
    


def main():
    ytmusic = YTMusic()
    df = pd.DataFrame()
    for artist in artists_list:
        save_top_10_songs(ytmusic, artist)
        
    



if __name__ == '__main__':
    main()
    