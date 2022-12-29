'''
    1. 상속(inheritance)
       1) class 자식 클래스 이름(부모 클래스 이름)
            pass
       2) super()
        - 부모 클래스의 속성 및 메서드를 가져와야 할 때 사용
            └> super.init()
                - 부모 클래스에서 정의되어 있던 생성자 사용

'''
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_human(self):
        print("-=-=-=-=-=-=-=-=-개인 정보-=-=-=-=-=-=-=-=-")
        print(f"이름 : {self.name}")
        print(f"나이 : {self.age}")


class Teacher(Human):
    def __init__(self, name, age, teacher_id, subject, salary):
        super().__init__(name, age)
        self.teacher_id = teacher_id
        self.subject = subject
        self.salary = salary

    def show_teacher(self):
        print("=================교사 정보=================")
        print(f"교사 no : {self.teacher_id}")
        print(f"담당 과목 : {self.subject}")
        print(f"월급 : {self.salary}")

class Student(Human):
    def __init__(self, name, age, student_id, grade, score):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade
        self.score = score

    def show_student(self):
        print("*****************학생 정보*****************")
        print(f"학생 no : {self.student_id}")
        print(f"학년 : {self.grade}")
        print(f"학점 : {self.score}")

teachar1 = Teacher("박진주", 25, 1, '물리', 210)
teachar1.show_human()
teachar1.show_teacher()


student1 = Student('박나은', 23, '0029392', 2, 3.3)
student1.show_human()
student1.show_student()
