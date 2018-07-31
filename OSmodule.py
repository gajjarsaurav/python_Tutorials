import os
# so you can find the current working directory by using this
curDir = os.getcwd()
print(curDir)
#       OR
print(os.getcwd())
os.mkdir('newDir')
import time
time.sleep(3)
os.rename('newDir', 'newDir2')
time.sleep(2)
os.rmdir('newDir2')
