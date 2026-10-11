class KthLargest:
    # we're given a stream of values and want to find the kth largest 
    # integer in that stream
    # as the stream grows we're constantly adjusting our kth largest value
    # self.k = k is kth largest
    # when the class is created the kth largest is none
    # since we're adding to a stream this looks like we can manlipulate a stack
    # or specifically a min-heap because we're finding the kth element even if 
    # there's duplicates

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


