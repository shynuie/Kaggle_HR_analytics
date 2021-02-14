import numpy as np
import os

os.chdir(os.path.dirname(__file__))


def _loading_data(mode):
    """
    Arg:
        mode: str, "train" or "test"
    Return:
        list of data
    """
    data_list = []
    with open(f"data/aug_{mode}.csv", "r") as datas:
        for data in datas:
            _list = data.split(',')
            _clean_data = []
            for feature in _list:
                _clean_data.append(feature.strip())
            data_list.append(_clean_data)
    return data_list


def clean(data_list):
    """
    Arg:
        data_list: list of data

    Return:
        cleaned data, list
    """
    _clean_data_list = []
    data_list = data_list[1:] #remove the tag line
    # for data in data_list:
    #     cd = data[0:2] # 0: ID, 1: city
    #     cd += [float(data[2])] # 2: city development 
    #     cd += _gender(data[3]) # 3: gender
    #     cd += _count_empty(data) # 4: count of emtpy data
    #     cd += _relevent_experience(data[4]) # 5: relevent experience
    #     cd += _enrolled_university(data[5]) # 6~9: enrolled university
    for data in data_list:
        data += _count_empty(data)
        data[2] = float(data[2])
        data = _experience(data)
        _clean_data_list.append(data)
    print(_clean_data_list)


def _count_empty(data):
    empty = 0
    for feature in data:
        if feature == "":
            empty += 1
    return [empty]


def _gender(data):
    gender = 0
    if data == "Male":
        gender = 1
    elif data == "Female":
        gender = -1
    return [gender]


def _relevent_experience(data):
    if data == "Has relevent experience":
        return [1]
    else:
        return [0]


def _enrolled_university(data):
    _dict = {"no_enrollment":[0,0,1,0], "Full time course":[1,0,0,0], "Part time course":[0,1,0,0], "":[0,0,0,1]}
    eu = _dict[data]
    return eu

def _experience(data):
    print(data[8])
    data[8] = data[8].replace(">20","20").replace("<1","0").replace(" ","")
    if data[8] == "":
        data[8] = 0
    data[8] = int(data[8])
    return data


def _categorical_data_break(data_list, column):
    _dict = {}
    break_list = []
    for data in data_list:
        if data[column] not in _dict:
            _dict[data[column]] = len(_dict)
    for data in data_list:
        single_list = [0 for i in range(len(_dict))]
        single_list[_dict[data[column]]] = 1
        data += [f"categorical column:{column}"]
        data += single_list
        break_list.append(data)
    print(break_list)
        
    




if __name__ == "__main__":
    dl = _loading_data("train")
    clean(dl)
    # _categorical_data_break(dl,5)