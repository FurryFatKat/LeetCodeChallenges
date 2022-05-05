dictionary={
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}
temp = []
s = 'MCDXLVII'
for c in s:
    temp.append(dictionary[c])
print(temp)
num = 0
for i, v in enumerate(temp):
    try:
        if v < temp[i+1]:
            num -= v
        else:
            num += v
    except:
        # pass
        num += v

print(num)
