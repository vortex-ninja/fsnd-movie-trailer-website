from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import Required


class QueryForm(FlaskForm):

    error_msg = 'Please input a number.'
    min_year = IntegerField('start year:',
                            default=1800,
                            validators=[Required(message=error_msg)])
    max_year = IntegerField('end year: ',
                            default=9999,
                            validators=[Required(message=error_msg)])
    number = IntegerField('number of movies:',
                          default=6,
                          validators=[Required(message=error_msg)])

    submit = SubmitField('Submit')
