from multiprocessing import Queue


colors = ['Red','Orange','Blue','Green']

queue = Queue()

#pushing item into queue:

for color in colors:
	queue.put(color)



#getting items from Queue

while not queue.empty():
	print(queue.get())