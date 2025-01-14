import random 
end = 0
BaskinRobbins = 0 

while end == 0: 
    ai = random.randint(1, 3) 
    print("com : ", ai) 
    BaskinRobbins = BaskinRobbins + ai 
    print("total : ", BaskinRobbins) 
    if BaskinRobbins > 31: 
        print("win") 
        end = 1 
    me = int(input("number ->> ")) 
    BaskinRobbins = BaskinRobbins + me 
    print("total : ", BaskinRobbins) 
    if BaskinRobbins > 31: 
        print("lose") 
        end = 1 
print("end")
