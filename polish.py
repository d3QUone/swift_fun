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
        elif char not in ["(", ")"] and char in numerals:
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
                exp.pop(i-1) #gap, cause no all moved to left...
                print "i={0}: {1}".format(i, exp)
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
    print "inp", inp
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
        elif item in operators:
            stack += item
            if proc != "":
                appen(item)
                proc = ""

            
        else:
            return "error"
    return out


cases3 = [["41+57", "98"], ["2*4", "8"], ["9+0-3", "6"], ["30-5/2+1", "28.5"], 
         ["12/3+1", "5"], ["40/8+10/10-2", "4"]]
test_stuff("CREPLACE", creplace, cases3)



# ---- UNIVERSAL TEST FUNCTION ----

def test_stuff(name, function, cases):
    print "Doing tests of", name
    for case in cases:
        # case[i] = [eq, ans]
        res = function(case[0])
        if res == case[1]:
            print "OK: {0} = {1}".format(case[0], case[1])
        else:
            print "Error: {0} != {1}".format(res, case[1])
        
