import os

# 현재 작업위치
print(os.getcwd())

# 현재 작업 위치의 파일 보기
print(os.listdir())
list1 = os.listdir()

#7-2 (추가) 해당 위치의 파일이 몇개 있고, 그리고 원하는 파일이 있는지 확인 유무.
print(f'{len(  os.listdir())  }개의 파일 또는 폴더가 있습니다.')
print('{}개의 파일 또는 폴더가 있습니다.'.format(     len(  os.listdir()  )     ))

def check(file):
    if file in os.listdir():
        print(f'{find}를 찾았습니다.')
    else:
        print("찾으시는 파일이 없습니다.")
        print(os.listdir())

# find = input('찾으려는 파일 명: ')
# check(find)

# 7-3 (추가) .py파일이 몇개인지
def check_py(list_dir):
    py_cnt = 0
    for file in list_dir:
        if ".py" in file:
            py_cnt = py_cnt + 1
    return py_cnt

print(f'파이선의 파일은 {check_py(os.listdir())}개 있습니다.')

# 다른 학우들 코드
# py_cnt = 0
# for file in list_dir:
#     if(files[-3:] == ".py"):
#         py_cnt += 1

