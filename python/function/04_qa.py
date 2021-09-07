# isalpha() :  값 중에 알파벳이냐
print( "python".isalpha() )
print( "p".isalpha() )
print( "p123".isalpha() )

#6-6 어떤 값또는 문자열을 입력받아서, 알파벳이 몇글자인지 확인해 보기
print("실습")
str1 = input("문자열 입력")
alpha_cnt = 0
num_cnt = 0
space_cnt = 0
# for i in range(len(str1)):                    # 한글도 카운트 하는 예외 발생
#     if str1[i].isalpha():
#         alpha_cnt = alpha_cnt + 1

for letter in str1:
    # if letter.isalpha():              # 한글도 카운트 하는 예외 발생
    #     alpha_cnt += 1
    if ord('a') <= ord(letter) <= ord('z') or ord('A') <= ord(letter) <= ord('Z') :
        alpha_cnt = alpha_cnt + 1
    elif letter.isnumeric():
        num_cnt += 1
    elif letter == ' ':
        space_cnt += 1

print(f"{str1} 에서 알파벳의 갯수는 {alpha_cnt}개 입니다.")
print(f"{str1} 에서 숫자의 갯수는 {num_cnt}개 입니다.")
print(f"{str1} 에서 공백의 갯수는 {space_cnt}개 입니다.")