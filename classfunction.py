class function():
    def Subfields():
        fields=['Machine Learning',
       'Neural Networks',
        'Vision',
        'Robotics',
        'Speech Processing',
        'Natural Language Processing'
               ]
        print ("Sub-fields in AI are:")
        for item in fields:
            print(item)
        return fields

    
    def OddEven():
        num = int(input("enter the number"))
        if ((num % 2)==1):
            print(num,"is odd number")
            OE=num,"is odd number"
        else:
            print(num,"is even number")
            OE=num,"is even number"
        return OE

    def Eligible():
        sex=input("Your gender:")
        age=int(input("Your age:"))
        if (age<25):
            print("NOT ELIGIBLE")
            marriage="NOT ELIGIBLE"
        else:
            print("ELIGIBLE")
            marriage="ELIGIBLE"
        return marriage
        
    def percentage(subject1,subject2,subject3,subject4,subject5):
        Subject1=int(input("Subject1"))
        Subject2=int(input("Subject2"))
        Subject3=int(input("Subject3"))
        Subject4=int(input("Subject4"))
        Subject5=int(input("Subject5"))
        total=subject1+subject2+subject3+subject4+subject5
        per=((total/500)*100)
        print("Total",total)
        print("percentage",per)
        
# Function to calculate the Area
    def calculate_area(height, breadth):
        Height=int(input("Height"))
        Breadth=int(input("Breadth"))
        print("Area formula: (Height*Breadth)/2")
        area = ((height * breadth) / 2)
        print("Area of Triangle:", area)
        
    # Function to calculate the Perimeter
    def calculate_perimeter(Height1, Height2, Breadth):
        Height1=int(input("Height1"))
        Height2=int(input("Height2"))
        Breadth=int(input("Breadth"))
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = Height1 + Height2 +Breadth 
        print("Perimeter of Triangle:", perimeter)