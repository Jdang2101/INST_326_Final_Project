class Song:
    """ Class Song:
    Properties:
        - title
        - artist
        - genre
    """
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
        
    # Should this function have a feature to allow the user to add songs to the playlist right away?
    # Or should it give it option to add a song on repeat until the user says no more songs?
    
    
    def viewListOfPlaylists(self):
        # Display the list of created playlists.
        for playlist in Playlist.playlists_database:
            print(playlist.playlist_title)
        
    
    def selectPlaylist(self, playlist_index):
        # Select a playlist to perform actions on.
        selected_playlist = input("Please enter the name of the playlist: ").upper()
        while selected_playlist not in [playlist.playlist_title for playlist in Playlist.playlists_database]:
            print("That playlist does not exist.")
            selected_playlist = input("Please enter the name of the playlist: ").upper()
        
    def viewSongsInPlaylist(self, playlist_title):
        # View the list of songs in a selected playlist along with their details.
        for playlist in Playlist.playlists_database:
            if playlist.playlist_title == selected_playlist:
                print(f"Songs in playlist '{playlist.playlist_title}':")
                for song in playlist.songs:
                    print(f"Title: {song['title']}")
                    print(f"Artist: {song['artist']}")
                    print(f"Genre: {song['genre']}")
                    print("--------------------")
                break

    def addSongToPlaylist(self, title, artist, genre):
        # Add a song to a selected playlist with the given details.
        for playlist in Playlist.playlists_database:
            if playlist.playlist_title == selected_playlist:
                song = {
                    'title': title,
                    'artist': artist,
                    'genre': genre
                }
                playlist.songs.append(song)
                print(f"The Song '{title}' by {artist} has been added to playlist '{playlist.playlist_title}'.")
                

    def deleteSongFromPlaylist(self, title, artist):
        # Delete a song from the selected playlist.
        pass

    def addSongToDatabase(self, title, artist, genre):
        # Add a song to the global database.
        pass

    def searchForPlaylist(self, playlist_title):
        # Search for a specific playlist by its title.
        pass
    
    


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