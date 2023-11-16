from flask import Flask, render_template
import sys, os

# get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# get the parent directory
parent_dir = os.path.dirname(current_dir)

# import main.py from the parent directory
sys.path.append(parent_dir)

from music.classes import Song, Playlist, Recommender

app = Flask(__name__)

# Homepage
@app.route("/")
def index():
    return render_template("index.html", title="Home")

# Playlist Page
@app.route("/playlists")
def playlists_page():
    return render_template("playlists.html", title="Playlists")

# Genres Page
@app.route("/genres")
def genres_page():
    return render_template("genres.html", title="Genres")