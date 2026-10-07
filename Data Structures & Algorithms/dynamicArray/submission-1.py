class DynamicArray:
    
    def __init__(self, capacity: int):
        assert capacity > 0
        self._array = [None]*capacity
        self._cap = capacity
        self._size = 0
        self._lastFreeIdx = 0

    def get(self, i: int) -> int:
        return self._array[i]

    def set(self, i: int, n: int) -> None:
        prev = self.get(i)
        self._array[i] = n
        if prev == None:
            self._size += 1
        if self._lastFreeIdx == None: 
            return
        else:
            if i >= self._lastFreeIdx:
                self._lastFreeIdx = i + 1
            if self._lastFreeIdx > self._cap - 1:
                self._lastFreeIdx = None

    def pushback(self, n: int) -> None:
        if self._lastFreeIdx == None:
            idx = self._cap
            self.resize()
            self._lastFreeIdx = idx
        self.set(self._lastFreeIdx, n)


    def popback(self) -> int:
        if self._lastFreeIdx == None: 
            idx = -1
            self._lastFreeIdx = self._cap - 1
        else:
            idx = self._lastFreeIdx - 1
            self._lastFreeIdx -= 1
        n = self.get(idx)
        self._array[idx] = None
        self._size -= 1

        return n

    def resize(self) -> None:
        capacity = self.getCapacity()
        self._array.extend([None]*capacity)
        self._cap = capacity * 2

    def getSize(self) -> int:
        return self._size
    
    def getCapacity(self) -> int:
        return self._cap
