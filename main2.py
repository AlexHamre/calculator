# importing math and setting up a loop
import math
running = True
print("type exit to exit")
print("this calculator has +,-,*,/,!,sqrt,^,and more later")
while running:
    # an input
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

        # does the thing
        if a == "":
            print("Error2")

        elif a[b] == "+":
            pre_op = a[:b]
            post_op = a[b + 1:]
            try:
                answer = float(pre_op) + float(post_op)
            except:
                print("Error1")

        elif a[c] == "-":
            pre_op = a[:c]
            post_op = a[c + 1:]
            try:
                answer = float(pre_op) - float(post_op)
            except:
                print("Error1")

        elif a[d] == "*":
            pre_op = a[:d]
            post_op = a[d + 1:]
            try:
                answer = float(pre_op) * float(post_op)
            except:
                print("Error1")

        elif a[f] == "^":
            pre_op = a[:f]
            post_op = a[f + 1:]
            try:
                answer = float(pre_op) ** float(post_op)
            except:
                print("Error1")

        elif a[g] == "s":
            pre_op = a[:g]
            try:
                answer = math.sqrt(float(pre_op))
            except:
                print("Error1")

        elif a[h] == "!":
            pre_op = a[:g]
            try:
                pre_op = int(pre_op)
                answer = (math.factorial(pre_op))
            except:
                print("Error1")

        elif a[e] == "/":
            pre_op = a[:e]
            post_op = a[e + 1:]
            if post_op == 0:
                print("don't divide by zero")
            else:
                try:
                    answer = float(pre_op) / float(post_op)
                except:
                    print("Error1")

        try:
            print(answer)
        except:
            print("Error")
        answer = ""
