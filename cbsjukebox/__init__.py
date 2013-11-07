#!/usr/bin/env python

# Scrapes the CBS Orchestra playlist from Anton Fig's website and downloads a
# sample of each song from YouTube.

from cbsjukebox.playlist import parse_playlist
from cbsjukebox.youtube import youtube_video_url, download_audio


def main():
    for artist, title in parse_playlist():
        description = '%s - %s' % (artist, title)
        url = youtube_video_url(artist, title)
        if not url:
            print "Couldn't find a result for %s" % description
            continue

        print 'Found YouTube URL for "%s": %s' % (description, url)
        try:
            download_audio(url, '/Users/stuart/Music/cbsjukebox')
        except:
            print 'Error downloading %s' % url


if __name__ == '__main__':
    main()
