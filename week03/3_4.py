class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class ListCreated:
    def is_empty(self):
        return self.head == None

    def __init__(self, node = None):
        if node != None:
            headNode = Node(node)
            self.head = headNode
        else:
            self.head = node

    def length(self):
        count = 0
        curNode = self.head
        while curNode !=None:
            count += 1
            curNode = curNode.next
        return count

    def travel(self):
        curNode = self.head
        while curNode != None:
            print(curNode.elem, end='\t')
            curNode = curNode.next
        print(" ")

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            curNode = self.head
            while curNode.next != None:
                curNode = curNode.next
            curNode.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node =Node(item)
            count = 0
            preNode = self.head
            while count < (pos - 1):
                count += 1
                preNode = preNode.next
            node.next = preNode.next
            preNode.next = node

    def search(self, item):
        curNode = self.head
        while curNode != None:
            if curNode.elem == item:
                return True
            curNode = curNode.next
        return False

    def remove(self, item):
        curNode = self.head
        preNode = None
        while curNode != None:
            if curNode.elem == item:
                if preNode == None:
                    self.head = curNode.next
                else:
                    preNode.next = curNode.next
                break
            else:
                preNode = curNode
                curNode =curNode.next

    def change(self,pos,new_item):
        if pos <= 0 or pos > (self.length() - 1):
            print("False")
        else:
            count = 0
            preNode = self.head
            while count < (pos - 1):
                count += 1
                preNode = preNode.next
            preNode.elem = new_item


if __name__ == '__main__':
    List=ListCreated()
    print("-----头部添加-----")
    List.add(11)
    List.add(22)
    List.add(33)
    List.travel()
    print("-----尾部追加-----")
    List.append(44)
    List.travel()
    print("指定位置插入")
    List.insert(2,100)
    List.travel()
    print("-----删除元素-----")
    List.remove(33)
    List.travel()
    print("-----改变元素-----")
    List.change(2,666)
    List.travel()
