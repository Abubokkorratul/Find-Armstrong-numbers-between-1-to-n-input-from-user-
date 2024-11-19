n = int(input("Enter a number (n): "))
print("Armstrong numbers between 1 and", n, ":")
for num in range(1, n + 1):
    sum_of_powers = sum(int(digit) ** len(str(num)) for digit in str(num))
    if sum_of_powers == num:
        print(num, end=" ")
