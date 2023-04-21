import json
from datetime import datetime, timedelta

import json_convert


def open_json_file(file_path):
    with open(file_path, "r", encoding='utf-8-sig') as my_file:
        sportsmens = my_file.read()
        sportsmens_json = json.loads(sportsmens)
    return sportsmens_json


def get_competition_results(sportsmens_json, results_json):
    sportsmens_result = []
    sportsmens_data = {}
    for sportsmens, results in zip(sorted(sportsmens_json), sorted(results_json)):
        if results == sportsmens:
            time_difference = get_time_difference(
                results_json[results]['start'], results_json[results]['finish'])
            name = sportsmens_json[sportsmens]['Surname']
            surname = sportsmens_json[sportsmens]['Name']
            number = sportsmens

            sportsmens_result.append({
                'number': number,
                'name': name,
                'surname': surname,
                'time': time_difference
            })

        sportsmens_result.sort(key=lambda x: x["time"])

    for result in sportsmens_result:
        time = result['time']
        time = get_time_format(time)
        print(f"""
            Занятое место: {sportsmens_result.index(result)+1}
            Нагрудный номер: {result['number']}
            Имя: {result['name']}
            Фамилия: {result['surname']}
            Результат: {time}
            """)


def get_time_format(time):
    time = timedelta(days=0, seconds=time)
    time = str(time).split(':')
    miliseconds = '%.2f' % float(time[2])
    time = f'{time[1]}:{miliseconds}'.replace('.', ',')
    return time


def get_time_difference(start: str, finish: str):
    start = start.replace(',', ':')
    finish = finish.replace(',', ':')


    time_start = datetime.strptime(start, "%H:%M:%S:%f")
    time_finish = datetime.strptime(finish, "%H:%M:%S:%f")
    difference = time_finish - time_start
    return difference.total_seconds()


if __name__ == "__main__":
    sportsmens_json = open_json_file("competitors2.json")
    results = json_convert.get_json("results_RUN.txt")
    results_json = open_json_file("result_RUN.json")
    get_competition_results(sportsmens_json, results_json)
