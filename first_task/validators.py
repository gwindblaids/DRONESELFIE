from datetime import datetime
import time
from typing import Dict
from models import Ticket


def validate_new_ticket_request(request_data: dict) -> Dict[bool, str]:
    expected_params = {'date', 'number', 'time'}
    result = {
        'status': False,
        'message': ''
    }

    if not expected_params.issubset(set(request_data.keys())):
        result['message'] = 'Invalid params'
    elif not request_data['number'].isdigit() or len(request_data['number']) not in range(1, 4):
        result['message'] = 'Invalid number. Number must be in range 1-999'
    elif Ticket.query.filter_by(number=request_data['number']).first():
        result['message'] = 'Such number already exists'
    else:
        try:
            datetime.strptime(request_data['date'], '%d.%m.%Y')
            time.strptime(request_data['time'], '%H:%M')
        except ValueError as err:
            result['message'] = f'{err}'

    if not result['message']:
        result['status'] = True
        result['message'] = 'Ticket create'

    return result
