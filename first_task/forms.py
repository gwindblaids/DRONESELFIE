from flask_wtf import FlaskForm
from wtforms import DateField, TimeField, StringField, SubmitField
from wtforms.validators import DataRequired, length, ValidationError
from models import Ticket


class TicketForm(FlaskForm):
    number = StringField('Number of ticket', validators=[DataRequired(), length(min=1, max=3)])
    date = DateField('Date', validators=[DataRequired()])
    time = TimeField('Time', validators=[DataRequired()])
    submit = SubmitField('Order a ticket')

    def validate_number(self, number: str):
        if not number.data.isdigit():
            raise ValidationError('Must be integer')
        elif Ticket.query.filter_by(number=number.data).first():
            raise ValidationError('Such number already exists')