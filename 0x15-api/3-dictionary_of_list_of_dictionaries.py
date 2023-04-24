#!/usr/bin/python3
"""
Returns to-do list information for all employees.
"""
import json
import requests

if __name__ == '__main__':
    # Define the API base URL
    base_url = "https://jsonplaceholder.typicode.com"

    # Get the list of users and todos from the API
    users = requests.get(f"{base_url}/users").json()
    todos = requests.get(f"{base_url}/todos").json()

    # Create a dictionary to store the todos for each user
    user_todos = {}
    for user in users:
        user_id = user.get('id')
        user_todos[user_id] = []
        for todo in todos:
            if user_id == todo.get('userId'):
                user_todos[user_id].append({
                    'task': todo.get('title'),
                    'completed': todo.get('completed'),
                    'username': user.get('username')
                })

    # Write the dictionary to a JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(user_todos, json_file)
