list=[6,78,64,33,55,55,34,1,97,37,22,25,70]
def swap(n):
    list[n],list[n+1]=list[n+1],list[n]
    return

def sort(list):
    cou=0
    while cou<len(list):
        cou2=0
        while cou2+1 < len(list):
            if list[cou2]>list[cou2+1]:
                swap(cou2)
            cou2+=1
            #print(list)
        cou+=1
def search(n,list):
    #sort(list)
    cou=0
    positionList=[]
    #go through list and check each position for 55 using counter
    quantity=0
    while cou < len(list):
        item=list[cou]
        #print("item: ",item)
        #print("n: ",n)
        if item==n:
            quantity+=1
            positionList.append(cou)

        cou+=1
        #print("count: ",cou)
    print("The number occurs in the list "+str(quantity)+" times in positions " + str(positionList) +".")


n=55
search(n,list)









#cou+=1