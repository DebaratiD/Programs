# This is to print duplicates in a list
l = []
print("Enter an array of elements: ")
z = input()
while z:
  l.append(z)
  z = input()

d=[]
for i in l:
  if l.count(i)>1 and i not in d:
    d.append(i)

print(d)
