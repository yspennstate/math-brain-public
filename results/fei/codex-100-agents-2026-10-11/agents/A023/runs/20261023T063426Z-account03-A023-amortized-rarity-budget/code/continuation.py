"""One already-funded source, with actual live-survivor withdrawal."""
import sys,time,json,itertools,importlib.util
from pathlib import Path
from fractions import Fraction as Q
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1];sp=importlib.util.spec_from_file_location('primary',RUN/'code/check.py');p=importlib.util.module_from_spec(sp);sp.loader.exec_module(p);h=p.h
START=time.perf_counter();CHECKS=0
def ck(ok):
 global CHECKS
 assert ok
 CHECKS+=1
 assert time.perf_counter()-START<60
def direct(t):
 N=len(t);out={}
 for mask in range(N):
  a=sum(v*(-1 if (x&mask).bit_count()%2 else 1) for x,v in enumerate(t))
  if a:out[mask]=Q(a*a,N*N)
 ck(sum(out.values())==1);return out
def edges(t):return sum((Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range(len(t).bit_length()-1)),Q(0))
m=6;options=[[{a:1},{a:0,a+1:0},{a:0,a+1:1}] for a in range(0,m,2)];MASS=DEPTH=CONSUMED=EZ=EM=ACTIVE=Q(0);EB={};rows=[]
for parts in itertools.product(*options):
 parent={i:v for part in parts for i,v in part.items()};free=[i for i in range(m) if i not in parent]
 for A,B in itertools.product([0,1],repeat=2):
  active=A==B==0
  assignments=itertools.product([0,1],repeat=len(free)) if active else [()]
  for bits in assignments:
   cf=parent|dict(zip(free,bits));fix=cf|{m+1:A,m+2:B};s=p.state(m,1,0,fix,0);reach=Q(1,1<<(len(cf)+2));MASS+=reach;DEPTH+=reach*len(cf);CONSUMED+=reach*(len(free) if active else 0);EZ+=reach*s['Z'];EM+=reach*s['M'];EB=h.add((1,EB),(reach,s['B']))
   data=[i for i in range(m) if i not in cf];base=[];table=[];flips=0
   for x in range(1<<len(data)):
    y=sum(v<<i for i,v in cf.items())+sum(((x>>j)&1)<<i for j,i in enumerate(data));seed=(-1)**sum(((y>>a)&1)*((y>>(a+1))&1) for a in range(0,m,2));val=seed*(-1 if A and y==(1 if B else 0) else 1);base.append(seed);table.append(val);flips+=int(val!=seed)
   spectrum=direct(table);seedp=direct(base);q={j:(seedp.get(j,Q(0))+Q(1,len(base)))/2 for j in range(len(base))};H={};CE={}
   for j,a in spectrum.items():h.lg(H,a,-a);h.lg(CE,q[j],-a)
   ID=edges(table);KL=h.add((1,CE),(-1,H));bank=h.add((1,h.rational(4*ID-Q(m,8))),(-1,CE))
   ck(H==s['H'] and CE==s['C'] and KL==s['K'] and bank==s['B']);ck(ID==s['ID'] and s['R']==0);ck(Q(flips,len(base))==s['M'])
   if active:ck(s['B']==h.rational(-Q(m,8)));ACTIVE+=reach
   rows.append({'fixed_core':cf,'A':A,'B':B,'reach':str(reach),'consumed_live':len(free) if active else 0,'B':p.vector(bank),'full_KL':p.vector(KL)})
ck(len(rows)==145);ck(MASS==1);ck(DEPTH==Q(13*m,16));ck(CONSUMED==Q(m,16));ck(EZ==m-4*CONSUMED);ck(EM==Q(1,1<<(m+1)));ck(ACTIVE==Q(1,4))
bound=Q(7*m,8)-1-(9*m+Q(15,4))*Q(1,1<<m)-4*CONSUMED;ck(bound==Q(473,256));ck(h.sign(h.add((1,EB),(-1,h.rational(bound))))>0)
for n in range(6,65):
 b=Q(5*n,8)-1-(9*n+Q(15,4))*Q(1,1<<n);ck(b>=Q(473,256));ck(b>1)
out={'status':'PASS','terminal_states':len(rows),'parent_profiles':27,'checks':CHECKS,'inherited_primary_checks':p.CHECKS,'elapsed_seconds':time.perf_counter()-START,'expected_core_depth':str(DEPTH),'expected_consumed_live':str(CONSUMED),'expected_source_Z':str(EZ),'expected_original_rare_lot':str(EM),'active_negative_mass':str(ACTIVE),'expected_B':p.vector(EB),'strict_analytic_lower_bound':str(bound),'scope':'Separate direct-character lane at every terminal; same author, independent-person review pending.'}
(RUN/'out/continuation_rows.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8');(RUN/'out/continuation_validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
