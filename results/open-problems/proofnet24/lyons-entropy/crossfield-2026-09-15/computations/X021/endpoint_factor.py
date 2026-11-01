import numpy as np
from scipy.optimize import brentq
from endpoint import details

def critical(K):
 d=details(K)
 # A persistent zero mode makes this scalar bisection unsuitable at singular M.
 if np.linalg.matrix_rank(d['d']['M'],tol=1e-12)<3:return None,d
 # R has a single positive direction; DPP gauge can give endpoint nulls.
 def minev(t):return np.linalg.eigvalsh(d['E']-t*d['R'])[0]
 lo=1e-5;hi=10
 while minev(hi)>0:hi*=2
 return brentq(minev,lo,hi),d

if __name__=='__main__':
 for r in [.01,.1,.2,.25,.28,.2886]:
  K=.5*np.eye(3)+1j*r*np.array([[0,1,1],[-1,0,1],[-1,-1,0]])
  print('balanced r',r,'factor',critical(K)[0])
 for r in [.01,.1,.2,.3,.45,.49]:
  K=.5*np.eye(3)+np.array([[0,r,0],[r,0,0],[0,0,0]])
  print('one edge r',r,'factor',critical(K)[0])
