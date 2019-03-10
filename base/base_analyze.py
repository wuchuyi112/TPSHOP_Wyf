import yaml


def analyze_file(file_name,key_name):
    file_path = "./data/" + file_name + ".yaml"
    with open(file_path,"r",encoding="utf-8") as f:
        data = yaml.load(f)
        # print(data)
        data_list = list()
        for i in data[key_name].values():
            data_list.append(list(i.values()))
        # print(data_list)
        return data_list

