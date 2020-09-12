print ( "PLEASE ENTER YOUR FULL NAME ")
first_name = input (" First name : ")
last_name = input (" Last name: ")
#calculating age

#exception handling using try statment
try:
    import datetime

    print("PLEASE ENTER YOUR DATE OF BIRTH ")
    Year = int(input("YEAR: "))
    Month = int(input(" MONTH: "))
    Day = int(input(" DAY:  "))
    Date_Of_Birth = datetime.datetime(Year, Month, Day)
    Age = (datetime.datetime.now() - Date_Of_Birth)
    age_in_days = int(Age.days)  # it helps to convert time into days.#
    Age_in_Years = age_in_days // 365
    print("Your are age is " + str(Age_in_Years) + "!!")
except Exception:
    print( "entered date is incorrect")

#ensuring the entered name is correct

first_byte = bytes (first_name, "ascii")
last_byte = bytes (last_name, "ascii")
year_byte = bytes(str(Year), "ascii")
Month_byte = bytes(str(Month), "ascii")
day_byte = bytes (str(Day), "ascii")
age_byte = bytes (str(Age_in_Years), "ascii")
binaryFN = (''.join(["{0:b}".format(x) for x in first_byte]))
binaryLN = (''.join(["{0:b}".format(y) for y in last_byte]))
binaryYear = (''.join(["{0:b}".format(v) for v in year_byte]))
binaryMonth = (''.join(["{0:b}".format(q) for q in Month_byte]))
binaryDay = (''.join(["{0:b}".format(t) for t in day_byte]))
binaryAge = (''.join(["{0:b}".format(e) for e in age_byte]))
bin_list1 = list(binaryFN)
bin_list2 = list(binaryLN)
bin_list3 = list(binaryYear)
bin_list4 = list(binaryMonth)
bin_list5 = list(binaryDay)
bin_list6 = list(binaryAge)
print (bin_list1)
#print (bin_list2)
#print (bin_list3)
#print (bin_list4)
#print (bin_list5)
#print (bin_list6)



#============counting zeros and ones in binary form of entered names==========#
#this is for first name:

onesFN = 0
zerosFN = 0
for object in bin_list1:
   if object == "1":
       onesFN = onesFN + 1
   elif object == "0":
       zerosFN = zerosFN + 1
print ("the total number of ones in binary form of first name is ",onesFN)
print ("the total number of zero in binary form of first name is", zerosFN)


# this is for last name:

onesLN = 0
zerosLN = 0
for object in bin_list2:
   if object == "1":
       onesLN =onesLN + 1
   elif object == "0":
       zerosLN = zerosLN + 1
print ("the total number of ones in binary form of last name is ",onesLN)
print ("the total number of zero in  binary form of last name is",zerosLN )


# this is for year
onesYear = 0
ZerosYear = 0
for object in bin_list3:
   if object == "1":
       onesYear =onesYear + 1
   elif object == "0":
       ZerosYear = ZerosYear + 1
print ("the total number of ones in binary form of year is ",onesYear)
print ("the total number of zero in  binary form of year is",ZerosYear )

#this is for month

onesmonth = 0
Zerosmonth = 0
for object in bin_list4:
   if object == "1":
       onesmonth =onesmonth + 1
   elif object == "0":
       Zerosmonth = Zerosmonth + 1
print ("the total number of ones in binary form of Month is ",onesmonth)
print ("the total number of zero in  binary form of Month is",Zerosmonth )

# this is for days

onesday = 0
Zerosday = 0
for object in bin_list5:
   if object == "1":
       onesday =onesday + 1
   elif object == "0":
       Zerosday = Zerosday + 1
print ("the total number of ones in binary form of Day is ",onesday)
print ("the total number of zero in  binary form of Day is",Zerosday )

# this is for Calculated age

onesage = 0
Zerosage = 0
for object in bin_list6:
   if object == "1":
       onesage =onesage + 1
   elif object == "0":
       Zerosage = Zerosage + 1
print ("the total number of ones in binary form of age is ",onesage)
print ("the total number of zero in  binary form of age is",Zerosage )



#just creating some random numbers to add with total numbers of ones and zeros so that it can come up with different value

import random
for x in range(100):
    y = random.randint(32,100)
converted_values = (onesLN,onesFN,zerosFN,zerosLN,onesYear,ZerosYear,onesmonth, Zerosmonth,onesday,Zerosday,onesage,Zerosage)
new_Values =[x+y for x in converted_values]
ascii_values = [char(x) for x in new_Values]




# ----Ascii values for password generator-------------#

import _string
from random import *


PASSWORD = "".join(choice (ascii_values)for x in range (randint(6,6)))
print (" Your generted six character password is", PASSWORD )
