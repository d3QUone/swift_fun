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
            
        
        
    return res

cases = [["(11+(3+4)/10-31+4*(2-3/40))", ["11", "3", "4", "+", "10", "/", "+", "31", "-", "4", "2", "3", "40", "/", "-", "*", "+"]],
         ["(1 +3*8- 10 -(-1)*5)", ["1", "3", "8", "*", "+", "10", "-", "5", "-1", "*", "-"]],
         ["((8+2*5)/(1+3*2-4))", ["8", "2", "5", "*" "+", "1", "4", "2", "3", "*", "+", "-", "/"]]]
    
print "Doing transforming into RPN"
for case in cases:
    res = polish(case[0])
    if res == case[1]:
        print "OK: {0} = {1}".format(case[0], case[1])
    else:
        print "Error: {0} != {1}".format(res, case[1])
        

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

cases2 = [
    [["11", "3", "4", "+", "10", "/", "+", "31", "-", "4", "2", "3", "40", "/", "-", "*", "+"], "-11.6"],
    [["1", "3", "8", "*", "+", "10", "-", "5", "-1", "*", "-"], "20"],
    [["8", "2", "5", "*", "+", "1", "4", "-", "2", "3", "*", "+", "/"], "6"]
    ]

print "Doing evaluations\n"
for case in cases2:
    res = count(case[0])
    if abs(float(res) - float(case[1])) <= 0.001:
        print "OK: {0} = {1}\n".format(case[0], case[1])
    else:
        print "Error in case {0}\n {1} != {2}".format(case[0], res, case[1])
