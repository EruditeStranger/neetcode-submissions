class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list()
        tlist = list()
        for a in s:
            slist.append(a)
        for a in t:
            tlist.append(a)
        if sorted(slist) == sorted(tlist):
            return True
        else:
            return False