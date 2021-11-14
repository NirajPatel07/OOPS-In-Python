class Grandfather:
  grandfather_name = "Harivansh Rai Bachchan"
  
class Father(Grandfather):
  father_name = "Amitabh Bachchan"
  
class Child(Father):
  def __init__(self, name):
    self.name = name
    
  def get_parents_details(self):
    print(f"Grandfather name is {self.grandfather_name} and Father name is {self.father_name}")
    
child1 = Child("Abhishek Bachchan")
child1.get_parents_details()