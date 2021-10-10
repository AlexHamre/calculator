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
            print("Error-blank")

        elif a[b] == "+":
            pre_op = a[:b]
            post_op = a[b + 1:]
            try:
                answer = float(pre_op) + float(post_op)
            except:
                print("Error-plus")

        elif a[c] == "-":
            pre_op = a[:c]
            post_op = a[c + 1:]
            try:
                answer = float(pre_op) - float(post_op)
            except:
                print("Error-minus")

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

        try:
            print(answer)
        except:
            print("Error-no answer")
        answer = ""
        del answer