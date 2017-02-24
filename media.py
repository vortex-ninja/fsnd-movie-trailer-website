"""Class definition for movie object"""

import webbrowser
import imdb


class Movie():
    """test doc string"""
    def __init__(self, title, storyline, trailer_youtube_url, imdb_id):

        imdb_access = imdb.IMDb()
        movie = imdb_access.get_movie(str(imdb_id))

        self.title = title
        self.storyline = storyline
        self.poster_image_url = movie['full-size cover url']
        self.trailer_youtube_url = trailer_youtube_url
        self.rating = movie['rating']

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
