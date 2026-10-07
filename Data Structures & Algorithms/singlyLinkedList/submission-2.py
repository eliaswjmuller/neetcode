class LinkedList:
    
    def __init__(self):
        self.list = []

    def get(self, index: int) -> int:
        if index >= len(self.list): 
            val = - 1
        else: 
            val = self.list[index]
        return val
        
    def insertHead(self, val: int) -> None:
        old = self.list.copy()
        self.list = [val]
        self.list.extend(old)

    def insertTail(self, val: int) -> None:
        self.list.append(val)

    def remove(self, index: int) -> bool:
        if len(self.list) > index:
            old_pre = self.list[:index]
            old_suff = self.list[index+1:]
            self.list = old_pre
            self.list.extend(old_suff)
            return True
        return False
        
    def getValues(self) -> List[int]:
        return self.list
        
