def DecimalToBinary(n):  if n==0:    return 0  else:    return (n% 2 + 10 * DecimalToBinary(n // 2))n=int(input("Enter the Decimal Value:"))print("Binary Value of Decimal number is:",DecimalToBinary(n))