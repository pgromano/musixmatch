import json

def jsonp2json(jsonp):
    try:
        l_index = jsonp.index(b'(') + 1
        r_index = jsonp.rindex(b')')
    except ValueError:
        print("Input is not in a jsonp format.")
        return
    return json.reads(jsonp[l_index:r_index])


def album(response):
    return jsonp2json(response.content)['message']['body']['album']


def album_list(response):
    album_list = jsonp2json(response.content)['message']['body']['album_list']
    return [album['album'] for album in album_list]


def artist(response):
    return jsonp2json(response.content)['message']['body']['artist']


def artist_list(response):
    artist_list = jsonp2json(response.content)['message']['body']['artist_list']
    return [artist['artist'] for artist in artist_list]


def lyrics(response):
    return jsonp2json(response.content)['message']['body']['lyrics']


def track(response):
    return jsonp2json(response.content)['message']['body']['track']


def track_list(response):
    track_list = jsonp2json(response.content)['message']['body']['track_list']
    return [track['track'] for track in track_list]
