"""Class definition for movie object"""

import webbrowser
import imdb
import re


class Movie():
    """test doc string"""
    def __init__(self, **kwargs):

        imdb_id = None
        imdb_url = None
        title = 'no_title'
        storyline = 'no storyline'
        trailer_youtube_url = None
        trailer_youtube_id = None
        rating = None
        year = None
        poster_image_url = None

        if 'imdb_id' in kwargs:
            imdb_id = kwargs['imdb_id']

        # Extract movie ID from url
        if 'imdb_url' in kwargs and not imdb_id:
            imdb_url = kwargs['imdb_url']
            imdb_id_match = re.search(r'(?<=tt)[0-9]+', imdb_url)
            imdb_id = imdb_id_match.group(0) if imdb_id_match else None

        # Access movie object through IMDb API

        if imdb_id:
            imdb_access = imdb.IMDb()
            movie = imdb_access.get_movie(imdb_id)
            if 'title' in movie.keys():
                title = movie['title']
            if 'plot outline' in movie.keys():
                storyline = movie['plot outline']
            if 'rating' in movie.keys():
                rating = movie['rating']
            if 'year' in movie.keys():
                year = movie['year']
            if 'full-size cover url' in movie.keys():
                poster_image_url = movie['full-size cover url']
            else:
                if 'cover_url' in movie.keys():
                    poster_image_url = movie['cover url']

        # Extract the youtube ID from the url

        if 'trailer_youtube_url' in kwargs:
            trailer_youtube_url = kwargs['trailer_youtube_url']
            youtube_id_match = re.search(r'(?<=v=)[^&#]+', trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',
                                                             trailer_youtube_url)
            trailer_youtube_id = (youtube_id_match.group(0)
                                  if youtube_id_match else None)

        if 'title' in kwargs:
            title = kwargs['title']
        if 'storyline' in kwargs:
            storyline = kwargs['storyline']

        self.imdb_id = imdb_id
        self.title = title
        self.storyline = storyline
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.rating = rating
        self.trailer_youtube_id = trailer_youtube_id
        self.year = year
