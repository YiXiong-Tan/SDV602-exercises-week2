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

if __name__ == "__main__":
    for i in fizz_buzz(3, 5, 15):
        print(i)