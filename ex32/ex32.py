숫자들 = [1, 2, 3, 4, 5]
과일들 = ['사과', '귤', '배', '살구']
잔돈들 = [1, '십원', 2, '백원', 3, '오백원']

#첫 번째 for 순환문은 list를 따라 돕니다.

for 숫자 in 숫자들:
    print(f"이 수는 {숫자}")

for i in 잔돈들:
    print(f"받은 잔돈 {i}")

원소들 = []

for i in range(0, 6):
    print(f"list에 {i} 숫자를 더합니다.")
    #append는 list가 알아듣는 함수입니다.
    원소들.append(i)

# 이것도 출력할 수 있습니다.
for i in 원소들:
    print(f"원소는 {i}")
