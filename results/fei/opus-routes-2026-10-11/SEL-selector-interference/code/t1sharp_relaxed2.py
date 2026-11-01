import numpy as np
from scipy.optimize import fsolve
exec(open('t1sharp_relaxed.py').read().split("best = (-9, None)")[0])
alpha = np.arcsin(np.sqrt(p[0]))
f = lambda th: H(np.array([np.cos(th)**2, np.sin(th)**2]))
fp = (f(alpha+1e-6)-f(alpha-1e-6))/2e-6
print('fprime(alpha)=', fp)
for t in (0.001, 0.01, 0.03, 0.1, 0.2, -0.01, -0.1):
    def eqs(z):
        w1, s = z
        return [w1*np.cos(t)**2 + (1-w1)*np.sin(s)**2 - p[0], w1*np.cos(t)*np.sin(t) + (1-w1)*np.sin(s)*np.cos(s)]
    w1, s = fsolve(eqs, [p[0], -p[0]/(1-p[0])*t])
    res = eqs([w1, s])
    val = w1*Phi((np.cos(t), np.sin(t))) + (1-w1)*Phi((np.sin(s), np.cos(s)))
    print('t=%7.3f s=%8.5f w1=%.5f resid=%.1e  E[Phi]=%+.6e  pred 2 w1 t f\'=%+.6e' % (t, s, w1, max(map(abs,res)), val, 2*w1*t*fp))
