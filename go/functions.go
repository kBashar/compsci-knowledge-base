package main

import (
	"fmt"
)

func add(x, y int) int {
	return x + y
}

func swap(a, b string) (string, string) {
	return b, a
}

func main() {
	fmt.Printf("Sum of %d, %d is %d\n", 4, 5, add(4,5))
	a, b := swap("Hello", "world")
	fmt. Println(a, b)
}