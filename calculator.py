
def calculator(fn, op, ln) -> int:
    if op == "+":
        return fn + ln
    elif op == "-":
        return fn - ln
    elif op == "*":
        return fn * ln
    elif op == "/":
        return fn / ln
    elif op == "**":
        return fn ** ln
    else:
        print("Invalid operator")



num1 = int(input("Whats your first number? ") or 2)


while True:
    op = input("Whats ur operator? ") or "+"
    num2 = int(input("Whats ur second number? ") or 3)
    num1 = calculator(num1, op, num2)
    print(num1)

    next = input("Do you want to add on to this answer? ").lower()

    if next in ["no", "n", "nope", "nah", "no thank you", "no thanks"]:
        break


print("Your final answer is " + str(num1))











    
    # if next in ["yes", "y", "ye", "yeah", "yep", "yup"]:
    #     # print(type(answer))
    #     calculator(num1, op, num2)
    # else:
    #     break
