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
        - createPlaylist(playlist_title):
            Create a new playlist with a given title. 

        - viewListOfPlaylists():
            Display the list of created playlists.

        - selectPlaylist(selected_playlist):
            Select a playlist to perform actions on.

        - viewSongsInPlaylist(selected_playlist):
            View the list of songs in a selected playlist along with their details.

        - addSongToSelectedPlaylist(title, artist, genre, selected_playlist):
            Add a song to the selected playlist.

        - deleteSongFromSelectedPlaylist(title, artist, selected_playlist):
            Delete a song from the selected playlist.

        - addSongToDatabase(title, artist, genre):
            Add a song to the global songs database.

        - deleteSongFromDatabase(title, artist)
            Delete a song from the global songs database

        - searchForPlaylist(playlist_title):
            Search for a specific playlist by its title.
    """
    playlists_database = []
    

    def __init__(self, creator, playlist_title):
        """
        Initialize a Playlist object.

        Args:
            creator (str): The creator of the playlist.
            playlist_title (str): The title of the playlist.
        """
        
        self.creator = creator
        self.playlist_title = playlist_title
        
        # The songs property is a list of dictionaries containing song details.
        self.songs = []
        # Append the playlist to the global playlists database.
        Playlist.playlists_database.append(self)

    def createPlaylist(self, playlist_title):
        """
        Create a new playlist with a given title along with a creator name.

        Args:
            playlist_title (str): The title of the new playlist.


        """
        # Get the input of the name of the creator of the playlist.
        creator = input("What is your name? ").upper()
        # 
        playlist_title = input("What is the playlist title? ").upper()
        new_playlist = Playlist(creator, playlist_title)
        Playlist.playlists_database.append(new_playlist)


    def viewListOfPlaylists(self):
        """
        Display the list of created playlists.
        """
        for playlist in Playlist.playlists_database:
            print(playlist.playlist_title)
        

    def selectPlaylist(self, selected_playlist):
        """
        Selects a playlist to perform actions on.

        Parameters:
        selected_playlist (str): The title of the playlist to select.

        Returns:
        None
        """
        while selected_playlist not in [Playlist.playlist_title for playlist in Playlist.playlists_database]:
            print("That playlist does not exist.")
                
    def viewSongsInPlaylist(self, selected_playlist):
        """
        View the list of songs in a selected playlist along with their details.

        Parameters:
        - selected_playlist (str): The title of the playlist to view.

        Returns:
        None
        """
        for playlist in Playlist.playlists_database:
            if Playlist.playlist_title == selected_playlist:
                print(f"Songs in playlist '{Playlist.playlist_title}':")
                for song in Playlist.songs:
                    print(f"Title: {song['title']}")
                    print(f"Artist: {song['artist']}")
                    print(f"Genre: {song['genre']}")
                    print("--------------------")
                break

    def addSongToSelectedPlaylist(self, title, artist, genre, selected_playlist):
        """
        Add a song to a selected playlist with the given details.

        Parameters:
        - title (str): The title of the song.
        - artist (str): The artist of the song.
        - genre (str): The genre of the song.
        - selected_playlist (str): The title of the playlist to add the song to.

        Returns:
        None
        """
        for playlist in Playlist.playlists_database:
            if Playlist.playlist_title == selected_playlist:
                song = {
                    'title': title.upper(),
                    'artist': artist.upper(),
                    'genre': genre.upper()
                }
                playlist.songs.append(song)
                print(f"The Song '{title.upper()}' by {artist.upper()} has been added to playlist '{playlist.playlist_title}'.")


    def deleteSongFromSelectedPlaylist(self, title, artist, selected_playlist):
        """
        Delete a song from the selected playlist.

        Parameters:
        - title (str): The title of the song to be deleted.
        - artist (str): The artist of the song to be deleted.
        - selected_playlist (str): The title of the playlist from which the song will be deleted.

        Returns:
        None
        """
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
        """
        Add a song to the global database.

        Parameters:
        title (str): The title of the song.
        artist (str): The artist of the song.
        genre (str): The genre of the song.
        """
        song = Song(title.upper(), artist.upper(), genre.upper())

        Song.songs_database.append(song)

    def deleteSongFromDatabase(self, title, artist):
        """
        Deletes a song from the database based on the given title and artist.

        Parameters:
        - title (str): The title of the song to be deleted.
        - artist (str): The artist of the song to be deleted.
        """
        for song in Song.songs_database:
            if Song.title == title.upper() and Song.artist == artist.upper():
                Song.songs_database.remove(song)
                break
            else:
                continue

    def searchForPlaylist(self, playlist_title):
        """
        Search for a specific playlist by its title.

        Parameters:
        - playlist_title (str): The title of the playlist to search for.

        Returns:
        None
        """
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
        - recomendSongsFromSongsDatabaseBasedOnGenre(genre)
        - recomendSongsFromSongsDatabaseBasedOnArtist(artist)

    Actions:
        - recommendSongsBasedOnGenre(genre):
            Recommend songs based on the given genre.

        - recommendSongsBasedOnArtist(artist):
            Recommend songs based on the given artist.

        - recomendSongsFromSongsDatabaseBasedOnGenre(genre):
            Recommend songs based on the given genre.

        - recomendSongsFromSongsDatabaseBasedOnArtist(artist):
            Recommend songs based on the given artist.
    """
            
    def __init__(self, database):
        self.database = database

    def recommendSongsBasedOnGenre(self, genre):
        # Recommend songs based on the given genre.
        recomendations = []

        for playlist in Playlist.playlists_database:
            for song in playlist.songs:
                if song.genre == genre.upper():
                    recomendations.append(song)
                    break
                else:
                    continue
        return recomendations

    def recommendSongsBasedOnArtist(self, artist):
        # Recommend songs based on the given artist.
        recomendations = []

        for playlist in Playlist.playlists_database:
            for song in playlist.songs:
                if song.genre == artist.upper():
                    recomendations.append(song)
                    break
                else:
                    continue
        return recomendations
    
    def recomendSongsFromSongsDatabaseBasedOnGenre(self, genre):
        # Recommend songs based on the given genre.
        recomendations = []

        for song in Song.songs_database:
            if song.genre == genre.upper():
                recomendations.append(song)
                break
            else:
                continue
        return recomendations
    
    def recomendSongsFromSongsDatabaseBasedOnArtist(self, artist):
         # Recommend songs based on the given artist.
        recomendations = []

        for song in Song.songs_database:
            if song.genre == artist.upper():
                recomendations.append(song)
                break
            else:
                continue
        return recomendations