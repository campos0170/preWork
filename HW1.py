#Problem 1 

def hello_name(USERNAME):

    print("Hello "+USERNAME+"!")
hello_name("Abraham")

#Problem 2

def first_Odds(n):
    for i in range(n):
        z = 2*i+1
        if z>100:
            continue
        else:
            print(z)


first_Odds(100)

#Problem 3

def max_num_in_list(a_list):
    max_ = a_list[0]
    for i in a_list:
        if i>max_:
            max_=i   
    print(max_)

max_num_in_list([1,2,3,42,1223422,123,45,64,23,1020,10102])

#Problem 5 

#function to determine if numbers are consecutive

con_ = [1,2,3,4,5,6]
nonc_=[1,3,34,4,78]

def is_consecutive(list_):
    t_ = []
    d = list_[1]-list_[0]
    n = len(list_)
    for i in range(n+1):
        if (i+1)>(n-1):
            break
        if (list_[i+1]-list_[i])!=d:   
            t_.append(False)
        else:
            t_.append(True)
    return all(t_)

    


# Problem 4

#function to determine if a specified year is a leap year.


def is_leap_year(year):

    if year % 4 == 0 and  ( year % 400==0 or year % 100!=0):

        print ("This is a leap year!")

    else:
        print("This is not a leap year!")

is_leap_year(2010)





