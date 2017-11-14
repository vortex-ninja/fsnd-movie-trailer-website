"""Class definition for movie object"""

import imdb
import re
from codecs import encode


class Movie(object):
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
                youtube_id_match = re.search(r'(?<=v=)[^&#]+',
                                             trailer_youtube_url)
                youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',
                                                                 trailer_youtube_url)
                trailer_youtube_id = (youtube_id_match.group(0)
                                      if youtube_id_match else None)

            return trailer_youtube_id

        def char_replace(s, to_be_replaced, replacement):
            for ch in to_be_replaced:
                if ch in s:
                    s = s.replace(ch, replacement)
            return s

        def get_imdb_info(imdb_id):
            """extracts imdb info through imdb api"""

            attrs = {'imdb_id': imdb_id}
            imdb_access = imdb.IMDb()
            movie = imdb_access.get_movie(imdb_id)

            # list of properties to be copied from imdb object
            props = ['title', 'plot outline', 'rating', 'year',
                     'full-size cover url', 'cover url']

            # ensure properties are unicode
            for prop in props:
                if prop in movie.keys():
                    prop_value = char_replace(prop, [' ', '-'], '_')
                    prop_value = encode(prop_value, 'utf-8')
                    attrs[prop_value] = movie[prop]

            if 'full_size_cover_url' not in attrs:
                if 'cover_url' in attrs:
                    attrs['full_size_cover_url'] = attrs['cover_url']
                else:
                    attrs['full_size_cover_url'] = ''

            attrs['imdb_url'] = "http://www.imdb.com/title/tt" + imdb_id + "/"

            return attrs

        imdb_id = get_imdb_id(kwargs)

        if imdb_id:
            attributes.update(get_imdb_info(imdb_id))

        trailer_youtube_id = get_youtube_id(kwargs)

        if trailer_youtube_id:
            attributes['trailer_youtube_id'] = trailer_youtube_id

        # Add properties that were passed as arguments
        attributes.update(kwargs)

        # set properties of the Movie object
        for key, value in attributes.items():
            setattr(self, key, value)

        print("[+] Movie '%s' object created" % getattr(self,
                                                        'title',
                                                        'title missing'))

# test_movie = Movie(imdb_id='0110413')
# print(test_movie.__dict__)
# print(type(test_movie.title))
# print(test_movie.title)