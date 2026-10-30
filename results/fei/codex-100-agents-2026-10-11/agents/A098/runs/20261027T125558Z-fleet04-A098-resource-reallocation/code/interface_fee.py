from fractions import Fraction as F
from math import lcm
from pathlib import Path
import json

# Fixed two fixtures; no search and no author-helper imports.
def spectrum(tab):
 return tuple(F(sum(y*(-1 if (s&x).bit_count()%2 else 1) for x,y in enumerate(tab)),len(tab))**2 for s in range(len(tab)))
def erase_lsb(p):return tuple(p[2*s]+p[2*s+1] for s in range(len(p)//2))
def expbracket(p,v,u):
 # 2^(den*[D(p||u)-D(p||v)+D(u||v)]).
 den=lcm(*(a.denominator for a in p),*(a.denominator for a in u))
 value=F(1)
 for a,b,c in zip(p,v,u):
  if a:value*=F(b/c)**int(den*a)
  if c:value*=F(c/b)**int(den*c)
 return den,value
checks=0
def ck(x):
 global checks
 checks+=1;assert x

records=[]
for n in [2,3]:
 tab=tuple(1 if x==(1<<n)-1 else -1 for x in range(1<<n))
 p=spectrum(tab);q=p if n==2 else (F(1,1<<n),)*(1<<n)
 R=erase_lsb(p);V=erase_lsb(q)
 children=[spectrum(tuple(y for x,y in enumerate(tab) if x&1==b)) for b in [0,1]]
 brackets=[]
 for b,child in enumerate(children):
  K=tuple(child[s]/(2*R[s]) for s in range(len(R)))
  outcome=sum(v*k for v,k in zip(V,K));u=tuple(v*k/outcome for v,k in zip(V,K))
  ck(sum(u)==1);ck(all(u[s]>0 for s,a in enumerate(child) if a))
  den,product=expbracket(child,V,u);brackets.append((den,product))
  if b==0:
   ck(u[0]==1 and all(a==0 for a in u[1:]));ck(V[0]<1)
  if n==2:
   ck(u==child);ck(product==1)
  elif b==1:
   ck(child==(F(1,4),)*4);ck(V==(F(1,4),)*4)
   ck(u==(F(1,16),F(5,16),F(5,16),F(5,16)))
   ck(product==5**3 and den==16)
 if n==2:
  ck(V==(F(1,2),F(1,2)))
  # Forward D(true-kernel constant||projected)=1; reverse is infinite.
  ck(V[0]**(-1)==2)
  records.append({'n':n,'forward_constant_child_fee_bits':'1','reverse_divergence':'INFINITY','update_brackets':'0,0'})
 else:
  ck(brackets[0][1]==1)
  # Averaging the two actual outcomes gives (3/32)*log2(5)>0.
  records.append({'n':n,'root_reference':'uniform','forward_update_average_excess_bits':'(3/32)log2(5)>0','exact_child_power_certificate':'2^(16*child_excess)=125'})
out={'status':'PASS','exact_assertions':checks,'fixtures':records,'scope':'A093 BOARD candidate independently reconstructed; no claim of reading a completed new A093 proof or of refuting A097 affine updates.'}
(Path(__file__).resolve().parents[1]/'out/INTERFACE_FEE.json').write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
print(json.dumps(out))
