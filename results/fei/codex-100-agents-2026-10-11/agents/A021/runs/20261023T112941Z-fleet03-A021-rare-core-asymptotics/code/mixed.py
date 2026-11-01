from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,time
ROOT=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('arith',ROOT/'code/arithmetic.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
sp2=importlib.util.spec_from_file_location('dp',ROOT/'code/check.py');dp=importlib.util.module_from_spec(sp2);sp2.loader.exec_module(dp)
plus,mul,const=m.plus,m.mul,m.const
count=0;delta=Q(1,64);U=Q(1,32)
def ck(x,s):
 global count
 count+=1;assert x,(count,s)
def R(a):
 p=m.spectrum(a);return [1-delta+delta*p[0]]+[delta*x for x in p[1:]]
def active(leaf,v):return v% (1<<leaf['d'])==leaf['h']
def state(leaf,v):
 d,h,a=leaf['d'],leaf['h'],leaf['a'];f=[(-1 if x&7==0 else 1)*(-1 if x>>3==0 else 1)*(aa if x==v else 1) for aa in a for y in range(1<<(6-d)) for x in [h+(y<<d)]]
 P=m.spectrum(f);q=dp.qdata(d,h);C=m.ce(P,[x*y for y in leaf['R'] for x in q]);H=m.entropy(P);I=sum((m.inf(f,i) for i in range(6-d)),Q(0));return f,C,H,I,plus(C,mul(H,-1))
def total(leaves,v):
 C={};H={};D={};I=Q(0);L={}
 for leaf in leaves:
  f,c,h,i,dd=state(leaf,v);w=leaf['p']*Q(1,1<<leaf['d'])
  C=plus(C,mul(c,w));H=plus(H,mul(h,w));D=plus(D,mul(dd,w));I+=w*i
  ck(m.ge(dd),'full terminal KL')
  if active(leaf,v):L=plus(L,mul(m.entropy(m.spectrum(leaf['a'])),delta*leaf['p']))
 B=plus(const(4*I-U),L,mul(C,-1));ck(m.ge(B,Q(1,16)),'unequal-frontier SAME reserve >=t/32')
 return B,D,H,I,L
def main():
 start=time.perf_counter();cases=0;frontiers=0
 for v in [0,1,63]:
  for mask in range(16):
   a=[1-2*((mask>>z)&1) for z in range(4)]
   root={'d':0,'h':0,'a':a,'R':R(a),'p':Q(1)};original=total([root],v)
   for depth in [1,2,4]:
    leaves=[{'d':depth,'h':h,'a':a,'R':R(a),'p':Q(1)} for h in range(1<<depth)]
    initial=total(leaves,v);E=plus(const(4*(original[3]-initial[3])),mul(original[2],-1),initial[2])
    ck(plus(initial[0],initial[1],E)==plus(original[0],original[1]),'original DATA history retained')
    def query(leaf,kind):
     nonlocal leaves,E,frontiers
     f,c,H,I,D=state(leaf,v);w=leaf['p']*Q(1,1<<leaf['d']);children=[]
     for b in [0,1]:
      child=dict(leaf)
      if kind=='CONTROL':
       child['a']=m.restrict(leaf['a'],0,b);child['R']=R(child['a']);child['p']/=2
      else:child['d']+=1;child['h']+=b*(1<<leaf['d'])
      children.append(child)
     newH=mul(plus(*(state(ch,v)[2] for ch in children)),Q(1,2));dh=plus(H,mul(newH,-1))
     if kind=='CONTROL':
      da=plus(m.entropy(m.spectrum(leaf['a'])),mul(plus(*(m.entropy(m.spectrum(ch['a'])) for ch in children)),-Q(1,2)))
      increment=plus(mul(da,delta*leaf['p']),mul(dh,-w))
     else:increment=plus(const(4*w*m.inf(f,0)),mul(dh,-w))
     E=plus(E,increment);leaves.remove(leaf);leaves+=children;now=total(leaves,v);frontiers+=1
     ck(plus(now[0],now[1],E)==plus(original[0],original[1]),'full unequal-depth signed history with BOTH KLs')
     return children
    chosen=next(l for l in leaves if active(l,v));children=query(chosen,'CONTROL')
    # DATA only on controller outcome0, leaving outcome1 at its old depth.
    datachildren=query(children[0],'DATA');newactive=next(l for l in datachildren if active(l,v))
    query(newactive,'CONTROL')
    ck(len({l['d'] for l in leaves})==2,'genuine unequal DATA depths')
    cases+=1
    if time.perf_counter()-start>110:raise RuntimeError('frozen120s cap')
 result={'status':'PASS','mixed_cases':cases,'frontiers':frontiers,'assertions':count,'support_assertions':m.count,'seconds':time.perf_counter()-start}
 (ROOT/'out/MIXED.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
