"""
Scans a csv file redirected into the script
 "--header" indicates the first row is a header row
"""
import sys as sys
import argparse
from typing import Type

def scan(has_header=False):
    print(f"has_header={has_header}")
    result = []
    values = []
    do_header = has_header
    header_names = {}
    try:
        for aline in sys.stdin:
            this_line = aline.strip().split(',')
            if do_header:
                header_names = this_line
                do_header = False
            else:
                a_dict = {}
                for i in range(0,len(this_line)):
                    if has_header :
                        a_dict[header_names[i]]= this_line[i]
                    else:
                        a_dict[i]= this_line[i]

                result += [a_dict]
                values += [this_line]

                print(result)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return result,values

    return result,values

# Exercise one
def sum_of(column_name, a_list_of_dictionary):
    """
    Return one value that is the sum of the column 
    column_name of each "row" (dictionary)
    """
    set_of_keys = a_list_of_dictionary[0].keys()
    sum = 0
    sum_performed = False

    for key in set_of_keys:
        if(str(key) == str(column_name)):   
            for a_dictionary in a_list_of_dictionary:
                try:
                    sum += int(a_dictionary[key])
                    sum_performed = True
                except:
                    sum = None
                    continue

    if sum_performed == False:
        sum = None

    return sum
    
          
#Exercise Two
def multiple_cols(column_names,a_list_of_dictionary):
    """
    Return a new list of "rows" (dictionary)
    That multiples the values of the named columns
    
    """
    multiples_of_columns = []
    set_of_keys = a_list_of_dictionary[0].keys()

    #match keys
    matched_keys = []
    for key in set_of_keys:
        for column_name in column_names:
            if(str(key).strip() == str(column_name).strip()):
                matched_keys.append(key)

    for matched_key in matched_keys:
        multiple_of_column = 1
        for a_dictionary in a_list_of_dictionary:
            try:
                # print(a_dictionary[matched_key])
                multiple_of_column *= int(a_dictionary[matched_key])
            except:
                multiple_of_column = None
                continue
        
        multiples_of_columns.append(multiple_of_column)

    return multiples_of_columns
    
    

#Exercise Three
# - fix display_table so that the columns all line up
def display_table(a_list_of_dictionary):
    lines = ""
    # Get a header line
    a_dictionary = a_list_of_dictionary[0]
    header_line = ""
    for key in a_dictionary:
        header_line += f'{str(key).strip()}\t'
    header_line = header_line.strip()

    # Make up the table
    lines += header_line 

    for a_dictionary in a_list_of_dictionary:
        a_line = ''
        for key,value in a_dictionary.items():
            #trim the blanks off the left and right of the string
            a_line += f'{value.strip()}\t'
        a_line = a_line.strip()
        lines += f'\n{a_line}'
    print(lines)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan some rows into a list of one list per line.")
    parser.add_argument('--header',action='store_true',help='The first row is a header row.')
    args = vars(parser.parse_args())
    # print(f'The args are {args}')
    print(parser.parse_args())
    #args = sys.argv
    #print(f'The args are {args}')
    dict_lst,values_lst = scan(args['header'])
    display_table(dict_lst)

    # Exercise 1 - sum of column specified
    #column_name = '2'
    #print(f'The sum of column {column_name} is {sum_of(column_name, dict_lst)}')
    
    # Exercise 2 - 
    # column_names = ['Value','Length']
    # multiples_cols = multiple_cols(column_names,dict_lst)

    # while True:
    #     if(len(multiples_cols) != 0):
    #         print(f'The multiple of column {column_names[0]} is {multiples_cols[0]}')
    #         del multiples_cols[0]
    #         del column_names[0]
    #     else:
    #         break



   

