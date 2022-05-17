def ex1(num):
    try:
        return 6 / num
    except:
        print("You cannot divide with zero")




def ex2(index, my_tuple=(1,2,3,4,5)):
    try:
        return my_tuple[index]
    except:
        print("Index number out of range")




def ex3(name):
    try:
      return "hello" + name
    except:
        print("Can't assgin numbers with string type")



if __name__ == '__main__':
    # Run your functions here
    print("Good Luck!")