from datahandler import save_data
import pandas as pd
import json


def test_datahandler():
    test_requests = pd.read_csv('testdata.csv')
    test_responses = pd.read_csv('testresponses.csv')
    for ((i, row), (n, resp_row)) in zip(test_requests.iterrows(), test_responses.iterrows()):
        response = save_data(json.dumps(row.to_dict()))
        assert response == resp_row[0], f'test number {i} failed'

