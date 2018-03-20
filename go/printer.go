package main

import (
	"C"
	"fmt"
)

//export Print
func Print(input *C.char) *C.char {
	goInput := C.GoString(input)
	fmt.Println(goInput)
	return C.CString("thanks yall")
}

func main() {}
