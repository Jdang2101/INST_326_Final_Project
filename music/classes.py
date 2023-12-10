class Song:
    """ Class Song:
    Properties:
        - title
        - artist
        - genre
    """
    songs_database = []

    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre


class Playlist:
    """ Class Playlist:
    Properties:
        - title
        - songs (list of dictionaries containing song details: title, artist, genre)

    Methods:
        - createPlaylist(title):
            Create a new playlist with a given title.

        - addSongToPlaylist(title, artist, genre):
            Add a song to a selected playlist with the given details.

        - deleteSongFromPlaylist(title, artist):
            Delete a song from the selected playlist.

        - addSongToDatabase(title, artist, genre):
            Add a song to the global database.

        - searchForPlaylist(title):
            Search for a specific playlist by its title.

        - viewListOfPlaylists():
            Display the list of created playlists.

        - viewSongsInPlaylist(title):
            View the list of songs in a selected playlist along with their details.

        - selectPlaylist(playlist_index):
            Select a playlist to perform actions on.

        - addSongToSelectedPlaylist(title, artist, genre):
            Add a song to the selected playlist.

        - deleteSongFromSelectedPlaylist(title, artist):
            Delete a song from the selected playlist.
    """
    playlists_database = []
    

    def __init__(self, creator, playlist_title):
        # Initialize the playlist with a creator and a title.
        self.creator = creator
        self.playlist_title = playlist_title
        self.songs = []

    def createPlaylist(self, playlist_title):
        # Create a new playlist with a given title.
        # The new playlist is appended to the global playlists database.
        creator = input("What is your name? ").upper()
        playlist_title = input("What is the playlist title? ").upper()
        new_playlist = Playlist(creator, playlist_title)
        Playlist.playlists_database.append(new_playlist)
    
    
    def viewListOfPlaylists(self):
        # Display the list of created playlists.
        for playlist in Playlist.playlists_database:
            print(playlist.playlist_title)
        
    
    def selectPlaylist(self, selected_playlist):
        # Select a playlist to perform actions on.
        while selected_playlist not in [Playlist.playlist_title for playlist in Playlist.playlists_database]:
            print("That playlist does not exist.")
        
    def viewSongsInPlaylist(self, selected_playlist):
        # View the list of songs in a selected playlist along with their details.
        for playlist in Playlist.playlists_database:
            if Playlist.playlist_title == selected_playlist:
                print(f"Songs in playlist '{Playlist.playlist_title}':")
                for song in Playlist.songs:
                    print(f"Title: {song['title']}")
                    print(f"Artist: {song['artist']}")
                    print(f"Genre: {song['genre']}")
                    print("--------------------")
                break

    def addSongToPlaylist(self, title, artist, genre, selected_playlist):
        # Add a song to a selected playlist with the given details.
        for playlist in Playlist.playlists_database:
            if Playlist.playlist_title == selected_playlist:
                song = {
                    'title': title.upper(),
                    'artist': artist.upper(),
                    'genre': genre.upper()
                }
                playlist.songs.append(song)
                print(f"The Song '{title.upper()}' by {artist.upper()} has been added to playlist '{playlist.playlist_title}'.")
                

    def deleteSongFromPlaylist(self, title, artist, selected_playlist):
        # Delete a song from the selected playlist.
        for playlist in Playlist.playlists_database:
            if playlist.playlist_title == selected_playlist.upper():
                for song in playlist.songs:
                    if song.title == title.upper() and song.artist == artist.upper():
                        playlist.songs.remove(song)
                        print(f"The song '{title.upper()}' by {artist.upper()} has been deleted from the playlist '{playlist.playlist_title}'.")
                        break
                    else:
                        if song == playlist.songs[-1]:
                            print(f"The song {title.upper()} was not found in the playlist {selected_playlist.upper()} database.")
                        else:
                            continue
            else:
                if playlist == Playlist.playlists_database[-1]:
                    print(f"Playlist {selected_playlist.upper()} was not found in the playlist database.")
                else:
                    continue


    def addSongToDatabase(self, title, artist, genre):
        # Add a song to the global database.
        
        song = Song(title.upper(), artist.upper(), genre.upper())

        Song.songs_database.append(song)

    def deleteSongFromDatabase(self, title, artist):
        for song in Song.songs_database:
            if Song.title == title.upper() and Song.artist == artist.upper():
                Song.songs_database.remove(song)
                break
            else:
                continue

    def searchForPlaylist(self, playlist_title):
        # Search for a specific playlist by its title.
        for playlist in Playlist.playlists_database:
            if playlist.playlist_title == playlist_title.upper():
                print(f"Playlist {playlist_title.upper()} was found in the playlist database.")
            else:
                if playlist == Playlist.playlists_database[-1]:
                    print(f"Playlist {playlist_title.upper()} was not found in the playlist database.")
                else:
                    continue   
    


class Recommender:
    """ Class Recommender:
    Properties:
        - database (list of dictionaries containing song details: title, artist, genre)

    Methods:
        - recommendSongsBasedOnGenre(genre)
        - recommendSongsBasedOnArtist(artist)

    Actions:
        - recommendSongsBasedOnGenre(genre):
            Recommend songs based on the given genre.

        - recommendSongsBasedOnArtist(artist):
            Recommend songs based on the given artist.
    """
            
    def __init__(self, database):
        self.database = database

    def recommendSongsBasedOnGenre(self, genre):
        # Recommend songs based on the given genre.
        pass

    def recommendSongsBasedOnArtist(self, artist):
        # Recommend songs based on the given artist.
        pass