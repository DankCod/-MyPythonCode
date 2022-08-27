class Node:#defining node class
    def __init__(self,data):
        self.data= data;
        self.next=None;

class linked_List:#defining linked list class
    def __init__(self):#initializing head
        self.head=None
    def printlist(self):
        temp=self.head;#go throug linked list
        while(temp):#^
            print(temp.data)
            temp=temp.next
    def push(self,new_data):
        new_node=Node(new_data);
        new_node.next=self.head
        self.head=new_node
    def insertAfter(self,prev_node,new_data):
        if prev_node is None:
            print('Previous node must be in linked list')
            return
        new_node=Node(new_data);
        new_node.next=prev_node.next;
        prev_node.next=new_node;
    def append(self,new_data):
        new_node=Node(new_data);
        if self.head== None:
            self.head=new_node;
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node;
    def delfront(self):
        temp=self.head;
        self.head=self.head.next;
        temp=None;
    def deletenode(self,key):
        temp=self.head
        if(temp.data==key):
            self.head=temp.next
            temp=None
            return
        while(temp!=None):
            prev=temp
            temp=temp.next
            if temp==None:
                print("Key must be in linked list");
                break
            if(temp.data==key):
                prev.next=temp.next
                temp=None
                break
    def delend(self):
        temp=self.head
        while(temp.next!=None):
            prev=temp
            temp=temp.next
        prev.next=None
        Temp=None


if __name__=='__main__':
    llist=linked_List()
    llist.head=Node(1);
    second=Node(2);
    third=Node(3);
    llist.head.next=second;
    second.next=third;
    llist.push(1)
    llist.insertAfter(second,0)
    llist.append(20)
    llist.delfront()
    llist.deletenode(90)
    llist.delend()
    llist.printlist()
