for x in range(1,41):
    if x % 5 == 0 and x % 7 != 0:
        print(str(x)+" is divided by 5")
    elif x % 7 == 0 and x % 5 != 0:
        print(str(x)+" is divided by 7")
    elif x % 5 == 0 and x % 7 == 0:
        print(str(x)+" is divided by 5 and 7")
    elif x ==13:
        pass
    else:
        print(str(x)+" is not impotrant")