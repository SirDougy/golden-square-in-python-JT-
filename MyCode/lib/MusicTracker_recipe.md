
## 1. Describe the Problem

> As a user  
> So that I can keep track of my music listening  
> I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class MusicTracker():
     def __init__(self):
        # self._tracks = []
        pass
        
    def add(self, song, artist, album):        
        # Parameters:
        #   song: string representing song title
        #   artist: string representing artist name
        #   album: string representing album title
        pass

    def already_played(self):
        # Returns:
        #   a list of songs
        pass


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

'''
initially there are no tracks
'''
tracker = MusicTracker()
tracker.already_played() 
    # +> []

'''
when we add a track
it is reflected in the list of tracks
'''
tracker = MusicTracker()
tracker.add('School', 'Nirvana', 'Bleach')
tracker.already_played()
    # => [{'School', 'Nirvana', 'Bleach'}]

'''
when we add multiple tracks
They are all reflected in the list of tracks
'''
tracker = MusicTracker()
tracker.add('School', 'Nirvana', 'Bleach')
tracker.add('Wonderwall', 'Oasis', 'Best Of')
tracker.add('Self Esteem', 'Offspring', 'Smash')
tracker.already_played()
    # => [{'School', 'Nirvana', 'Bleach'}, {'Wonderwall', 'Oasis', 'Best Of'}, {'Self Esteem', 'Offspring', 'Smash'}]

'''
raises an error if 
missing song title
'''
tracker = MusicTracker()
tracker.add('', 'Nirvana', 'Bleach')  # raises error "ERROR - info missing"

'''
raises an error if 
missing artist name
'''
tracker = MusicTracker()
tracker.add('School', '', 'Bleach')  # raises error "ERROR - info missing"

'''
raises an error if 
missing album title
'''
tracker = MusicTracker()
tracker.add('School', 'Nirvana', '')  # raises error "ERROR - info missing"

'''

```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

