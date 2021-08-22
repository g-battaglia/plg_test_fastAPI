import json

# Create function to unite list of strings:


def unite_list(list_of_strings):
    return ' '.join(list_of_strings)


def get_tabs():
    with open('./tabs/tab1.json', 'r') as f:
        first_data = json.load(f)
    with open('./tabs/tab2.json', 'r') as f:
        second_data = json.load(f)
    with open('./tabs/tab3.json', 'r') as f:
        third_data = json.load(f)

    first_data["item"]["content"] = unite_list(first_data["item"]["content"])
    second_data["item"]["content"] = unite_list(second_data["item"]["content"])
    third_data["item"]["content"] = unite_list(third_data["item"]["content"])
    data = [first_data, second_data, third_data]
    return data


if __name__ == '__main__':
    # print(get_tabs())
    get_tabs()
