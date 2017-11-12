from heapq import *

class Heap():
	"""docstring for Heap"""
	def __init__(self):
		self.heap = []

	def add(self,num):
		h=self.heap
		heappush(h,-num)
		heapify(h)
		print h

	def kth(self,arr,k):
		i=0
		while i<k:
			self.add(arr[i])
			i+=1
		while(i<len(arr)-1):
			heappushpop(self.heap,-arr[i])
			i+=1
		return heappop(self.heap)


ans=Heap()
arr=[1,2,7,6,3,5,9]
k=2
print ans.kth(arr,k)