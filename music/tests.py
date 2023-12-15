import classes


def test_1_for_createPlaylist():
    outcome = False
    playlist1 = classes.Playlist("Ryan", "Playlist1")
    
    playlist1.createPlaylist("test")

    for playlist in playlist1.playlists_database:
        if playlist == "TEST":
            outcome = True
        else:
            continue
    assert outcome == False

def test_2_for_createPlaylist():
    outcome = False
    playlist1 = classes.Playlist("Ryan", "Playlist2")
    
    playlist1.createPlaylist("Test2")

    for playlist in playlist1.playlists_database:
        if playlist == "TEST2":
            outcome = True
        else:
            continue
    assert outcome == False