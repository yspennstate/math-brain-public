from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import importlib.util,json,time,sys,hashlib
R=Path(__file__).resolve().parents[1]
OLD=R.parent/'20261023T014825Z-account03-A052-critical-source-structure/code/check_rank_pair.py'
spec=importlib.util.spec_from_file_location('prior',OLD);h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
COUNT=0
def ck(t):
 global COUNT
 COUNT+=1
 if not t:raise AssertionError(COUNT)
def bits(mask,n):return [j for j in range(n) if mask>>j&1]
def pack(x,ps):return sum((x>>j&1)<<i for i,j in enumerate(ps))
def embed(x,ps):return sum((x>>i&1)<<j for i,j in enumerate(ps))
def branches(f,A):
 n=len(f).bit_length()-1;aa=bits(A,n);cc=bits(((1<<n)-1)^A,n)
 return [tuple(f[embed(u,aa)|embed(z,cc)] for z in range(1<<len(cc))) for u in range(1<<len(aa))]
@lru_cache(None)
def profile(f):
 ff=list(f);return h.entropy(ff),h.inf(ff),h.release(ff)['a']
def aggregate(f,A):
 ch=branches(f,A);q=F(1,len(ch));H,I,_=profile(f)
 hs=h.add(*[(profile(g)[0],q) for g in ch]);ei=q*sum(profile(g)[1] for g in ch);ea=q*sum(profile(g)[2] for g in ch)
 return {'L':h.add((H,1),(hs,-1)),'Q':I-ei,'rho':ei-ea,'S':h.add((h.constant(F(15,4)*ea),1),(hs,-1)),'a':ea,'H':H,'I':I}
def transform(f,A,qmatrix,d):
 n=len(f).bit_length()-1;aa=bits(A,n);cc=bits(((1<<n)-1)^A,n);out=[]
 for y in range(1<<n):
  x=y
  for j,c in enumerate(cc):
   flip=sum(((qmatrix>>(j*len(aa)+i))&1)*((y>>a)&1) for i,a in enumerate(aa))%2
   x^=flip<<c
  out.append(f[x]*(-1 if (d&y).bit_count()%2 else 1))
 return tuple(out)
def case(f,A,qmatrix,d):
 before=aggregate(f,A);ff=transform(f,A,qmatrix,d);after=aggregate(ff,A)
 delta=after['I']-before['I']
 ck(before['H']==after['H']);ck(before['L']==after['L']);ck(before['S']==after['S'])
 ck(after['Q']+after['rho']-delta==before['Q']+before['rho'])
 ck(sorted((str(profile(g)[0]),profile(g)[2]) for g in branches(f,A))==sorted((str(profile(g)[0]),profile(g)[2]) for g in branches(ff,A)))
 ck(h.add((before['H'],1),(h.constant(F(15,4)*before['I']),-1),(before['S'],1))==h.add((after['L'],1),(h.constant(F(15,4)*(after['Q']+after['rho']-delta)),-1)))
 return before,after,delta
def main():
 start=time.perf_counter();pilot='--pilot' in sys.argv;roots=cases=0
 for n in ([2] if pilot else [2,3]):
  for t in range(1<<(1<<n)):
   f=tuple(1-2*(t>>x&1) for x in range(1<<n));roots+=1
   for A in range(1,(1<<n)-1):
    width=A.bit_count()*(n-A.bit_count())
    for q in range(1<<width):
     for d in range(1<<n):case(f,A,q,d);cases+=1
   if time.perf_counter()-start>53:raise TimeoutError('frozen53s')
 fixtures=[]
 for k in ([2] if pilot else [2,3,4]):
  f=tuple(h.root(k));p=F(1,1<<k)
  # Q has row c,z,control1,...; column a,b. row2 col0 is bit4.
  before,after,delta=case(f,3,1<<4,0)
  ck(delta==p/4);ck(before['Q']==p);ck(after['Q']==5*p/4);ck(before['rho']==after['rho']==p/4)
  ck(after['Q']+after['rho']==3*p/2)
  fixtures.append({'k':k,'delta':str(delta),'original_Q_plus_rho':str(before['Q']+before['rho']),'new_Q_plus_rho':str(after['Q']+after['rho'])})
 out={'status':'PASS','pilot':pilot,'tables':roots,'preconditioned_cases':cases,'checks':COUNT,'fixtures':fixtures,'seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest()}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
