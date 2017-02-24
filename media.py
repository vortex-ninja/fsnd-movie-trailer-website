"""Class definition for movie object"""


class Movie():
    def __init__(self, title, storyline, poster_image_url, yt_trailer_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.yt_trailer_url = yt_trailer_url
