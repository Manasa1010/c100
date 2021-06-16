class Person(object):
    def __init__(self,name,age,gender,occupation,vehicals):
        self.name=name
        self.age=age
        self.gender=gender
        self.occupation=occupation
        self.vehicals=vehicals or {}

    def tellOccupation(self):
        print("I am a "+self.occupation)

    def tellAge(self):
        print("My age is"+str(self.age))

    def noOfCars(self):
        count=0
        for i in self.vehicals:
            count+=1
        print()            

def main():
    person1=Person("Aditi",17,"girl","painter",{"car1":"tayota","car2":"BMW"})
    print(person1.vehicals["car1"])
    person1.tellOccupation()
    person1.tellAge()
main()    