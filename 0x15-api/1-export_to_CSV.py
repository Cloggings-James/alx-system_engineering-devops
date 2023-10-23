#!/usr/bin/python3
import requests
import csv
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
def export_to_csv(employee_id, user_data, tasks):
    if user_data and tasks:
        filename = f"{employee_id}.csv"
        with open(filename, mode='w', newline='') as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in tasks:
                writer.writerow([employee_id, user_data['name'], task['completed'], task['title']])
        print(f"Data has been exported to {filename}")
    else:
        print("Employee not found")

if __name__ == "__main__":
    if len(argv) == 2 and argv[1].isdigit():
        employee_id = int(argv[1])
        user_data, tasks = fetch_employee_data(employee_id)
        export_to_csv(employee_id, user_data, tasks)
    else:
        print("Usage: 1-export_to_CSV.py <employee_id>")

