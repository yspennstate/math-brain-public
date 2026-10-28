from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,time,sys
ROOT=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('arith',ROOT/'code/arithmetic.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
plus,mul,const=m.plus,m.mul,m.const
count=0
def ck(x,label):
 global count
 count+=1;assert x,(count,label)
def qdata(d,h):
 out=[Q(1)]
 for block in range(2):
  e=min(3,max(0,d-3*block));v=(h>>(3*block))&((1<<e)-1)
  if e==0:q=[Q(9,16)]+[Q(1,16)]*7
  elif e==1:q=[Q(1,4)]*4 if v==0 else [Q(13,16)]+[Q(1,16)]*3
  elif e==2:q=[Q(1,16),Q(15,16)] if v==0 else [Q(15,16),Q(1,16)]
  else:q=[Q(1)]
  out=[x*y for y in q for x in out]
 return out
def run(pilot=False):
 start=time.perf_counter();rows=[]
 for vertex in ([None,0,1,63] if pilot else [None]+list(range(64))):
  table=[(-1 if x&7==0 else 1)*(-1 if x>>3==0 else 1)*(-1 if x==vertex else 1) for x in range(64)]
  nodes=[]
  def solve(d,h):
   f=[table[h+(y<<d)] for y in range(1<<(6-d))];q=qdata(d,h)
   I=sum((m.inf(f,j) for j in range(6-d)),Q(0));C=m.ce(m.spectrum(f),q)
   stop=plus(const(4*I),mul(C,-1));value=stop;action='stop'
   if d<5:
    go=mul(plus(solve(d+1,h),solve(d+1,h+(1<<d))),Q(1,2))
    diff=plus(stop,mul(go,-1))
    if not diff:action='tie'
    else:
     lo,hi=m.bounds(diff);ck(lo>0 or hi<0,'certified Bellman comparison')
     if lo>0:value=go;action='query'
   nodes.append({'d':d,'h':h,'action':action,'value':{str(k):str(v) for k,v in value.items()}})
   return value
  root=solve(0,0);lo,hi=m.bounds(root)
  ck(lo>=Q(1,4),'all-stopping-cuts data-account >=1/4')
  rows.append({'vertex':vertex,'lower':str(lo),'upper':str(hi),'root_expression':{str(k):str(v) for k,v in root.items()},'nodes':nodes})
  if time.perf_counter()-start>55:raise RuntimeError('frozen60s cap')
 result={'status':'PASS','functions':len(rows),'nodes':sum(len(x['nodes']) for x in rows),'assertions':count,'support_assertions':m.count,'seconds':time.perf_counter()-start,'rows':rows}
 (ROOT/'out'/('PILOT.json' if pilot else 'BELLMAN.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
if __name__=='__main__':run('--pilot' in sys.argv)
