balance = 550.90
while True:
    try:
        deposit = float (input) ("Enter the amount to deposit:")
        break
    except ValueError:
        print(f' please Enter the valid amount')
balance += deposit 
print(f'Total Balance is : {balance}') 
