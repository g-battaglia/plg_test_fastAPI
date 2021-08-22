import json


def get_tabs():
    with open('./tabs/tab1.json', 'r') as f:
        first_data = json.load(f)
    with open('./tabs/tab1.json', 'r') as f:
        second_data = json.load(f)
    with open('./tabs/tab1.json', 'r') as f:
        third_data = json.load(f)

    data = [first_data, second_data, third_data]
    return data
