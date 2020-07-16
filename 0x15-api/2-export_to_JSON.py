#!/usr/bin/python3
'''point 2 json'''

if __name__ == '__main__':

    import csv
    import json
    import requests
    import sys

    USER_ID = ""
    USERNAME = ""
    TASK_COMPLETED_STATUS = []
    TASK_TITLE = []
    ARRAY_TASKS = []
    DATA = {}

    req_emp = requests.get('https://jsonplaceholder.typicode.com/users')
    req_tot = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = req_tot.json()
    employees = req_emp.json()
    for reg in tasks:
        if reg.get('userId') == eval(sys.argv[1]):
            TASK_TITLE.append(reg.get('title'))
            if reg.get('completed') == 1:
                TASK_COMPLETED_STATUS.append(True)
            if reg.get('completed') == 0:
                TASK_COMPLETED_STATUS.append(False)
    for employee in employees:
        if employee.get('id') == eval(sys.argv[1]):
            USER_ID = employee.get('id')
            USERNAME = employee.get('username')
    for i in range(0, len(TASK_COMPLETED_STATUS)):
        text = {"task": "", "completed": None, "username": USERNAME}
        text.update(task=TASK_TITLE[i], completed=TASK_COMPLETED_STATUS[i])
        ARRAY_TASKS.append(text)
    DATA.update({USER_ID: ARRAY_TASKS})
    with open('{}.json'.format(USER_ID), 'wt', encoding='utf-8') as f:
        json.dump(DATA, f)
