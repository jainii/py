# NAME : YASH JAIN
# ID: 17DCE014


import numpy as np 
m , n = 4, 4		
def row_sum(arr) : 
	sum = 0
	print("\nFinding Sum of each row:\n") 
	for i in range(4) : 
		for j in range(4) : 		 
			sum += arr[i][j]
		# Print the row sum 
		print("Sum of the row",i,"=",sum) 	
		sum = 0
def column_sum(arr) : 
	sum = 0
	print("\nFinding Sum of each column:\n") 
	for i in range(4) : 
		for j in range(4) : 		 
			sum += arr[j][i] 		
		print("Sum of the column",i,"=",sum) 		 
		sum = 0	 
if __name__ == "__main__" : 
	arr = np.zeros((4, 4)) 
	x = 1	
	for i in range(m) : 
		for j in range(n) : 
			arr[i][j] = x 
			x += 1		 
	row_sum(arr)  
	column_sum(arr)