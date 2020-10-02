a=int(input("Enter a?"));
b=int(input("Enter b?"));
c=int(input("Enter c?"));
d=int(input("Enter d?"));

if a>b and b>c and c>d:
  print ("a is largest");
if b>a and b>c and b>d:
 print ("b is largest");
if c>b and c>b and c>d:
  print ("c is largest");
if d>a and d>b and d>c:
 print ("d is largest");