from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import importlib.util,json,time,math
R=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('direct_math',R/'code/direct_math.py');u=importlib.util.module_from_spec(sp);sp.loader.exec_module(u)
add,scale=u.add,u.scale;count=0
def ck(x,label):
 global count
 count+=1;assert x,(count,label)
def c(x):return {2:Q(x)} if x else {}
def restriction(f,i,b):return tuple(v for x,v in enumerate(f) if (x>>i)&1==b)
@lru_cache(None)
def V(f):
 p=u.spectrum(f);up=[sum((v for t,v in enumerate(p) if t&s==s),Q(0)) for s in range(len(p))]
 return add(*(scale(u.log(up[s]/p[s]),p[s]) for s in range(1,len(p)) if p[s]))
def gv(f,coords=None):
 n=len(f).bit_length()-1
 return add(*(add(V(f),scale(add(V(restriction(f,i,0)),V(restriction(f,i,1))),-Q(1,2))) for i in (range(n) if coords is None else coords)))
def phi(x):return scale(u.log(1/x),x) if x else {}
def seed(x):return (-1 if x&7==0 else 1)*(-1 if x>>3==0 else 1)
def main():
 start=time.perf_counter();n=3;d=Q(1,2);delta=Q(1,64)
 a=tuple(1 if x.bit_count()>1 else -1 for x in range(8));h=tuple(aa*(1 if y==0 else -1) for aa in a for y in [0,1]);f=tuple(seed(x)*(aa if x in [0,1] else 1) for aa in a for x in range(64))
 b=tuple(seed(x) for x in range(64));bh=[Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(b)),64) for s in range(64)]
 def T(s):
  A=[v+2*delta*(s-1)*(j&1) for j,v in enumerate(bh)];M=[v*v+4*delta*delta*(1-s*s)*(j&1) for j,v in enumerate(A)];Z=[sum((v for t,v in enumerate(M) if t&j==j),Q(0)) for j in range(64)]
  ck(sum(M)==1,'actual complete marginal');return add(*(scale(u.log(Z[j]/(A[j]*A[j])),A[j]*A[j]) for j in range(1,64)),c(5*delta*(1-s*s)))
 va,ga,gh,gf=V(a),gv(a),gv(h),gv(f);gd=gv(f,range(6));single=scale(phi(d*d),n);smooth=scale(add(T(Q(0)),scale(add(T(d),T(-d)),-Q(1,2))),n)
 ck(add(ga,scale(gh,-1))==single,'owner singleton exact')
 ck(V(f)==add(scale(va,2*delta),T(Q(0))),'full output potential exact')
 residual=add(gf,scale(gh,-2*delta));ck(residual==add(scale(single,2*delta),smooth,gd),'FULL residual direct-character replay')
 ck(u.spectrum(h)[1]==0,'root selector singleton is zero')
 for side in [0,1]:ck(u.spectrum(restriction(h,1,side))[1]==d*d,'both controller child singletons retained')
 fdict=tuple(seed(x)*(aa if x in [0,1] else 1) for aa in [-1,1] for x in range(64));ck(gd==gv(fdict,range(6)),'DATA bill independent of majority profile')
 corrected=add(gf,scale(ga,-2*delta));Id=sum((Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(6)),Q(0))
 ck(Id>=Q(21,16),'DATA influence lower bound');ck(u.lower(add(corrected,c(37)))>=0,'corrected lower bound');ck(u.lower(add(c(49),scale(corrected,-1)))>=0,'corrected upper bound');ck(u.lower(add(c(256*Id),scale(corrected,-1)))>=0,'SAME256 repair')
 for m in range(1,257):
  dm=Q(math.comb(2*m,m),1<<(2*m));nextd=Q(math.comb(2*m+2,m+1),1<<(2*m+2))
  ck(nextd==dm*Q(2*m+1,2*m+2),'exact binomial recurrence')
  ck(Q(1,4*m)<=dm*dm<=Q(1,2*m+1),'squared coefficient bounds')
  ck(dm<=Q(1,2),'compact child means')
 for truth in [Q(101,8)<13,Q(19,32)<1,64*(6*256+38)==100736,Q(100736,64)-37==1537,1537>256*6,Q(3,2)-Q(12,64)==Q(21,16),49<256*Q(21,16)]:ck(truth,'uniform curvature/witness integer certificates')
 witness={'status':'ANALYTIC_ACTUAL_BOOLEAN_COUNTERFAMILY','definition':'b=g3 tensor g3; a=odd majority_n; F=b*a only at adjacent x=0,1; h=(-1)^y*a','K':256,'m':'2^100736','control_bits_n':'2^100737+1','delta':'1/64','proved_residual_lower':1537,'allowed_DATA_bill_upper':1536,'root_selector_singleton':0,'scope':'unproved combined-selector GV owner extension ONLY; NOT FEI; corrected original-a owner has SAME256 payment'}
 (R/'out/WITNESS.json').write_text(json.dumps(witness,indent=2)+'\n',encoding='utf-8')
 out={'status':'PASS','actual_control_bits':3,'scalar_cases':256,'assertions':count,'seconds':time.perf_counter()-start,'implementation':'direct character sums and direct upper-set sums; separate48-term rational-log arithmetic; no production import'}
 (R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':main()
