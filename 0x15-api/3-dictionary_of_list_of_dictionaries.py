#!/usr/bin/python3
""" Script uses JSON Placeholder API to fetch information about a employee """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    res = requests.get(user)
    json_o = res.json()
    d_task = {}
    for user in json_o:
        name = user.get('username')
        userId = user.get('id')
        todos = '{}todos?userId={}'.format(url, userId)
        res = requests.get(todos)
        task = res.json()
        l_task = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            l_task.append(dict_task)

        d_task[str(userId)] = l_task
        filename = 'todo_all_employees.json'
        with open(filename, mode='w') as f:
            json.dump(d_task, f)
