class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        dict1 = {}
        dict2 = {}
        for i in range(len(t)):
            elem1 = s[i]
            elem2 = t[i]
            dict1[elem1]=dict1.get(elem1,0)+1
            dict2[elem2]=dict2.get(elem2,0)+1
        
        return dict1 == dict2 

        