from sys import argv

스크립트, 입력_파일 = argv

def 모두_출력(파일):
    print(파일.read())

def 되감기(파일):
    파일.seek(0)

def 한_줄_출력(줄_수, 파일):
    print(줄_수, 파일.readline())

현재_파일 = open(입력_파일, encoding='utf-8')

print("파일 전체를 출력해봅시다.\n")

모두_출력(현재_파일)

print("이번에는 테이프처럼 되감아봅시다.")

되감기(현재_파일)

print("세 줄을 출력해봅시다.")

현재_줄_수 = 1
한_줄_출력(현재_줄_수, 현재_파일)

현재_줄_수 = 현재_줄수 + 1
한_줄_출력(현재_줄_수, 현재_파일)

현재_줄_수 = 현재_줄_수 + 1
한_줄_출력(현재_줄_수, 현재_파일)