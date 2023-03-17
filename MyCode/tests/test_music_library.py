from lib.music_library import MusicLibrary
from lib.track import Track

'''
initially there are no tracks
'''
def initially_there_are_no_tracks():
    library = MusicLibrary()
    assert library.tracks == []

