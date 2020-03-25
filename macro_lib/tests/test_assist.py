#test file for macro_lib._assist

import macro_lib._assist as a

def testAskOnce():
    print("Start testing _ask_for_one()")
    print("----------------------------------------------------------------------")    
    output = a._ask_for_one_("This is a test. You can entered what ever you want," 
        + " but it has to be a list. "
        + "First try entering a non-list and see if the system"
        + " prompt return any error, "
        + "next try entering a string", type([]))
    if output == None:
        print ("quit function is working properly")
        print("--------------------------------")
        return ":)"
    if (input(f"Is what you have just entered {output}? Type yes, if it is\n").strip().lower() == 'yes'):
        print('Great!')
        print("-----------------------------------------------------")
        return ":)"
    else:
        print("the test has failed")
        return ":("

def testAsk():
    print("Start testing _ask_")
    print("-----------------------------------------------------")
    print("You will be prompted to enter three numbers")
    promptList = ["This is a test. You can entered what ever you want," 
        + "but this time it has to be a number. "
        + "First try entering a non-number and see if the system"
        + " prompt return any error, "
        + "next try entering a number"] * 3
    argumentList = [type(1), type(1)]
    print("-----------------------------------------------------")
    print("First we will check if the methods will accept matched arguments")
    try:
        a._ask_(promptList, argumentList)
        print("The function should not accept two inputs with different length")
        print("test failed")
        return ":("
    except:
        print("Good!")
    print("-----------------------------------------------------")
    print("Now we will test if the function will except argument other than a list")
    try:
        a._ask_("hello", "world")
        print("The function should not accept arguments other than list")
        print("test failed")
        return ":("
    except:
        print("Good!")
        argumentList.append(type(1))
    print("-----------------------------------------------------")
    result = a._ask_(promptList, argumentList)
    if result == None:
        print("quit() is functioning correctly")
        print("--------------------------------")
        return ":)"
    arg1, arg2, arg3 = result
    if input(f"is {arg1}, {arg2}, {arg3} the number you have Entered. If true type yes\n").strip().lower() == 'yes':
        print("success")
        return ":)"
    else:
        print("test failed")
        return ":("

if __name__ == "__main__":
    if testAskOnce() == ":)":
        if testAsk() == ":)":
            print("all tests cases have passed! :)")
        else:
            print("_ask_ () has issues :(")
    else:
        print("test failed :(")