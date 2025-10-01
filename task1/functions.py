from collections import deque
from operation import Operation

def process_via_fifo(requests):
    queue = deque()
    for operation, value in requests:
        if operation == Operation.ADD:
            queue.append(value)
        elif operation == Operation.DELETE and queue:
            queue.popleft()
    return list(queue)

def process_via_array(requests):
    array = []
    for  operation, value in requests:
        if operation == Operation.ADD:
            array.append(value)
        elif operation == Operation.DELETE and array:
            array.pop()
    return array