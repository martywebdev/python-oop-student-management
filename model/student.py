class Student:
    def __init__(self, id, name, course, mobile):
        self.id = id
        self.name = name
        self.course = course
        self.mobile = mobile

    def __repr__(self):
        return f"<Student id={self.id}, name={self.name}, course={self.course}, mobile={self.mobile}>"
