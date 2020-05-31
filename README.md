# Simple Python Multiprocessing

This function is designed to provide simple multiprocessing capabilities to speed up repetitive function calls by spreading the load among multiple CPU cores

# How to use:

import runParallelProcesses from simpleMultiprocessing.py

1st argument: number of processes to make

2nd argument: the function you want to run over multiple processes

3rd argument: list of tuples representing the arguments you want to pass in into each function in each process.
The length of this list should match the number of processes your are making.

For example, if you are trying to tune a machine learning algorithm with different parameters, your arguments could look something like this:

numProcesses = 2

func = myTrainingFunction

args = [(X_data, Y_data, myParamA=1, etc...), (X_data, Y_data, myParamA=2, etc...)]

results = runParallelProcesses(numProcesses, func, args);
