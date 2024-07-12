from models import Student, University, Course

students = {
    1: Student(id=1, name="Aarav Sharma", age=20, email="aarav.sharma@example.com"),
    2: Student(id=2, name="Vivaan Singh", age=22, email="vivaan.singh@example.com"),
    3: Student(id=3, name="Diya Patel", age=21, email="diya.patel@example.com"),
    4: Student(id=4, name="Ananya Rao", age=23, email="ananya.rao@example.com"),
    5: Student(id=5, name="Aditya Iyer", age=24, email="aditya.iyer@example.com"),
    6: Student(id=6, name="Ishaan Joshi", age=20, email="ishaan.joshi@example.com"),
    7: Student(id=7, name="Kiara Gupta", age=22, email="kiara.gupta@example.com"),
    8: Student(id=8, name="Aryan Khanna", age=21, email="aryan.khanna@example.com"),
    9: Student(id=9, name="Anika Kapoor", age=23, email="anika.kapoor@example.com"),
    10: Student(id=10, name="Rohan Mehta", age=24, email="rohan.mehta@example.com")
}
student_id_counter = 11

universities = {
    1: University(id=1, name="MBCET", country="INDIA"),
    2: University(id=2, name="CET", country="INDIA"),
    3: University(id=3, name="MIT", country="USA")
}
university_id_counter = 4


courses = {
    1: Course(id=1, name="Python Basics", description="Learn Basic of Python Language", university_id=1),
    2: Course(id=2, name="FAST API", description="Learn FastAPI", university_id=2),
    3: Course(id=3, name="MongoDB", description="Learn MongoDB", university_id=3)
}
course_id_counter = 4