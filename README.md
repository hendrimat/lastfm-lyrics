# Last.fm lyrics
Python script which displays lyrics (from Genius.com) to the currently scrobbling song in your terminal.

## Requirements
Python 3\
[LyricsGenius](https://github.com/johnwmillr/LyricsGenius)

## Setup
Before using this package you'll need to sign up for a (free) account that authorizes access to [the Genius API](http://genius.com/api-clients). The Genius account provides a `client_access_token` that is required by the package.\
You also need to create an [API account](https://www.last.fm/api/account/create) on Last.fm to get an API key.

## Usage
Can be used with any music player that has scrobbling support.

1. Insert your Last.fm username and API keys into the script.
2. Execute the script in your terminal ```$ python PATH/TO/SCRIPT```

## Credit
[0nse](https://github.com/0nse)'s [Now Playing](https://github.com/0nse/now_playing) script is used to get song information from Last.fm.
