# [Touraj] :: This is an exapmle how to implement factory pattern in Python

class Button(object):
   #  Abstract class for other button types!
   html = ""
   def get_html(self):
      return self.html

class Image(Button):
   #  Inheriting from Button Class
   html = "<img></img>"

class Input(Button):
   #  Inheriting from Button Class
   html = "<input></input>"

class Flash(Button):
   #  Inheriting from Button Class
   html = "<obj></obj>"

class ButtonFactory():
   #  return the desired button base on type
   def create_button(self, typ):
      targetclass = typ.capitalize()
      # for more control you can replace following line with a couple of if else statments!
      return globals()[targetclass]()

# Using the Factory for creating different buttons!
button_obj = ButtonFactory()
button = ['image', 'input', 'flash']
for b in button:
   print(button_obj.create_button(b).get_html())