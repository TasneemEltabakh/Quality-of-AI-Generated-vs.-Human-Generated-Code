n=int(input("Enter the range of number(Limit):"))i=1pr=0while i<=n:  if(i%2==0):    pr=2*pow(i, 2) +1    print(pr,end=" ")  else:    pr = 2*pow(i, 2) - 1    print(pr, end=" ")  i+=1