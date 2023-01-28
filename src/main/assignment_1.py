import numpy as np

import math

BiInputAsArray = np.array([0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,1])

BiInputAsList= BiInputAsArray.tolist()

#print(BiInputAsList)
def BinarayToDecimal(BinarayInput):
    
    Sign = 0
    if BinarayInput[0] == 0:
        Sign = (1)
    else: 
        Sign = (-1)
    
    ExpotentList = []
    for index,i in enumerate(BinarayInput[1:12]):
        ExpotentList.append((BinarayInput[i]) * (2**(10-index)))
    
    ExpotentTotal = 0
    for i in range(0, len(ExpotentList)):
        ExpotentTotal = ExpotentTotal + ExpotentList[i]
        
    
    MantisaList = [1]
    for index,i in enumerate(BinarayInput[12:]):
        if (BinarayInput[i] ==1):
            MantisaList.append((BinarayInput[i]) *(0.5)**(index+1))
            
    MantisaTotal = 0
    for i in range(0, len(MantisaList)):
        MantisaTotal = MantisaTotal + MantisaList[i]  
    
    ExpotentFinal = (ExpotentTotal-1023)
    
    BinarayToDecimal = (Sign) * ((2**ExpotentFinal) * (MantisaTotal))
    
    return BinarayToDecimal
  
Number1 = BinarayToDecimal(BiInputAsList) #This is string. Use float() to convert to float if needed
Number2 = math.floor(float(format(round(BinarayToDecimal(BiInputAsList),1), '3')))
Number3 = '%g'%(float(format(round(BinarayToDecimal(BiInputAsList)), '3f'))) 

def AbsoluteError (MeasuredValue, ApproximatedValue):
    
    diff = (MeasuredValue - ApproximatedValue)
    
    AbsoluteError = abs(diff)
    return AbsoluteError
  
def RelativeError (MeasuredValue, ApproximatedValue):
    
    diff = (MeasuredValue - ApproximatedValue)
    
    AbsoluteError = abs(diff)
    RelativeError = AbsoluteError / abs( MeasuredValue)
    
    return RelativeError
  
Number4_1 = AbsoluteError (float(Number1),float(Number3))
Number4_2 = RelativeError (float(Number1),float(Number3) )

#This section was taken from code given in class, then modified**
def func(x):
    return x*x*x - x*x + 2
def bisection_method(left: float, right: float, given_function: str):
    # pre requisites
    # 1. we must have the two ranges be on opposite ends of the function (such that
    # function(left) and function(right) changes signs )
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return
    tolerance: float = .0001
    diff: float = right - left
    # we can only specify a max iteration counter (this is ideal when we dont have all
    # the time in the world to find an exact solution. after 10 iterations, lets say, we
    # can approximate the root to be ###)
    max_iterations = 20
    iteration_counter = 0
    while (diff >= tolerance and iteration_counter <= 20):
        iteration_counter += 1
        # find function(midpoint)
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)
        if evaluated_midpoint == 0.0:
            break
        
        # find function(left)
        x = left
        evaluated_left_point = eval(given_function)
        
        # this section basically checks if we have crossed the origin point (another way
        # to describe this is if f(midpoint) * f(left_point) changed signs)
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint >0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0
        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)
        # OPTIONAL: you can see how the root finding for bisection works per iteration
    return (iteration_counter)
if __name__ == "__main__":
    # caveat with this method is it only finds sqrt(2)...how can we find a zero of any function?
    #babylonian_method(10)
    # bisection gives us#This section was taken from code given in class, then modified**
def custom_derivative(value):
    return (3 * value* value) + (8 * value)
def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    # remember this is an iteration based approach...
    iteration_counter = 0
    # finds f
    x = initial_approximation
    f = eval(sequence)
    # finds f' 
    f_prime = custom_derivative(initial_approximation)
    
    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)
        # finds f' 
        f_prime = custom_derivative(initial_approximation)
        # division operation
        approximation = f / f_prime
        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1
    return(iteration_counter)
if __name__ == "__main__":
    # newton_raphson method
    initial_approximation: float = 7
    tolerance: float = .0001
    sequence: str = "x**3 + (4*(x**2)) - 10"
    Number6_2 = newton_raphson(initial_approximation, tolerance, sequence) the first zero of any function to a certain error threshold
    left = -4
    right = 7
    function_string = "x**3 + (4*(x**2)) - 10"
    Number6_1 = bisection_method(left, right, function_string)
    
    
Number5 = "n.a"
Answers =  np.array([Number1, Number2, Number3, Number4_1, Number4_2, Number5, Number6_1, Number6_2])

print(Answers[0])
print()
print(Answers[1])
print()
print(Answers[2])
print()
print(Answers[3])
print(Answers[4])
print()
print(Answers[5])
print()
print(Answers[6])
print(Answers[7])
