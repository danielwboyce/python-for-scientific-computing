import numpy as np

h=np.array([0.1,0.01,0.001])
fplush=np.exp(h)
fminush=np.exp((-1)*h)
f=np.array([1,1,1])

forwardfirstd=(fplush-f)/h
centerfirstd=(fplush-fminush)/(2*h)
centersecondd=(fplush-2*f+fminush)/h**2

errorforwardfirstd=np.abs(centerfirstd-f)
errorcenterfirstd=np.abs(centersecondd-f)

for n in range(0,3):
    print('When h = {:.3f}, \n'.format(h[n]),
      'I found--using the forward-difference formula--that the first derivative of e^x at x = 0 was {:.12f}'.format(forwardfirstd[n]),
      '(with error {:e}). \n'.format(errorforwardfirstd[n]),
      'I also found--using the centered-difference formula--that the first derivative of e^x at x = 0 was {:.12f}'.format(centerfirstd[n]),
      '(with error {:e})'.format(errorcenterfirstd[n]),
      'and that the second derivative was {:.12f}.\n'.format(centersecondd[n]))
    