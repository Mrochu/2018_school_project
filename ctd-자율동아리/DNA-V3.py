import random
import copy
import time

Ob_num = 100                            #부모개수
Ob_ber = 50                             #DNA크기
Turn_num = 1000                            #세대교체회수

obeject = list()                        #객체 게임회수
point = list()                          #객체 점수 저장
parrent_sort = list()                   #부모 객체 점수 저장

num = 0
numturn = 0
therenum = 0
therenumturn = 0
forenum = 0
forenumturn = 0

OIlist = list()

def initmake(x,num):
    i = 0
    while i < num:
        i = i + 1
        x.append(0) 

def init(num):
    i = 0
    z = list()
    while i < num:
        i = i + 1
        z.append(0)
    return z

def object_make (Ob_num,Ob_ber):
    i = 0
    obeject = list()
    while i < Ob_num:
        i = i + 1
        line = list()                                               # 안쪽 리스트로 사용할 빈 리스트 생성
        j = 0
        while j < Ob_ber:
            j = j + 1
            line.append(random.randint(0,1))                       # 안쪽 리스트에 0 추가
        obeject.append(line)                                    # 전체 리스트에 안쪽 리스트를 추가
    return obeject

def find_parrent (point,Ob_num,OIlist) :                  #부모의 점수를 정렬합니다.
    parrent_sorts = list()
    check = list()
    check = copy.deepcopy(point)
    check.sort(reverse = True)
    OIlist = check
    #print(check[0:])
    i = 0
    while i < Ob_num: 
        j = 0
        while j < Ob_num:
            if check[i:i+1] == point[j:j+1]:
                parrent_sorts.append(j)
            j = j + 1
        i = i + 1
    a = (len(parrent_sorts)//10)
    #print(parrent_sorts[0:a])
    return parrent_sorts

def parrent_DNA(Ob_num,Ob_ber,parrent_sort,obeject) :         #부모가될 상위 10%를 찾습니다.그리고 자식을 만듭니다.
    temp_obeject = list()
    temp_obeject = object_make (Ob_num,Ob_ber)
    d = 0
    i = 0
    while i < Ob_num//10:                                               
        k = 0
        while k < Ob_num//10:                                          
            j = 0
            a = random.randint(0, 15)
            b = random.randint(16, 35)

            if random.randint(0, 50) == 0:
                
                if random.randint(0, 1) == 1:
                    x = random.randint(0, random.randint(0, Ob_ber-1))
                    
                    temp_obeject[d][x] = 0
                else:
                    x = random.randint(0, random.randint(0, Ob_ber-1))
                    
                    temp_obeject[d][x] = 1
                
            if random.randint(0, 1) == 1:
                while j < a:
                    temp_obeject[d][j] = obeject[i][j]
                    j = j + 1
            else:
                while j < a:
                    temp_obeject[d][j] = obeject[k][j]
                    j = j + 1
                    
            if random.randint(0, 1) == 1:
                while j < b:
                    temp_obeject[d][j] = obeject[i][j]
                    j = j + 1
            else:
                while j < b:
                    temp_obeject[d][j] = obeject[k][j]
                    j = j + 1
                    
            if random.randint(0, 1) == 1:
                while j < Ob_ber:
                    temp_obeject[d][j] = obeject[i][j]
                    j = j + 1
            else:
                while j < Ob_ber:
                    temp_obeject[d][j] = obeject[k][j]

                    j = j + 1
                    
            if random.randint(0, 25) == 0:
                f = 0
                while f < Ob_ber:
                    temp_obeject[d][f] = random.randint(0, 1)
                    f = f + 1

            
            d = d + 1
            k = k + 1
        i = i + 1
    return temp_obeject       
     
def game(obeject,point,Ob_num,Ob_ber,num,numturn,therenum,therenumturn,forenum,forenumturn):                              #게임을 하고 객체점수 저장
    i = 0
    #print(obeject[0:])
    while i < Ob_num:                                               #객체 1
        k = 0
        while k < Ob_num:                                           #객체 2
            j = 0
            if i != k :                                            #나 자신과 싸우면 안되지
                while j < Ob_ber:                                   #카드패
                    #tlist1 = list()
                    #tlist2 = list()
                    #tlist1 = obeject[i : i+1]
                    #tlist2 = obeject[k : k+1]
                    #print(tlist1[0:])
                    if obeject[i][j] == 1 and obeject[k][j] == 1:    #elif tlist1[j:j+1] == 0 and tlist1[j:j+] == 0:  #   point[i] #   point[k]                                     
                        point[i] = point[i] + 2
                        point[k] = point[k] + 2
                        num = num + 4
                        numturn = numturn + 2

                    if obeject[i][j] == 1 and obeject[k][j] == 0:
                        point[i] = point[i] - 1
                        point[k] = point[k] + 3
                        
                        therenum = therenum + 3
                        therenumturn = therenumturn + 1

                        num = num - 1
                        numturn = numturn + 1

                    if obeject[i][j] == 0 and obeject[k][j] == 1:
                        point[i] = point[i] + 3
                        point[k] = point[k] - 1
                        therenum = therenum + 3
                        therenumturn = therenumturn + 1

                        num = num - 1
                        numturn = numturn + 1

                    if obeject[j:j+1] == 0 and obeject[k][j] == 0:
                        point[i] = point[i] - 2
                        point[k] = point[k] - 2
                        therenum = therenum - 4
                        therenumturn = therenumturn + 2

                    j = j + 1
            k = k + 1
        i = i + 1
    #배신회수
    print(therenumturn)
        
    #배신자들이 평균얻은 점수
    print(therenum)
        
    #협력회수
    print(numturn)
        
    #협력자들이 평균얻은 점수
    print(num)
    return point

def update(Ob_num,Ob_ber,parrent_sort,obeject,Turn_num,point):
    print("대략")
    print(3 * 1000)
    #time.sleep(5)
    
    initmake(point,Ob_num)
    
    initmake(parrent_sort,Ob_num)

    i = 0
    while i < Turn_num:
        #print("-----------------------------------------------------" , sep='\n')
        print(i , sep='\n')
        #print("-----------------------------------------------------" , sep='\n')
        obeject = object_make (Ob_num,Ob_ber)

        point = game(obeject,point,Ob_num,Ob_ber,num,numturn,therenum,therenumturn,forenum,forenumturn)

        parrent_sort = find_parrent(point,Ob_num,OIlist)

        obeject = parrent_DNA(Ob_num,Ob_ber,parrent_sort,obeject)

        
        

        #최고점
        

        #최저점
        


        if i == Turn_num:
            print(point[0:])
            
        
        point = init(Ob_num)
        
        i = i + 1
        
update(Ob_num,Ob_ber,parrent_sort,obeject,Turn_num,point)    

