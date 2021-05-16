def check_prime(number):
    if ((number % 2 == 0 and number %3 == 0) and (number !=2 or number != 3)):
        return "Numer jo i thjeshte"
    else:
        return "Numer i thjeshte"
print (check_prime(5))