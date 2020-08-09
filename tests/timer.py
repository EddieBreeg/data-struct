from time import time
from structLib import Struct

def timer(function, n, *args):
    t=0
    for _ in range n:
        s=time()
        function(*args)
        t+=time()-s
    return t/n


