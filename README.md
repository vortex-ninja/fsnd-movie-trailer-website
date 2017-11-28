# fsnd - movie-trailer-website

### Live demo

https://movie-trailer-website-pro.herokuapp.com/

### Overview:
App lets you query IMDb TOP 250 list for movies released between given years.

### Functions implemented:
* `between_years(min_year=0, max_year=9999, n=6)`: returns a list of `n` movies made between years `min_year` and `max_year`
* `filter_movies(movies, *args)`: returns a list of `Movie` objects that have attributes given as args parameters

### How to use:
1. Set environment variables with `source .env`.
2. Start application by running `flask run` from the directory where `app.py` file is located.

`Movie` objects can be created in two ways:
* Create objects yourself
* Use `between_years()` function to generate a list of `Movie` objects

When you create objects yourself you can pass as many keyword parameters as you want.
Parameters that are used to display information in a rendered file are:
* `title`
* `trailer_youtube_url`
* `rating`
* `imdb_url`
* `poster_image_url`

If `trailer_youtube_url` is present a tile on click will play the trailer, otherwise it will follow `imdb_url` link.
When both `trailer_youtube_url` and `imdb_url` are missing nothing will happen on click.

Objects created with either `imdb_url` or `imdb_id` parameters will have their attributes assigned
information retrieved through IMDb API.
If other parameters are also present they will overwrite those assigned by information from IMDb.

### Example

You create Movie object big_lebowski like this:
`big_lebowski = media.Movie(title="Big Lebowski", imdb_id="0118715", 
                            trailer_youtube_url="https://www.youtube.com/watch?v=cd-go0oBF4Y")`

Some of the assigned attributes will be:
* `title`: "Big Lebowski" passed as an argument and not "The Big Lebowski" retrieved through IMDb
* `trailer_youtube_url`: "https://www.youtube.com/watch?v=cd-go0oBF4Y" passed as an argument
* `storyline`: This will come from IMDb if available
* `poster_image_url`: This will come from IMDb if available
* `rating`: This will come from IMDb if available

This object on click will show youtube trailer.
