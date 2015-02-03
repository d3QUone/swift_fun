import Darwin
import UIKit
println("Working with functions\n")

// creates a line of a given str
func 🏫🏫🏫(😄: String, 🙊:[String]){
    var persons = countElements(😄)
    var verb: String
    if persons == 0 {
        verb = "Somebody has "
    }
    else if persons == 1 {
        verb = " has "
    }
    else {
        verb = " have "
    }
    if countElements(🙊) == 0 {
        println(😄 + verb + "no animals")
    }
    else {
        for 🐼 in 🙊 {
            println(😄 + verb + 🐼)
        }
    }
    println("-------------------")
}

🏫🏫🏫("😃 and 😉", ["🐶", "🐺", "🐱"])
🏫🏫🏫("😳", ["😾"])
🏫🏫🏫("", [])
🏫🏫🏫("", ["👅", "👍", "👃", "💬"])


println("\nWorking with lists\n")
var out = [Int]()
for i in 1..<10 {
    var j = i*i
    out.append(j)
}
println(out)


println("\nTrying to work with interpretering math equals")
// creates random math equals
func create_test_cases(amount: Int) -> [String]{
    //               |-- correct cases --|-------------- incorrect cases ----------------|
    let available = [["cos", "sin", "exp", "ccs", "cosa", "sen", "sinn", "ex", "exponent"], ["+", "-", "*", "/", "(", ")"], ["PI", "E"], [""]]
    
    var res = [String]()
    for i in 0..<amount {
        var s = ""
        var brackets: Int = 0
        var sign: Int = 0
        let len: Int = Int(arc4random_uniform(10)+1)*2
        for j in 0..<len {
            let group_num: Int = Int(arc4random_uniform(4))
            let group_len: Int = countElements(available[group_num])
            let item_num: Int = Int(arc4random_uniform(UInt32(group_len)))
            let item = available[group_num][item_num]
            var spaces: String = ""
            if j < len - 1 {
                for sp in 0..<Int(arc4random_uniform(3)) {
                    spaces += " "
                }
            }
            if group_num == 0 {
                // function chosen
                s += item + spaces + "("
                brackets -= 1
            }
            else if group_num == 1 {
                // operator chosen
                if brackets < 0 {
                    // close bracket
                    s += item + spaces + ") "
                    brackets += 1
                }
                else {
                    s += item + spaces + " "
                }
            }
            else {
                // add sign between nums
                if sign < 0 {
                    sign += 1
                    s += available[1][Int(arc4random_uniform(4))]
                }
                // const or any numeral
                if item == "" {
                    s += String(arc4random_uniform(100)) + spaces
                }
                else {
                    s += item + spaces
                }
                sign -= 1
            }
        }
        res.append(s)
    }
    return res
}


func do_calc(input: String) -> String {
    println("Got: \(input)")
    let input_len: Int = countElements(input)
    var i: Int = 0
    var out: Float = 0.0
    var brackets: Int = 0
    var char: Character
    var queue = [String]()
    while i < input_len {
        char = input[advance(input.startIndex, i)]
        // get func.... fuck it's too complex now
        // add checkup on additional symbols e.g: sinax
        if char == "c" {
            if input[advance(input.startIndex, i+1)] == "o" {
                if input[advance(input.startIndex, i+2)] == "s"{
                    queue.append("cos")
                }
                else {
                    return "error: unknown constant"
                }
            }
            else {
                return "error: unknown constant"
            }
        }
        else if char == "s" {
            if input[advance(input.startIndex, i+1)] == "i" {
                if input[advance(input.startIndex, i+2)] == "n"{
                    queue.append("sin")
                }
                else {
                    return "error: unknown constant"
                }
            }
            else {
                return "error: unknown constant"
            }
        }
        else if char == "e" {
            if input[advance(input.startIndex, i+1)] == "x" {
                if input[advance(input.startIndex, i+2)] == "p"{
                    queue.append("exp")
                }
                else {
                    return "error: unknown constant"
                }
            }
            else {
                return "error: unknown constant"
            }
            
        }
        
        // ....
        
        i += 1
    }
    return "\(out)"
}

// run tests
var math_input = create_test_cases(15)
for test_case in math_input {
    println(do_calc(test_case))
}