from multiprocessing import Process, Manager



def dothing(L,i):
	L.append("anything")

def dothing2(L,i):
	L.append("Nothing")


if __name__ == "__main__":
	with Manager() as manager:
		L = manager.list()
		processes = []
		for i in range(5):
			p = Process(target=dothing, args=(L,i))
			p.start()
			processes.append(p)
		for i in range(3):
			p2 = Process(target=dothing2, args=(L,i))
			p2.start()
			processes.append(p2)
		for pr in processes:
			pr.join()
		print(L)