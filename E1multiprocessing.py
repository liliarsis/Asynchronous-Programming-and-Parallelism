# This code shows how the Multiprocessing package allows our functions to work asynchronously.

from multiprocessing import Process


def print_func(continent='Asia'):
    print('The name of continent is : ', continent)

if __name__ == "__main__":  # confirms that the code is under main function
    names = ['America', 'Europe', 'Africa']     # The greater the number of calls we make to the function, the easier to observe asynchronous behavior. 
    #names = ['ags', 'BC', 'BCS', 'Camp', 'Chis', 'Chih', 'CDM', 'Coah', 'Col', 'Dgo', 'Gto', 'Gro', 'Hgo', 'Jal']
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()
    """ In a synchronous system the list of names will be printed in the order in which they are listed
     In this asynchronous system we can see that the names are printed in disorder, 
     because the time of their process is different.
     complete the processes """
    for proc in procs:
        proc.join()
