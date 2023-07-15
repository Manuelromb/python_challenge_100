print("hello, this is the beginning")

while True:
        try:
                n = int(input("inform a number: "))
        except ValueError:
                print("You didn't input a number, try again")
                continue
        
        print(f"your number is {n}")
        break
