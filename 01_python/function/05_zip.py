# 파일 2개이상 합치기
a = [1,2,3]
b = ['a','b','c']
c = [[1,2,3,4,5],['가','나','다'],'TEST']

print( zip(a,b) )           # 실제로 메모리에 저장되는 형태
print( list(zip(a,b)) )     # 사용자 눈으로 확인하기 위해 list에 담아서 출력
print( list(zip(a,b,c)) )