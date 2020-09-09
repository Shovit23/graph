from pygame import mixer
file = '/root/Music/ARASH-feat-Helena-Broken-Angel.mp3'
mixer.init()
mixer.music.load(file)
mixer.music.play()
