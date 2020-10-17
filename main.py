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

# 리스트 (내장함수)
li = [3,1,'배가',4,'고파요',5,1,2,2,1]
print(li[0:3])

# 리스트의 길이를 구하는 함수 : len()
print("리스트의 길이 : ")
print(len(li))

# 리스트 원소 오름차순 정렬해주는 함수 : .sort()
# sort()는 정렬된 리스트를 반환하지 않음
li_2 = [3,1,4,5,2]
print("정렬하기 전")
print(li_2)
print("정렬하고 난 후")
li_2.sort()
print(li_2)

# 리스트 내의 특정 원소 인덱스 반환해주는 함수 .index()
print("반환 된 인덱스")
print(li.index("배가"))

# 리스트 내의 특정 원소의 갯수 세기 : .count(요소)
print("2가 몇번 등장?")
print(li.count(2))

#딕셔너리 (내장함수)
pairs = {'잔나비' : '뜨거운 여름밤', '소히' : '산책', '홍크':'어쩌면'}

# 하나의 키 -Value 쌍을 추가하는 방법
# 딕셔너리형 변수 [키] = value
print(pairs)
pairs['스탠딩에그'] = '휴식'
print(pairs)
# 특정 Key - Value 삭제하는 방법 : del 함수
# del 변수[key]
del pairs['스탠딩에그']
print(pairs)

# key로 value얻기 : 변수.get(키)

print(pairs.get('잔나비'))

# 제어문 - 분기문
# score = int(input("점수 입력 : "))
# if(score>=85):
#     print("PASS")
# else :
#     print("FAIL")

# 예제 - 2

activity = input("너 동아리 뭐해? : ")
if(activity == "멋쟁이사자처럼"):
    print("어 너도 멋사야?")
else :
    print("..그래..")