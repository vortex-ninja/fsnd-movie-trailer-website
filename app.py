"""functions that display, operate on class Movie objects"""

from flask import Flask, render_template, url_for
import imdb
import media


def sort_by_rating(movies):
    """returns a list with movies sorted by rating"""
    return sorted(movies, key=lambda x: x.rating, reverse=True)


def between_years(min_year=0, max_year=9999, n=9):
    """returns top n movies from imdb top250 list
    produced between min_year and max_year"""

    imdb_access = imdb.IMDb()
    top250 = imdb_access.get_top250_movies()

    results = []
    for movie in top250:
        if movie['year'] >= min_year and movie['year'] <= max_year:
            results.append(media.Movie(imdb_id=movie.movieID))
        if (len(results) >= n):
            return results
    return results


def filter_movies(movies, *args):
    """returns a list of Movie objects that have
       attributes specified in args"""

    results = []
    for movie in movies:
        if set(args) <= set(movie.__dict__.keys()):
            results.append(movie)
    return results


big_lebowski = media.Movie(title="The Big Lebowski",
                           storyline=u"A flick about a dude whose rug is stolen.",
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
movies = filter_movies(movies, 'title', 'rating')

# sorts movies by imdb rating
# movies = sort_by_rating(movies)

# creates a sublist of movies from IMDb Top 250 list
# movies = between_years(1990, 2000, 9)


app = Flask(__name__)
app.config['PREFERRED_URL_SCHEME'] = 'https'


@app.route('/')
def main_page():
    """creates an html file and renders templates in it"""

    return render_template('index.html', movies=movies)


# Starts flask server

print(app.config['PREFERRED_URL_SCHEME'])

if __name__ == '__main__':
    app.secret_key = 'Top secret key'
    # app.debug = True
    app.run(host='0.0.0.0', port=5051)
