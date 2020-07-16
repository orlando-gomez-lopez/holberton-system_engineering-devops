#!/usr/bin/python3
'''point 1 csv'''

if __name__ == '__main__':

    import csv
    import json
    import requests
    import sys

    USER_ID = ""
    USERNAME = ""
    TASK_COMPLETED_STATUS = []
    TASK_TITLE = []

    req_emp = requests.get('https://jsonplaceholder.typicode.com/users')
    req_tot = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = req_tot.json()
    employees = req_emp.json()
    for reg in tasks:
        if reg.get('userId') == eval(sys.argv[1]):
            TASK_TITLE.append(reg.get('title'))
            if reg.get('completed') == 1:
                TASK_COMPLETED_STATUS.append("True")
            if reg.get('completed') == 0:
                TASK_COMPLETED_STATUS.append("False")
    for employee in employees:
        if employee.get('id') == eval(sys.argv[1]):
            USER_ID = employee.get('id')
            USERNAME = employee.get('username')
    with open('{}.csv'.format(USER_ID), mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"\
', quoting=csv.QUOTE_ALL)
        for i in range(0, len(TASK_COMPLETED_STATUS)):
            employee_writer.writerow(["{}".format(USER_ID), "{}".format(USERNAME), "{}\
".format(TASK_COMPLETED_STATUS[i]), "{}".format(TASK_TITLE[i])])
