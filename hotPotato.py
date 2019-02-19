import queue

def hotPotato(namelist,num):
    simqueue = queue.Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato([1,2,3,4,5,6],7))
