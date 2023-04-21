import json

def get_json(filename):
    out_file = open("result_RUN.json", "w")

    data = {}
    data1 = {}
    with open(filename, 'r', encoding='utf-8-sig') as fh:
        for line in fh:
            id = line.strip().split(None)[0]
            type = line.strip().split(None)[1]
            time = line.strip().split(None)[2]

            if type == 'start':
                start = time
            if type == 'finish':
                finish = time

                data = {
                    'start': start,
                    'finish': finish
                }
                data1[id] = data
    json.dump(data1, out_file,  indent=4)
    out_file.close()
