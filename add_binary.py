"""Add Binary - leetcode Solution"""

class Solution:
    # Define function addBinary to get two binary strings and return their sum
    def addBinary(self, a: str, b: str) -> str:
        # Get the sum of two binary strings
        sum = bin(int(a, 2) + int(b, 2))
        # Return the sum
        return sum[2:]


