#Grade Marking of School
n=int(input("Enter your marks:-"))
if n>=90 and n<=100:
    print("Congratulations, You Got Grade 'A'.")
elif n>=80 and n<90:
    print("Congratulations, You Got Grade 'B'.")
elif n>=70 and n<80:
    print("Congratulations, You Got Grade 'C'.")
elif n>=60 and n<70:
    print("Congratulations, You Got Grade 'D'.")
elif n>=50 and n<60:
    print("Congratulations, You Got Grade 'E'.")
else:
    print("Sorry, You are Failed.")