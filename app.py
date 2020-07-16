from flask import Flask, render_template, request
from datahandler import save_data
import json

page_app = Flask(__name__)


@page_app.route('/', methods=['post', 'get'])
@page_app.route('/index', methods=['post', 'get'])
def show_index():
    message = ''
    if request.method == 'POST':
        fdata = json.dumps(request.form)
        message = save_data(fdata)
    return render_template('index.html', message=message)


page_app.run(host='0.0.0.0')
