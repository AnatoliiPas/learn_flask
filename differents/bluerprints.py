from datetime import date
from flask import Blueprint


different = Blueprint('differents', __name__)


@different.route('/date-json')
def date_json():
    return {'date': date.today()}
