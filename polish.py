
# ---- UNIVERSAL TEST FUNCTION ----

def test_stuff(name, function, cases):
    print "Doing tests of", name
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
    op = {"*": 4, "/": 4, "+": 3, "-": 2}
    try:
        return op[o]
    except:
        return None


# create RPN
def polish(exp):
    exp = exp.replace(" ", "").split("")
    stack = []    
    s_append = stack.append
    i = 0
    operators = ["*", "/", "+", "-"]
    numerals = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while len(exp) > 1:
        char = exp[i]
        if char in operators:
            try:
                a = float(exp[i-2])
                b = float(exp[i-1])
                if item == "*":
                    res = a*b
                elif item == "/":
                    res = a/b
                elif item == "+":
                    res = a+b
                elif item == "-":
                    res = a-b
                exp[i-2] = res
                exp.pop(i-1)
                exp.pop(i-1) #gap, cause no all moved to left...
                print "i={0}: {1}".format(i, exp)
                i = 0
            except:
                print "ex", item
                return "Incorrect char"
        #elif char not in ["(", ")"] and char in numerals:
            # numeral
            # ????
    return res


cases1 = [["(11+(3+4)/10-31+4*(2-3/40))", ["11", "3", "4", "+", "10", "/", "+", "31", "-", "4", "2", "3", "40", "/", "-", "*", "+"]],
         ["(1 +3*8- 10 -(-1)*5)", ["1", "3", "8", "*", "+", "10", "-", "5", "-1", "*", "-"]],
         ["((8+2*5)/(1+3*2-4))", ["8", "2", "5", "*" "+", "1", "4", "2", "3", "*", "+", "-", "/"]]]
#test_stuff("transforming into RPN", polish, cases1)


# evaulate RPN - OK
def count(a_list):
    exp = list(a_list)
    operators = ["*", "/", "+", "-"]
    i = 0
    while len(exp) > 1:
        item = exp[i]
        if item in operators:
            try:
                a = float(exp[i-2])
                b = float(exp[i-1])
                if item == "*":
                    res = a*b
                elif item == "/":
                    res = a/b
                elif item == "+":
                    res = a+b
                elif item == "-":
                    res = a-b
                exp[i-2] = res
                exp.pop(i-1)
                exp.pop(i-1) #gap, cause no all items were moved to left...
                #print "i={0}: {1}".format(i, exp)
                i = 0
            except:
                print "ex", item
                return "Incorrect char"
        else:
            i += 1
    return str(exp[0])


cases2 = [[["11", "3", "4", "+", "10", "/", "+", "31", "-", "4", "2", "3", "40", "/", "-", "*", "+"], "-11.6"],
          [["1", "3", "8", "*", "+", "10", "-", "5", "-1", "*", "-"], "20"],
          [["8", "2", "5", "*", "+", "1", "4", "-", "2", "3", "*", "+", "/"], "6"]]
#test_stuff("COUNT", count, cases2)
    


# ---------------------- new style -----------------------

def creplace(simple_input):
    inp = simple_input # it definitly has no spaces
    print "input eval:", inp
    proc = ""
    stack = ""
    out = []
    append = out.append
    i = 0
    operators = ["*", "/", "+", "-"]
    numerals = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
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
                    a = int(operator_power(stack[0]))
                    b = int(operator_power(item))
                    if a > b:
                        while a > b and len(stack) > 0:
                            append(stack[0])
                            stack = stack[1:]
                            if len(stack) > 0: 
                                a = int(operator_power(stack[0]))
                                b = int(operator_power(item))                        
                    stack += item
                except Exception as e:
                    print "operator-exception:", e, "item:", item
                    return "operator error"
        else:
            return "error"
        i += 1
    out += list(stack)
    print "out:", out
    return out


cases3 = [["41+57", "98"], ["2*4", "8"], ["9+0-3", "6"], ["30-5/2+1", "28.5"], 
         ["12/3+1", "5"], ["40/8+10/10-2", "4"]]
print "Doing tests of CREPLACE"
for case in cases3:
    buf = creplace(case[0])
    res = count(buf)
    if abs(float(res) - float(case[1])) < 0.001:
        print "OK: {0} = {1}".format(case[0], case[1])
    else:
        print "Error: {0} != {1}".format(res, case[1])
    print " "
        
