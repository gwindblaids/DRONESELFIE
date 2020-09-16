from datetime import datetime

from flask import render_template, request, jsonify, flash

from app import app, db
from forms import TicketForm
from models import Ticket
from validators import validate_new_ticket_request


def create_new_ticket(number, date, time):
    ticket = Ticket(number=number, date=date, time=time)
    db.session.add(ticket)
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def general_page():
    if request.method == 'GET' and request.args:
        validation_result = validate_new_ticket_request(request.args)
        if validation_result['status']:
            create_new_ticket(number=request.args['number'], date=datetime.strptime(request.args['date'], '%d.%m.%Y'),
                              time=request.args['time'])
        return jsonify(validation_result)
    else:
        ticket_form = TicketForm()
        if ticket_form.validate_on_submit():
            create_new_ticket(number=ticket_form.number.data, date=ticket_form.date.data, time=ticket_form.time.data)
            flash('Ticket create')
    return render_template('ticket-form.html', form=ticket_form)
