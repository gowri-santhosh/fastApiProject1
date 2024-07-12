from pydantic import BaseModel
class Student(BaseModel):
    id: int
    name: str
    age: int
    email: str

class University(BaseModel):
    id: int
    name: str
    country: str

class Course(BaseModel):
    id: int
    name: str
    description: str
    university_id: int

