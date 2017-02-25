"""Class definition for movie object"""

import webbrowser
import imdb
import re


class Movie():
    """test doc string"""
    def __init__(self, title, storyline, trailer_youtube_url, imdb_url):

        # Extract movie ID from url

        imdb_id_match = re.search(r'(?<=tt)[0-9]+', imdb_url)
        imdb_id = imdb_id_match.group(0) if imdb_id_match else None

        # Access movie object through IMDb API

        imdb_access = imdb.IMDb()
        movie = imdb_access.get_movie(str(imdb_id))

        # Extract the youtube ID from the url

        youtube_id_match = re.search(r'(?<=v=)[^&#]+', trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
                        r'(?<=be/)[^&#]+', trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        self.imdb_id = imdb_id
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = movie['full-size cover url']
        self.rating = movie['rating']
        self.yt_trailer_id = trailer_youtube_id

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
