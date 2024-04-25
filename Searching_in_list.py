

def Binarysearch(l , low , high,key):
    if high < low :
        return "the number is does not exist"
    while low <=high:
        mid = low + (high-low)//2
        if l[mid] == key:
            return mid+1
        elif l[mid] < key:
            return Binarysearch(l, mid+1 , high , key)
        else:
            return Binarysearch(l , low ,mid-1 , key)
        
def linearSearch( l , key):
    for i in range(len(l)):
        if l[i] == key:
            return i+1
    return "the number is does not exist"

def TernarySearch(l , low , high , key):
    while low <= high:
        mid1 = low + (high-low)//3
        mid2 = high - (high - low)//3
        if l[mid1] == key:
            return mid1+1
        if l[mid2] == key:
            return mid2+1
        
        if key <l[mid1]:
            return TernarySearch(l , low , mid1 -1 , key)
        elif key > l[mid2]:
            return TernarySearch(l , mid2+1 , high , key)
        else :
            return TernarySearch(l , mid1 + 1 , mid2 - 1 , key)
        
# Chocolate Problem
        
def isPossible(l , N , K , height):
    sum = 0
    for i in l:
        if i > height:
            sum += i - height
    return (sum>=K)


def ChocolateProblem(l , N , K ):
    high = max(l)
    low = 0
    while high-low > 1:
        mid = (high+low)//2
        if isPossible(l , N , K , mid):
            low = mid
        else:
            high = mid-1
    if isPossible(l , N , K , high):
        return high
    else:
        return low

def ThreeLargestNumber()


if __name__ == '__main__':
    import random

    l = random.choices(range(1,10000), k=1000)
    # print(l)
    random.shuffle(l)
    l.append(7890)
    l.sort()
    b = linearSearch(l ,7890)
    print(b)

    # l.sort()
    # print(l)
    a = Binarysearch(l , 0 , len(l) , 7890)
    c = TernarySearch(l , 0 , len(l) , 7890)
    print(l[a-1])
    print(l[a])
    print(l[a+1])

    print(c)
    print(ChocolateProblem(l , len(l) , 899))