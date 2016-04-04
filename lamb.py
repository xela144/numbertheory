import numpy as np
import matplotlib.pyplot as plt

def runningMean(x, N):
    y = np.zeros((len(x),))
    for ctr in range(len(x)):
         y[ctr] = np.sum(x[ctr:(ctr+N)])
    return y/N

#lis = [4,5,3,1,2,1,3,4,5,6,7,7,6,2,3,3,2,3]

# time 
t = np.arange(0.0,2.0,0.001)

# signal
x = np.cos(2*np.pi*10*t) + np.cos(2*np.pi*25*t) + np.cos(2*np.pi*50*t) + np.cos(2*np.pi*100*t)

r = np.random.randn(len(t)/50)
f = runningMean(x, len(t)/40)
rr = np.random.randn(len(t)/40)
rrr = np.random.randn(len(t)/20)

# Plot the running mean and the signal
plt.plot(t,x, 'r', t,f,'b');plt.show()

# Plot the convolution of random signals
plt.plot(np.convolve(rrr, np.convolve(r,rr)));plt.show()

# Plot the convolution of the signal and the running mean
modes = ['full', 'same', 'valid']
for m in modes:
    plt.plot(np.convolve(x,f, mode=m));
#plt.legend(modes, loc='lower center');
plt.show()
