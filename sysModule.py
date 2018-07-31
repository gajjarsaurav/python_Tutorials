import sys
sys.stderr.write('this is the stderr text\n')
sys.stderr.flush()
sys.stdout.write('this is the stdout text\n')

#   to get the file path using argv
print(sys.argv)
# len(sys.argv) - will give the length of list of arguments
if len(sys.argv) > 1:
    print(sys.argv[1])

# or if we want to deal with integers or floating point no., then
if len(sys.argv) > 1:
    print(float(sys.argv[0]) + 4)


# let's just define a function which takes parameters as any item of list sys.argv, and then process it to give an output
def main(arg):
    print(arg)

main(sys.argv)
