import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('../')

from ch2.perceptron import Perceptron

from server import Chatter

c = Chatter()
p = Perceptron()

print(p)
print(c)