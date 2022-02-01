#Main programme.
def birth_year(x):
    print("You were bron on :",x[:4])
    return
def gender(x):
    if x[4:7]>"1" and x[4:7]<"366":
        print("You are male")
    elif x[4:7]>"501" and x[4:7]<"866":
        print("You are female")
    return

