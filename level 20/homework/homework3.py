score=int(input("enter your score (0-100): "))
if score>100:
    print("score can not be more than 100")
elif score>90 and score<100:
    print("your grade is A")
elif score>80 and score<89:
    print("your grade is B")
elif score>70 and score<79:
    print("your grade is C")
elif score>60 and score<69:
    print("your grade is D")
else:
    print("your grade is F")