import statistics

exampleList = [1,3,4,5,7,88,46,8,8,9,54,56]
mean_value = statistics.mean(exampleList)
print(mean_value)

median_value = statistics.median(exampleList)
print(median_value)

std_dev = statistics.stdev(exampleList)
print(std_dev)
