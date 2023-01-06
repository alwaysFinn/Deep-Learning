'''
    1. 클래스는 딥러닝 프로그램을 작성할 때 자주 사용됨

    2. 설명
        1) self
            - 인스턴스(instance) 자기 자신을 의미함
        2) init() 함수
            - 생성자의 의미
            - self.age  현재 인스턴스의 age 변수

    3. 변수 구분
        1) 인스턴스 변수 : 구체적인 하나의 인스턴스에서 사용되는 변수
        2) 클래스 변수 : 해당 클래스에서 전체적으로 공유되는 변수
                      즉, 모든 인스턴스끼리 공유되는 정보


- self : 자기 자신을 가리킴
- __init__은 생성자의 의미
'''
class Human:
    def __init__(self):
        self.age = 0

    def old(self):
        self.age += 1

# 인스턴스 생성
human1 = Human()
human2 = Human()

for i in range(10):
    human1.old()

print(human1.age)

for i in range(20):
    human2.old()

print(human2.age)
print()

class Student:
    def __init__(self, id, name, age, gender, department):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department

    def show(self):
        print('=========학생 정보 조회=========')
        print(f"학번 : {self.id}")
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")
        print(f"성별 : {self.gender}")
        print(f"학과 : {self.department}")

    def add_age(self, offset):
        self.age += offset

student1 = Student("164803", '박을수', 26, '남', '물리학')
student2 = Student('161243', '박수지', 26, '여', '패션디자인학')
student3 = Student('169332', '윤지선', 26, '여', '경영학')

student1.show()
student2.show()
student3.show()

print()
print('              2년 뒤,,,           ')
print()

student1.add_age(2)
student1.show()

print()
print('              시간이 흘러 취업을 한 을수, 업무를 한다             ')
print()

class Client:
    client_cnt = 0

    def __init__(self, id, name, age, gender, point):
        self.id = id
        self.name= name
        self.age = age
        self.gender = gender
        self.point = point
        Client.client_cnt += 1

    def show(self):
        print("=============고객 정보 조회=============")
        print(f"고객 번호 : {self.id}")
        print(f"고객 성명 : {self.name}")
        print(f"고객 나이 : {self.age}")
        print(f"고객 성별 : {self.gender}")
        print(f"고객 포인트 : {self.point}")
        print(f"현재 총 고객 수 : {self.client_cnt}")


client1 = Client("1421", "윤지선", 29, "여자", "210000000")
client1.show()
client2 = Client("2321412", "정다은", 27, "여자", "55200")
client2.show()
client3 = Client("743324", "민두창", 54, "남자", "9250")
client3.show()
print()
print(f"[종합] 현재 총 고객 수 : {Client.client_cnt}")


print()
print("           어라,,,?           ")
print()