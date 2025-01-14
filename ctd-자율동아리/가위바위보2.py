import random
print ("가위 바위 보")
for x in range(5):
    print
    computer= random.choice(["가위","바위","보"])

    print ("사용자 >>")
    user = input()
    print ("컴퓨터 >>" + computer)

    if computer == user:
        print ("비김")
        
    elif (user == "가위" and computer == "보")or      \
         (user == "바위" and computer == "가위")or      \
         (user == "보" and computer == "바위"):
        print ("이김")
    else:
        print ("짐")
