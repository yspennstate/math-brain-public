from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,time
r=Path(__file__).resolve().parents[1]
spec={'helper':'own stage18 exact arithmetic, copied unchanged','family':'five local seed/reference types; every local edited vertex','domain':'g3/q3, g2/uniform4,constant2/q13,char1/q15,constant1/q15','case_count':20,'symmetry':'none','arithmetic':'exact Fraction FWHT, physical edges and prime-log identities','memory_estimate_mb':60,'max_seconds':60}
(r/'LOCAL_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
sp=importlib.util.spec_from_file_location('arith',r/'code/arithmetic.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
count=0;cases=0;start=time.perf_counter()
def ck(x,s):
 global count
 count+=1;assert x,(count,s)
L3,L13,L15=m.lg(3),m.lg(13),m.lg(15)
families=[([-1]+[1]*7,[Q(9,16)]+[Q(1,16)]*7),([-1,1,1,1],[Q(1,4)]*4),([1]*4,[Q(13,16)]+[Q(1,16)]*3),([-1,1],[Q(1,16),Q(15,16)]),([1,1],[Q(15,16),Q(1,16)])]
def bank(f,q):
 n=len(f).bit_length()-1;I=sum((m.inf(f,i) for i in range(n)),Q(0));return m.plus(m.const(4*I),m.mul(m.ce(m.spectrum(f),q),-1))
for kind,(f,q) in enumerate(families):
 for v in range(len(f)):
  edited=f.copy();edited[v]*=-1;X=m.mul(m.plus(bank(f,q),m.mul(bank(edited,q),-1)),len(f))
  if kind==0:expected=m.plus(m.const(24),m.mul(L3,-7)) if v==0 else m.plus(m.mul(L3,5),m.const(-8 if v.bit_count()==1 else -24))
  elif kind==1:expected=m.const(-8*sum(f[v]*f[v^(1<<i)] for i in range(2)))
  elif kind==2:expected=m.plus(m.mul(L13,3),m.const(-16))
  elif kind==3:expected=m.plus(m.mul(L15,2),m.const(8))
  else:expected=m.plus(m.mul(L15,2),m.const(-8))
  ck(X==expected,'local signed edit coefficient');ck(m.bounds(X)[1]<= (Q(118,9) if kind==0 else 16),'uniform local X bound');cases+=1
 beta=m.plus(m.const(-1),m.mul(L3,Q(9,8))) if kind==0 else bank(f,q)
 ck(m.ge(beta,Q(3,4) if kind==0 else -Q(1,3)),'seed bank lower bound')
out={'status':'PASS','cases':cases,'assertions':count,'support_assertions':m.count,'seconds':time.perf_counter()-start}
(r/'out/LOCAL.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
