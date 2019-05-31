n = int(input())
phonebook={}

for i in range(0, n):
    name, id = input().split()
    phonebook[name] = id

while(1):
    temp = ''
    name = input()
    if name == temp:
        break

    if name in phonebook:
        print(name + "=" + phonebook[name])
    else:
        print("Not Found")

