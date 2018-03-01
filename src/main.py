from Crypto.Hash import SHA
from Crypto.Cipher import ARC4 as A
import foo


def do_some_other_stuff():
    foo = 'bar'
    cipher = A.new('tempkey')

    f = foo.Foo()

    return foo



def main():
    print 'This is for test purposes only'
    hash1 = hashlib.sha512()


    h = SHA.new()
    h.update(b'Hello')
    print h.hexdigest()

    do_some_other_stuff()
