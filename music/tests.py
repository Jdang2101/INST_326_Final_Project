import classes


def test_1_for_createPlaylist():
    outcome = False
    
    classes.Playlist.createPlaylist("TestPlaylist")

    for playlist in classes.Playlist.playlists_database:
        if playlist == "TESTPLAYLIST":
            outcome = True
        else:
            continue
    assert outcome == True