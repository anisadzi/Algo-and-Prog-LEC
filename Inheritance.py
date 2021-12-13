class Person():
    def __init__ (self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def setAddress(self, address):
        self.address = address

    def getaddress(self):
        return self.address

    def __str__(self):
        return self.name, "("+self.address+")"



class Student(Person):
    def __init__ (self, name, address, course = {}, grade = {}, numcourses = 0):
        Person.__init__(self, name, address)
        self.name = name
        self.address = address
        self.course = course
        self.grade = grade
        self.numcourses = numcourses

    def addCourseGrade(self, course, grade):
        self.course = course
        self.grade = grade

    def printGrades(self):
        print(self.course, ":", self.grade)

    def __str__(self):
        return "Student : ",self.name, "("+self.address+")"



class Teacher(Person):
    def __init__ (self, name, address, course = {}, numcourses = 0):
        Person.__init__(self, name,address)
        self.course = course
        self.numcourses = numcourses

    def addCourse(self, course):
        if course in self.course:
            return False
        if course not in self.course:
            self.course = course
            return True

    def removeCourse(self, course):
        if course in self.course:
            delattr(Teacher, "courses")
            return True
        if course not in self.course:
            return False

    def __str__(self):
        return "Teacher : ",self.name, "("+self.address+")"
