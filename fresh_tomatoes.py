"""functions that display, operate on class Movie objects"""

import webbrowser
import os
import jinja2
import codecs
import imdb
import media

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


def render_template(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


def open_movies_page(movies):
    """creates an html file and renders templates in it"""

    with codecs.open('fresh_tomatoes.html', 'w', encoding="utf-8") as output_file:
        output_file.write(render_template('main_page_head.html') +
                          render_template('main_page_content.html', movies=movies))

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)


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
