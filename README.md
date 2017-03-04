# fsnd-project-1
Movie Trailer Website

###Overview:
Renders an HTML file with basic information about movies shown on page as movie tiles.

###Requirements:
To work properly package [IMDbPY](http://imdbpy.sourceforge.net/) is required.

###Functions implemented:
* `open_movies_page(movies)`: renders an html file with movies passed as a list of Movie objects(more about class Movie below)
* `sort_by_rating(movies)`: sorts a list of Movie objects by rating
* `between_years(min_year=0, max_year=9999, n=9)`: returns a list of 'n' movies made between years 'min_year' and 'max_year
* `filter_movies(movies, *args)`: returns a list of Movie objects that have attributes given as args parameters

###How to use
You can create a list of Movie objects in two ways:
1 Create objects one by one yourself and put them in a list
2 Use `between_years()` function to return a list of Movie objects

When you create objects yourself you can pass as many keyword parameters as you want.
Parameters that are used to display information in a rendered file are:
* title
* trailer_youtube_url
* rating
* imdb_url
* poster_image_url

If trailer_youtube_url is present a tile on click will play the trailer, otherwise it will follow imdb_url link.
when both trailer_youtube_url and imdb_url are missing nothing will happen on click.

Objects created with either imdb_url or imdb_id parameters will have their attributes assigned information retrieved through IMDb API
If other parameters are also present they will overwrite those assigned by information from IMDb.

###Example

You create Movie object big_lebowski putting this line of code in entertainment_center.py:
'big_lebowski(title="Big Lebowski", imdb_id="0118715", youtube_trailer_url="https://www.youtube.com/watch?v=cd-go0oBF4Y")'
Some of the assigned attributes will be:
* title: "Big Lebowski" passed as an argument and not "The Big Lebowski" retrieved through IMDb
* trailer_youtube_url: "https://www.youtube.com/watch?v=cd-go0oBF4Y" passed as an argument
* storyline: This will come from IMDb if available
* poster_image_url: This will come from IMDb if available
* rating: This will come from IMDb if available

This object on click will show youtube trailer.

###Have fun!
