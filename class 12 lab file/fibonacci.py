def fibonacci(max):
     a,b=0,1
     while a<max:
          yield a
          a,b=b,a+b
n=int(raw_input("Fibonacci values upto number:"))
for i in fibonacci(n):
     print i,
