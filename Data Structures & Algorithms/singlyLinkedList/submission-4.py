class SLLNode:
    def __init__(self, val: int, next = None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.dummy = SLLNode(0) # Inspired by solution
        self.tail = self.dummy

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        curr = self.dummy.next
        for _ in range(index):
            if curr is None:
                return -1
            curr = curr.next
        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        self.dummy.next = SLLNode(val, self.dummy.next)
        if self.tail is self.dummy:
            self.tail = self.dummy.next

    def insertTail(self, val: int) -> None:
        self.tail.next = SLLNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        if index < 0:
            return False
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
            if prev is None:
                return False
        if prev.next is None:
            return False
        if prev.next is self.tail:
            self.tail = prev
        prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        vals, curr = [], self.dummy.next
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals