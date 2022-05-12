def isPrime(n):
    result= "Number is prime"
    if n <2:
        result = "Please enter a number greater than 2"
    elif n%2 == 0:
        result = "Number is not prime"
    else:
        fifth = n//5
        for x in range(3, fifth):
            if n%x == 0:
                result = "Number is not prime"
                return result
    #return result


