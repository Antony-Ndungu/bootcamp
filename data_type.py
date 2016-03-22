def data_type(arg): 
    """The function 'data_type()' returns results based on arguments supplied to the function
    @params arg
    """
    if type(arg) == str:   #if arg is a string return the length of the string
        return len(arg)
    elif arg == None:      #if arg is equal to None return 'no value'
        return "no value"
    elif type(arg) == bool:  #if the type of arg is equal to bool return arg
        return arg
    elif type(arg) == int:   #if the type of arg is int
        if(arg < 100):
            return "less than 100"
        else:
            return "more than 100"
    elif type(arg) == list:
        if(len(arg) > 2):
            return arg[2]
        else:
            return None