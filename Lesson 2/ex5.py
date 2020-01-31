while True:
    inp = input("name password ")
    a = inp.split()
    if a[1] == 'truepass':
        print("Password for user: "+a[0]+" is correct")
        break
    else:
        print("Password for user: "+a[0]+" is incorrect")
        print("Please try again")
