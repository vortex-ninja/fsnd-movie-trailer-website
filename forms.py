from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import NumberRange


def msg_swap(form, field):
    """Swaps error message for IntegerField check"""

    msg_to_rpl = u'Not a valid integer value'
    err_msg = u'Please enter a number'
    print(form.min_year.data)
    if msg_to_rpl in field.errors:
        field.errors[field.errors.index(msg_to_rpl)] = err_msg


class QueryForm(FlaskForm):

    min_year = IntegerField('start year:', validators=[msg_swap])
    max_year = IntegerField('end year:', validators=[msg_swap])
    number = IntegerField('number of movies:',
                          validators=[msg_swap, NumberRange(min=1, max=6)])
    submit = SubmitField('Submit')
