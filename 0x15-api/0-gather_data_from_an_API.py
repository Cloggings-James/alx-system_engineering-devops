#!/usr/bin/python3
import requests
from sys import argv
def fetch_employee_data(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        tasks_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        tasks_response = requests.get(tasks_url)
        tasks = tasks_response.json()
        completed_tasks = [task for task in tasks if task['completed']]
        total_tasks = len(tasks)

        print(f"Employee {data['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print("Employee not found")

if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit():
        employee_id = int(argv[1])
        fetch_employee_data(employee_id)
    else:
        print("Usage: 0-gather_data_from_an_API.py <employee_id>")

