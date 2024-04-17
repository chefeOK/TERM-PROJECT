class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = self.english_score + self.c_score + self.python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()
        self.rank = None

    def calculate_grade(self):
        average = self.average_score
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

class ScoreManager:
    def __init__(self):
        self.students = []

    def insert_student(self, student):
        self.students.append(student)

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[i]
                return True
        return False

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def sort_students_by_total_score(self):
        self.students.sort(key=lambda x: x.total_score, reverse=True)

    def count_students_above_80(self):
        count = 0
        for student in self.students:
            if student.total_score >= 80:
                count += 1
        return count

    def assign_ranks(self):
        sorted_students = sorted(self.students, key=lambda x: x.total_score, reverse=True)
        for i, student in enumerate(sorted_students):
            student.rank = i + 1

    def print_student_info(self):
        for student in self.students:
            print(f"학번: {student.student_id}, 이름: {student.name}, 영어: {student.english_score}, C언어: {student.c_score}, 파이썬: {student.python_score}, 총점: {student.total_score}, 평균: {student.average_score}, 학점: {student.grade}, 등수: {student.rank}")

# 사용 예시
score_manager = ScoreManager()

# 학생 정보 입력
for _ in range(5):
    student_id = input("학번을 입력하세요: ")
    name = input("이름을 입력하세요: ")
    english_score = int(input("영어 점수를 입력하세요: "))
    c_score = int(input("C언어 점수를 입력하세요: "))
    python_score = int(input("파이썬 점수를 입력하세요: "))
    student = Student(student_id, name, english_score, c_score, python_score)
    score_manager.insert_student(student)

# 등수 할당
score_manager.assign_ranks()

# 출력
score_manager.print_student_info()

# 80점 이상 학생 수 출력
print("80점 이상 학생 수:", score_manager.count_students_above_80())

# 특정 학생 삭제
delete_id = input("삭제할 학생의 학번을 입력하세요: ")
if score_manager.delete_student(delete_id):
    print(f"{delete_id} 학생 정보가 삭제되었습니다.")
else:
    print("해당 학번의 학생을 찾을 수 없습니다.")

# 총점 기준으로 학생들을 정렬하여 출력
score_manager.sort_students_by_total_score()
print("총점 기준 정렬 후:")
score_manager.print_student_info()

# 특정 학생 이름으로 검색
search_name = input("검색할 학생의 이름을 입력하세요: ")
found_student = score_manager.search_student_by_name(search_name)
if found_student:
    print(f"{search_name} 학생 정보:")
    print(f"학번: {found_student.student_id}, 이름: {found_student.name}, 영어: {found_student.english_score}, C언어: {found_student.c_score}, 파이썬: {found_student.python_score}, 총점: {found_student.total_score}, 평균: {found_student.average_score}, 학점: {found_student.grade}, 등수: {found_student.rank}")
else:
    print("해당 이름의 학생을 찾을 수 없습니다.")
