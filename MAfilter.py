#How do I do this
# so this module input in are points that were detected by boundaries, and output the angles which is filtered
#What it needs to do that?
# -> case bases operation
# -> Storing indexes and previous info
# -> Operating filter

from numba.experimental import jitclass
from numba import uint8, float32
import numpy as np

spec = [
    ('lenght', uint8),               # a simple scalar field
    ('buf', float32[:]),
    ('bufindex', uint8),          # an array field
    ('impulse', float32[:]),          # an array field
    ('out', float32),          # an array field
]

@jitclass(spec)
class FIR_filter(object):

    def __init__(self,lenght):
        self.lenght = lenght
        self.buf = np.zeros(lenght,dtype=np.float32)
        self.bufindex = 0
        self.out = 0
        self.impulse = np.full((lenght),1/lenght,dtype=np.float32)
    
    def updata(self,data):
        self.buf[self.bufindex] = data
        self.bufindex +=1
        if self.bufindex== self.lenght:
            self.bufindex=0
        sum_index = self.bufindex
        self.out=0
        for n in range(self.lenght):
            if sum_index>0:
                sum_index -=1
            else:
                sum_index = self.lenght-1
            self.out += self.impulse[n] * self.buf[sum_index]
        return self.out