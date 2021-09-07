# dir
# a = [1,2,3]
# print(dir(a))

# dir enumerate : 순서와 값을 동시에 뽑아줌
a = ['a','b','c','d','e']
print(enumerate(a))         # 리스트에 저장하지 않으면 보이지 않음.
print(list(enumerate(a)))

for idx, val in enumerate(a):
    print(idx, val)

# dir enumerate : 순서와 값을 동시에 뽑아줌
str1 = "Hello"
print(enumerate(str1))      # 리스트에 저장하지 않으면 보이지 않음.
print(list(enumerate(str1)))

for idx, val in enumerate(str1):
    print(idx, val)

# tuple