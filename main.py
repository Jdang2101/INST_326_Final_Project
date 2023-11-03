

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
    def __init__(self, title, songs):
        self.title = title
        self.songs = songs

    def createPlaylist(self, title):
        # Create a new playlist with a given title.
        pass

    def addSongToPlaylist(self, title, artist, genre):
        # Add a song to a selected playlist with the given details.
        pass

    def deleteSongFromPlaylist(self, title, artist):
        # Delete a song from the selected playlist.
        pass

    def addSongToDatabase(self, title, artist, genre):
        # Add a song to the global database.
        pass

    def searchForPlaylist(self, title):
        # Search for a specific playlist by its title.
        pass

    def viewListOfPlaylists(self):
        # Display the list of created playlists.
        pass

    def viewSongsInPlaylist(self, title):
        # View the list of songs in a selected playlist along with their details.
        pass

    def selectPlaylist(self, playlist_index):
        # Select a playlist to perform actions on.
        pass

    def addSongToSelectedPlaylist(self, title, artist, genre):
        # Add a song to the selected playlist.
        pass

    def deleteSongFromSelectedPlaylist(self, title, artist):
        # Delete a song from the selected playlist.
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