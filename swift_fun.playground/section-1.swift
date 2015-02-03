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
    /*
    let ava_Operators = ["(", ")", "+", "-", "*", "/"]
    let ava_Consts = ["PI", "E"]
    let ava_Funcs = ["cos", "sin", "exp"]
    */
    // fix smth to add more signs into expr

    let available = [["cos", "sin", "exp"], ["(", ")", "+", "-", "*", "/"], ["PI", "E"]]
    
    var res = [String]()
    for i in 0..<amount {
        var s = ""
        let len: Int = Int(arc4random_uniform(10)+1)*2
        for j in 0..<len {
            let group_num: Int = Int(arc4random_uniform(3))
            let group_len: Int = countElements(available[group_num])
            let item_num: Int = Int(arc4random_uniform(UInt32(group_len)))
            
            let item = available[group_num][item_num]
            var spaces: String = ""
            for sp in 0..<group_num {
                spaces += " "
            }
            
            if group_num == 0 {
                s += item + spaces + "(" + spaces
            }
            else {
                let num: String = String(arc4random_uniform(100))
                s += item + spaces + num + " "
            }
        }
        res.append(s)
    }
    return res
}

func do_calc(input: String) -> Float {
    var out: Float = 0.0
    // ???
    var brackets: Int = 0
    
    return out
}

// do tests...
var math_input = create_test_cases(10)
for test_case in math_input {
    println(do_calc(test_case))
}


