#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

import time

# import our Random class from python/Random.py file
sys.path.append(".")
from python.MySort import MySort

# default num quantiles = 1
num_q = 1

log = False

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        if sys.argv[i] == '-f':
            InputFile = sys.argv[i+1]
            haveInput = True
            continue

        if sys.argv[i] == '-n':
            num_q = int(sys.argv[i+1])
            if num_q <= 0:
                print("Number of quantiles must be greater than or equal to 1")
                sys.exit(0)
            else:
                continue

        if sys.argv[i] == '-scale':
            scale = sys.argv[i+1]
            if scale == "log":
                log = True
                continue
            else:
                continue

    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("    -f                 specify input file (required)")
        print ("    -n                 specify number of quantiles (optional, default 1)")
        print ("    -scale             if 'log', set the plot scale to log. if not present or not 'log', scale normally ")
        print
        sys.exit(1)


    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()


    # time the sorting to see how long they take
    t1 = time.time()
    times = Sorter.DefaultSort(times)
    t2 = time.time()

    #print(times[-1])

    t3 = time.time()
    times_avg = Sorter.DefaultSort(times_avg)
    t4 = time.time()

    # for fun, print how long the two operations take
    #print(t2-t1, "", t4-t3)
    # try some other methods! see how long they take

    # times_avg = Sorter.DefaultSort(times_avg)
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # find quantile positions from given number of quantiles

    # first, get percentiles between 0 and 1
    percentiles = np.arange(0, 1.01, 1 / (num_q+1))[1:-1]
    #print(percentiles)

    # then, use them to find the indices, at which the quantiles lie

    # estimated quantiles: percentile*(len(array)+1)
    # cast to an int, select that element from the original array

    time_quantiles = []
    time_avg_quantiles = []
    for perc in percentiles:
        time_quantiles.append(times[int(perc*(len(times)+1))])
        if len(times_avg) == 1:
            pass 
        else:
            time_avg_quantiles.append(times_avg[int(perc*(len(times_avg)+1))])

    #print(time_quantiles, time_avg_quantiles)
        
    # alternatively, i found this numpy quantile function after figuring my own.
    # time_quantiles = np.quantile(times, percentiles)
    # time_avg_quantiles = np.quantile(times_avg, percentiles)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE

    fig, ax = plt.subplots(1, 2, figsize=(10,4), sharey=False)

    # histograms with 100 bins to make percentiling easier to see

    # for times only
    ax[0].hist(times, 100, label="Times", color="gray")
    if log:
        ax[0].set_yscale("log")

    # plot quantile lines
    for i, q in enumerate(time_quantiles):
        ax[0].axvline(q, color="C{}".format(i), linestyle="--", label="Q{}".format(i+1)) #label="{:.2f}".format(percentiles[i]))
    
    ax[0].legend()
    ax[0].set_ylabel("Frequency")
    ax[0].set_xlabel("Time btw Cookies Eaten (d)")
 
    # plot average times
    ax[1].hist(times_avg, 100, label="Avg. Times", color="gray")

    # plot quantile lines
    for i, q in enumerate(time_avg_quantiles):
        ax[1].axvline(q, color="C{}".format(i), linestyle="--", label="Q{}".format(i+1)) #label="{:.2f}".format(percentiles[i]))

    if log:
        ax[1].set_yscale("log")
    ax[1].legend()
    ax[1].set_ylabel("Frequency")
    ax[1].set_xlabel("Avg. Time btw Cookies Eaten (d)")

    plt.suptitle("Cookie Analysis, Rate = {}".format(rate))
    fig.savefig("analysis.jpg", dpi=180)
    plt.show()