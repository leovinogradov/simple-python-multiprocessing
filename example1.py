import simpleMultiprocessing as multiprocessing

# Use fibonacci function for testing
def Fibonacci(n):
    if n<0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n==1:
        return 0
    # Second Fibonacci number is 1
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


if __name__ == "__main__":
    numProcesses = 4
    args = [(28,), (30,), (32,), (34,)]
    func = Fibonacci

    results = multiprocessing.runParallelProcesses(numProcesses, func, args)

    print("\nFinal results:", results);
