class Father:
  father_name = "Saif Ali Khan"
    
class Mother:
  mother_name = "Kareena Kapoor"
    
class Child(Father, Mother):
  def __init__(self, name):
    self.name = name
    
  def get_parent_details(self):
    print(f"Father name is {self.father_name} and Mother name is {self.mother_name}")
    
child1 = Child("Taimur")
child1.get_parent_details()