""" Write a Script to create two list student ans address which contain the name of  student and their respective address. print student name with it's address """
address=[]
student=[]
c=0
def createList():
    for i in range (5):
        x=input("Enter Student Name:")
        y=input("Enter Student's Address:")
        student.append(x)          
        address.append(y)        
    for i in range (5):
        print('{} lives in {}'.format(student[i],address[i]))
createList()
        
        
