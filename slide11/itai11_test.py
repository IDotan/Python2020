from slide11 import itai11

test_string = "abcdefghijklmnopqrstuvwxyz"
result_string = "abcdefghijklmnopqrstuvwxyz"
jumps = 26
if itai11.encrypt_line(test_string, jumps) != result_string:
    raise EOFError
if itai11.decrypt_line(result_string, jumps) != test_string:
    raise EOFError

test_string = "abcdefghijklmnopqrstuvwxyz"
result_string = "bcdefghijklmnopqrstuvwxyza"
jumps = 27
if itai11.encrypt_line(test_string, jumps) != result_string:
    raise EOFError
if itai11.decrypt_line(result_string, jumps) != test_string:
    raise EOFError

test_string = "ab cdef ghijklmnopqrstuvwxyz"
result_string = "kl mnop qrstuvwxyzabcdefghij"
jumps = 10
if itai11.encrypt_line(test_string, jumps) != result_string:
    raise EOFError
if itai11.decrypt_line(result_string, jumps) != test_string:
    raise EOFError

test_string = "abcdefghijklmnopqrstuvwxyz*+"
result_string = "abcdefghijklmnopqrstuvwxyz*+"
jumps = 52
if itai11.encrypt_line(test_string, jumps) != result_string:
    raise EOFError
if itai11.decrypt_line(result_string, jumps) != test_string:
    raise EOFError

test_string = "abcdefghijklmnopqrstuvwxyz"
result_string = "fghijklmnopqrstuvwxyzabcde"
jumps = 5
if itai11.encrypt_line(test_string, jumps) != result_string:
    raise EOFError
if itai11.decrypt_line(result_string, jumps) != test_string:
    raise EOFError

test_string = "abcdefghijklmnopqrstuvwxyz 1234567890"
result_string = "stuvwxyzabcdefghijklmnopqr 1234567890"
jumps = 70
if itai11.encrypt_line(test_string, jumps) != result_string:
    raise EOFError
if itai11.decrypt_line(result_string, jumps) != test_string:
    raise EOFError

test_string = "abcdefghijklmnopqrstuvwxyz 1234567890"
result_string = "fghijklmnopqrstuvwxyzabcde 6789012345"
jumps = 5
if itai11.encrypt_line(test_string, jumps) != result_string:
    raise EOFError
if itai11.decrypt_line(result_string, jumps) != test_string:
    raise EOFError

test_string = "abcdefghijklmnopqrstuvwxyz1234567890"
result_string = "klmnopqrstuvwxyzabcdefghij1234567890"
jumps = 10
if itai11.encrypt_line(test_string, jumps) != result_string:
    raise EOFError
if itai11.decrypt_line(result_string, jumps) != test_string:
    raise EOFError

test_string = "abcdefghijklmnopqrstuvwxyz1234567890"
result_string = "mnopqrstuvwxyzabcdefghijkl3456789012"
jumps = 12
if itai11.encrypt_line(test_string, jumps) != result_string:
    raise EOFError
if itai11.decrypt_line(result_string, jumps) != test_string:
    raise EOFError

test_string = "abcdefghijklmnopqrstuvwxyz1234567890"
result_string = "uvwxyzabcdefghijklmnopqrst1234567890"
jumps = 20
if itai11.encrypt_line(test_string, jumps) != result_string:
    raise EOFError
if itai11.decrypt_line(result_string, jumps) != test_string:
    raise EOFError

test_string = "abcdefghijklmnopqrstuvwxyz 1234567890"
result_string = "wxyzabcdefghijklmnopqrstuv 3456789012"
jumps = 22
if itai11.encrypt_line(test_string, jumps) != result_string:
    raise EOFError
if itai11.decrypt_line(result_string, jumps) != test_string:
    raise EOFError
