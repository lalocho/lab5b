class Heap:
    def __init__(self):
        self.heap_array = []

    # INSERTS ITEM AT END OF ARRAY THEN HEAPIFIES IT
    def insert(self, k):
        self.heap_array.append(k)
        for i in range(len(self.heap_array) - 1//2, -1, -1):
            self.heapify(len(self.heap_array), i)

    # SWAPS THE FIRST AND LAST ITEM THEN REMOVES LAST ITEM AND HEAPIFIES AFTER
    def extract_min(self):
        if self.is_empty():
            return None
        min_elem = self.heap_array[0]
        self.heap_array[0] = self.heap_array[len(self.heap_array)-1]
        self.heap_array.pop()
        # self.heapify(len(self.heap_array),0)
        for i in range(len(self.heap_array)//2 - 1, -1, -1):
            self.heapify(len(self.heap_array), i)

        return min_elem

    # CHECKS IF VALID HEAP, IF NOT SWAPS ITEMS TO BECOME A VALID MIN HEAP
    def heapify(self, length, index):
        smallest = index
        left = index*2 + 1
        right = index*2 + 2
        if left < length and self.heap_array[left] < self.heap_array[smallest]:
            smallest = left
        if right < length and self.heap_array[right] < self.heap_array[smallest]:
            smallest = right
        if smallest != index:
            temp = self.heap_array[index]
            self.heap_array[index] = self.heap_array[smallest]
            self.heap_array[smallest] = temp

    def is_empty(self):
        return len(self.heap_array) == 0

    # PRINTS THE ARRAY IN INCREASING ORDER
    def heapsort(self):
        while not self.is_empty():
            print(self.extract_min())


def main():
    f = open('test.txt')
    line = f.readline()
    minHeap = Heap()
    while line:
        # getting only the passwords from each line
        try:  # ignores line if irregularity with data
            for num in line.split(','):  # ignores commas in input list
                minHeap.insert(int(num))
        except:
            print()
        line = f.readline()

    f.close()
    minHeap.heapsort()

main()