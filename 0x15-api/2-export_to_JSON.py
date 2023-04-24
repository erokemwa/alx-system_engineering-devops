#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
"""

import json
import requests
from sys import argv

if __name__ == '__main__':

    # Get the user ID from the command line argument
    id = argv[1]

    # Get the user information from the API and extract the username
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        id)).json()
    username = user.get('username')

    # Get the todo list for the user from the API
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id)).json()

    # Set the filename for the JSON file
    json_filename = id + ".json"

    # Create a list of tasks for the user
    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)

    # Create a dictionary with the user ID
    dictionary = {}
    dictionary[id] = tasks

    # Write the dictionary to a JSON file
    with open(json_filename, "w") as json_file:
        json.dump(dictionary, json_file)
