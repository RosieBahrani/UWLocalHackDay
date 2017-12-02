import youtube_dl
import pafy

url = open ('/Users/mahshidbahrani/Downloads/Unknown-14').read()

options = {
  'format': 'bestaudio/best',
  'extractaudio' : True,  # only keep the audio
  'audioformat' : "mp3",  # convert to mp3 
  'outtmpl': '%(id)s',    # name the file the ID of the video
  'noplaylist' : True,    # only download single song, not playlist
}
ydl_opts = {}
with youtube_dl.YoutubeDL(options) as ydl:
    #change this line and instead of the string with the link, give it the variable "url".
 # video = pafy.new('https://www.youtube.com/watch?v=65_PmYipnpk')
    video = pafy.new(url)
    print (video.title)
    audiostreams = video.audiostreams
    audiostreams[1].download()
#    bestaudio = video.getbestaudio()
#    bestaudio.download()
 #   ydl.download(['https://www.youtube.com/watch?v=Ymovqj73k1Q'])

