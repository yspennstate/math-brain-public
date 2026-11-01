import numpy as np

def Q(r,s):
 A=1-r*r;B=1-s*s;C=1-r*r*s*s
 R=np.arctanh(r);S=np.arctanh(s);D=np.arctanh(r*s);k=.5*np.log(C/A/B)
 q=np.zeros((4,4))
 q[0,0]=2*(2*C-B)/(A*C);q[1,1]=2*(2*C-A)/(B*C);q[0,1]=2/C-2*k
 q[0,2]=-2*(R+s*D);q[0,3]=-2*(S-s*k)
 q[1,2]=-2*(R-r*k);q[1,3]=-2*(S+r*D)
 q[2,2]=4*(1+r*R+r*s*D);q[3,3]=4*(1+s*S+r*s*D)
 q[2,3]=2*(s*R+r*S-D-r*s*k)
 return q+q.T-np.diag(q.diagonal())
if __name__=='__main__':
 for d in [0,.2,1,3]:
  for a in [d+.001,d+.2,d+1,d+4]:
   h=1e-5
   q1=Q(np.tanh((a+d+h)/2),np.tanh((a-d+h)/2))
   q0=Q(np.tanh((a+d-h)/2),np.tanh((a-d-h)/2))
   print(d,a, np.linalg.eigvalsh((q1-q0)/(2*h)))
