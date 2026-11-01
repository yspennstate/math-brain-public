from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import importlib.util,time,json,sys
R=Path(__file__).resolve().parents[1]
sp=importlib.util.spec_from_file_location('base',R/'code/check.py');c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c)
m=c.m;plus,mul,const=c.plus,c.mul,c.const
count=0
def ck(x,label):
 global count
 count+=1
 assert x,(count,label)
def output(a):return [c.seed(x)*(aa if x in (0,1) else 1) for aa in a for x in range(64)]
start=time.perf_counter();indices=list(combinations(range(8),4));pilot='--pilot' in sys.argv
if pilot:indices=indices[:2]
rootT=c.T(Q(0));D=c.GV(output([-1,1]),range(6));heavy_cases=0;zero_cases=0
for selected in indices:
 a=[1 if z in selected else -1 for z in range(8)];f=output(a)
 ds=[Q(m.fwht(a)[1<<j],8) for j in range(3)]
 ga=c.GV(a);gf=c.GV(f);va=c.V(a)
 ck(c.V(f)==plus(mul(va,Q(1,32)),rootT),'arbitrary balanced potential split')
 smooth=plus(*(plus(rootT,mul(plus(c.T(d),c.T(-d)),-Q(1,2))) for d in ds))
 corrected=plus(gf,mul(ga,-Q(1,32)))
 ck(corrected==plus(D,smooth),'arbitrary balanced exact control/DATA cancellation')
 ck(sum(d*d for d in ds)<=1,'Parseval singleton mass')
 heavy=sum(abs(d)>Q(1,2) for d in ds);heavy_cases+=bool(heavy);zero_cases+=all(d==0 for d in ds)
 ck(heavy<=3,'at most three heavy singleton coefficients')
 ck(m.ge(plus(const(70),mul(corrected,-1))),'all-balanced upper70')
 Id=sum((m.inf(f,j) for j in range(6)),Q(0));ck(Id>=Q(21,16),'all-balanced DATA reserve')
 ck(m.ge(plus(const(256*Id),mul(corrected,-1))),'all-balanced SAME256 transfer')
 h=[aa*(1 if y==0 else -1) for aa in a for y in (0,1)]
 ck(plus(ga,mul(c.GV(h),-1))==plus(*(c.phi(d*d) for d in ds)),'all-balanced marked singleton cocycle')
 if time.perf_counter()-start>110:raise RuntimeError('frozen runtime cap')
out={'status':'PASS','pilot':pilot,'actual_control_bits':3,'balanced_truth_tables':len(indices),'symmetry':'none','assertions':count,'heavy_singleton_cases':heavy_cases,'all_zero_singleton_cases':zero_cases,'seconds':time.perf_counter()-start,'scope':'Finite corroboration of analytic arbitrary-control-dimension balanced shared-controller repair, not its all-dimensional proof.'}
(R/'out'/('BALANCED_PILOT.json' if pilot else 'BALANCED.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
