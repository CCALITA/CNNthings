import numpy as np
import sys
np.random.seed(612)  # "Legacy Random Generation", refers to the official doc.
inx = np.arange(0,1000,eval(input('Integer in 1-100:')))
val = np.random.uniform(0,1,1000)[inx]
buf = 'SN\tIndex\tValue\n' + '\n'.join([f'{i+1}\t{inx[i]}\t{val[i]}'for i in range(0,inx.size)])
sys.stdout.write(buf)
