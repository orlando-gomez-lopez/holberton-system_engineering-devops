#!/usr/bin/python3
'''point 2 json'''

if __name__ == '__main__':

    import csv
    import json
    import requests
    import sys

    USER_ID = []
    USERNAME = []
    TASK_COMPLETED_STATUS = []
    TASK_TITLE = []
    USER_ID_TASK = []
    ARRAY_TASKS = []
    DATA = {}

    req_emp = requests.get('https://jsonplaceholder.typicode.com/users')
    req_tot = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = req_tot.json()
    employees = req_emp.json()
    for reg in tasks:
        TASK_TITLE.append(reg.get('title'))
        if reg.get('completed') == 1:
            TASK_COMPLETED_STATUS.append(True)
        if reg.get('completed') == 0:
            TASK_COMPLETED_STATUS.append(False)
        USER_ID_TASK.append(reg.get('userId'))
    for employee in employees:
        USER_ID.append(employee.get('id'))
        USERNAME.append(employee.get('username'))
    for j in range(0, len(USERNAME)):
        ARRAY_TASKS = []
        for i in range(0, len(TASK_COMPLETED_STATUS)):
            if USER_ID[j] == USER_ID_TASK[i]:
                t = {"username": USERNAME[j], "task": "", "completed": None}
                title = TASK_TITLE[i]
                t.update(task=title, completed=TASK_COMPLETED_STATUS[i])
                ARRAY_TASKS.append(t)
        DATA.update({USER_ID[j]: ARRAY_TASKS})
    with open('todo_all_employees.json', 'wt', encoding='utf-8') as f:
        json.dump(DATA, f)
