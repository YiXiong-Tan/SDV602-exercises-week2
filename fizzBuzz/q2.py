def fizz_buzz(up_to):
    result = ''
    i = 0
    
    while i < up_to+1:
        
        if(i % 3 == 0 and i % 5 == 0):
            print('fizzbuzz')

        elif(i % 3 == 0):
            print('fizz')

        elif(i % 5 == 0):
            print('buzz')

        else:
            print(i)

        i = i + 1

if __name__ == "__main__":
    fizz_buzz(15)