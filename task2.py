class Student:
    """
    __init__" is a reseved method in python classes. 
    It is called as a constructor in object oriented terminology. 
    This method is called when an object is created from a class and 
    it allows the class to initialize the attributes of the class.
    """
    def __init__(self, id, marks):
        self.id = id
        self.marks = marks
    #The “self” is automatically assigned to the newly created instance of Student class.

    def calculateAverage(self):
        total = 0

        for key in self.marks:
            total = total+self.marks[key]
        average = total/len(self.marks)
        return average

    def displayAverage(self):
        print(self.calculateAverage())


if __name__=='__main__':
    # The __init__() function is defined with three variables but when we are creating the Student instance, 
    # we have to provide only two arguments: id and marks.
    student1 = Student(1234, {'CSF': 75, 'FunPro': 80, 'WT': 85})
    student1.displayAverage()

    student2 = Student(1235, {'CSF': 74, 'FunPro': 50, 'WT': 85})
    student2.displayAverage()
