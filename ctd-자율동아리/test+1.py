class gameboard():
    gameboard = [["1","2","3","4"],["5","6","7","8"],
                 ["9","10","11","12"],["13","14","15","0"]]
    def findzero(self):
        i,j = (0,0)
        while i<4 :
            while j<4:
                if self.gameboard[i][j] == "0":
                    a = 4*i+j
                    print(a)
                    return 4*i+j
                j+=1
            i+=1
            j=0

    def right(self):
        dontmove = [3, 7, 11, 15]
        zeroposition = self.findzero()
        if zeroposition in dontmove:
            print("허용되지 않은 이동입니다")
        else:
            temp = self.gameboard[zeroposition // 4][zeroposition % 4]
            self.gameboard[zeroposition // 4][zeroposition % 4] = self.gameboard[zeroposition // 4][
                zeroposition % 4 + 1]
            self.gameboard[zeroposition // 4][zeroposition % 4 + 1] = temp
    def up (self):
        dontmove = [0, 1, 2, 3]
        zeroposition = self.findzero()
        if zeroposition in dontmove:
            print("허용되지 않은 이동입니다")
        else:
            temp = self.gameboard[zeroposition // 4 - 1][zeroposition % 4]
            self.gameboard[zeroposition // 4 - 1 ][zeroposition % 4] = self.gameboard[zeroposition // 4][
                zeroposition % 4 ]
            self.gameboard[zeroposition // 4][zeroposition % 4 ] = temp
    def down(self):
        dontmove = [12, 13, 14, 15]
        zeroposition = self.findzero()
        if zeroposition in dontmove:
            print("허용되지 않은 이동입니다")
        else:
            temp = self.gameboard[zeroposition // 4+1][zeroposition % 4]
            self.gameboard[zeroposition // 4+1][zeroposition % 4] = self.gameboard[zeroposition // 4][
                zeroposition % 4]
            self.gameboard[zeroposition // 4][zeroposition % 4] = temp

    def left(self):
        dontmove = [0,4,8,12]
        zeroposition = self.findzero()
        if zeroposition in dontmove :
            print("허용되지 않은 이동입니다")
        else :
            temp = self.gameboard[zeroposition//4][zeroposition%4]
            self.gameboard[zeroposition//4][zeroposition%4] = self.gameboard[zeroposition//4][zeroposition%4-1]
            self.gameboard[zeroposition//4][zeroposition%4-1] = temp

    def printgameboard(self):
        i=0
        while i<4:
            print(self.gameboard[i])
            i+=1

gameboard = gameboard()
while True:
    key = input("a 왼쪽 s 아래쪽 d 오른쪽 w 위쪽으로 0 이 이동ㅇ합니다.")
    if key == "a":
        gameboard.left()
        print(gameboard.gameboard[0])
        print(gameboard.gameboard[1])
        print(gameboard.gameboard[2])
        print(gameboard.gameboard[3])
    elif key == "s":
        gameboard.down()
        print(gameboard.gameboard[0])
        print(gameboard.gameboard[1])
        print(gameboard.gameboard[2])
        print(gameboard.gameboard[3])
    elif key == "d":
        gameboard.right()
        print(gameboard.gameboard[0])
        print(gameboard.gameboard[1])
        print(gameboard.gameboard[2])
        print(gameboard.gameboard[3])
    elif key == "w":
        gameboard.up()
        print(gameboard.gameboard[0])
        print(gameboard.gameboard[1])
        print(gameboard.gameboard[2])
        print(gameboard.gameboard[3])
    else:
        print("잘못된 이동입니다")
        print(gameboard.gameboard[0])
        print(gameboard.gameboard[1])
        print(gameboard.gameboard[2])
        print(gameboard.gameboard[3])
        a = 1


