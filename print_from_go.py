import ctypes
lib = ctypes.CDLL('./go/printer.so')
string_to_print = "hello from python to go"
lib.Print.restype = ctypes.c_char_p
returned = lib.Print(string_to_print)
print(ctypes.cast(returned, ctypes.c_char_p).value)
