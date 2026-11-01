import numpy as np

def matrix(r,s,third=True):
 a=np.sqrt(r);b=np.sqrt(s)
 v=np.array([a*(1-s),b*(1-r)])
 w=np.array([a*s,b*r])
 u=np.array([a*(1+3*s),b*(1+3*r)])
 I=np.outer(v,v)/(2*(1-r)*(1-s))+2*np.outer(w,w)/(1-r*s)
 if third:I+=np.outer(u,u)/(2*(3+r+s+3*r*s))
 P=np.array([[-(1-s),2*a*b],[2*a*b,-(1-r)]])/8
 T=2*np.log((1-r*s)**2/((1-r*r)*(1-s*s)))
 return np.linalg.eigvalsh(I-T*P),T
if __name__=='__main__':
 for third in [False,True]:
  worst=(1,None)
  for r in [.01,.1,.2,.4,.6,.8,.9,.99,.999,.9999,.999999]:
   for s in [.0001,.01,.1,.2,.4,.6,.8,.9,.99,.999]:
    if s>=r:continue
    val,T=matrix(r,s,third)
    if val[0]<worst[0]:worst=(val[0],(r,s,T))
    if val[0]<-1e-10:print('FAIL',third,r,s,val,T)
  print('min',third,worst)
