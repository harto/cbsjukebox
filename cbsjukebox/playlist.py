import bs4
import re
import urllib2


def parse_playlist(url='http://www.antonfig.com/lnsongs.htm'):
    """
    Parses the playlist URL to produce a list of (artist, title) tuples."
    """

    html = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html)

    # :-(
    playlist_table = soup.find('table', border=1, cellpadding=4, width='92%', align='center')
    # :-(
    playlist_rows = filter(lambda tr: 'bgcolor' not in tr.attrs, playlist_table.find_all('tr')[1:])

    cleanup_whitespace = lambda s: re.sub(r'\s+', ' ', s, 0, re.MULTILINE)
    normalise_artist = lambda s: s#re.sub(r'(.+), (.+)', r'\2 \1', s).strip()
    normalise_title = lambda s: re.sub(r'"([^"]+)".*', r'\1', s).strip()

    def to_playlist_entry(row):
        artist, title = map(cleanup_whitespace, row.stripped_strings)
        return (normalise_artist(artist), normalise_title(title))

    return map(to_playlist_entry, playlist_rows)
