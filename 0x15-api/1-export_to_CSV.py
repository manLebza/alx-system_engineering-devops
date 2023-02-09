#!/usr/bin/python3
""" Script uses JSON placeholder API  to get Employee information """
import CSV
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    userId = sys.argv[1]
    user = '{}users/{}'.format(url, userId)
    res = requests.get(user)
    json_o = res.json()
    name = json_o.get('username')

    todos = '{}todos?userId={}'.format(url, userId)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        l_task.append([userId, name, task.get('completed'),
                      task.get('title')])
        filename = '{}.csv'.format(userId)
        with open(filename, mode='w') as employee_file:
            employee_writer = csv.writer(employee_file, delimiter=',',
                                         quotechar='"', quoting=csv.QUOTE_ALL)

            for task in l_task:
                employee_writer.writerow(task)
