count=0def NumberOfUpperCase(str,i):  global count  if (str[i] >= 'A' and str[i] <= 'Z'):    count+=1  if (i >0):    NumberOfUpperCase(str, i - 1)  return countstr=input("Enter your String:")NoOfUppercase=NumberOfUpperCase(str,len(str)-1)if(NoOfUppercase==0):  print("No UpperCase Letter present in a given string.")else:  print("Number Of UpperCase Letter Present in a given String is:",NoOfUppercase)