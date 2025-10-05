class PersonalAssistant:
 
  def __init__(self, todos):
    # self.contacts = {'Ann': 'Marketing Coordinator', 'Chelsea': 'Software Developer', 'Nichole': 'Sales Representative', 'Max': 'Technical Writer'}

    self.todos = todos

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todos(self):
    return self.todos
  
  def get_birthday(self, name):
    if name == "Mark":
      print (name + "'s Birthday is 05/05/1995!")
    elif name == "Melissa":
      print (name + "'s Birthday is 11/02/2002!")
    elif name == "Emily":
      print (name + "'s Birthday is 02/05/2005!")
    else:
      print ("Can't find a Birthday for " + name + ".")


  # Complete the get_contact function code
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return name + " is not in the list"


# Code to test output of the class
# assistant = PersonalAssistant()
# Change name to one from your contacts
# print(assistant.get_contact("Mark"))

# assistant.add_todo("Pick up groceries")
# print(assistant.get_todos())

# print(assistant.get_birthday("Emily"))