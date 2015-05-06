#!/usr/bin/env python
# encoding: utf-8

from threading import Semaphore
from threading import BoundedSemaphore
import threading
import random
import time

N=2
M=3
mutex = BoundedSemaphore()
emptyA = BoundedSemaphore(N) #empty space for A
emptyB = BoundedSemaphore(N) #empty space for B
A = Semaphore(0) #Number of A
B = Semaphore(0) #Number of B
aNum=0
bNum=0

AQuotas = Semaphore(N) #semaphore to ensure A-B <=N
BQuotas = Semaphore(M) #semaphore to ensure A-B >= -M

class AProducer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global mutex, emptyA, A, B, AQuotas, BQuotas, aNum
        while True:
            emptyA.acquire()
            AQuotas.acquire()
            mutex.acquire()
            aNum+=1
            print("AProducer(%s) produce an A, now A: %s, now B: %d" % (self.name, aNum, bNum))
            mutex.release()
            BQuotas.release()
            A.release()
            time.sleep(random.randint(1,4))

class BProducer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global mutex, emptyB, A, B, AQuotas, BQuotas, bNum
        while True:
            emptyB.acquire()
            BQuotas.acquire()
            mutex.acquire()
            bNum+=1
            print("BProducer(%s) produce an B, now A: %s, now B: %d" % (self.name, aNum, bNum))
            mutex.release()
            AQuotas.release()
            B.release()
            time.sleep(random.randint(1,4))

class CProducer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global A, B, emptyA, emptyB,aNum,bNum
        while True:
            A.acquire()
            B.acquire()
            aNum-=1
            bNum-=1
            print("CProducer(%s) produce a C, now A: %s, now B: %d" % (self.name, aNum, bNum))
            emptyA.release()
            emptyB.release()
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









