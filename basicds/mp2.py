from multiprocessing import Process


def print_func(continent='ASIA'):
	print(continent)




if __name__ == "__main__":
	names = ['America','Europe','Africa']
	procs = []
	#instantiating without any argument
	proc = Process(target=print_func)
	procs.append(proc)
	proc.start()

	#instantiating process with arguments
	for name in names:
		proc = Process(target=print_func,args=(name,))
		procs.append(proc)
		proc.start()


	#Complete the process
	for proc in procs:
		proc.join()