def BubbleSort(arr,n):  if(n>0):    for i in range(0,n):      if (arr[i]>arr[i+1]):        temp = arr[i]        arr[i] = arr[i + 1]        arr[i + 1] = temp    BubbleSort(arr, n - 1)arr=[]n = int(input("Enter the size of the array: "))print("Enter the Element of the array:")for i in range(0,n):  num = int(input())  arr.append(num)BubbleSort(arr, n - 1)print("After Sorting Array Elements are:")for i in range(0,n):  print(arr[i],end=" ")