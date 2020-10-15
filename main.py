# input(__prompt) : prompt는 있어도 되고 없어도 됨
# banjang = input("반장의 이름을 입력하세요")
# print("우리반 반장 이름은", banjang)

# # input(__prompt)은 문자열을 입력 받기 때문에 원하는 결과가 출력되지 않음
# number1 = int(input("첫번째 숫자를 입력하세요 : "))
# number2 = int(input("두번째 숫자를 입력하세요 : "))
#
# print(number1 / number2)
# # 나눗셈
#     # 몫          : //
#     # 나머지       : %
#     # 몫 + 나머지  : /
# # 거듭제곱 : ** 밑 ** 승수

# 문자열 (내장함수)

str = "Hedgehog"
str2 = "는 좋'은 동아'리입'니다"

print(str[0:4])

# 문자열의 길이 : len(문자열 변수)
print(len(str))

# 특정 문자의 득장 횟수 : 문자열 변수.count('특정문자')
print(str.count('e'))

# 문자열을 특정 기준으로 나누기 : 문자열 변수.split()
print(str2.split("'"))

# 특정 문자 인덱스 찾기 : find('문자'), index('문자')
print(str2.find("좋"))
print(str2.index("리"))
# find와 index의 차이는 찾고자 하는 문자가 "없을 때"