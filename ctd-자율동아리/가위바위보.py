import random

ai= random.random()

   

if ai <=0.33:

    ai="가위"

elif ai <=0.66:

    ai="바위"

elif ai > 0.66:

    ai="보"

            

while True :

    my = input("가위,바위,보를 결정하세요 : ")

    

    if my=="가위" :

        if ai == "가위" :

            print("비겼습니다.")

            print("AI는 %s를 냈습니다." % ai)

            break

        elif ai == "바위" : 

            print("졌습니다.")

            print("AI는 %s를 냈습니다." % ai)

            break

        elif ai == "보" :

            print("이겼습니다.")

            print("AI는 %s를 냈습니다." % ai)

            break

    

                   

    elif my =="바위" :

        if ai == "가위" :

            print("이겼습니다.")

            print("AI는 %s를 냈습니다." % ai)

            break

        elif ai == "바위" : 

            print("비겼습니다.")

            print("AI는 %s를 냈습니다." % ai)

            break

        elif ai == "보" :

            print("졌습니다.")

            print("AI는 %s를 냈습니다." % ai)

            break

        

    elif my =="보" :

        if ai == "가위" :

            print("졌습니다.")

            print("AI는 %s를 냈습니다." % ai)

            break

        elif ai == "바위" : 

            print("이겼습니다.")

            print("AI는 %s를 냈습니다." % ai)

            break

        elif ai == "보" :

            print("비겼습니다.")

            print("AI는 %s를 냈습니다." % ai)

            break

                            

    else:

        print("가위,바위,보 중에 고르세요")
