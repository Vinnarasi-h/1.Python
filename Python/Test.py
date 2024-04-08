class triangle():
    def area():
            Height=int(input("Height="))
            Breadth=int(input("Breadth="))
            Area =(Height*Breadth)/2
            print("Area formula =(Height*Breadth)/2")
            print("Area of Triangle:",Area)
            
    def perimeter():
            Height1=int(input("Height1="))
            Height2=int(input("Height2="))
            Breadth=int(input("Breadth="))
            Perimeter  = Height1+Height2+Breadth
            print("Perimeter formula = Height1+Height2+Breadth")
            print("Perimeter of Triangle:",Perimeter)



class FindPercent():
    def percentage():
        Subject1= 98
        print("Subject1:",Subject1)
        Subject2= 87
        print("Subject2:",Subject2)
        Subject3= 95
        print("Subject3:",Subject3)
        Subject4= 95
        print("Subject4:",Subject4)
        Subject5= 93
        print("Subject5:",Subject5)
        Total = (Subject1+ Subject2+ Subject3+ Subject4+ Subject5)
        print("Total :",Total)
        Per= (Total/500)*100
        print("Percentage:",Per)



def percentage():
    Subject1= 98
    print("Subject1:",Subject1)
    Subject2= 87
    print("Subject2:",Subject2)
    Subject3= 95
    print("Subject3:",Subject3)
    Subject4= 95
    print("Subject4:",Subject4)
    Subject5= 93
    print("Subject5:",Subject5)
    Total = (Subject1+ Subject2+ Subject3+ Subject4+ Subject5)
    print("Total :",Total)
    Per= (Total/500)*100
    print("Percentage:",Per)


    
def eligible():
    gender=input("Your Gender:")
    age=int(input("Your Age:"))
    male_age_limit=21
    female_age_limit=18
    if gender.lower()== "male":
        if age >= male_age_limit:
            print ("ELIGIBLE")
        else:
            print ("NOT ELIGIBLE")
    elif gender.lower() == "female":
          if age >= female_age_limit:
              print ("ELIGIBLE")
          else:
              print ("NOT ELIGIBLE")
    else:
        print ("INVALID GENDER")  
            

 

def OddEven():
    num = int(input("Enter a number:"))
    if (num%2==0):
            print(num,"is a Even number")
    else:
            print("odd number")
 
class ElegiblityForMarriage():
    def eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        male_age_limit=21
        female_age_limit=18
        if gender.lower()== "male":
            if age >= male_age_limit:
                print ("ELIGIBLE")
            else:
                print ("NOT ELIGIBLE")
        elif gender.lower() == "female":
              if age >= female_age_limit:
                  print ("ELIGIBLE")
              else:
                  print ("NOT ELIGIBLE")
                  
class SubfieldsInAI():
       def Subfields():
            print("Sub-fields in AI are:")
            list=('Machine Learning','Neural Networks','Vision,Robotics','Speech Processing','Natural Language Processing')
            for i in list:
                print(i)
            

            

        
    
    

            

        
        
        
   
   

 
    
    

            


