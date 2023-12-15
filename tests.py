from music.classes import Playlist
import unittest
from gui.frontend import app

class TestPlaylist(unittest.TestCase):
    """
    Test the Playlist class by creating a playlist and checking if it is in the database
    """
    
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

class TestFrontend(unittest.TestCase):
    """
    Test the frontend of the application
    """
    def test_1_for_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    def test_2_for_playlists(self):
        tester = app.test_client(self)
        response = tester.get("/playlists")
        self.assertEqual(response.status_code, 200)

    def test_3_for_playlist_create(self):
        tester = app.test_client(self)
        response = tester.get("/playlists/create")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()