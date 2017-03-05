import fresh_tomatoes
import media


big_lebowski = media.Movie(title="The Big Lebowski",
                           storyline=u"A flick bout a dude whose rug is stolen.",
                           trailer_youtube_url="https://www.youtube.com/watch?v=cd-go0oBF4Y",
                           imdb_url="http://www.imdb.com/title/tt0118715/?ref_=nv_sr_1")

the_game = media.Movie(imdb_url="http://www.imdb.com/title/tt0119174/",
                       storyline="A bored with life guy gets to play an interesting game.",
                       trailer_youtube_url="https://www.youtube.com/watch?v=0kqQNBR09Rc")

clean_shaven = media.Movie(trailer_youtube_url="https://www.youtube.com/watch?v=6aInRjIwjpU",
                           imdb_id='0106579')

memento = media.Movie(title=u"Memento",
                      imdb_url="http://www.imdb.com/title/tt0209144/",
                      trailer_youtube_url="https://www.youtube.com/watch?v=0vS0E9bBSL0")

twelve_monkeys = media.Movie(imdb_id="0114746",
                             trailer_youtube_url="https://www.youtube.com/watch?v=wuggl3cZD8A")

moon = media.Movie(imdb_id="1182345",
                   trailer_youtube_url="https://www.youtube.com/watch?v=twuScTcDP_Q")

empty_movie = media.Movie()

movies = [big_lebowski, the_game, clean_shaven, memento, twelve_monkeys, moon,
          empty_movie]

# removes films that don't have at least 'title' and 'rating' attributes
movies = fresh_tomatoes.filter_movies(movies, 'title', 'rating')

# sorts movies by imdb rating
movies = fresh_tomatoes.sort_by_rating(movies)

# creates a sublist of movies from IMDb Top 250 list
# movies = fresh_tomatoes.between_years(1990, 2000, 9)

# renders and opens html file
fresh_tomatoes.open_movies_page(movies)
