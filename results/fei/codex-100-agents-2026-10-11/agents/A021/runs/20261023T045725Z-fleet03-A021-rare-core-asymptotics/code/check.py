from pathlib import Path
import importlib.util,json,time,sys
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('arithmetic',ROOT/'code'/'arithmetic.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
plus,mul,lg,ce,entropy,spectrum,inf,restrict,const=m.plus,m.mul,m.lg,m.ce,m.entropy,m.spectrum,m.inf,m.restrict,m.const
count=0
def ck(x,label):
 global count
 count+=1
 assert x,(count,label)
def R(a,delta):
 p=spectrum(a);return [1-delta+delta*p[0]]+[delta*x for x in p[1:]]
def G(a,delta):return plus(entropy(R(a,delta)),mul(entropy(spectrum(a)),-delta))
def J(a,delta,w):
 s=Q(sum(a),len(a));r=1-delta+delta*s*s
 return plus(G(a,delta),mul(lg(r),1-w))
def qdata(d,h):
 ans=[Q(1)]
 for block in range(2):
  e=min(3,max(0,d-3*block));v=(h>>(3*block))&((1<<e)-1)
  if e==0:q=[Q(9,16)]+[Q(1,16)]*7
  elif e==1:q=[Q(1,4)]*4 if v==0 else [Q(13,16)]+[Q(1,16)]*3
  elif e==2:q=[Q(1,16),Q(15,16)] if v==0 else [Q(15,16),Q(1,16)]
  else:q=[Q(1)]
  ans=[x*y for y in q for x in ans]
 return ans
def function(v,d,h,a):
 return [(-1 if (x&7)==0 else 1)*(-1 if (x>>3)==0 else 1)*(aa if x==v else 1)
  for aa in a for y in range(1<<(6-d)) for x in [h+(y<<d)]]
def state(v,d,h,a,delta):
 f=function(v,d,h,a);p=spectrum(f);q=qdata(d,h);r=R(a,delta)
 c=ce(p,[x*y for y in r for x in q]);H=entropy(p)
 I=sum((inf(f,i) for i in range(6-d)),Q(0))
 return c,H,I,plus(c,mul(H,-1))
def run(pilot):
 start=time.perf_counter();delta=Q(1,64);U=Q(2,64);rows=0;tree_nodes=0
 vertices=[0] if pilot else [0,1,63]
 controls=range(4) if pilot else range(16)
 for v in vertices:
  for mask in controls:
   a=[1-2*((mask>>z)&1) for z in range(4)]
   for d in [1,2,5]:
    w=Q(1,1<<d);eta=delta/w;h=v% (1<<d)
    states=[state(v,d,hh,a,delta) for hh in range(1<<d)]
    C=mul(plus(*(x[0] for x in states)),w);I=w*sum(x[2] for x in states)
    B=plus(const(4*I-U),mul(entropy(spectrum(a)),delta),mul(C,-1))
    ck(m.ge(B,Q(26,576)),'consume actual paid data bank')
    # Full active branch spectrum; all inactive complete costs remain in C.
    def query(aa,coord):
     nonlocal tree_nodes
     tree_nodes+=1
     parent=state(v,d,h,aa,delta);children=[restrict(aa,coord,b) for b in [0,1]]
     st=[state(v,d,h,child,delta) for child in children]
     drop=plus(parent[0],mul(plus(*(x[0] for x in st)),-Q(1,2)))
     da=plus(entropy(spectrum(aa)),mul(plus(*(entropy(spectrum(ch)) for ch in children)),-Q(1,2)))
     gain=plus(mul(drop,w),mul(da,-delta))
     predicted=plus(J(aa,delta,w),mul(plus(*(J(ch,delta,w) for ch in children)),-Q(1,2)))
     ck(gain==predicted,'localized exact potential gain')
     ck(m.ge(gain),'localized Jensen release')
     ck(parent[2]==sum(x[2] for x in st)/2,'affine remaining physical influence')
     dh=plus(parent[1],mul(plus(*(x[1] for x in st)),-Q(1,2)))
     dk=plus(mul(plus(*(x[3] for x in st)),Q(1,2)),mul(parent[3],-1))
     ck(dk==plus(dh,mul(drop,-1)),'BOTH full child KL signed conversion')
     ck(plus(gain,mul(dk,w),mul(da,delta),mul(dh,-w))=={},'signed original source conservation')
     # The actual controller marginal differs from the original-density reference.
     p=spectrum(function(v,d,h,aa));n=1<<(6-d)
     ck([sum(p[z*n:(z+1)*n]) for z in range(len(aa))]==R(aa,eta),'actual conditional density')
     ck(m.ge(parent[3]) and all(m.ge(x[3]) for x in st),'all full KL nonnegative')
     return gain,children
    for coord in [0,1]:
     gain,children=query(a,coord);ck(m.ge(plus(B,gain),Q(26,576)),'same bank no reset')
     # Outcome-dependent stopping: query remaining bit ONLY after control outcome0.
     gain2,_=query(children[0],0)
     total=plus(gain,mul(gain2,Q(1,2)))
     ck(m.ge(total),'stopped active-only controller tree')
     leafH=plus(mul(entropy(spectrum(children[1])),Q(1,2)),
       mul(plus(*(entropy(spectrum(restrict(children[0],0,b))) for b in [0,1])),Q(1,4)))
     spent=plus(entropy(spectrum(a)),mul(leafH,-1))
     ck(plus(mul(spent,delta),mul(leafH,delta))==mul(entropy(spectrum(a)),delta),'original entropy earmark not renewed')
     rows+=1
    if time.perf_counter()-start>110:raise RuntimeError('frozen main cap')
 result={'status':'PASS','query_cases':rows,'tree_nodes':tree_nodes,'assertions':count,'support_assertions':m.count,'seconds':time.perf_counter()-start}
 (ROOT/'out'/('PILOT.json' if pilot else 'DIRECT.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(result))
if __name__=='__main__':run('--pilot' in sys.argv)
