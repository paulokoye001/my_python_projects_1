#       Age-Based Applicant Screening System for HR or Employers 
age = int(input("Enter your age: "))
empployes_age = 23 <= age <= 30

match age:
    case _ if age < 23:
        print("Not qualified.")
    case _ if age > 30:
        print("You didn't meet our recruitment criteria.")
    case 29:
        print("Please, what's your month of birth?\nYou might be very close to our age restrictions.")
    case _ if empployes_age:
        print("You are qualified!")
    case _:
        print("You have entered invalid data.")


