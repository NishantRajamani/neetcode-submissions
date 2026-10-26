class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for i in s:
            if i.isalpha() or i.isnumeric():
                continue
            else:
                s=s.replace(i,'')
        print(s)
        return s == s[::-1]