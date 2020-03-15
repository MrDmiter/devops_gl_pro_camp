import psutil
import sys
arguments = sys.argv[1:]
if len(arguments) == 0:
	print ("You forgot to pass arguments, please eneter 'mem' in case you want to see memory metrics or 'cpu' in case you want to see cpu metrics")
	sys.exit(1)
if len(arguments) > 1:
	print ("Only one argument is allowed, please eneter either 'mem' in case you want to see memory metrics or 'cpu' in case you want to see cpu metrics")
	sys.exit(1)	
metric = arguments[0] 
if metric == "cpu":
	print (psutil.cpu_times())
elif metric == "mem":
	print (psutil.virtual_memory())
	print (psutil.swap_memory())
else:
	print ("Not supported argument, please enter 'cpu' or 'mem' argument")