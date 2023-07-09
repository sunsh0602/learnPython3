def 더하기(a, b):
    print(f"덧셈 {a} + {b}")
    return a + b

def 빼기(a, b):
    print(f"뺄셈 {a} - {b}")
    return a - b

def 곱하기(a, b):
    print(f"곱셈 {a} * {b}")
    return a * b

def 나누기(a, b):
    print(f"나눗셈 {a} / {b}")
    return a / b

print("함수만으로 계산해봅시다")

나이 = 더하기(30, 5)
키 = 빼기(78, 4)
몸무게 = 곱하기(90, 2)
아이큐 = 나누기(100, 2)

print(f"나이: {나이}, 키: {키}, 몸무게: {몸무게}, IQ: {아이큐}")

print("추가 문제")
값 = 더하기(나이, 빼기(키, 곱하기(몸무게, 나누기(아이큐, 2))))

print("결과: ", 값, "손으로 계산할 수 있나요?")