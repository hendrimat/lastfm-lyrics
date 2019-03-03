#!/usr/bin/env python
# -*_ coding: utf-8 -*-

""" Python script which displays lyrics (from Genius.com) to the currently scrobbling song on Last.fm in your terminal.

Author: Hendrik Matvejev
Website: https://github.com/hendrimat/lastfm-lyrics
License: GPL-3.0
Python 3

Usage:
    get api keys from last.fm and genius
    insert api keys and username into the script
    execute script '$ python PATH/TO/SCRIPT'
"""

import requests
import lyricsgenius as genius
import os


#Insert your Last.fm username and Genius and Last.fm api keys
LASTFM_API = 'YOUR_API_KEY' #https://www.last.fm/api/account/create
GENIUS_API = 'YOUR_API_KEY' #https://genius.com/api-clients/new
USER = 'YOUR_LASTFM_USERNAME'
SLEEP_TIME = 5 #time between requests


def make_request():
    base_url = 'https://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks'
    parameters = {
        'api_key':    LASTFM_API,
        'format':     'json',
        'limit':      '1',
        'nowplaying': 'true',
        'user':       USER
    }
    return requests.get(base_url, parameters)


def process_result(request):
    response = request.json()
    return response['recenttracks']['track'][0]


def is_now_playing(track):
    return track['@attr']['nowplaying'] == 'true'


def format_track(track):
    artist = track['artist']['#text']
    title = track['name']
    return '%s - %s' % (artist, title)

last_track = ""
now_playing_track = "as"

api = genius.Genius(GENIUS_API)

clear = lambda : os.system('tput reset')

if __name__ == '__main__':
    import time

    while True:
        try:
            request = make_request()
            if request.status_code == 200:
                most_recent_track = process_result(request)

                if is_now_playing(most_recent_track):
                    now_playing_track = format_track(most_recent_track)

                    if last_track != now_playing_track:
                        last_track = now_playing_track

                        artist, title = now_playing_track.split("-")
                        artist = artist.strip()
                        title = title.strip()
                        song = api.search_song(title, artist)
                        lyrics = song.lyrics
                        clear()
                        print(lyrics)

                        now_playing_track = last_track

                    else:
                        time.sleep(SLEEP_TIME)

        except:
            pass

        time.sleep(SLEEP_TIME)
