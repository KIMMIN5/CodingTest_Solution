from dataclasses import dataclass

@dataclass
class HeapType:
    heapSize:int
    heap:list[100]

def create():
    return 

def init(HeapType h):
h.heapSize = 0
for i in range(100):
    heap[i] = -1