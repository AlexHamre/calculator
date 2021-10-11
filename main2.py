# importing math and setting up a loop
import math

running = True
print("type exit to exit")
print("this calculator has +,-,*,/,!,sqrt,^,and more later")
while running:
    # the input
    a = input("write math: ")
    # code so you can exit
    if a == "exit":
        running = False
        print("exiting")
    else:
        # finds operators
        b = a.find("+")
        c = a.find("-")
        d = a.find("*")
        e = a.find("/")
        f = a.find("^")
        g = a.find("sqrt")
        h = a.find("!")

        # checks if you enter blank
        if a == "":
            print("Error-blank")

        # checks for operator and does appropriate math
        elif a[b] == "+":
            # pre_op is all numbers in a from zero to + (b in this case)
            pre_op = a[:b]
            # post_op is everything after +
            post_op = a[b + 1:]
            # This checks if it can properly add your numbers together
            try:
                answer = float(pre_op) + float(post_op)
                # If it can't add them it prints "Error-plus"
            except:
                print("Error-plus")

        # the rest is nearly the same as addition

        elif a[d] == "*":
            pre_op = a[:d]
            post_op = a[d + 1:]
            try:
                answer = float(pre_op) * float(post_op)
            except:
                print("Error-multiply")

        elif a[f] == "^":
            pre_op = a[:f]
            post_op = a[f + 1:]
            try:
                answer = float(pre_op) ** float(post_op)
            except:
                print("Error-power")

        elif a[g] == "s":
            pre_op = a[:g]
            try:
                answer = math.sqrt(float(pre_op))
            except:
                print("Error-Square")

        elif a[h] == "!":
            pre_op = a[:h]
            try:
                pre_op = int(pre_op)
                answer = (math.factorial(pre_op))
            except:
                print("Error-factorial")

        elif a[e] == "/":
            pre_op = a[:e]
            post_op = a[e + 1:]
            try:
                answer = float(pre_op) / float(post_op)
            except:
                print("Error-div")

        elif a[c] == "-":
            pre_op = a[:c]
            post_op = a[c + 1:]
            try:
                answer = float(pre_op) - float(post_op)
            # If - doesn't work it runs a check for a second - to fix -8-8
            except:
                # This finds the second - in the input, and tries again
                c = a.find("-", 1)
                pre_op = a[:c]
                post_op = a[c + 1:]
                try:
                    answer = float(pre_op) - float(post_op)
                except:
                    print("Error-minus")
                    
        # Tries to print the answer
        try:
            print(answer)
        # if the answer is undefined it prints an error
        except:
            print("Error-no answer")

        # makes the answer undefined again
        answer = ""
        del answer
