class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        a = sum(self.scores)/(len(self.scores))
        if a < 40:
            grade = "T"
        elif 40 <= a and a < 55:
            grade = "D"
        elif 55 <= a and a < 70:
            grade = "P"
        elif 70 <= a and a < 80:
            grade = "A"
        elif 80 <= a and a < 90:
            grade = "E"
        elif 90 <= a and a <= 100:
            grade = "O"
        #self.grade = grade
        return grade

    #def printPerson(self):
    #    Person.printPerson(self)
    #    print("Grade:", self.grade)

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())