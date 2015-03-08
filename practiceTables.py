from random import randint, shuffle

def multPrac(upper):
    a = randint(2,upper)
    b = randint(2,upper)
    return (a, b)

def divPrac(upper):
    a = randint(2,upper)
    b = randint(2,12)
    while a*b > upper:
        a = randint(2,upper)
        b = randint(2,12)
    lis = [a*b, b]
    #shuffle(lis)
    return lis

if __name__ == "__main__":
    try:
        if input("Choose m or d: ").upper() == 'D': 
            while(True):
                upper = int(input("Choose an upper bound: "))
                num = int(input("Number of practice problems: "))
                for i in range(0,num):
                    a,b = divPrac(upper)
                    formatLength = len(str(upper))
                    formatString = "{:" + str(formatLength) +"} ÷ {:" + str(formatLength) + "} = "
                    print(formatString.format(a,b))
        
        else:
            while(True):
                upper = int(input("Choose an upper bound: "))
                num = int(input("Number of practice problems: "))
                for i in range(0,num):
                    a,b = multPrac(upper)
                    formatLength = len(str(upper))
                    formatString = "{:" + str(formatLength) +"} x {:" + str(formatLength) + "} = "
                    print(formatString.format(a,b))
    except ValueError:
            print("Goodbye!!!")
