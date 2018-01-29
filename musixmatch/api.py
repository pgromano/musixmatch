from . import parser
import requests


__all__ = ['ArtistClient', 'AlbumClient', 'LyricsClient', 'TrackClient']


# Global Variables for API URL
API_URL = "http://api.musixmatch.com/ws/1.1/"
# Album API URL
ALBUM_URL = API_URL + "album.get"
ARTIST_ALBUMS_URL = API_URL + "artist.albums.get"
# Artist API URL
ARTIST_RELATED_URL = API_URL + "artist.related.get"
ARTIST_SEARCH_URL = API_URL + "artist.search"
ARTIST_URL = API_URL + "artist.get"
CHART_ARTISTS_URL = API_URL + "chart.artists.get"
# Lyrics API URL
MATCHER_LYRICS_URL = API_URL + "matcher.lyrics.get"
TRACK_LYRICS_URL = API_URL + "track.lyrics.get"
# Tracks API URL
ALBUM_TRACKS_URL = API_URL + "album.tracks.get"
MATCHER_TRACK_URL = API_URL + "matcher.track.get"
TRACK_URL = API_URL + "track.get"
TRACK_SEARCH_URL = API_URL + "track.search"
CHART_TRACKS_URL = API_URL + "chart.tracks.get"


class BaseClient(object):
    """ Helper base client for storing API authentication tokens

    Arguments
    ---------
    api_key : str
        Developer key
    api_secret : str
        Developer secret. Not currently necessary for the Musixmatch API, but
        included for future inclusion.
    api_auth_token : str
        Developer Authentication token. Not currently necessary for the Musixmatch API, but
        included for future inclusion.
    """

    def __init__(self, api_key, api_secret=None, api_auth_token=None, **kwargs):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_auth_token = api_auth_token


class ArtistClient(BaseClient):
    """ API client to query artist database

    Arguments
    ---------
    api_key : str
        Developer key
    api_secret : str
        Developer secret. Not currently necessary for the Musixmatch API, but
        included for future inclusion.
    api_auth_token : str
        Developer Authentication token. Not currently necessary for the Musixmatch API, but
        included for future inclusion.
    """

    def albums(self, artist_id, artist_mbid=None, g_album_name=True,
               s_release_date='asc', page=0, page_size=10):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'artist_id': artist_id,
                 'artist_mbid': artist_mbid,
                 'g_album_name': g_album_name,
                 's_release_date': s_release_date,
                 'page': page,
                 'page_size': page_size}
        response = requests.get(ARTIST_ALBUMS_URL, params=query)
        return parser.album_list(response)

    def chart(self, page_size=10, page=0, country='us'):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'page': page,
                 'page_size': page_size,
                 'country': country}
        response = requests.get(CHART_ARTISTS_URL, params=query)
        return parser.artist_list(response)

    def get(self, artist_id):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'artist_id': artist_id}
        response = requests.get(ARTIST_URL, params=query)
        return parser.artist(response)

    def related(self, artist_id, page_size=10, page=0):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'artist_id': artist_id,
                 'page_size': page_size,
                 'page': page}
        response = requests.get(ARTIST_RELATED_URL, params=query)
        return parser.artist_list(response)

    def search(self, q_artist=None, f_artist_id=None,
               page=0, page_size=10):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'q_artist': q_artist,
                 'f_artist_id': f_artist_id,
                 'page': page,
                 'page_size': page_size}
        response = requests.get(ARTIST_SEARCH_URL, params=query)
        return parser.artist_list(response)


class AlbumClient(BaseClient):
    """ API client to query album database

    Arguments
    ---------
    api_key : str
        Developer key
    api_secret : str
        Developer secret. Not currently necessary for the Musixmatch API, but
        included for future inclusion.
    api_auth_token : str
        Developer Authentication token. Not currently necessary for the Musixmatch API, but
        included for future inclusion.
    """

    def artist(self, artist_id, sort='asc', group=None,
               page_size=10, page=0):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'artist_id': artist_id,
                 's_release_date': sort,
                 'g_album_name': group,
                 'page_size': page_size,
                 'page': page}
        response = requests.get(ARTIST_ALBUMS_URL, params=query)
        return parser.album_list(response)


    def get(self, album_id):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'album_id': album_id}
        response = requests.get(ALBUM_URL, params=query)
        return parser.album(response)


class LyricsClient(BaseClient):
    """ API client to query lyrics database

    Arguments
    ---------
    api_key : str
        Developer key
    api_secret : str
        Developer secret. Not currently necessary for the Musixmatch API, but
        included for future inclusion.
    api_auth_token : str
        Developer Authentication token. Not currently necessary for the Musixmatch API, but
        included for future inclusion.
    """
    def match(self, q_track=None, q_artist=None):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'q_track': q_track,
                 'q_artist': q_artist}
        response = requests.get(MATCHER_LYRICS_URL, params=query)
        return parser.lyrics(response)

    def track(self, track_id):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'track_id': track_id}
        response = requests.get(TRACK_LYRICS_URL, params=query)
        return parser.lyrics(response)


class TrackClient(BaseClient):
    """ API client to query track database

    Arguments
    ---------
    api_key : str
        Developer key
    api_secret : str
        Developer secret. Not currently necessary for the Musixmatch API, but
        included for future inclusion.
    api_auth_token : str
        Developer Authentication token. Not currently necessary for the Musixmatch API, but
        included for future inclusion.
    """

    def album(self, album_id, f_has_lyrics=True, page=0, page_size=10):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'album_id': album_id,
                 'f_has_lyrics': f_has_lyrics,
                 'page': page,
                 'page_size': page_size}
        response = requests.get(ALBUM_TRACKS_URL, params=query)
        return parser.track_list(response)

    def chart(self, page_size=10, page=0, country='us', f_has_lyrics=True):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'country': country,
                 'f_has_lyrics': f_has_lyrics,
                 'page': page,
                 'page_size': page_size}
        response = requests.get(CHART_TRACKS_URL, params=query)
        return parser.track_list(response)

    def get(self, album_id):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'album_id': album_id}
        response = requests.get(TRACK_URL, params=query)
        return parser.track(response)

    def lyrics(self, track_id):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'album_id': track_id}
        response = requests.get(TRACK_LYRICS_URL, params=query)
        return parser.lyrics(response)

    def match(self, q_artist=None, q_track=None, f_has_lyrics=True, f_has_subtitle=True):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'q_artist': q_artist,
                 'q_track': q_track,
                 'f_has_lyrics': f_has_lyrics,
                 'f_has_subtitle': f_has_subtitle}
        response = requests.get(MATCHER_TRACK_URL, params=query)
        return parser.track(response)

    def search(self, q_track=None, q_artist=None, q_lyrics=None,
               f_artist_id=True, f_music_genre_id=False,
               f_lyrics_language=False, f_has_lyrics=True,
               s_artist_rating='asc', s_track_rating='asc',
               quorum_factor=0.5, page_size=10, page=0):
        query = {'apikey': self.api_key,
                 'format': 'jsonp',
                 'callback': 'callback',
                 'q_track': q_track,
                 'q_artist': q_artist,
                 'q_lyrics': q_lyrics,
                 'f_lyrics_language': f_lyrics_language,
                 'f_has_lyrics': f_has_lyrics,
                 's_artist_rating': s_artist_rating,
                 's_track_rating': s_track_rating,
                 'quorum_factor': quorum_factor,
                 'page_size': page_size,
                 'page': page}
        response = requests.get(TRACK_SEARCH_URL, params=query)
        return parser.track_list(response)
