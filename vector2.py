
from math  import sqrt


	
class Vector:
	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z

	def abs(self):
		return abs(sqrt(self.x * 2 + self.y * 2 +self.z * 2))
		
	
	def __add__(self, other): 
  
		return f"the sum of v0 and v1 is:{self.x + other.x} {self.y + other.y} {self.z + other.z}"
  

	def __sub__(self, other):
  
		return f"the differnce of v0 and v1 is:{self.x - other.x} {self.y - other.y} {self.z - other.z}"
  
    
	def dot(self, other): 
  
		return f"the dot product of vo and v1 is:{self.x * other.x + self.y * other.y + self.z * other.z}"
  
	#



v0 = Vector(1, 2, 3) 
v1 = Vector(5, 6, 7) 



print("sqrt of vector1:", v0.abs()) 

print(v0+ v1)

print(v1 - v0)

print(v0.dot(v1))







