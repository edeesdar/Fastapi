from fastapi import FastAPI,Path
from typing import Optional

app = FastAPI()

students = {
    1:{
        "name":"Edees",
        "age":23
    }
}

@app.get("/")
def index():
    return {"name":"First Data"}

@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    return students[student_id]


@app.get("/get-by-name")
def get_student(name:Optional[str] = None ):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
    return {"data":"not found"}     