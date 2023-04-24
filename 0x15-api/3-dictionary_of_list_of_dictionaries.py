#!/usr/bin/python3

"""Fetches JSON data from an API"""

import json
import requests

# Check if the current module is the main program
if __name__ == "__main__":

    # Define the user URL for the API
    user_url = "https://jsonplaceholder.typicode.com/users/"

    # Get JSON data from the API and store it in a dictionary
    user_dict = requests.get(user_url).json()

    # Define the output file name
    file_name = "todo_all_employees.json"

    # Initialize an empty dictionary
    _dict = {}

    # Iterate over each user in the dictionary
    for elem in user_dict:

        # Get the user's name and ID
        name = elem.get("username")
        user_id = str(elem.get("id"))

        # Get the user's to-do list from the API
        user_data = requests.get("{}{}/todos".format(user_url, user_id))
        user_data = user_data.json()

        # Initialize an empty list for the user's to-do items
        _dict[user_id] = []

        # Iterate over each to-do item for the user
        for item in user_data:

            # Create a dictionary for each to-do item
            inner_dict = {}

            # Add the username, task, and completion status to the dictionary
            inner_dict["username"] = name
            inner_dict["task"] = item.get("title")
            inner_dict["completed"] = item.get("completed")

            # Add the dictionary to the user's to-do list
            _dict[user_id].append(inner_dict)

    # Write the dictionary to a JSON file
    with open(file_name, 'w') as f:
        json.dump(_dict, f)
