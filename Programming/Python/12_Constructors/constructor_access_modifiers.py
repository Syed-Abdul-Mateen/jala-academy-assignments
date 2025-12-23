# Apply private, public, protected and default access modifiers to the constructor

class Sample:

    def __init__(self):
        print("Public Constructor")

    def _protected_init(self):
        print("Protected Constructor")

    def __private_init(self):
        print("Private Constructor")

s = Sample()
s._protected_init()
