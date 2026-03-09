'''
You are given an array of characters which represents a string s. Write a function which reverses a string.
You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:

Input: s = ["n","e","e","t"]
Output: ["t","e","e","n"]

Example 2:

Input: s = ["r","a","c","e","c","a","r"]
Output: ["r","a","c","e","c","a","r"]

'''

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) !=0:
            l = 0
            r = len(s)-1
            while l<r:
                temp = s[r]
                s[r] = s[l]
                s[l] = temp
                l+=1
                r-=1
        return s

if __name__ == "__main__":
    myInstance = Solution()
    print(myInstance.reverseString(["b","o","o","k"]))
    print(myInstance.reverseString(["p","l","a","c","e"]))