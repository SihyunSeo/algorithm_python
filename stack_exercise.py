# 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기 (pop, push 함수 사용하지 않고 직접 구현해보자!!)

stack_list = list()

def push(data):
    stack_list.append(data)
    
def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data

for index in range(10):
    push(index)
    
print(f"stack_list : {stack_list}")
print(f"stack_list_size : {len(stack_list)}")

for index in range(len(stack_list)):
    print(f"stack_list_pop: {pop()}")