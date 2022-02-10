# 노드 : 데이터 저장 단위(데이터값, 포인터) 로 구성
# 포인터 : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

# C언에서의 주요한 구조이지만 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원한다.

# node 개념 맛보기
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# node1 = Node(1)
# node2 = Node(2)
# node1.next = node2

# head = node1

# 링크드 리스트로 데이터 추가하기
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
        
# def add(data):
#     node = head
#     while node.next:
#         node = node.next
    
#     node.next = Node(data)
    
# node1 = Node(1)

# head = node1

# for index in range(1, 10):
#     add(index)
    
# node = head
# while node.next:
#     print(node.next)
#     node = node.next
# print(node.data)

# 링크드 리스트의 장단점
# * 장점
# 1. 미리 데이터 공간을 미리 할당하지 않아도 됌 -> 배열은 미리 데이터 공간을 할당 해야 함

# * 단점
# 1. 연결을 위한 별도 데이터 공간이 필요하므로 저장 공간 효율이 높지 않음
# 2. 연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
# 3. 중간 데이터 삭제시, 앞뒤 데이터의 연결을 재구성해야 하는 부가적인 작업 필요

# 생성된 링크드 리스트 중간에 데이터값 넣어보기
# node3 = Node(1.5)
# node = head
# search = True
# while search:
#     if node.data == 1:
#         search = False
#     node = node.next
#     node.next = node3
#     node3.next = node_next
    
# node = head
# while node.next:
#     print(node.data)
#     node = node.next
# print(node.data)

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)
    
    def add(self, data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
        
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
            
linkedList1 = NodeMgmt(0)
linkedList1.desc()

for data in range(1, 10):
    linkedList1.add(data)
    
print(linkedList1.data)