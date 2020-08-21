def spiralDiaSum(n): 
      
    if n == 1: 
        return 1
    if n == 0:
    	return 0
    return (4 * n*n - 6 * n + 6 +
               spiralDiaSum(n-2)) 
      
print("NACHIKETA MANISH BUDDHA: 17DCE004")
n = 1001; 
print(spiralDiaSum(n))