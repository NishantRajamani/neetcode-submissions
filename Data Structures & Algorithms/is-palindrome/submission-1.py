import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = -1
        if s == '':
            return True
        for i in s:
            if i.isalpha() or i.isnumeric():
                continue
            else:
                s=s.replace(i,'')
        for i in range(math.ceil(len(s)/2)):
            print(i)
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True