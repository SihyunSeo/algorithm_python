# 1. 큐 구조
# - 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
# - FIFO(First in First out)

# 2. 알아두어야 할 용어
# - Enqueue: 큐에 데이터를 넣는 기능
# - Dequeue: 큐에서 데이터를 꺼내는 기능

import queue

data_queue = queue.Queue()
data_queue.put("coding")
data_queue.put(1)

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
print(data_queue.get())
print(data_queue.qsize())
