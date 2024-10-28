
# python 1 print and variable

# 변수 선언과 출력하기

name = "Alice"
age = 25
print(f"Hello, {name}! you are {age} years old.")

# 조건문
# 짝수 , 홀수
number = int(input("Enter a number : "))
if number % 2 == 0 :
    print("Even number")
else:
    print("Odd number")

# 반복문
# for문을 이용한 구구단 출력

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}X{j} = {i*j}")
    print()

# while
# while문을 이용한 숫자 맞추기 게임
import random

number_to_guess = random.randint(1,10)
guess = None

while guess != number_to_guess:
    guess = int(input("Guess the number (1-10) :"))
    if guess > number_to_guess:
        print("Too low")
    else:
        print("Too High")

print(f"You guessed it ! {guess}")

# list dictionary
# 리스트의 요소를 하니씩 출력
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 딕셔너리를 이용한 학생 점수 관리
score = {"Alice" : 85, "Bob" : 90, "Charlie" : 78}
for student, score in score.items():
    print(f"name  : {student} Score : {score}")

#함수

#두 수의 합을 계산하는 함수
def add_number(a, b):
    return a+b

result = add_number(3,5)
print("Sum : ",result)


# Class
# 간단한 Dog 클래스 정의
class Dog:

    def __init__(self, name, age): # 초기화 메서드
        self.name = name           # 인스턴스 변수
        self.age = age             # 인스턴스 변수

    def bark(self):                # 메서드
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy",3) # init을 통해 세팅하고
my_dog.bark() # bark를 통해 print 호출

class GuardDog(Dog):  # Dog 클래스를 상속받음
    def guard(self):
        print(f"{self.name} is guarding the house!")

# GuardDog 인스턴스 생성
guard_dog = GuardDog("Rex", 5)
guard_dog.bark()  # Dog 클래스의 메서드 사용, 출력: Rex says Woof!
guard_dog.guard()  # GuardDog의 메서드 사용, 출력: Rex is guarding the house!

"""
클래스는 객체를 만들기 위한 설계도 역할을 합니다.
인스턴스는 클래스를 기반으로 생성된 개별 객체입니다.
메서드는 클래스 내부에 정의된 함수로, 인스턴스의 동작을 정의합니다.
상속을 통해 클래스의 재사용성과 확장성을 높일 수 있습니다.
"""



#파일 읽기 쓰기

# 텍스트 파일에 쓰기
with open("sample.txt","w") as file:
    file.write("Hello, Python !\nThis is a test file")

# 텍스트 파일 읽기
with open("sample.txt","r") as file:
    content = file.read()
    print(content)


#예외처리
#예외를 이용한 안전한 숫자 입력받기
try:
    number = int(input("Enter an integer :"))
    print("Your Number : ",number)
except ValueError:
    print("That's not a valid Integer")

