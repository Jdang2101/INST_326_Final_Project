from music.classes import Playlist
import unittest

class TestPlaylist(unittest.TestCase):
    """
    Test the Playlist class"""
    
    def test_1_for_createPlaylist(self):
        playlist1 = Playlist("Ryan", "Playlist1")
        
        playlist1.createPlaylist("test")

        for playlist in playlist1.playlists_database:
            if playlist.playlist_title == "TEST":
                self.assertEqual(playlist.playlist_title, "TEST")
            else:
                continue

    def test_2_for_createPlaylist(self):
        playlist1 = Playlist("Ryan", "Playlist2")
        
        playlist1.createPlaylist("Test2")

        for playlist in playlist1.playlists_database:
            if playlist.playlist_title == "TEST2":
                self.assertEqual(playlist.playlist_title, "TEST2")
            else:
                continue