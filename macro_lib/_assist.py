#module consists of functions aim to enable easy access to the library's functionality
from pathlib import Path

'''
Give a brief introduction to the functionality of this package. Load the 
text from the hidden file
'''
def introduce():
    with open(Path(__file__).parent / ".intro.txt") as f:
        print(f.read())

'''
Return the version of the library
'''
def version():
    print("1.0")

'''
Ask the user for appropriate input, which serves as the argument 
passed into the function that calls this method. It first prompt 
the user for input and then check whther the input is valid
'''
def _ask_for_one_(prompt, class_type):
    while True:
        user_input = input(str(prompt) + '\n').strip()
        if (user_input.lower() == "quit()"):
            return None
        #check to make sure the expression is valid
        try:
            arg = eval(user_input)
        except:
            print("Invalid expression. Please check your input again.")
            print("--------------------------------------------------")
            continue
        #check to make sure the expression matches with the expected argument type
        if (type(arg) == class_type):
            return arg
        else:
            print(f"you have entered a {str(type(arg))} but the argument required is {class_type}")
            print("---------------------------------------------------------------------------------")

'''
Ask the user for more than inputs, which serve as a list of arguments 
that will be passed into the function that calls this method. It calls
 _ask_for_one multiple times
'''
def _ask_(prompts, class_type_list):
    #check to make sure the arguments are valid
    if type(prompts) != type (list()) or type (class_type_list) != type(list()):
        raise ValueError("arguments must be a list")
    if len(prompts) != len(class_type_list):
        raise ValueError("there should be an equal number of prompts and argument types")
    else:
        output = []
        for i in range(len(prompts)):
            arg = _ask_for_one_(prompts[i], class_type_list[i])
            if (arg == None):
                return None
            output.append(arg)
        return output
