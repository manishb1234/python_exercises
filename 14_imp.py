#Remove duplicates
#imp question

#input - a = ["1", 1, "1", 2]
#output - ['1',2,1]

a = ["1", 1, "1", 2]

#match each element with each
b=[]
#see chatgpt for this, it doesnt compare same item,
# only earlier items


count=0
for i in range(len(a)):
    duplicate=False
    for j in range(i):
        count = count + 1
        if a[i] == a[j]:
            duplicate=True
            break
    if not duplicate:
        b.append(a[i])
print(b, count)

#convert using a set function, set has
#no duplicates
b=list(set(a))
print(b)

#using dict.fromkeys() as keys unique
nums = [1, 2, 2, 3, 1]
unique = list(dict.fromkeys(nums))
print(unique)





