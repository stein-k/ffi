import ctypes
#lib = ctypes.cdll.LoadLibrary('./go/printer.so')
lib = ctypes.CDLL('./go/printer.so')
string_to_print = b"hello from python to go\n"
returned = lib.Print(string_to_print)
print(returned)
