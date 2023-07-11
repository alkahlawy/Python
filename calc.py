num1 = float(input("please enter the first num")) 
op = input("please enter the operator")
num2 = float(input("please enter the second num"))

if(op=="+"):
    sum = num1 + num2
    print("the answer is :" , sum)
elif (op == "-"):
    diff = num1 - num2
    print("the answer is : " , diff)
elif (op == "*"):
    mul = num1 * num2
    print("the answer is : " , mul)
elif (op == "/"):
    if(num2 == 0):
        print ("division by zero error!")
    else :
        div = num1 / num2
        print("the answer is : " , div)
