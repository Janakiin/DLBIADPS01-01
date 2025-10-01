import timeit

from functions import process_via_array, process_via_fifo
from operation import Operation

requests = [
    (Operation.ADD, 1),
    (Operation.ADD, 2),
    (Operation.ADD, 3),
    (Operation.DELETE, None),
    (Operation.ADD, 4)
]

print("Array:", process_via_array(requests))
print("FIFO:", process_via_fifo(requests))

execution_time_via_arrays = timeit.timeit(
    stmt="process_via_array(requests)",
    globals=globals(),
    number=1000
)
print(f"Durchschnittliche Laufzeit. Array: {(execution_time_via_arrays/1000) * 1000 :.6f} ms pro Durchlauf")

execution_time_via_fifo = timeit.timeit(
    stmt="process_via_fifo(requests)",
    globals=globals(),
    number=1000
)
print(f"Durchschnittliche Laufzeit.FIFO: {(execution_time_via_fifo/1000) * 1000:.6f} ms pro Durchlauf")
print((execution_time_via_fifo/1000) * 1000 - (execution_time_via_arrays/1000) * 1000)
