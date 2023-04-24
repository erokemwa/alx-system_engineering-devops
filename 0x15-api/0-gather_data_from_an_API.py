#!/usr/bin/python3

"""
Use JSONPlaceholder API to get information about employee
"""

import requests
import sys

# check if the script is being run directly
if __name__ == '__main__':

    # get the employee ID from the command line argument
    employee_ID = int(sys.argv[1])

    # construct the URL to retrieve the employee's information
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_ID)

    # make a request to the API and convert the response to a JSON object
    response = requests.get(user_url)
    res_json = response.json()

    # extract the employee's name from the JSON object
    name = res_json.get('name')

    # construct the URL to retrieve the employee's tasks
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        employee_ID)

    # make a request to the API and convert the response to a JSON object
    todo_json = requests.get(todo_url).json()

    # initialize counters and lists
    total_tasks = 0
    num_completed_tasks = 0
    completed_tasks = []

    # loop through the tasks and count the number of completed tasks
    for task in todo_json:
        total_tasks += 1
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
            num_completed_tasks += 1

    # output the employee's name, the number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(name,
          num_completed_tasks, total_tasks))
    for item in completed_tasks:
        print("\t {}".format(item))
