"""Class definition for movie object"""

import imdb
import re


class Movie():
    """class that stores information about a movie"""
    def __init__(self, **kwargs):

        # a dictionary that will be used to set object's instance attributes
        attributes = {}

        def get_imdb_id(kwargs):
            """extracts imdb id if possible"""

            imdb_id = None
            if 'imdb_id' in kwargs:
                imdb_id = kwargs['imdb_id']

            # extracts movie ID from url
            if 'imdb_url' in kwargs and not imdb_id:
                imdb_url = kwargs['imdb_url']
                imdb_id_match = re.search(r'(?<=tt)[0-9]+', imdb_url)
                imdb_id = imdb_id_match.group(0) if imdb_id_match else None

            return imdb_id

        def get_youtube_id(kwargs):
            """extracts the youtube ID from the url"""

            trailer_youtube_id = None
            if 'trailer_youtube_url' in kwargs:
                trailer_youtube_url = kwargs['trailer_youtube_url']
                youtube_id_match = re.search(r'(?<=v=)[^&#]+', trailer_youtube_url)
                youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',
                                                             trailer_youtube_url)
                trailer_youtube_id = (youtube_id_match.group(0)
                                      if youtube_id_match else None)

            return trailer_youtube_id

        def get_imdb_info(imdb_id):
            """extracts imdb info through imdb api"""

            attrs = {'imdb_id': imdb_id}
            imdb_access = imdb.IMDb()
            movie = imdb_access.get_movie(imdb_id)
            if 'title' in movie.keys():
                attrs['title'] = movie['title']
            if 'plot outline' in movie.keys():
                attrs['storyline'] = movie['plot outline']
            if 'rating' in movie.keys():
                attrs['rating'] = movie['rating']
            if 'year' in movie.keys():
                attrs['year'] = movie['year']
            if 'full-size cover url' in movie.keys():
                attrs['poster_image_url'] = movie['full-size cover url']
            else:
                if 'cover_url' in movie.keys():
                    attrs['poster_image_url'] = movie['cover url']
            attrs['imdb_url'] = "http://www.imdb.com/title/tt" + imdb_id + "/"

            return attrs

        imdb_id = get_imdb_id(kwargs)

        if imdb_id:
            attributes.update(get_imdb_info(imdb_id))

        trailer_youtube_id = get_youtube_id(kwargs)

        if trailer_youtube_id:
            attributes['trailer_youtube_id'] = trailer_youtube_id

        attributes.update(kwargs)

        for key, value in attributes.items():
            setattr(self, key, value)

        print "[+] Movie '%s' object created" % getattr(self, 'title', 'title missing')
