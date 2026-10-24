"""Exact transfer-word identities; numerical attacks on actual nonnegative
Boolean convolution hosts. Numerical results alone are not sign certificates.
"""
from pathlib import Path
from collections import Counter
import itertools,json,argparse
import numpy as np
from scipy.optimize import minimize

# A/B indicator for vertical, forward-cross, backward-cross.
COLORS={'Z':(0,0,0),'X':(1,1,1),'Y':(1,0,0),'V':(0,1,1),
        'U':(1,0,1),'T':(1,1,0),'R':(0,1,0),'S':(0,0,1)}

def word_orbits():
 C={}
 for block in [{(0,0):('Z',0),(0,1):('X',3),(1,0):('Y',1),(1,1):('V',2)},
               {(0,0):('U',2),(0,1):('R',1),(1,0):('S',1),(1,1):('T',2)}]:
  for state in itertools.product(range(2),repeat=5):
   terms=[block[state[i],state[(i+1)%5]] for i in range(5)]
   k=sum(d for _,d in terms);word=tuple(name for name,_ in terms)
   canonical=min(word[i:]+word[:i] for i in range(5))
   C.setdefault(k,Counter())[canonical]+=1
 assert {k:sum(v.values()) for k,v in C.items()}=={0:1,4:5,6:15,8:30,10:13}
 return C

class Model:
 def __init__(self,q,k):
  self.q=q;self.words=word_orbits()[k]
  x,y=np.divmod(np.arange(q*q),q);u,v=x.copy(),y.copy();shape=(q*q,q*q)
  self.indices=[np.broadcast_to(x[:,None]^y[:,None],shape),
                np.broadcast_to(x[:,None]^v[None,:],shape),
                np.broadcast_to(u[None,:]^y[:,None],shape)]
 def raw_value_gradient(self,a,b):
  kernels=[a,b];matrices={}
  for name,color in COLORS.items():
   m=np.ones((self.q**2,self.q**2))
   for c,index in zip(color,self.indices):m*=kernels[c][index]
   matrices[name]=m
  cache={};grads={name:np.zeros_like(m) for name,m in matrices.items()}
  def product(word):
   if word in cache:return cache[word]
   if len(word)==1:return matrices[word[0]]
   P=product(word[:-1])@matrices[word[-1]];cache[word]=P;return P
  value=0.
  for word,c in self.words.items():
   value+=c*np.sum(matrices[word[0]]*product(word[1:]).T)
   for i,name in enumerate(word):grads[name]+=c*product(word[i+1:]+word[:i]).T
  g=[np.zeros(self.q),np.zeros(self.q)]
  for name,color in COLORS.items():
   for i,c in enumerate(color):
    w=grads[name].copy()
    for j,cj in enumerate(color):
     if j!=i:w*=kernels[cj][self.indices[j]]
    g[c]+=np.bincount(self.indices[i].ravel(),weights=w.ravel(),minlength=self.q)
  scale=self.q**5
  return scale*value,scale*g[0],scale*g[1]
 def objective(self,z):
  p=np.exp(z-z.max());p/=p.sum();a=p[:self.q]+p[self.q:];b=p[:self.q]-p[self.q:]
  value,ga,gb=self.raw_value_gradient(a,b);gp=np.r_[ga+gb,ga-gb]
  return value,p*(gp-p@gp)

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--q',type=int,default=8);parser.add_argument('--k',type=int,default=6);parser.add_argument('--starts',type=int,default=100);args=parser.parse_args()
 model=Model(args.q,args.k);rng=np.random.default_rng(638414+args.q+args.k)
 z=rng.normal(size=2*args.q);v,g=model.objective(z);h=1e-5
 fd=np.array([(model.objective(z+h*np.eye(2*args.q)[i])[0]-model.objective(z-h*np.eye(2*args.q)[i])[0])/(2*h) for i in range(2*args.q)])
 out={'status':'numerical colored-coefficient search on actual nonnegative Boolean hosts',
      'q':args.q,'full_host_size':2*args.q,'k':args.k,
      'word_orbits':[{'word':word,'coefficient':c} for word,c in model.words.items()],
      'fd_gradient_max_error':float(max(abs(fd-g))),'tests':[]}
 output=Path(__file__).with_name(f'continuation_20261003_global_C{args.k}_q{args.q}_search.json')
 for trial in range(args.starts):
  z=rng.normal(size=2*args.q)*rng.choice([.2,1,2,4,8])
  res=minimize(model.objective,z,jac=True,method='L-BFGS-B',options={'maxiter':400,'ftol':1e-14,'gtol':1e-10})
  p=np.exp(res.x-res.x.max());p/=p.sum();a=p[:args.q]+p[args.q:];b=p[:args.q]-p[args.q:]
  out['tests'].append({'value':float(res.fun),'p':p.tolist(),'a':a.tolist(),'b':b.tolist(),'success':bool(res.success)})
  if trial%10==0:print('q',args.q,'k',args.k,'trial',trial,'minimum',min(t['value'] for t in out['tests']),flush=True);output.write_text(json.dumps(out,indent=2))
  if res.fun< -1e-9:break
 out['minimum']=min(t['value'] for t in out['tests']);output.write_text(json.dumps(out,indent=2))
 print(json.dumps({k:v for k,v in out.items() if k!='tests'},indent=2))
if __name__=='__main__':main()
