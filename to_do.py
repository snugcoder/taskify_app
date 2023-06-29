import requests
import json
import pdb
import os
class ToDo:
#This is a document where a ToDoist API was implemented
#However this implementation would require a UI where a user would be prompted to enter in their credentials
#We haven't learned that yet..

    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url)
        self.jsonData = self.response.json()
      
    def get_projects(self):
        #get information from the api
        #get the tasks listed under specified user
        user_id = int(input("What is your userID: "))
        #for all user ids that are same, gather all the tasks and list them
        for entry in self.jsonData:
            if entry['userId'] == user_id: print(entry)
        

    #updating a new task
    def update_task(self):
        try: 
            update_id = int(input("Which task would you like to update: ")) - 1
            update_text = input("Update Task: ")
            self.jsonData[update_id]['title'] = update_text
            print("The task was updated")
            complete_val = input("Would you like to complete this task? (y/n): ")
            print(self.jsonData[update_id])
            if complete_val == 'y':
                self.complete_task(update_id)
        except IndexError:
            print("That is out of bounds")
        except ValueError:
            print("Please input a value")
        #just update the infromation using SQL
        #this is important because we will mostly be updating information in the api
        pass #indicates that nothing is happening - will be changed later

    #completing a task
    def complete_task(self, index):
        #just set task in database to complete
        # this can only be accessed if the id is known
        update_status = input("Mark as complete? (y/n): ")
        if update_status == "y":
        #if not self.jsonData[index]['completed']: 
            self.jsonData[index]['completed'] = True
        elif update_status not in ['y', 'n']:
            print("Invalid input. :C")
            
    #deleting a project 
    def del_item(self):
        try:
            del_id = int(input("Which task do you want to delete: ")) - 1
            print(self.jsonData.pop(del_id))
        except ValueError:
            print("Please input a value.")
        except IndexError:
            print("That is out of bounds.")

    #helper function for testing status codes    
    def help_test(self):
        print('Response status code:', self.response.status_code)
        #print ('Response data: ', self.jsonData)
########## testing code ############

#we use cases for the demo, because we want our project to continue based on user input

def run_to_do():
    print("Welcome!")
    done = False
    
    while not done:
        print("List Tasks - (1)")
        print("Update Task - (2)")
        print("Set task to complete - (3)")
        print("Delete a task - (4)")
        print("Exit - (5) \n")
        try:
            userInput = int(input("What would you like to do: "))
            match userInput:
                case 1:
                    to_do_list_test.get_projects()
                case 2:
                    to_do_list_test.update_task()
                case 3:
                    fin_id = int(input("What task would you like to complete: ")) - 1
                    to_do_list_test.complete_task(fin_id)
                    print(to_do_list_test.jsonData[fin_id])
                case 4:
                    to_do_list_test.del_item()
                case 5:
                    print("Exiting...")
                    done = True
                case _:
                    print("Likely an invalid input. Try again.")
        except ValueError:
            print("\nPlease enter a number.")
        except IndexError:
            print("\nThat is out of bounds.")


#making a ToDo Object -> Testing code
to_do_list_test = ToDo('https://jsonplaceholder.typicode.com/todos')
run_to_do()
#to_do_list_test.help_test()
#to_do_list_test.get_projects()
# to_do_list_test.del_item()
#to_do_list_test.update_task()
#print(to_do_list_test.jsonData) #print data




'''
#get request
url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)

print('Response status code:', response.status_code)
print('Response content:', response.content)
#print('Response JSON data:', response.json)

# Post request , ask cassidy about ID and USERID
# data = {'title': 'delectus aut autem', 'body':'', 'userId': }

jsonData = response.json()
#where we send the HTTP POST request to the api using request.post - the parameters contain the api and payload (data) to be sent in the request body

print(response.status_code)
#prints the status code of the HTTP response that the server recieved 

#print(response.json())
#prints the response as a json
#note: response.json()- converts the response body into a dictionary***
'''