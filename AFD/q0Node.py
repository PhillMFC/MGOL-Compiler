class Node:
    def __init__(self, **kwargs):
        self.info: dict = kwargs
        self.previousNode: Node = kwargs.get("previousNode")
        self.nextNode: Node = kwargs.get("nextNode")
        self.nodeState = kwargs.get("nodeState")

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.previousNode is None:
            self.previousNode = new_node
            return
        else:
            new_node.nextNode = self.head
            self.previousNode = new_node

    def printInfo(self):
        print(f'Previous node(s): {self.previousNode}\nNext node(s): {self.nextNode}\nState: {self.nodeState}')

node = Node(previousNode = [1,2], nextNode = [3,4,5], nodeState = "q0")
node.printInfo()