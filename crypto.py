import binascii

def strxor(a, b):     # xor two strings
    if len(a) > len(b):
        return "".join(["%s" % (ord(x) ^ ord(y)) for (x, y) in zip(a, b)])
    else:
        return "".join(["%s" % (ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

"""
key = binascii.hexlify('12ef')
m1= binascii.hexlify('abcd')

CT = "0x30293fa" # also 50500602
CT_hexlify = "3530353030363032"
print binascii.hexlify('50500602')

print strxor(CT_hexlify, key)
print m1

print key, m1
print hex(31326566), hex(61626364)
print strxor(key, m1) # this outputs 50500602

print binascii.hexlify("50500602") #this differs radically from the hex() function, below.
print hex(50500602) # this outputs 0x30293fa
print strxor(key, CT) # this outputs 37302412580. Should be m1 again. In fact it is not!
print hex(37302412580) # 0x8af65a524

print strxor(CT, m1) #Should be the key. Outputs 67352410582.
print hex(67352410582) # 0xfae8439d6
"""

print hex(int("12ef", 16) ^ int("abcd", 16))

print ""

CT = "09e1c5f70a65ac519458e7e53f36"
dawn = "61747461636b206174206461776e"
hexkey2 = "0x6895b196690e8c30e07883844858L"
CT_prime = "9e1c5f70a65ac519458e7f13b33"

key = "6882584180668208783833014078833834481583"
hexkey = "0x1439e17f30590b098c428d270cb95257afL"
altkey = "09156212201430841026901218576037193"
dawn2 = "61747461636b61746461776e"
key2 = "68825841806682087878225150398208380"
dawnxor = "6882584180668208783833014078833834481583"
dawn2xor = "68825841806682087878225150398208380"

print binascii.hexlify("attack at dusk")

print hex(int("09e1c5f70a65ac519458e7e53f36", 16) ^ int("61747461636b206174206461776e", 16))
print ""
print hex(int("6895b196690e8c30e07883844858", 16) ^ int("61747461636b206174206461776e", 16))
print ""

print hex(int("6895b196690e8c30e07883844858", 16) ^ int("61747461636b206174206475736b", 16))
""

print hex(int(CT, 16) ^ int(dawn, 16))
