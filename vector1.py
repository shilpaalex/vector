
from math  import sqrt


	
class Vector:
	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z

	def abs(self):
		return abs(sqrt(self.x * 2 + self.y * 2 +self.z * 2))
		
	
	def __add__(self, other): 
  
		return Vector(self.x + other.x, self.y + other.y, self.z + other.z) 
  

	def __sub__(self, other):
  
		return Vector(self.x - other.x, self.y - other.y, self.z - other.z) 
  
    
	def dot(self, other): 
  
		return self.x * other.x + self.y * other.y+ self.z * other.z 
  
	def __repr__(self): 
  
		out = str(self.x )+"  " +str(self.y )+"  "+str(self.z)
  
		return out 
  
  



v0 = Vector(1, 2, 3) 
v1 = Vector(5, 6, 7) 



print("sqrt of vector1:", v0.abs()) 

print("Addition of v0 and v1: " +repr(v0+ v1)) 

print("Subtraction v0 and v1: " + repr(v1 - v0)) 

print("Dot Product of v0 and v1: " +str(v0.dot(v1))) 







