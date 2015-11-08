import itertools


class Mathematics:
	def __init__(self):
		print 'using mathematics class'
		
	def permutations(self,data,value):
		#data needs to be give as a list
		permutations = list(itertools.permutations(data,value))
		return permutations
		
	def combinations(self,data,value):
		#data needs to be a list, and value is number to be taken at time
		combinations = list(itertools.combinations(data,value))
		return combinations
		
		
# Testing the Class 
if __name__ == '__main__': 
	print 'testing the class'
	#instantiate the class
	compute = Mathematics()
	data = ['python','java','node']
	value = 2
	print compute.permutations(data,value)
	print compute.combinations(data,value)