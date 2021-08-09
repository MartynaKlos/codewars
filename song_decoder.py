import re


def song_decoder(song):
    old_song = song.replace("WUB", " ")
    final_old_song = old_song.split()
    result = " ".join(final_old_song)
    return result



print(song_decoder('AWUBWUBWUBBWUBWUBWUBC'))
