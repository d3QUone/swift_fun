import math
operators = ["^", "*", "/", "+", "-"]
functions = ["sin", "cos", "exp", "tan", "ln", "log"]
numerals = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# --- evaulate RPN - OK ---
def count(a_list):
    exp = list(a_list)
    i = 0
    while len(exp) > 1:
        try:
            item = exp[i]
        except:
            return "ii-e" #"Incorrect input"
        if item in operators:
            try:
                a = float(exp[i-2])
                b = float(exp[i-1])
                if item == "^":
                    res = a**b
                elif item == "*":
                    res = a*b
                elif item == "/":
                    res = a/b
                elif item == "+":
                    res = a+b
                elif item == "-":
                    res = a-b
                exp[i-2] = res
                exp.pop(i-1)
                exp.pop(i-1)
                i = 0
            except:
                return "io-e" #"Incorrect operator"
        elif item in functions:
            try:
                a = float(exp[i-1])
                if item == "sin":
                    res = math.sin(a)
                elif item == "cos":
                    res = math.cos(a)
                elif item == "tan":
                    res = math.tan(a)
                elif item == "exp":
                    res = math.exp(a)
                elif item == "ln":
                    res = math.log(a, math.e)
                elif item == "log":
                    res = math.log(a, 10)
                exp[i-1] = res
                exp.pop(i)
                i = 0
            except:
                return "if-e" #"Incorrect function"
        else:
            i += 1
    return str(exp[0])


# func to add zero if needed - OK
def help_with_zero(exp):
    ooo = []
    ooppend = ooo.append
    b = ""
    i = 0
    n_o = 0
    while i < len(exp):
        char = exp[i]
        if char in operators:
            n_o += 1
            if len(b) > 0:
                ooppend(b)
                b = ""
        elif char in numerals:
            b += char
        i += 1
        if i == len(exp):
            ooppend(b)    
    if len(ooo) - n_o == 0:
        exp = "0" + exp
    return exp


# get power, OK
def operator_power(o):
    op = {"^": 4, "/": 3, "*": 3, "-": 2, "+": 2} #"-": 2, 
    try:
        return op[o]
    except:
        return None


# -------- create RPN -------- OK
def creplace(simple_input):
    inp = help_with_zero(simple_input) # it definitly has no spaces    
    print "CREPLACE input eval:", inp
    proc = ""
    stack = ""
    out = []; append = out.append
    i = 0
    while i < len(inp):
        item = inp[i]
        if item in numerals:
            proc += item
            if i == len(inp) - 1: append(proc) 
        elif item in operators:
            if proc != "":
                append(proc)
                proc = ""
            if len(stack) == 0:
                stack += item
            else:
                try: # do it on the whole stack
                    for t in range(len(stack)):
                        j = len(stack) - 1 #top-stack-index
                        a = int(operator_power(stack[j]))
                        b = int(operator_power(item))
                        if a >= b:
                            append(stack[j])
                            stack = stack[:j] + stack[j+1:]
                    stack += item
                except Exception as e:
                    print "operator-exception:", e, "item:", item
                    return "oe"
        else:
            return "ee"
        i += 1
    # add reversed stack to output
    i = len(stack) - 1
    while i >= 0:
        append(stack[i])
        i -= 1
    return out


# ---- MAIN ---- OK
def calc(exp):
    exp = exp.replace(" ", "")
    print "inp:", exp
    sub_exp = "" # a top-bracket exp 
    i = 0
    a = -1
    b = -1
    brackets = 0
    # this must simplyfy input to no-brackets expression
    while i < len(exp): #or len(exp) > 0
        if exp[0] == "(" and exp[len(exp)-1] == ")":
            exp = exp[1:-1]
            i = 0
            print "updated exp to", exp # just not to waste time
        char = exp[i]
        if char == "(":
            a = i
            brackets -= 1
        elif char == ")":
            b = i
            brackets += 1
            if a != -1 and b > a:
                # do calcs, replace by result:
                sub_exp = exp[a+1:b] 
                sub_RPN = creplace(sub_exp)
                sub_result = count(sub_RPN)
                if sub_result in ["ii-e", "io-e", "if-e"]:
                    return sub_result
                exp = exp[:a] + sub_result + exp[b+1:]
                print "sub:", sub_exp, "| full:", exp, " | b =", brackets
                i = -1 # cause +1 at the end -> i will be at the beginning 0
                brackets = 0 # cause starting from the beginning now
                a = -1
                b = -1
            else:
                print "i = {0}, smth wrong".format(i) # wrong input as usual
        i += 1
    if brackets == 0:
        sub_RPN = creplace(exp)
        exp = count(sub_RPN)
        print "finaly total simplify:", exp, ", bracket-balance - OK"
        return exp
    else:
        print "bracket-disbalance:", brackets
        return "disb"



# ---- test func ----
def test_stuff(name, function, cases):
    print "Doing tests of {0}...\n".format(name)
    # case[i] = [eq, ans]
    for case in cases:
        res = function(case[0])
        try:
            if abs(float(res) - float(case[1])) < 0.001:
                print "-OK: {0} = {1}".format(case[0], case[1])
            else:
                print "---Error: {0} != {1}".format(res, case[1])
        except:
            try:
                if res == case[1]:
                    print "-OK: {0} = {1}".format(case[0], case[1])
                else:
                    print "---Error: {0} != {1}".format(res, case[1])
            except:
                print "---Error:", res
        print " "


def test():
    # test transorming into RPN
    cases1 = [["11+3*9", ["11", "3", "9", "*", "+"]],
              ["1*2*3-4*5*6", ["1", "2", "*", "3", "*", "4", "5", "*", "6", "*", "-"]],
              ["-1-2", ["0", "1", "-", "2", "-"]]]
    test_stuff("CREPLACE", creplace, cases1)

    # test evaulation ready RPN
    cases2 = [[["11", "3", "4", "+", "10", "/", "+", "31", "-", "4", "2", "3", "40", "/", "-", "*", "+"], "-11.6"],
              [["1", "3", "8", "*", "+", "10", "-", "5", "-1", "*", "-"], "20"],
              [["8", "2", "5", "*", "+", "1", "4", "-", "2", "3", "*", "+", "/"], "6"]]
    test_stuff("COUNT", count, cases2)

    # testing both function on simple cases
    cases3 = [["4^2", "16"], ["41+57", "98"], ["2*4", "8"], ["9+0-3", "6"], ["2*3-1", "5"], ["12/3+1", "5"],
              ["12+3*41-33", "102"], ["40/8+10/10-2", "4"], ["2*3*4-5*6", "-6"], ["30-5/2+1", "28.5"], 
              ["-1.0-3", "-4"], ["-2*4.1", "-8.2"], ["0-10-20", "-30"], ["100-500-100", "-500"],
              ["-2*3*4+10-2.4/100", "-14.024"]]

    print "Doing tests of CREPLACE...."
    for case in cases3:
        buf = creplace(case[0])
        res = count(buf)
        try:
            if abs(float(res) - float(case[1])) < 0.001:
                print "OK: {0} = {1}".format(case[0], case[1])
            else:
                print "Error: {0} != {1}".format(res, case[1])
        except:
            print "Error:", res, "; buf:", buf
        print " " 

    # testing all together on any cases (but no functions yet)
    cases4 = [["1+(2+(3+4*(5+6)))", 50], ["(((1-2)-3)-4)-5", -13], ["(1 +3/(45* (33/44)-5))", 1.10434],
              ["30/(3+50)-11*(21-44/11)", -186.4339], ["(30/(3+50)-11*(21-44/11))", -186.4339],
              ["(30/(3+50)-11*(21-44/11)", "disb"]]
    test_stuff("MONSTER CALC", calc, cases4)
