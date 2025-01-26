from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name":"Edees",
        "age":23,
        "year":"year 12"
    }
}

class Student(BaseModel):
    name : str
    age : int 
    year: str

class updateStudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int]=None 
    year: Optional[str]=None

@app.get("/")
def index():
    return {"name":"First Data"}
#GET METHOD
@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    return students[student_id]


@app.get("/get-by-name")
def get_student(name:Optional[str] = None ):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"data":"not found"}     

@app.get("/get-by-name2/{student_id }")
def get_student(student_id:int,name:Optional[str] = None ):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"data":"not found"}     

#POST METHOD
@app.post("/create-student/{student_id}")
def create_student(student_id : int,student : Student):
    if student_id in students:
        return{"Error":"Student Exist"}
    students[student_id] = student
    return students[student_id]

#PUT METHOD

@app.put("/update-student/{student_id}")
def update_student(student_id : int,student : updateStudent):
    if student_id not in students:
        return {"Error":"Student not exist"}
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year
    return students[student_id]
# DELETE
@app.delete("/delete-student{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error":"Student doesn't exist"}
    del students[student_id]
    return {"Message":"student deleted Successfully"}
