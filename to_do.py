#This is a document where a ToDoist API was implemented
#However this implementation would require a UI where a user would be prompted to enter in their credentials
#We haven't learned that yet...
import requests
import os
from todoist_api_python.api import TodoistAPI

#AUTHORIZATION
AUTH_URL = "https://todoist.com/oauth/authorize"
CLIENT_KEY = "" #the unique client ID of the registered ToDoist app
SECRETSTRING = "SEO2023"
#get the client ID and set the scope of the to do list
auth_response = requests.get(AUTH_URL, {
    'client_id': CLIENT_ID,
    'scope' : {task : add , data : read , data : read_write , data : delete , project : delete},
    'state' : SECRETSTRING
})

#if the state passed back from the user authentication does not match our state here,
#the authentication process will fail
auth_response_data = auth_response.json()
auth_code = auth_response_data['code']
POST_URL = "https://todoist.com/oauth/access_token"
token_response = requests.get


#tfetching a list of the users tasks


api = TodoistAPI("8959c09a77aac1924ee195278acccdb0e929d358")
#might need to change the api in quotes to a different key
try:
    projects = api.get_projects() 
    print(projects)
except Exception as error:
    print(error)


#adding a new project
try:
    project = api.add_project(name="Shopping List")
     project_id = project['id']
    print(project)
except Exception as error:
    print(error)

#adding a new task
try:
    task = api.add_task(content="Buy Milk", project_id=project_id)
    taskID = task['id']
    print(task)
except Exception as error:
    print(error)

#updating a new task
try:
    is_success = api.update_task(task_id=taskID, due_string="tomorrow")
    print(is_success)
except Exception as error:
    print(error)

#completing a task
try:
    is_success = api.close_task(task_id=taskID)
    print(is_success)
except Exception as error:
    print(error)

#deleting a project
try:
    is_success = api.delete_project(project_id=project_id)
    print(is_success)
except Exception as error:
    print(error)