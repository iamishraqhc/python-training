class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def popCharacter(self):
        ch = self.stack.pop()
        return ch

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def dequeueCharacter(self):
        ch = self.queue.pop(0)
        return ch


s = input()
obj = Solution()
l = len(s)

for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True

for i in range (int(l/2)):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

if isPalindrome:
    print("The word, " + s + " is a palindrome.")

else:
    print("The word, " + s + " is not a palindrome.")