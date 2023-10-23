#!/usr/bin/python3
import json
import requests

def fetch_employee_data(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    if not user_data:
        return None

    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    employee_tasks = []
    for task in tasks_data:
        task_dict = {
            "username": user_data.get("username"),
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        employee_tasks.append(task_dict)

    return employee_id, employee_tasks

def export_all_employees_to_json():
    all_employee_data = {}

    for employee_id in range(1, 11):
        data = fetch_employee_data(employee_id)
        if data:
            employee_id, employee_tasks = data
            all_employee_data[str(employee_id)] = employee_tasks

    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(all_employee_data, json_file)

    print(f"Data for all employees has been exported to {filename}")

if __name__ == "__main__":
    export_all_employees_to_json()

