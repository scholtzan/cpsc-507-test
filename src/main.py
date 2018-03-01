from Crypto.Hash import SHA
from Crypto.Cipher import ARC4 as A


def do_some_other_stuff():
    foo = 'bar'
    cipher = A.new('tempkey')

    return foo



def main():
    print 'This is for test purposes only'
    hash1 = hashlib.md5()


    h = SHA.new()
    h.update(b'Hello')
    print h.hexdigest()

    do_some_other_stuff()
