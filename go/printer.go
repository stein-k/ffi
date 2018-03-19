package main

import (
	"C"
	"fmt"
)

//export Print
func Print(input string) int {
	fmt.Println(input)
	return 15
}

func main() {}
