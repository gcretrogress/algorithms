from typing import List
def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)

    # Initialize left_products and right products arrays
    left_products = [1] * n
    right_products = [1] * n

    # Compute left_products
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    
    # Compute right_products
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    
    # Compute answer
    answer = [left_products[i] * right_products[i] for i in range(n)]

    # print the constructed prod array 
    for i in range(n): 
        print(answer[i], end=' ')

    return answer


# Driver code 
arr = [10, 3, 5, 6, 2] 
n = len(arr) 
print("The product array is:") 
var: List[int]
var = productExceptSelf(n, arr) 
print ('\n')