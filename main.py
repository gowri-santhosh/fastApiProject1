from fastapi import FastAPI, HTTPException
from models import Student, University, Course
from schemas import StudentCreate, UniversityCreate, CourseCreate
from data import students, student_id_counter, universities, university_id_counter, courses, course_id_counter

app = FastAPI()


@app.post("/students/", response_model=Student)
def create_student(student: StudentCreate):
    global student_id_counter
    new_student = Student(id=student_id_counter, **student.model_dump())
    students[student_id_counter] = new_student
    student_id_counter += 1
    return new_student


@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]


@app.post("/universities/", response_model=University)
def create_university(university: UniversityCreate):
    global university_id_counter
    new_university = University(id=university_id_counter, **university.model_dump())
    universities[university_id_counter] = new_university
    university_id_counter += 1
    return new_university


@app.get("/universities/{university_id}", response_model=University)
def read_university(university_id: int):
    if university_id not in universities:
        raise HTTPException(status_code=404, detail="University not found")
    return universities[university_id]


@app.post("/courses/", response_model=Course)
def create_course(course: CourseCreate):
    global course_id_counter
    if course.university_id not in universities:
        raise HTTPException(status_code=404, detail="University not found")
    new_course = Course(id=course_id_counter, **course.model_dump())
    courses[course_id_counter] = new_course
    course_id_counter += 1
    return new_course


@app.get("/courses/{course_id}", response_model=Course)
def read_course(course_id: int):
    if course_id not in courses:
        raise HTTPException(status_code=404, detail="Course not found")
    return courses[course_id]