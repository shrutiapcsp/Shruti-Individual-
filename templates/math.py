# Define a class for Checking prime number
class Check :

    # Constructor
    def __init__(self,number) :
        self.num = number

    # define a method for checking number is prime or not
    def isPrime(self) :

        for i in range(2, int(num ** (1/2)) + 1) :

            # if any number is divisible by i
            # then number is not prime
            # so return False
            if num % i == 0 :
                return False

        # if number is prime then return True
        return True


# Main code
if __name__ == "__main__" :

    # input number
    num = 11

    # make an object of Check class
    check_prime = Check(num)

    # method calling
    print(check_prime.isPrime())

    num = 14
    check_prime = Check(num)
    print(check_prime.isPrime())