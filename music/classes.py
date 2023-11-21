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
    songs_database = []

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
        selected_playlist = input("Please enter the name of the playlist: ").upper()
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
        selected_playlist = input("Please enter the name of the playlist: ").upper()
        for playlist in Playlist.playlists_database:
            if playlist.playlist_title == selected_playlist:
                song = {
                    'title': title.upper(),
                    'artist': artist.upper(),
                    'genre': genre.upper()
                }
                playlist.songs.append(song)
                print(f"The Song '{title}' by {artist} has been added to playlist '{playlist.playlist_title}'.")
                

    def deleteSongFromPlaylist(self, title, artist):
        # Delete a song from the selected playlist.
        selected_playlist = input("Please enter the name of the playlist: ").upper()
        for playlist in Playlist.playlists_database:
            if playlist.playlist_title == selected_playlist:
                for song in playlist.songs:
                    if song['title'] == title.upper() and song['artist'] == artist.upper():
                        playlist.songs.remove(song)
                        print(f"The song '{title}' by {artist} has been deleted from the playlist '{playlist.playlist_title}'.")
                    else:
                        print(f"The song '{title}' by {artist} was not found in the the playlist '{playlist.playlist_title}'.")
                    break
            else:
                print(f"{playlist.playlist_title}The playlist you entered was not found")


# Should we be making the functions like this one below or the one above? I think the one below works best if we are asking the user for all the inputs and using those inputs instead of the parameters that we are passing in to create songs or to add songs to certain playlists.


    def addSongToDatabase(self):
        # Add a song to the global database.
        added_song_title = input("Please enter the title of a song you would like to add")
        added_song_artist = input("Please enter the name of the artists from the song you just entered.")
        added_song_genre = input("Please enter the genre associated with the song you entered.")
        song_to_be_added = Song(added_song_title.upper(), added_song_artist.upper(), added_song_genre.upper())


        Playlist.songs_database.append(song_to_be_added)


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