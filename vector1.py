
from math  import sqrt


	
class Vector:
	def __init__(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z

	def abs(self):
		return abs(sqrt(self.x * 2 + self.y * 2 +self.z * 2))
		
	
	def __add__(self, V): 
  
		return Vector(self.x + V.x, self.y + V.y, self.z + V.z) 
  

	def __sub__(self, V):
  
		return Vector(self.x - V.x, self.y - V.y, self.z - V.z) 
  
    
	def dot(self, V): 
  
		return self.x * V.x + self.y * V.y + self.z * V.z 
  
	def __repr__(self): 
  
		out = repr(self.x )+ "  " + repr(self.y )+"  "+repr(self.z)
  
		#if self.y >= 0: 
			#out += " "
		#out += str(self.y) + " "
		#if self.z >= 0: 
			#out += "  "
		#out += str(self.z) + " "
  
		return out 
  
  
if __name__ == "__main__": 
  
	v0 = Vector(1, 2, 3) 
	v1 = Vector(5, 6, 7) 
	
  
    
	print("sqrt of vector1:", v0.abs()) 

	print("Addition of v0 and v1: " +repr(v0+v1)) 
  
	print("Subtraction v0 and v1: " + repr(v1 - v0)) 
  
	print("Dot Product of v0 and v1: " +str(v0.dot(v1))) 
	






