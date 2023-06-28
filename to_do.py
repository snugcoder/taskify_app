class ToDo:
#This is a document where a ToDoist API was implemented
#However this implementation would require a UI where a user would be prompted to enter in their credentials
#We haven't learned that yet...
import requests
import json
import pdb
import os
#get request
url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.posts(url)

print('Response status code:', response.status_code)
print('Response content:', response.content)
print('Response JSON data:', response.json)

 # Post request , ask cassidy about ID and USERID
 data = {'title': 'delectus aut autem', 'body':'', 'userId': }

response = requests.post(api,data)
#where we send the HTTP POST request to the api using request.post - the parameters contain the api and payload (data) to be sent in the request body

print(response.status_code)
 #prints the status code of the HTTP response that the server recieved 

print(response.json())
 #prints the response as a json
 #note: response.json()- converts the response body into a dictionary***




def get_projects():
    #get information from the api

#updating a new task
def update_task():
   #just update the infromation using SQL
   #this is important because we will mostly be updating information in the api

#completing a task
def complete_task():
    #just set task in database to complete

#deleting a project
def del_item():
    