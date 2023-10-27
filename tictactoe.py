def main():
    rest=True

    while rest :
        move=input("do you want to play the first move ? (yes/no) :")

        if(move=='yes' or move == 'YES' or move == 'Yes'):



            print("hello")
            matrix = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]


            print_matrix(matrix)

            won=False
            blck=9
            while blck>0:
                if input_matrix(matrix) :
                    won=True
                    break
                blck-=1
                if blck>0:
                    if put_o(matrix,blck) :
                        won=True
                        break
                blck-=1

            if won== False :
                import cowsay
                cowsay.cow("draw : no one won !!")

            tryy=input("Do you want to play again ? ('press enter' for yes and 'n' for no)  :")
            if tryy=='n':
                rest=False

        else :
            print("hello")
            matrix = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]


            print_matrix(matrix)

            won=False
            blck=9
            while blck>0:
                if put_o(matrix,blck) :
                    won=True
                    break

                blck-=1
                if blck>0:
                    if input_matrix(matrix) :
                        won=True
                        break

                blck-=1

            if won== False :
                import cowsay
                cowsay.cow("draw : no one won !!")

            tryy=input("Do you want to play again ? ('press enter' for yes and 'n' for no)  :")
            if tryy=='n':
                rest=False




def input_matrix(matrix):
    """while True:
        move_in=int(input("enter your move"))
        if move_in in matrix :
            pp=0
            for row_idx, row in enumerate(matrix):
                    if pp==1:
                        break
                    for col_idx, element in enumerate(row):
                        if element == move_in:
                            matrix[row_idx][col_idx]='X'
                            pp=1
                            if check_win(matrix,'X'):
                                import cowsay
                                cowsay.cow("YOU WON !!!!!!!!!!!!")
                                return True
                            break
            break
        else :
            print("invalid move")"""

    while True:
        poss = (input("At what number would you like to put your 'X': "))
        lstt=[]
        for i in range (3) :
            for j in range (3):
                if (matrix[i][j]!='X') and (matrix[i][j]!='O'):
                    lstt.append(matrix[i][j])
        lst1=str(lstt)
        if not poss in lst1 :
            print("invalid input")
            continue
        pos=int(poss)
        pp=0
        for row_idx, row in enumerate(matrix):
            if pp==1:
                break
            for col_idx, element in enumerate(row):
                if element == pos:

                    matrix[row_idx][col_idx] = 'X'

                    print("Here is your move:")
                    print_matrix(matrix)
                    pp=1
                    if check_win(matrix,'X'):
                        import cowsay
                        cowsay.cow("YOU WON !!!!!!!!!!!!")
                        return True


                    break



        if pp==0:
            print("Box already filled, try again")
        else:
            break

    return False





def check_win(matrix,chk):
    pp=0
    for i in range(3):
        if matrix[0][i]==chk and matrix[1][i]==chk  and matrix[2][i]==chk :
            pp=1
            return True

        elif matrix[i][0]==chk and matrix[i][1]==chk  and matrix[i][2]==chk :
            pp=1
            return True

    if pp==0:
        if (matrix[0][0]==chk and matrix[1][1]==chk  and matrix[2][2]==chk) or (matrix[0][2]==chk and matrix[1][1]==chk  and matrix[2][0]==chk) :
            pp=1
            return True

    return False




def print_matrix(matrix):
    print()
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 'X':
                print("\033[92mX\033[0m", end=" ")
            elif matrix[i][j] == 'O':
                print("\033[91mO\033[0m", end=" ")
            else:
                print(matrix[i][j], end=" ")

            if j < 2:
                print("|", end=" ")
        print()
        if i < 2:
            print("-" * 9)  # Adjusted for colored characters
    print()

    


def who_won (matrix):
    if(check_win(matrix,'O')):
        return -1
    elif check_win(matrix,'X'):
        return 1
    else:
        return 0


def maxi(matrix,lft):
    left_boxes=[]
    matrix_test=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range (3):
        for j in range (3):
            matrix_test[i][j]=matrix[i][j]
    for row_idx, row in enumerate(matrix_test):
        for col_idx, element in enumerate(row):
            if (element != 'X' and element != 'O'):
                left_boxes.append([row_idx,col_idx])
    values=[]
    if len(left_boxes)==0:
        val=who_won(matrix_test)

        return val

    for elemts in left_boxes :
        r1=elemts[0]
        c1=elemts[1]
        prev=matrix_test[r1][c1]
        matrix_test[r1][c1]='X'
        if check_win(matrix_test,'X'):
            d=1
            values.append([d,r1,c1])
        else:

            val=mini(matrix_test,lft)
            values.append([val,r1,c1])
            matrix_test[r1][c1]=prev

    rr=-1
    cc=-1
    vaa=-10
    for idx in values :
        if(idx[0] > vaa):
            vaa=idx[0]
            rr=idx[1]
            cc=idx[2]
    if lft==len(left_boxes):
        matrix[rr][cc]='X'
        print("here is my move")
        print_matrix(matrix)
        if check_win(matrix,'X') :
            print("IMPOSSIBLE !! HOW CAN A STUPID FUCK LIKE U WIN ?")
            return True
        else :
            return False
    else:
        return vaa





def mini(matrix,lft):
    left_boxes=[]
    matrix_test=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range (3):
        for j in range (3):
            matrix_test[i][j]=matrix[i][j]
    for row_idx, row in enumerate(matrix_test):
        for col_idx, element in enumerate(row):
            if (element != 'X' and element != 'O'):
                left_boxes.append([row_idx,col_idx])
    values=[]
    if len(left_boxes)==0:
        val=who_won(matrix_test)
        return val

    for elemts in left_boxes :
        r1=elemts[0]
        c1=elemts[1]
        prev=matrix_test[r1][c1]
        matrix_test[r1][c1]='O'
        if check_win(matrix_test,'O'):
            d=-1
            values.append([d,r1,c1])
        else :

            val=maxi(matrix_test,lft)
            values.append([val,r1,c1])
            matrix_test[r1][c1]=prev

    rr=-1
    cc=-1
    vaa=10
    for  idx in values :
        if(idx[0] < vaa):
            vaa=idx[0]
            rr=idx[1]
            cc=idx[2]
    if lft==len(left_boxes):
        matrix[rr][cc]='O'
        print("here is my move")
        print_matrix(matrix)
        if check_win(matrix,'O') :
            print("I WON BITCH")
            return True
        else :
            return False
    else:
        return vaa



def put_o(matrix,box):
    vals=[]
    if mini(matrix,box) :
        return True
    else :
        return False




main()
