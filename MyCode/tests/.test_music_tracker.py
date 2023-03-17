import pytest
from lib.music_tracker import MusicTracker

'''
initially there are no tracks
'''
def test_music_tracker():
    tracker = MusicTracker()
    assert tracker.already_played() == []

'''
when we add a track
it is reflected in the list of tracks
'''
def test_add_track():
    tracker = MusicTracker()
    tracker.add('School', 'Nirvana', 'Bleach')
    assert tracker.already_played() == [('School', 'Nirvana', 'Bleach')]

'''
when we add multiple tracks
They are all reflected in the list of tracks
'''
def test_add_multiple_tracks():
    tracker = MusicTracker()
    tracker.add('School', 'Nirvana', 'Bleach')
    tracker.add('Wonderwall', 'Oasis', 'Best Of')
    tracker.add('Self Esteem', 'Offspring', 'Smash')
    assert tracker.already_played() == [('School', 'Nirvana', 'Bleach'), ('Wonderwall', 'Oasis', 'Best Of'), ('Self Esteem', 'Offspring', 'Smash')]

'''
raises an error if 
missing song title
'''
def test_raise_error_no_song():
    tracker = MusicTracker()
    with pytest.raises(Exception) as err:
        tracker.add('', 'Nirvana', 'Bleach')
    assert str(err.value) == "ERROR - info missing"


'''
raises an error if 
missing artist name
'''
def test_raise_error_no_artist():
    tracker = MusicTracker()
    with pytest.raises(Exception) as err:
        tracker.add('School', '', 'Bleach')
    assert str(err.value) == "ERROR - info missing"

'''
raises an error if 
missing album title
'''
def test_raise_error_no_album():
    tracker = MusicTracker()
    with pytest.raises(Exception) as err:
        tracker.add('School', 'Nirvana', '')
    assert str(err.value) == "ERROR - info missing"