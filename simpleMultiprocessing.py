from multiprocessing import Pool

def runParallelProcesses(numProcesses, func, args):
    # numProcesses: number of processes to create. Create as many as the number of cores your machine has
    # func: your function to call
    # args: lists of tuples of arguments to call your function
    #   -> process 0 will run args[0], process 1 will run args[1], etc

    p = Pool(processes=numProcesses)
    processes = []
    results = []

    for i in range(numProcesses):
        res = p.apply_async(func, args[i]) # call your training function with your arguments
        processes.append(res)
        print("started getting result for", i)

    for j, process in enumerate(processes):
        result = process.get() # get results asynchronously
        print(f"got result {j}:", result)
        results.append(result);

    p.close()
    return results
