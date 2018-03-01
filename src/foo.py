from Crypto.Cipher import Blowfish
import ansible.runner

class Foo:
    def __init__(self):
        self.f = 123

    def risky_stuff(self):
        bs = Blowfish.block_size
        key = b'An arbitrarily long key'
        iv = Random.new().read(bs)
        cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)

        return cipher

    def bar(self):
        runner = ansible.runner.Runner(
            module_name='ping',
            module_args='',
            pattern='web*',
            forks=10
        )
        datastructure = runner.run()
