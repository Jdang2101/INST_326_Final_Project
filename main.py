import sys
import argparse
from gui.frontend import app


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
        creator = input("What is your name? ")
        playlist_title = input("What is the playlist title? ")
        new_playlist = Playlist(creator, playlist_title)
        Playlist.playlists_database.append(new_playlist)
        
    # Should this function have a feature to allow the user to add songs to the playlist right away?
    # Or should it give it option to add a song on repeat until the user says no more songs?
    
    
    def viewListOfPlaylists(self):
        # Display the list of created playlists.
        pass
    
    def selectPlaylist(self, playlist_index):
        # Select a playlist to perform actions on.
        pass
        
    def viewSongsInPlaylist(self, playlist_title):
        # View the list of songs in a selected playlist along with their details.
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

def main(gui_enabled: bool):
    """ The main function which will be executed when the script is run.

    Args:
        gui_enabled (bool): Whether or not the GUI is enabled.
    """

    # Check to see if the GUI is enabled.
    if gui_enabled:
        # If the GUI is enabled, then run the GUI code.
        app.run(debug=True)

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    
    #For the sake of readability it is important to insert comments all throughout.
    #Complicated operations get a few lines of comments before the operations commence. 
    #Non-obvious ones get comments at the end of the line.
    #For example:
    #This function uses the argparse module in order to parse command line arguments.
    
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    
    #Then we will add arguments to this parser object.
    #In this case, we have a required positional argument.
    #Followed by an optional keyword argument which contains a default value.
    
    parser.add_argument('--gui', '-g', type=bool, default=False, help='Enable the GUI')  
    
    args = parser.parse_args(args_list) #We need to parse the list of command line arguments using this object.

    return args

if __name__ == "__main__":
    #If name == main statements are statements that basically ask:
    #Is the current script being run natively or as a module?
    #It the script is being run as a module, the block of code under this will not be executed.
    #If the script is being run natively, the block of code below this will be executed.
    
    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
    
    #The returned object is an object with those command line arguments as attributes of an object.
    #We will pass both of these arguments into the main function.
    #Note that you do not need a main function, but you might find it helpfull.
    #You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.
    
    main(arguments.gui)
