ip = "220.4.8.0"
prefix = 24
numberOfSubnetsDesired = 2


def decimalToBinary(n):
    x = str(bin(n).replace("0b", ""))
    while len(x) < 8:
        x = "0" + x
    return x + "."

def binaryToCIDR(n):
    return '.'.join([str(int(x, 2)) for x in n.split(".")])

def makeMask(n):
    biMask = ['1' for x in range(n)] + ['0' for x in range(32 - n)]
    [biMask.insert(i, '.') for i in range(8, 32, 9)]
    return ''.join(biMask)

mask = binaryToCIDR(makeMask(prefix))
remainingBits = 32 - prefix
sizeOfInitialSubnet = 2 ** remainingBits
subnetAddress = ""

prefixModifier = 0
while (2 ** prefixModifier) < numberOfSubnetsDesired:
    prefixModifier = prefixModifier + 1
newPrefix = prefixModifier + prefix

newMask = binaryToCIDR(makeMask(newPrefix))

addressSizeOfNewSubnets = 2 ** (32-prefix-prefixModifier)
maxHostsOnSubnet = addressSizeOfNewSubnets - 2

binaryIP = ''.join([decimalToBinary(int(x)) for x in ip.split(".")])[:-1]
binaryMask = ''.join([decimalToBinary(int(x)) for x in mask.split(".")])[:-1]

for x in range(0, (len(binaryIP) - remainingBits)):
    if binaryIP[x] == '.':
        subnetAddress = subnetAddress + '.'
        continue
    if binaryIP[x] == '1' and binaryMask[x] == '1':
        subnetAddress = subnetAddress + "1"
    else:
        subnetAddress = subnetAddress + "0"
for x in range(1, remainingBits):
    subnetAddress = subnetAddress + "0"

print("Size of the initial subnet:", sizeOfInitialSubnet)
print("IP:  ", ip, binaryIP)
print("Mask:", mask, binaryMask)
print("Subnet Address: ", binaryToCIDR(subnetAddress), subnetAddress)
print("New Prefix: ", newPrefix)
print("New Mask: ", newMask)
print("Address size of subnet: ", addressSizeOfNewSubnets)
print("Max Hosts per subnet: ", maxHostsOnSubnet)

