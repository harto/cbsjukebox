import gdata.youtube.service as youtube
import os.path
import sh


def youtube_video_url(artist, title):
    service = youtube.YouTubeService()
    query = youtube.YouTubeVideoQuery()
    query.vq = artist + ' ' + title
    #query.orderBy = 'viewCount'
    feed = service.YouTubeQuery(query)
    try:
        return feed.entry[0].media.player.url
    except IndexError:
        return None


def download_audio(url, target_dir):
    output = os.path.join(target_dir, r'%(title)s.%(ext)s')
    # Execute in subprocess; youtube_dl dies after the first download completes
    output = sh.youtube_dl(url, output=output)
    # Report last line of output
    print unicode(output).strip().split('\n')[-1]
