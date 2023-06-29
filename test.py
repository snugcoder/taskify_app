#Creating Tests using .asserts from python
import http.client
import unittest
from to_do import ToDo
#import the to_do.python
#should these tests be booleans? --if an error is caught then the test fails
#how should we test?: test with mock update data to see if api works
mock_todo = ToDO('https://jsonplaceholder.typicode.com/todos')

class TestToDo(unittest.TestCase):
    def test_get_projects(self, get_projects):
        #tests if the projects can be taken from to-do-ist
        #if we can call the list of projects then we are good (w/ json)
        conn = http.client.HTTPSConnection("https://jsonplaceholder.typicode.com/todos")
        conn.request("GET", "/")
        r1 = conn.getresponse()
        if r1.status == 200:
            print('OK')
        else: print("error")
        c = app.test_client()
        rv = c.get("https://jsonplaceholder.typicode.com/todos", query_string={'userId' : 1})
        assert json.loads(rv.get_data()) == expected_data
    
    def test_update(self):
        self.assertEquals
    def test_complete_task(self):
        #tests if a task is marked as complete
        self.assertTrue(self.complete_task(2), "The task was completed")

    def test_del(self):
        self.assertTrue(self.del_item(), "The task was deleted")