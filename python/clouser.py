def enclosing_function():
   myVar = 1117
   print("It is enclosing function which encloses a nested function.")

   def nested_function(val):
       print("I am in nested function and I can access myVar from my enclosing function's scope.")
       print("The value of myVar is:", myVar)
       
       myVar = myVar + 10
       temp = myVar + val
       print("Value after adding {} to {} is {}.".format(val, myVar, temp))

   nested_function(10)


# Execution
enclosing_function()