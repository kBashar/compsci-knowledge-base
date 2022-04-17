1. A Go file starts with a package statement. Programs run from ```package main```. 
2. In import we are importing packages.
3. Random number genrator is deterministic, same seed generates same random number in same environment.
4. grouping all imports in a parenthesized style is called **factored import statement**.  
   ```go
    import (
        "fmt"
        "math"
    )
   ```
5. In Go, a name is exported if it starts with a capital letter. 
6. first variable name then type.
7. A function can return multiple values.
8. There is named return value
    ```go
        func split(sum int) (x, y int) {
	        x = sum * 4 / 9
	        y = sum - x
	        return
        }
    ```
9. A variable is declared in package or function level. 
10. `var` statement declares a variable list. 
    ```go
        var python, java, c bool
        var name string
        var i int
    ```
11. A `var` declaration can have value intializer one per variable.  
    If a value is initialized type is need not be declared.
    ```go
        var i, j int = 1,2
        var python, java, go = true, true, "Nein"
    ```
12. There is a variable declaration shorthand. It can only be used inside a function. Outside a function in package level only keywords like `var func` and such are allowed.
    ```go
        func some_func(){
           t := true
           python, java := "scripting", "oop"     
        }

13. Variables declared without an explicit initial value are given their **zero value**.  
    The zero value is:  
    
        0 for numeric types,
        false for the boolean type, and
        "" (the empty string) for strings.