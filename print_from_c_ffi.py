from cffi import FFI

ffi = FFI()
lib = ffi.dlopen('./c/print.so')
ffi.cdef('int print(char string[]);')
returned = lib.print(b'hello from python through cffi\n')
print(returned)
