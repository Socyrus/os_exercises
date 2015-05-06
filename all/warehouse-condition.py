#!/usr/bin/env python
# encoding: utf-8

import threading
import time
import random

condition = threading.Condition()
N = 2
M = 3
A = 0
B = 0

class AProducer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, N, M, A, B
        while True:
            if condition.acquire():
                if (A<N and A-B<N):
                    A+=1
                    print("AProducer(%s) produce an A, now A: %d, now B: %d" % (self.name, A, B))
                    condition.notify()
                else:
                    print("AProducer(%s) stop producing, now A:%d, now B:%d" % (self.name, A, B))
                    condition.wait()
                condition.release()
                time.sleep(random.randint(1,4))

class BProducer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, N, M, A, B
        while True:
            if condition.acquire():
                if (B<N and A-B>-M):
                    B+=1
                    print("BProducer(%s) produce a  B, now A: %d, now B: %d" % (self.name, A, B))
                    condition.notify()
                else:
                    print("BProducer(%s) stop producing, now A:%d, now B: %d" % (self.name, A, B))
                    condition.wait()
                condition.release()
                time.sleep(random.randint(1,4))

class CProducer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global condition, N, M, A, B
        while True:
            if condition.acquire():
                if (A>0 and B>0):
                    B-=1
                    A-=1
                    print("CProducer(%s) produce a  C, now A: %d, now B: %d" % (self.name, A, B))
                    condition.notify()
                else:
                    print("CProducer(%s) stop producing, now A:%d, now %d" % (self.name, A, B))
                    condition.wait()
                condition.release()
                time.sleep(random.randint(1,4))

if __name__ == "__main__":
    for i in range(0,1):
        ap = AProducer()
        ap.start()


    for i in range(0,1):
        bp = BProducer()
        bp.start()

    for i in range(0,1):
        cp = CProducer()
        cp.start()







