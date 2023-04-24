#!/usr/bin/python3
"""
Use JSONPlaceholder API to get information about employee
"""
import requests
import sys

if __name__ == '__main__':

    employee_ID = int(sys.argv[1])
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_ID)
    response = requests.get(user_url)
    res_json = response.json()
    name = res_json.get('name')
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        employee_ID)
    todo_json = requests.get(todo_url).json()
    total_tasks = 0
    num_completed_tasks = 0
    completed_tasks = []

    for task in todo_json:
        total_tasks += 1
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
            num_completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(name,
          num_completed_tasks, total_tasks))
    for item in completed_tasks:
        print("\t {}".format(item))
