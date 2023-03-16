class MusicTracker():
    def __init__(self):
        self._tracks = []
       
        
    def add(self, song, artist, album):  
        self._tracks.append((song, artist, album)) 
        if song == '' or artist == '' or album == '':
            raise Exception("ERROR - info missing")     
        # Parameters:
        #   song: string representing song title
        #   artist: string representing artist name
        #   album: string representing album title
        

    def already_played(self):
        return self._tracks
