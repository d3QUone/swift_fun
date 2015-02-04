import math

# ---- test func ----
def test_stuff(name, function, cases):
    print "Doing tests of {0}...".format(name)
    for case in cases:
        # case[i] = [eq, ans]
        res = function(case[0])
        if abs(float(res) - float(case[1])) < 0.001:
            print "OK: {0} = {1}".format(case[0], case[1])
        else:
            print "Error: {0} != {1}".format(res, case[1])
        print " "


# --- get power ---
def operator_power(o):
    op = {"^": 4, "/": 3, "*": 3, "-": 2, "+": 2}
    try:
        return op[o]
    except:
        return None

operators = ["^", "*", "/", "+", "-"]
functions = ["sin", "cos", "exp", "tan", "ln", "log"]

#def do_aryphmetics(char):

# --- evaulate RPN - OK ---
def count(a_list):
    exp = list(a_list)
    i = 0
    while len(exp) > 1:
        item = exp[i]
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
                print "ex", item
                return "Incorrect operator"
        elif item in functions:
            try:
                a = float(exp[i-1])
                # calcs ...
                res = "func-calc"
                exp[i-1] = res
                exp.pop(i)
                i = 0
            except:
                print "ex", item
                return "Incorrect function"
        else:
            i += 1
    return str(exp[0])


cases1 = [["(11+(3+4)/10-31+4*(2-3/40))", ["11", "3", "4", "+", "10", "/", "+", "31", "-", "4", "2", "3", "40", "/", "-", "*", "+"]],
         ["(1 +3*8- 10 -(-1)*5)", ["1", "3", "8", "*", "+", "10", "-", "5", "-1", "*", "-"]],
         ["((8+2*5)/(1+3*2-4))", ["8", "2", "5", "*" "+", "1", "4", "2", "3", "*", "+", "-", "/"]]]

cases2 = [[["11", "3", "4", "+", "10", "/", "+", "31", "-", "4", "2", "3", "40", "/", "-", "*", "+"], "-11.6"],
          [["1", "3", "8", "*", "+", "10", "-", "5", "-1", "*", "-"], "20"],
          [["8", "2", "5", "*", "+", "1", "4", "-", "2", "3", "*", "+", "/"], "6"]]
#test_stuff("COUNT", count, cases2)


# -------- create RPN -------- 
def creplace(simple_input):
    inp = simple_input # it definitly has no spaces
    print "input eval:", inp
    proc = ""
    stack = ""
    out = []
    append = out.append
    numerals = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
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
            # magic goes below
            if len(stack) == 0: stack += item
            else:
                try:
                    # do it on the whole stack
                    for t in range(len(stack)):
                        j = len(stack) - 1 #top-stack-index
                        a = int(operator_power(stack[j]))
                        b = int(operator_power(item))
                        if a >= b:
                            print "pop stack({0}): {1}".format(j, stack[j])
                            append(stack[j])
                            stack = stack[:j] + stack[j+1:]
                        else:
                            print "push to stack({0}): {1}".format(j, item) 
                    stack += item
                except Exception as e:
                    print "operator-exception:", e, "item:", item
                    return "operator error"
        else:
            return "error"
        i += 1
    # add reversed stack to output
    i = len(stack) - 1
    print "len =", len(stack)
    while i >= 0:
        append(stack[i])
        i -= 1
    print "out:", out
    return out


cases3 = [["4^2", "16"], ["41+57", "98"], ["2*4", "8"], ["9+0-3", "6"], ["2*3-1", "5"], ["12/3+1", "5"],
          ["12+3*41-33", "102"], ["40/8+10/10-2", "4"], ["2*3*4-5*6", "-6"], ["30-5/2+1", "28.5"]]
print "Doing tests of CREPLACE...."
for case in cases3:
    buf = creplace(case[0])
    res = count(buf)
    if abs(float(res) - float(case[1])) < 0.001:
        print "OK: {0} = {1}".format(case[0], case[1])
    else:
        print "Error: {0} != {1}".format(res, case[1])
    print " "
        
