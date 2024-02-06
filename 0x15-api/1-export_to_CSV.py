#!/usr/bin/python3
'''using this REST API, for a given employee ID, returns
information about his/her TODO list progress in csv format.'''
import json
import requests
import sys


def todo_csv():
    id_ = int(sys.argv[1])
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{id_}'
    todo_url = f'{base_url}/todos?userId={id_}'
    
    user = requests.get(user_url)
    todo = requests.get(todo_url)

    userInfo = json.loads(user.text)
    todoList = json.loads(todo.text)

    name = userInfo['name']
    details = ""
    userID = userInfo['id']
    userName = userInfo['username']
    nameId = f'"{userID}", "{userName}",'
 
    count = 0
    countCheck = 0

    for property in todoList:
        count += 1

    for property in todoList:
        countCheck += 1
        taskCompStat = property['completed'] 
        taskTitle = property['title']
        
        details += f'{nameId} "{taskCompStat}", "{taskTitle}"'
        if countCheck == count:
            pass
        else:
            details = details + '\n'
    

    print(details)

if __name__ == "__main__":
    todo_csv()
