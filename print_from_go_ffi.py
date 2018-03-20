from cffi import FFI

ffi = FFI()
lib = ffi.dlopen('./go/printer.so')
ffi.cdef('char* Print(char string[]);')

returned = lib.Print(b'hello from python through cffi\n')
print(ffi.string(cdata=returned))