import statistics as s       # This will be helpful when we don't want to write statistics as a whole, instead we can replace it with s just so that it becomes handy

data = [2,3,4,5,5,6,7,8,99,67]
v = s.variance(data)
print(v)


# Now let's suppose we don't even wan't to use s.mean, we wan't to use only mean , for that
from statistics import mean
print(mean(data))

# let's just say you don't want to type mean also , then use
from statistics import mode as m
print(m(data))

#   we can also combinely import the functions
from statistics import median as M, mode as m

#    let's just say that we need to import everything, for that
from statistics import *
#    so in this way we don't actually need to use modeuleName.functionName()
