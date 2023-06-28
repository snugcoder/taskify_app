#This is a document where a ToDoist API was implemented
#However this implementation would require a UI where a user would be prompted to enter in their credentials
#We haven't learned that yet...
import requests
import json
import pdb
import os
from todoist_api_python.api import TodoistAPI

#AUTHORIZATION
#the curl code allows a visual of what users should be getting redirected to 
#curl -v -X POST https://todoist.com/oauth/authorize?client_id=b065b475909a4866adc110b57d6cf5b6&scope=data:read,data:delete&state=secretstring
CURL_URL = "https://todoist.com/oauth/authorize?client_id=b065b475909a4866adc110b57d6cf5b6&scope=data:read,data:delete&state=secretstring"
AUTH_URL = "https://todoist.com/oauth/authorize"
CLIENT_ID = "b065b475909a4866adc110b57d6cf5b6" #the unique client ID of the registered ToDoist app
SECRETSTRING = "SEO2023"
#get the client ID and set the scope of the to do list
auth_response = requests.post(AUTH_URL, {
'client_id' : CLIENT_ID,
'state' : SECRETSTRING,
'scope' : {"task" : "add" , "data" : "read" , "data" : "read_write" , "data" : "delete" , "project" : "delete"} 
})

print(auth_response)
print(auth_response.status_code)

    
#Formating with JSON 
get_check = requests.get(CURL_URL).json()
data = auth_response.json()
'''
auth_code = auth_response_data['code']
POST_URL = "https://todoist.com/oauth/access_token"
token_response = requests.get
'''

#tfetching a list of the users tasks


api = TodoistAPI("8959c09a77aac1924ee195278acccdb0e929d358")

def get_projects(api):
    #might need to change the api in quotes to a different key
    try:
        projects = api.get_projects() 
        print(projects)
    except Exception as error:
        print(error)


#adding a new project
def make_new_projects(api):
    try:
        project = api.add_project(name="Shopping List")
        project_id = project['id']
        print(project)
    except Exception as error:
        print(error)

#adding a new task
def new_task(api):
    try:
        task = api.add_task(content="Buy Milk", project_id=project_id)
        taskID = task['id']
        print(task)
    except Exception as error:
        print(error)

#updating a new task
def update_task(api):
    try:
        is_success = api.update_task(task_id=taskID, due_string="tomorrow")
        print(is_success)
    except Exception as error:
        print(error)

#completing a task
def complete_task(api):
    try:
        is_success = api.close_task(task_id=taskID)
        print(is_success)
    except Exception as error:
        print(error)

#deleting a project
def del_project(api):
    try:
        is_success = api.delete_project(project_id=project_id)
        print(is_success)
    except Exception as error:
        print(error)