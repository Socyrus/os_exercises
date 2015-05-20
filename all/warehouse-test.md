###测试仓库容量
N=2
主程序：
```
ap = AProducer()
ap.start()
```
只有A生产者，直到容量满了
结果：
```
AProducer(Thread-1) produce an A, now A: 1, now B: 0
AProducer(Thread-1) produce an A, now A: 2, now B: 0
```
A产生了两个，容量满了就停了

###测试不等式-M<=A-B<=N
因为当容量限制满足之后，右边的不等式一定成立
只需要测试A-B>=-M
主程序:
```
    ap = AProducer()
    ap.start()
    bp = BProducer()
    bp.start()
    bp2 = BProducer()
    bp2.start()
    bp3 = BProducer()
    bp3.start()
    bp4 = BProducer()
    bp4.start()
```
在这个程序里，B的产生速度应该是A的4倍
设N=10,M=3
结果：
```
AProducer(Thread-1) produce an A, now A: 1, now B: 0
BProducer(Thread-2) produce an B, now A: 1, now B: 1
BProducer(Thread-3) produce an B, now A: 1, now B: 2
BProducer(Thread-4) produce an B, now A: 1, now B: 3
BProducer(Thread-5) produce an B, now A: 1, now B: 4
AProducer(Thread-1) produce an A, now A: 2, now B: 4
BProducer(Thread-2) produce an B, now A: 2, now B: 5
AProducer(Thread-1) produce an A, now A: 3, now B: 5
BProducer(Thread-3) produce an B, now A: 3, now B: 6
AProducer(Thread-1) produce an A, now A: 4, now B: 6
BProducer(Thread-5) produce an B, now A: 4, now B: 7
AProducer(Thread-1) produce an A, now A: 5, now B: 7
BProducer(Thread-4) produce an B, now A: 5, now B: 8
AProducer(Thread-1) produce an A, now A: 6, now B: 8
BProducer(Thread-2) produce an B, now A: 6, now B: 9
AProducer(Thread-1) produce an A, now A: 7, now B: 9
BProducer(Thread-3) produce an B, now A: 7, now B: 10
AProducer(Thread-1) produce an A, now A: 8, now B: 10
AProducer(Thread-1) produce an A, now A: 9, now B: 10
AProducer(Thread-1) produce an A, now A: 10, now B: 10
```
从结果可以看出，当B比A多了三个之后
B就停止产生了，只有当A被产生之后，B才继续生产
