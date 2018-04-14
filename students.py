""" Test Code - stores students and scores in database """

from peewee import *

db = SqliteDatabase("students.db")


class Student(Model):
    username = CharField(max_length = 255, unique=True)
    points = IntegerField(default=0)
    
    class Meta:
        database = db
        
students= [
    {"username": "Finn",
     "points": "5000"},
    {"username": "georgeB",
     "points": "6000"},
    {"username": "queenie",
     "points": "7000"},
    {"username": "georgeMooris",
     "points": "4000"},
    {"username": "Azana",
     "points": "10000"}]

def add_student():
    for student in students:
        try:
            Student.create(username=student["username"],
                           points=student["points"])
        except IntergrityError:
            student_record = Student.get(username=student["username"])
            student_record.points = student["points"]
            student_record.save()
            
def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student
    



if __name__ == "__main__":
    db.connect()
    db.create_tables([Student], safe=True)
    add_student()
    print("Our top student right now is: {0.username}.".format(top_student()))
