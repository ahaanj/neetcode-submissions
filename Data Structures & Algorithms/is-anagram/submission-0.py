class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if the lengths are already uneven then not possible so this is the guard
            return False
        
        countS = {} #make new dic
        countT = {} # make new dic
        for char in s:
            #Access the character in the dictioary to see how many times its present
            countS[char] = countS.get(char, 0) + 1
        
        for char in t:
            #Access the character in the dictioary to see how many times its present
            countT[char] = countT.get(char, 0) + 1 
        
        return countT == countS