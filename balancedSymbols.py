import stacks

def matches(opens,closes):
    openers = "([{"
    closers = ")]}"
    return openers.index(opens) == closers.index(closes)

def parCheckers(symbolString):
    S = stacks.stack()
    balanced = True
    index = 0

    while balanced and index < len(symbolString):
        symbol = symbolString[index]
        if symbol in "([{":
            S.push(symbol)
        else:
            if S.isEmpty():
                balanced = False
            else:
                top = S.pop()
                if not matches(top,symbol):
                    balanced = False
        index += 1
    if balanced and S.isEmpty():
        return True
    else:
        return False
# print(parCheckers('(({{[[]]}}))'))
# print(parCheckers('}{{)(}{}][][90{}'))


def descending(l):
    length = len(l)
    if length == 0 or length == 1:
        return True
    else:
        for i in range(1,length):
            if l[i] > l[i-1]:
                return False
        return True
# print(descending([]))
# print(descending([4,4,3]))
# print(descending([19,18,18,27]))

def valley(l):
    if len(l) < 3:
        return False
    for i in range(len(l)//2):
        if l[i] < l[i+1]:
            return False
    for i in range(len(l)//2,len(l)):
        if l[i] < l[i-1]:
            return False
    return True
# print(valley([3,2,1,2,3]))

def valley(list):
  if(len(list)==0):
    return(True)
  if(len(list)==1):
    return(False)
  if(list[0]<list[1]):
    return(False)
  for i in range(0,len(list)-1):

    if(list[i]<list[i+1]):
      pos=i
      break
    if(list[i]==list[i+1]):
      return(False)
  else:
    return(False)
  for i in range(pos,len(list)-1):
    if(list[i]>=list[i+1]):
      return(False)
  return(True)
# print(valley([4,3,4,5,6,7,8]))

def transpose(m):
    return list(map(list,zip(*m)))
# print(transpose([[1,1,1],[2,2,2],[3,3,3]]))

def progression(l):

