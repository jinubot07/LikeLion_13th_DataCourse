# abs 함수 : 절대값구하기
print(abs(3))
print(abs(-13))

# 6-2 실습 - 두 개의 값을 입력받아서, 값의 차이의 절대값를 구하는 프로그램을 만들어보자.
def gap_abs(num1,num2):
    return abs(num1-num2)

a, b = map(int, input("2개 숫자 입력(공백 구분): ").split())
print(gap_abs(a,b))