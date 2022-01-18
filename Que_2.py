import queue
# Last in First out Que
data_queue = queue.LifoQueue()

data_queue.put("funcoding")
data_queue.put(1)

print("---------------LIFO QUE---------------")
print(f"data_queue_size : {data_queue.qsize()}")
print(f"data_queue_get : {data_queue.get()}")
print(f"afterGet_data_queue_size : {data_queue.qsize()}")
print(f"data_queue_get : {data_queue.get()}")

# 중요한 부분!!!
# Question? : 어디에 큐가 많이 쓰일까?
# - 멀티 태스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨(이정도는 설명할 정도로 인지하고 있자!!!!)
# - 큐의 경우에는 장단점 보다는 (특별히 언급되는 장단점이 없다.), 큐의 활용 예로 프로세스 스케쥴링 방식을 함께 이해해두는 것이 좋다.

data_queue = queue.PriorityQueue()
# 인자값이 두개인데 첫번째가 우선순위, 두번째가 값이다.
data_queue.put((10, "korea"))
data_queue.put((5, 1))
data_queue.put((15, "china"))

print("---------------Priority QUE---------------")
print(f"data_queue_size : {data_queue.qsize()}")
print(f"data_queue_get : {data_queue.get()}")
print(f"afterGet_data_queue_size : {data_queue.qsize()}")
print(f"data_queue_get : {data_queue.get()}")
print(f"afterGet_data_queue_size : {data_queue.qsize()}")
print(f"data_queue_get : {data_queue.get()}")
# -> 결과값으로 볼 수 있듯이 우선순위가 낮은 순서가 가장 출력 우선순위로 선정이 되고 우선순위가 높은 순서대로 데이터가 출력이 된다.