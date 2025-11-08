def my_function():
    local_variable ="I am local"
    print(local_variable)
    my_function()
    def outer_function():
        enclosing_variable = "I am enclosing"
        def inner_function():
            print(enclosing_variable)
        inner_function()
    outer_function()
    global_variable = "I am global"
    def my_function():
        print(global_variable)
    my_function()
    print(global_variable)
    result=len("hello,world!")
    print(result)