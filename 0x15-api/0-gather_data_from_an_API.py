#!/usr/bin/python3
'''point 0 jsonplaceholder website'''

if __name__ == '__main__':

    import json
    import requests
    import sys

    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    EMPLOYEE_NAME = ""
    TASK_TITLE = []

    req_emp = requests.get('https://jsonplaceholder.typicode.com/users')
    req_tot = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = req_tot.json()
    employees = req_emp.json()
    for reg in tasks:
        if reg.get('userId') == eval(sys.argv[1]):
            if reg.get('completed') == 1:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(reg.get('title'))
            TOTAL_NUMBER_OF_TASKS += 1
    for employee in employees:
        if employee.get('id') == eval(sys.argv[1]):
            EMPLOYEE_NAME = employee.get('name')
    print("Employee {} is done with tasks({}/{}):\
".format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))
