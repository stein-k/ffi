from ctypes import cdll, c_char_p, create_string_buffer

lib = cdll.LoadLibrary('./c/print.so')
string_to_print = b"hello from python to c\n"
returned = lib.print(string_to_print)
print(returned)
