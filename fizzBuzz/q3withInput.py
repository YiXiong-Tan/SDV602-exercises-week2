def fizz_buzz(fizz_on_multiple_of, buzz_on_multiple_of, up_to):
    i = 0
    listoftuples = []

    while i < up_to+1:
        tuples = []
        if(i % fizz_on_multiple_of == 0 and i % buzz_on_multiple_of == 0):
            tuples = (i,'fizzbuzz')

        elif(i % fizz_on_multiple_of == 0):
            tuples = (i,'fizz')

        elif(i % buzz_on_multiple_of == 0):
            tuples = (i,'buzz')

        else:
            tuples = (i,str(i))

        listoftuples.append(tuples)
        i = i + 1
    
    return listoftuples

def get_input(just_a_num):
    test = 0
    while True:
        try:
            if(just_a_num == 1):
                test = input("fizz on multiple of> ")
            if(just_a_num == 2):
                test = input("buzz on multiple of> ")
            if(just_a_num == 3):
                test = input("Up to> ")

            test = int(test)
            break
        except:
            print(f'Oops! {test} was not a number')

    return test

if __name__ == "__main__":

    print('--------\nFizzBuzz\n--------')

    fizz_on_multiple_of = get_input(1)
    buzz_on_multiple_of  = get_input(2)
    up_to = get_input(3)

    for i in fizz_buzz(fizz_on_multiple_of, buzz_on_multiple_of, up_to):
        print(f'The number is {i[0]}. The phrase is {i[1]}.')