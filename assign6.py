'''Assignment 1 and Assignment 2'''


'''part 1 of assignment 1 .''' 
# import json

# class Employee:
#     def __init__(self, Name, DOB, Height, City, State):
#         self.name = Name
#         self.dob = DOB
#         self.height = Height
#         self.city = City
#         self.state = State
        
#     def __str__(self):
#         return f"Name: {self.name}, DOB: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"


# f= open('employee.json')
# f1= json.load(f)


# employees = []  
# for data in f1['employee details']:
#     employee = Employee(data["Name"], data["DOB"], data["Height"], data["City"], data["State"])
    
#     employees.append(employee)


# for employee in employees:
#     print(employee)

# f.close()

'''contd part 2 of assignment'''

# state_capitals= {"Telangana":"Hyderabad","Kerala":"Thiruvanthapuram",
#                  "Andhra Pradesh":"Amaravati","Tamilnadu":"Chennai","Karnataka":"Banglore",
#                  "Goa":"Patna","Maharastra":"Mumbai"}


# import json
# f=open('state.json','w')
# json.dump(state_capitals,f)
# f.close()
# f1=open('state.json')
# data=json.load(f1)
# print(type(json.dumps(data,indent=3)))

'''Assignment 2'''

# class Dog:
#     def __init__(self,name,age,coat_color):
#         self.name=name
#         self.age=age
#         self.coat_color=coat_color

#     def description(self):
#         print("Name: {} \n Age: {}".format(self.name,self.age))
#     def get_info(self):
#         print("Coat Color: {}".format(self.coat_color))

# class JackRussellTerrier(Dog):
#     def char(self):
#         print('I am a perfect family dog.')
#     def char1(self):
#         print('I am adventurous too!')
# class Bulldog(Dog):
#     def breed(self):
#         print('I am dependable and predictable')
#     def breed1(self):
#         print('I am sweet and people-oriented.')

# dog1= Dog("Snowy",4,'White')
# dog1.description()
# dog1.get_info()

# dog2=JackRussellTerrier("Rocky",5,"Brown")
# dog2.description()
# dog2.get_info()
# dog2.char1()
# dog2.char()

# dog3=Bulldog("Lucky",3,"white")
# dog3.description()
# dog3.get_info()
# dog3.breed()
# dog3.breed1()
