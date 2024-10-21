#Homework8 task1
from min_heap import MinHeap

# test array of wires
array = [10, 12, 5, 12, 25, 11, 5, 5, 7, 18]

#accumulator array
result_array = []

# two temp variables
temp1 = 0
temp2 = 0

#create min heap
min_heap = MinHeap(array)


while min_heap.get_size() != 1:
    #get two min values from the created heap
    temp1 = min_heap.extract_min()
    temp2 = min_heap.extract_min()

    #sum them up
    temp_sum = temp1 + temp2

    #insert sumed value back to the heap
    min_heap.insert(temp_sum)

    #insert same value to the result array
    result_array.append(temp_sum)

#sum the values from result array and show them
total_sum = sum(result_array)
print(total_sum)
