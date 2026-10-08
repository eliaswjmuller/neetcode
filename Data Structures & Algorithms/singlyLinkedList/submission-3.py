class SLLNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    

class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head == None:
            return - 1 
        else:
            curr_idx = 0
            curr_node = self.head
            while curr_idx < index:
                curr_node = curr_node.next
                if curr_node == None:
                    return - 1
                curr_idx += 1
            return curr_node.val
        
    def insertHead(self, val: int) -> None:
        old_head = self.head
        new_head = SLLNode(val, old_head)
        self.head = new_head

    def insertTail(self, val: int) -> None:
        new_tail = SLLNode(val, None)
        if self.head == None:
            self.head = new_tail
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next 
        curr.next = new_tail
        return

    def remove(self, index: int) -> bool:
        if self.head == None:
            return False 
        
        elif index == 0: 
            self.head = self.head.next
            return True
        else:
            curr_idx = 0
            prev_elem = None
            curr_node = self.head
            while curr_idx < index:
                prev_elem = curr_node
                curr_node = curr_node.next
                if curr_node == None:
                    return False
                curr_idx += 1
            next_elem = curr_node.next
            prev_elem.next = next_elem
            return True
        
        
    def getValues(self) -> List[int]:
        arr = []
        next = self.head
        while next != None:
            curr = next
            arr.append(curr.val)
            next = curr.next

        return arr
        
        
