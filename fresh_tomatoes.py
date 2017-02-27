import webbrowser
import os
import jinja2
import codecs

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


def render_template(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)


def open_movies_page(movies):

    # create a file and render templates in it
    with codecs.open('fresh_tomatoes.html', 'w', encoding="utf-8") as output_file:
        output_file.write(render_template('main_page_head.html') +
                          render_template('main_page_content.html', movies=movies))

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)

