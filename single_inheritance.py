class Car:
  def __init__(self):
    self.number_of_wheels = 4
  
  def get_number_of_wheels(self):
    return self.number_of_wheels 
    
class BMW(Car):
  def __init__(self, model):
      super().__init__()
      self.brand = "BMW"
      self.model = model
      
  def get_info(self):
    return f"Car brand is {self.brand}, car model is {self.model}, car has {self.number_of_wheels} wheels"
  

obj = BMW("A7")
print(obj.get_info())