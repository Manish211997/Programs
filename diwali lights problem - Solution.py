# Approach
# find the Lcm of number from left to right
# If the number is 1 2 3 Then finding the LCM of 1 2 which is 2
# Then output of LCM of 1 2 that is 2
# now taking LCM of 2 3 then we get 6 which is the final answer


# down is the program to calculate the lcm of 2 numbers

def lcm_func(a,b):
    n=max(a,b)
    ind=1
    n2=max(a,b)
    while 1:
        if n%a==0 and n%b==0:
            break
        ind+=1
        n=n2*ind
    return n

# Taking test cases as input

Testcases = int(input())

# looping through the test cases

for i in range(Testcases):
    l = [int(x) for x in input().split()]      # taking input the timing of diwali lights

    le = len(l)

    lcm_var=l[0]                                # putting the first number of the input in the variable

    for i in range(1,le):                       #looping thought the list
        if lcm_var==0 or l[i]==0:
            lcm_var=-1
            break
        lcm_var=lcm_func(lcm_var,l[i])          #Calculating the lcm of the present and previous numbers lcm

    print(lcm_var)                              # printing the output
	
