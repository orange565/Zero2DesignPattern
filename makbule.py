"this is homework"
#Görevler:
#1-Python Arithmetic Operators
x=7
y=5
print ("Number-1 is = ",x)
print ("Number-2 is = ",y)

#+	Addition	x + y
result = x+y
print("Result for Addition = " ,result)

#-	Subtraction	x - y	
result = x-y
print("Result for Subtraction = " ,result)

#*	Multiplication	x * y	
result = x*y
print("Result for Multiplication = " ,result)

#/	Division	x / y	
result = x/y
print("Result for Division = " ,result)

#%	Modulus	x % y	
result = x%y
print("Result for Modulus = " ,result)

#**	Exponentiation	x ** y	
result = x**y
print("Result for Exponentiation = " ,result)

#//	Floor division	x // y
result = x//y
print("Result for Floor division = " ,result)

###########################################################################
#Karşılaştırma Operatörleri

#==	Equal	x == y	
if x==y:
    print("Numbers are equal: ",x,"-",y)
else:
    print("Numbers are not equal: ",x,"-",y)

#!=	Not equal	x != y	
if x!=y:
    print("Numbers are not equal: ",x,"-",y)
else:
    print("Numbers are equal: ",x,"-",y)

#>	Greater than	x > y	
if x > y:
    print("Number-1 is greater than Number-2: ",x,"-",y)

#<	Less than	x < y	
if x < y:
    print("Number-1 is less than Number-2: ",x,"-",y)

#>=	Greater than or equal to	x >= y	
if x >= y:
    print("Number-1 is greater than Number-2 or equal: ",x,"-",y)

#<=	Less than or equal to	x <= y
if x <= y:
    print("Number-1 is less than Number-2 or equal: ",x,"-",y)

############################################################################
#Logical Operators
#and	
if(x>y and x>3):
    print("Number-1 is greater than Number-2 and Number-1 is greater 3",x,"-",y)

#or	
if(x>y or x>3):
    print("Number-1 is greater than Number-2 or Number-1 is greater 3",x,"-",y)

#not	
if not(x < y and x < 10):
    print("Number-1 is --not-- less than Number-2 and Number-1 is less than 10",x,"-",y)

#Atama Operatörleri
#Simple assignment operator ( = )
x=50;
print("Value After Simple assignment operator (=): ",x)

#Add and equal operator ( += )
x+=1;
print("Value After Add and equal operator ( +=1 ): ",x)

#Subtract and equal operator ( -= )
x-=1;
print("Value After Subtract and equal operator ( -=1 ): ",x)

#Asterisk and equal operator ( *= )
x*=2;
print("Value After Asterisk and equal operator ( *=2 ): ",x)

#Divide and equal operator ( /= )
x/=2;
print("Value After Divide and equal operator ( /=2 ): ",x)

#Modulus and equal operator ( %= )
x%=3;
print("Value After Modulus and equal operator ( %=3 ): ",x)

#Double divide and equal operator ( //= )
x//=3;
print("Value After Double divide and equal operator ( //=3 ): ",x)

#Exponent assign operator ( **= )
x**=3;
print("Value After Exponent assign operator ( **=3 ): ",x)


#Üyelik ve Kimlik Operatörleri

#Karşılaştırma ve Mantıksal Operatörlerin Kullanımı