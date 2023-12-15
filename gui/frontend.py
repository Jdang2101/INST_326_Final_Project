from flask import Flask, render_template, request
import sys, os

# get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# get the parent directory
parent_dir = os.path.dirname(current_dir)

# add the parent directory to our path so we can import the classes from music/classes.py
sys.path.append(parent_dir)

from music.classes import Song, Playlist, Recommender

app = Flask(__name__)

# Homepage
@app.route("/")
def index():
    return render_template("index.html", title="Home", playlists=Playlist.playlists_database)


# Playlist Page
@app.route("/playlists")
def playlists_page():
    return render_template("playlists.html", title="Playlists", playlists=Playlist.playlists_database)

# Playlist View Page
@app.route("/playlists/<playlist_title>")
def playlist_view_page(playlist_title):
    # get the playlist from the database
    for playlist in Playlist.playlists_database:
            if str(playlist.playlist_title) == str(playlist_title):
                return render_template("view_playlist.html", title=playlist.playlist_title, playlist=playlist)
            else:
                return render_template("error/404.html", title="404")

# Playlist Creation Page
@app.route("/playlists/create", methods=["GET", "POST"])
def playlists_create_page():
    # Check if the request method is GET
    if request.method == 'GET':
        # If it is, return the create_playlist.html template
        return render_template("create_playlist.html", title="Create a Playlist")
    else:
        # If it is not, handle the POST request
        author = request.form['author']
        title = request.form['title']
        songs = []
        # get the songs from the form
        while True:
            try:
                song_title = request.form[f"song_title_{len(songs)}"]
                song_artist = request.form[f"artist_{len(songs)}"]
                song_genre = request.form[f"genre_{len(songs)}"]
                song = Song(song_title.upper(), song_artist.upper(), song_genre.upper())
                songs.append(song)
            except:
                break
        
        # create the playlist
        playlist = Playlist(title.upper(), author.upper())
        # add the songs to the playlist
        for song in songs:
            playlist.songs.append(song)

        # save the playlist to the database
        Playlist.playlists_database.append(playlist)

        return render_template("view_playlist.html", title=title, playlist=playlist)


# Genres Page
@app.route("/recommend")
def genres_page():
    return render_template("/recommend.html", title="Recommended Playlists")

# 404 Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html", title="404")