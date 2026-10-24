from fractions import Fraction
from itertools import product
N=4; alpha=Fraction(1,2); mu=Fraction(1,10); L=16

def rising(a,k):
 r=Fraction(1)
 for j in range(k): r*=a+j
 return r

def nu(x):
 s=sum(x); return rising(alpha,s)*rising(alpha,N-s)/rising(2*alpha,N)
states=list(product((0,1), repeat=N))
nu_d={x:nu(x) for x in states}

def g2(x):
 s=sum(x); return Fraction(2*s*(N-s),N*(N-1))

def root22(x): return 1 if sum(x)==2 else 0

# Joint transition for m loci under model 'c023' or 'c026'.
def step(dist, m, model):
 out={}
 for xs,pr in dist.items():
  if not pr: continue
  for v in range(N):
   if model=='c023':
    qs=[]
    for x in xs:
     p1=Fraction(sum(x),N)*(1-mu)+Fraction(N-sum(x),N)*mu
     qs.append(p1)
    for bits in product((0,1), repeat=m):
     q=Fraction(1,N)
     ys=[]
     for x,b,p1 in zip(xs,bits,qs):
      q*=p1 if b else (1-p1)
      y=list(x); y[v]=b; ys.append(tuple(y))
     key=tuple(ys); out[key]=out.get(key,Fraction(0))+pr*q
   else:
    for A in range(N):
     for B in range(N):
      qs=[]
      for x in xs:
       pa=(1-mu) if x[A] else mu
       pb=(1-mu) if x[B] else mu
       qs.append((pa+pb)/2)
      for bits in product((0,1), repeat=m):
       q=Fraction(1,N*N*N)
       ys=[]
       for x,b,p1 in zip(xs,bits,qs):
        q*=p1 if b else (1-p1)
        y=list(x); y[v]=b; ys.append(tuple(y))
       key=tuple(ys); out[key]=out.get(key,Fraction(0))+pr*q
 return out

def calc(pattern, model):
 m=max(pattern)+1
 dist={xs: __import__('functools').reduce(lambda a,b:a*b,[nu_d[x] for x in xs],Fraction(1)) for xs in product(states, repeat=m)}
 d1=step(dist,m,model)
 d1c={xs:pr*root22(xs[pattern[0]]) for xs,pr in d1.items() if root22(xs[pattern[0]])}
 d2=step(d1c,m,model)
 return sum(pr*g2(xs[pattern[1]])*g2(xs[pattern[2]]) for xs,pr in d2.items())

patterns={'distinct':(0,1,2),'childsame':(0,1,1),'h0h1':(0,0,1),'h0h2':(0,1,0),'allsame':(0,0,0)}
res={}
for model in ['c023','c026']:
 print(model)
 for name,p in patterns.items():
  v=calc(p,model); res[(model,name)]=v; print(name,v,float(v))
 total=(Fraction((L-1)*(L-2),L*L)*res[(model,'distinct')] + Fraction(L-1,L*L)*res[(model,'childsame')] + 2*Fraction(L-1,L*L)*res[(model,'h0h1')] + Fraction(1,L*L)*res[(model,'allsame')])
 print('TOTAL',total,float(total))
 res[(model,'total')]=total
print('diff',res[('c026','total')]-res[('c023','total')],float(res[('c026','total')]-res[('c023','total')]))

assert res[("c023","distinct")] == Fraction(9,1024)
assert res[("c026","distinct")] == Fraction(45301,5120000)
assert res[("c023","total")] == Fraction(11495,1048576)
assert res[("c026","total")] == Fraction(2888599,262144000)
assert res[("c026","total")]-res[("c023","total")] == Fraction(14849,262144000)
print("C026 full-tree two-generation witness PASS")
print("event=root 2|2 at generation 1 and both two-leaf children split at generation 2")
print("C023=11495/1048576")
print("C026=2888599/262144000")
print("difference=14849/262144000")
print("ALL_EXACT_CHECKS_PASS")
