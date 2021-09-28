sentence = input("문장입력 : ")
alpha_cnt = 0
space_cnt = 0

sentence.append(" ")  # 여기서 에러남!
print(sentence, type(sentence))

check = []              # "알파벳 하나" + " "(공백하나) 를 하나의 영단어로 카운트하기
for i in range(ord('a'),ord('z')):
    check.append(chr(i)+" ")
print(check)

# for i in range(space_cnt):
#     if letter in str1:
#     # if letter.isalpha():              # 한글도 카운트 하는 예외 발생
#     #     alpha_cnt += 1
#     if ord('a') <= ord(letter) <= ord('z') or ord('A') <= ord(letter) <= ord('Z') :
#         alpha_cnt = alpha_cnt + 1
#     elif letter.isnumeric():
#         num_cnt += 1
#     elif letter == ' ':
#         space_cnt += 1
