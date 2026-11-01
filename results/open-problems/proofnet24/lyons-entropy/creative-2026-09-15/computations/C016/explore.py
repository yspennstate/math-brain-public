from fractions import Fraction as Q
from math import log
import json

class P:
 def __init__(self,a=0):
  if isinstance(a,P): self.a=a.a; return
  if not isinstance(a,(list,tuple)): a=[a]
  a=list(map(Q,a))
  while len(a)>1 and a[-1]==0: a.pop()
  self.a=tuple(a)
 def __add__(self,b):
  b=P(b);return P([(self.a[i] if i<len(self.a) else 0)+(b.a[i] if i<len(b.a) else 0) for i in range(max(len(self.a),len(b.a)))])
 __radd__=__add__
 def __neg__(self): return P([-x for x in self.a])
 def __sub__(self,b): return self+-P(b)
 def __rsub__(self,b): return P(b)+-self
 def __mul__(self,b):
  b=P(b); c=[Q(0)]*(len(self.a)+len(b.a)-1)
  for i,x in enumerate(self.a):
   for j,y in enumerate(b.a):c[i+j]+=x*y
  return P(c)
 __rmul__=__mul__
 def __pow__(self,n):
  out=P(1)
  for _ in range(n):out=out*self
  return out
 def __truediv__(self,b):return R(self,b)
 def __repr__(self):return str(list(map(str,self.a)))
 def val(self,t): return sum(float(x)*t**i for i,x in enumerate(self.a))
 def divmod(self,b):
  b=P(b);a=list(self.a);c=[Q(0)]*max(1,len(a)-len(b.a)+1)
  while len(a)>=len(b.a) and a!=[Q(0)]:
   n=len(a)-len(b.a);v=a[-1]/b.a[-1];c[n]=v
   for i,x in enumerate(b.a):a[n+i]-=v*x
   while len(a)>1 and a[-1]==0:a.pop()
  return P(c),P(a)
 def zero(self):return self.a==(Q(0),)
def gcd(a,b):
 while not b.zero():a,b=b,a.divmod(b)[1]
 return P([x/a.a[-1] for x in a.a])
class R:
 def __init__(self,a=0,b=1):
  if isinstance(a,R):self.a,self.b=a.a,a.b;return
  self.a,self.b=P(a),P(b)
  g=gcd(self.a,self.b);self.a=self.a.divmod(g)[0];self.b=self.b.divmod(g)[0]
  c=self.b.a[-1];self.a=P([x/c for x in self.a.a]);self.b=P([x/c for x in self.b.a])
 def __add__(self,b):
  b=R(b);return R(self.a*b.b+b.a*self.b,self.b*b.b)
 __radd__=__add__
 def __neg__(self):return R(-self.a,self.b)
 def __sub__(self,b):return self+-R(b)
 def __rsub__(self,b):return R(b)+-self
 def __mul__(self,b):
  b=R(b);return R(self.a*b.a,self.b*b.b)
 __rmul__=__mul__
 def __truediv__(self,b):
  b=R(b);return R(self.a*b.b,self.b*b.a)
 def __pow__(self,n):return R(self.a**n,self.b**n)
 def __repr__(self):return str(self.a)+' / '+str(self.b)
 def val(self,t):return self.a.val(t)/self.b.val(t)

if __name__=='__main__':
 t=R(P([0,1]));v=(1+t)/2
 aa=2*((1-v)**2+v**2)+2*(1-v)*(1-3*v)**2/(1+v)+2*v*(2-3*v)**2/(2-v)
 bb=2-2*v*(1-3*v)/(1+v)+2*(1-v)*(2-3*v)/(2-v)
 cc=4+2*v**2/(1-v*v)+2*(1-v)**2/(v*(2-v))
 print('Fuu',aa,'Fuv',bb,'Fvv',cc,'det',aa*cc-bb*bb)
 print('4bb',4*bb,'2aa',2*aa)
