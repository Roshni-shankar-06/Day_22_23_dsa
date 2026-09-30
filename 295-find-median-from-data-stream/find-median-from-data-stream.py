class MedianFinder:
  def __init__(self):
    self.maxHeap = []
    self.minHeap = []

  def addNum(self, num: int) -> None:
    if not self.maxHeap or num <= -self.maxHeap[0]:
      heapq.heappush(self.maxHeap, -num)
    else:
      heapq.heappush(self.minHeap, num)

    
