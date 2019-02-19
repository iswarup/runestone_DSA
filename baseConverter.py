import stacks

def divideBy2(decNumber):
    remStack = stacks.stack()

    while decNumber > 0:
        rem = decNumber % 2
        remStack.push(rem)
        decNumber = decNumber // 2

    binaryString = ""
    while not remStack.isEmpty():
        binaryString += str(remStack.pop())

    return binaryString

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"
    remStack = stacks.stack()

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remStack.isEmpty():
        newString += digits[remStack.pop()]

    return newString

print(baseConverter(26,26))
print(divideBy2(25))

