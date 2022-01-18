# 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기
import queue

queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

print(f"queue_list_size : {len(queue_list)}")

for value in range(len(queue_list)):
    print(f"dequeue_queue_list_value : {dequeue()}")