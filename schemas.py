from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    email: str

class UniversityCreate(BaseModel):
    name: str
    country: str

class CourseCreate(BaseModel):
    name: str
    description: str
    university_id: int
