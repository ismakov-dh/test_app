from validate_email import validate_email
import pandas as pd
import re
import json

db_file = 'database.csv'


def check_fio(text):
    match = re.match(r'[а-яА-ЯёЁ]', text)
    return not bool(match)


def sp_save_data(data, db=None):
    try:
        db = pd.read_csv(db_file)
    except FileNotFoundError:
        db = pd.DataFrame({'count': [], 'email': [], 'fio': []})
    db = db.append(pd.DataFrame([data]))
    db.to_csv(db_file, index=False)
    return int(data['count']) % 2


def save_data(fdata):
    data = json.loads(fdata)
    result = validate_email(data['email']) and check_fio(data['fio'])
    if result:
        c = sp_save_data(data)
        return f'{result}, {c}'
    else:
        return str(result)
