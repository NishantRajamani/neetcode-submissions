class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_dict = {n: s.count(n) for n in s}
            t_dict = {n: t.count(n) for n in s}
            print(s_dict, t_dict)
            return s_dict == t_dict

        