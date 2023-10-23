#!/usr/bin/python3
import requests
import json
from sys import argv
def fetch_employee_data(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        tasks_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        tasks_response = requests.get(tasks_url)
        tasks = tasks_response.json()
        return data, tasks
    else:
        return None, None
def export_to_json(employee_id, user_data, tasks):
    if user_data and tasks:
        data_to_export = {str(employee_id): [{"task": task['title'], "completed": task['completed'], "username": user_data['name']} for task in tasks]}
        filename = f"{employee_id}.json"
        with open(filename, 'w') as json_file:
            json.dump(data_to_export, json_file)
        print(f"Data has been exported to {filename}")
    else:
        print("Employee not found")

if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit():
        employee_id = int(argv[1])
        user_data, tasks = fetch_employee_data(employee_id)
        export_to_json(employee_id, user_data, tasks)
    else:
        print("Usage: 2-export_to_JSON.py <employee_id>")

