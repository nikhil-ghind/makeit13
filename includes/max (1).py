def max_number(lst):        #function to find maximum number
    length=len(lst)         #provides length of single matrix
    max_lst=[]
    for i in lst:
        max_lst.append(max(i))
    max_number=max(max_lst)
    return(max_number)      #returns maximam of a 2D list

    
def get_similar(lst,x,y):       #Function to find length of similar numbers
    similar_Numbers=0
    if(x>=0 and x<4 and y>=0 and y<4):        #to check size of matrix
        if(lst[x][y]==lst[x-1][y]):
            similar_Numbers=similar_Numbers+1
        if(lst[x][y]==lst[x+1][y]):
            similar_Numbers=similar_Numbers+1
        if(lst[x][y] == lst[x][y-1]):
            similar_Numbers=similar_Numbers+1
        if(lst[x][y] == lst[x][y+1]):
            similar_Numbers=similar_Numbers+1
    return similar_Numbers       #returns similarity of numbers


def obtain_Zeros(lst):     #returns the position of all the zeros in the list
    zero_List=[]
    for i in range(0,len(lst)):
       for j in range(0,len(lst[i])):
          if(lst[i][j]==0):
                zero_List.append([i,j])
    return zero_List            

def seuence(x):
    if (x == '1'):
        return [[1, 2, 3, 4], [3, 3, 5, 4], [1, 2, 5, 4], [1, 1, 2, 3]]
    elif (x == '2'):
        return [[], [], [], []]
    elif (x == '3'):
        return [[], [], [], []]
    elif (x == '4'):
        return [[], [], [], []]
    elif (x == '5'):
        return [[], [], [], []]
    elif (x == '6'):
        return [[], [], [], []]
    elif (x == '7'):
        return [[], [], [], []]
    elif (x == '8'):
        return [[], [], [], []]
    elif (x == '9'):
        return [[], [], [], []]
    elif (x == '10'):
        return [[], [], [], []]
    elif (x == '11'):
        return [[], [], [], []]
    elif (x == '12'):
        return [[], [], [], []]
    elif (x == '13'):
        return [[], [], [], []]
    elif (x == '14'):
        return [[], [], [], []]
    elif (x == '15'):
        return [[], [], [], []]
    elif (x == '16'):
        return [[], [], [], []]
    elif (x == '17'):
        return [[], [], [], []]
    elif (x == '18'):
        return [[], [], [], []]
    elif (x == '19'):
        return [[], [], [], []]
    elif (x == '20'):
        return [[], [], [], []]
    elif (x == '21'):
        return [[], [], [], []]
    elif (x == '23'):
        return [[], [], [], []]
    elif (x == '24'):
        return [[], [], [], []]
    elif (x == '25'):
        return [[], [], [], []]
    elif (x == '26'):
        return [[], [], [], []]
    elif (x == '27'):
        return [[], [], [], []]
    elif (x == '28'):
        return [[], [], [], []]
    elif (x == '29'):
        return [[], [], [], []]

    elif (x == '30'):
        return [[], [], [], []]
    elif (x == '31'):
        return [[], [], [], []]
    elif (x == '32'):
        return [[], [], [], []]
    elif (x == '33'):
        return [[], [], [], []]
    elif (x == '34'):
        return [[], [], [], []]
    elif (x == '35'):
        return [[], [], [], []]
    elif (x == '36'):
        return [[], [], [], []]

    elif (x == '37'):
        return [[], [], [], []]
    elif (x == '38'):
        return [[], [], [], []]
    elif (x == '39'):
        return [[], [], [], []]
    elif (x == '40'):
        return [[], [], [], []]
    elif (x == '41'):
        return [[], [], [], []]
    elif (x == '42'):
        return [[], [], [], []]
    elif (x == '43'):
        return [[], [], [], []]
    elif (x == '44'):
        return [[], [], [], []]
    elif (x == '45'):
        return [[], [], [], []]
    elif (x == '46'):
        return [[], [], [], []]
    elif (x == '47'):
        return [[], [], [], []]
    elif (x == '48'):
        return [[], [], [], []]
    elif (x == '49'):
        return [[], [], [], []]
    elif (x == '50'):
        return [[], [], [], []]
    


            
        
lst=[[1,2,0,4],[4,5,6,7],[6,0,18,10],[10,10,11,6]]
print(max_number(lst))
print(obtain_Zeros(lst))
