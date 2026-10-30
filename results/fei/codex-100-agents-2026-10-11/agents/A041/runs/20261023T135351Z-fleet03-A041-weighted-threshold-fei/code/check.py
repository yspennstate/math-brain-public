from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import ast,json,time,sys,hashlib
R=Path(__file__).resolve().parents[1]; O=R/'out'; pilot='--pilot' in sys.argv
old=R.parent/'20261023T050523Z-fleet03-A041-weighted-threshold-fei/code/check.py'
spec={'helper':'A041-sharp-joint-singleton-v1','family':'all three-bit Boolean signs; disjoint binary root/two-bit child/literal formulas; asymmetric four-bit chains; two actual AND4 low-carry controls; compressed Maj3 towers and nearconstant AND2 sharpness controls','domain':{'laws':[['1/3']*3,['1/4','1/2','3/4']],'flat_count':32 if pilot else 512,'formula_count':32 if pilot else 512,'chain_count':4 if pilot else 32,'AND4_low_carry_controls':2,'Maj3_depths':list(range(1,13)),'nearconstant_AND2_r':list(range(1,13)),'physical_exclusions':2},'symmetry':'none; all labelled tables in declared domain retained','arithmetic':'Fraction direct centered-product spectrum and coefficient products, rational prime-exponent logarithms, rigorous20-term atanh log intervals; all-alpha envelope follows analytic scalar inequality','memory_estimate_MB':100,'maximum_runtime_seconds':55,'source_helper_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'mode':'pilot' if pilot else 'main'}
(O/('FROZEN_PILOT.json' if pilot else 'FROZEN_SPEC.json')).write_bytes((json.dumps(spec,indent=2)+'\n').encode('utf-8'))
start=time.monotonic();module=ast.parse(old.read_text(encoding='utf-8'))
defs=ast.Module(body=[x for x in module.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef))],type_ignores=[])
ns={'__file__':str(old),'assertions':0,'start':start};exec(compile(defs,str(old),'exec'),ns)
ns['L2'],ns['U2']=ns['series'](Q(2));ck=ns['ck'];logint=ns['logint'];base=ns['spectrum']
def add(*terms):
 out={}
 for a,v in terms:
  for p,e in v.items():out[p]=out.get(p,Q(0))+a*e
 return {p:e for p,e in out.items() if e}
@lru_cache(None)
def facts(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def lv(q):return add((1,facts(q.numerator)),(-1,facts(q.denominator)))
def vint(v):
 lo=hi=Q(0)
 for p,e in v.items():
  l,u=logint(Q(p));lo+=e*(l if e>=0 else u);hi+=e*(u if e>=0 else l)
 return lo,hi
LN4={2:Q(2)}
def spectrum(ps,vals):
 f=base(ps,vals);P=f['P'];f['H']=f['D']-f['R']; f['J1']=Q(0);f['Jh']=Q(0);f['L1']={};f['Lh']={};W={}
 for s,p in P.items():
  if not s or not p:continue
  j=f['j'][s];t=abs(f['c'][s]);u=t*2**j;v=lv(1/(u*u))
  if s.bit_count()==1:
   f['J1']+=p*j;f['L1']=add((1,f['L1']),(p,v))
   ck(t*(j+logint(1/u)[1])<=1-t or u==1)
   ck(t*j<=1-t)
  else:f['Jh']+=p*j;f['Lh']=add((1,f['Lh']),(p,v));W[s]=p/(u*u)
 B=2*f['D']-f['R']-f['J1'];ck(B>=0)
 ck(vint(f['L1'])[1]<=2*B or (not f['L1'] and not B))
 Z=sum(W.values(),Q(0));H=f['H']
 f['Q']={s:(p if s.bit_count()<=1 else (H*W.get(s,0)/Z if Z else Q(0))) for s,p in P.items()}
 f['n']=add((H,lv(Z/H))) if H else {}
 f['K']=add(*[(p,lv(p/f['Q'][s])) for s,p in P.items() if p])
 ck(f['K']==add((1,f['n']),(-1,f['Lh'])));ck(sum(f['Q'].values())==1)
 return f
ns['spectrum']=spectrum;gate=ns['gate'];literal=ns['literal'];build0=ns['build']
def enrich(f):
 if 'local' not in f:
  f.update(Tu=Q(0),Vu={},C1=Q(0),Ch=Q(0),J1tree=f['J1'],L1tree=f['L1'],Jhtree=f['Jh'],Lhtree=f['Lh'],ntree=f['n'],Ktree=f['K'],Rt=f['R'])
  return f
 g,weights,ch=f['local'];active=[i for i,c in enumerate(ch) if c['w']]
 for c in ch:enrich(c)
 T=Q(0);V={}
 for k,i in enumerate(active):
  s=g['P'][1<<k];a=dict(weights)[i];b=a-s/ch[i]['w'];coef=g['c'][1<<k]
  if s:
   z=s/ch[i]['w']*ch[i]['H'];j=g['j'][1<<k];T+=z*j;V=add((1,V),(z,lv(1/(coef*coef*4**j))))
  T+=b*ch[i]['J1'];V=add((1,V),(b,ch[i]['L1']))
 C1=Ch=Q(0);nl=len(ch[0]['ps'])
 for s,p in f['P'].items():
  if not s or not p:continue
  parts=(s&((1<<nl)-1),s>>nl);am=sum((1<<k for k,i in enumerate(active) if parts[i]),0)
  j=g['j'][am]+sum((ch[i]['j'][parts[i]] for i in active if parts[i]),0)
  k=f['j'][s]-j;ck(k>=0)
  if s.bit_count()==1:C1+=p*k
  else:Ch+=p*k
 f['Tu']=T+sum((a*ch[i]['Tu'] for i,a in weights),Q(0));f['Vu']=add((1,V),*[(a,ch[i]['Vu']) for i,a in weights])
 f['C1']=C1+sum((a*ch[i]['C1'] for i,a in weights),Q(0));f['Ch']=Ch+sum((a*ch[i]['Ch'] for i,a in weights),Q(0))
 for key,field in [('J1tree','J1'),('Jhtree','Jh')]:f[key]=g[field]+sum((a*ch[i][key] for i,a in weights),Q(0))
 for key,field in [('L1tree','L1'),('Lhtree','Lh'),('ntree','n'),('Ktree','K')]:f[key]=add((1,g[field]),*[(a,ch[i][key]) for i,a in weights])
 # Exact source partitions, independently computed from the final physical spectrum.
 ck(f['J1']==f['J1tree']-f['Tu']+f['C1'])
 ck(add((1,f['L1']),(1,f['Vu']),(f['C1'],LN4))==f['L1tree'])
 ck(f['Jh']==f['Jhtree']+f['Tu']+f['Ch'])
 ck(add((f['Ch'],LN4),(1,f['Lh']))==add((1,f['Lhtree']),(1,f['Vu'])))
 ck(add((1,f['K']),(-1,f['Ktree']))==add((f['Ch'],LN4),(-1,f['Vu']),(1,f['n']),(-1,f['ntree'])))
 ck(add(*[(p,lv(p/f['T'][s])) for s,p in f['P'].items() if p])==f['Ktree'])
 ck(all(f['T'][s]==p for s,p in f['P'].items() if s.bit_count()<=1))
 # All-alpha identity: rational ln4 coefficient and exact mantissa-log coefficient.
 Bj=2*f['D']-f['Rt']-f['J1tree'];ck(Bj>=0)
 ck(vint(f['L1tree'])[1]<=2*Bj or (not f['L1tree'] and not Bj))
 ck(f['Tu']+f['J1']+Bj==2*f['D']-f['Rt']+f['C1'])
 if time.monotonic()-start>55:raise RuntimeError('frozen runtime exceeded')
 return f
def build(t,l,r):return enrich(build0(t,l,r))
flat=formulas=chains=0;positive_carry=0
laws=[(Q(1,3),)*3,(Q(1,4),Q(1,2),Q(3,4))]
for ps in laws:
 for t in range(16 if pilot else 256):gate(t,ps);flat+=1
 for rt in range(4 if pilot else 16):
  for ct in range(4 if pilot else 16):
   f=build(rt,gate(ct,ps[:2]),literal(ps[2]));formulas+=1;positive_carry+=int(f['C1']>0)
 for rt in range(2 if pilot else 16):
  f=build(rt,build(6,gate(8,ps[:2]),literal(ps[2])),literal(Q(2,5)));chains+=1;positive_carry+=int(f['C1']>0)
controls=[]
for ps,mass,jf,jlocal in [((Q(1,3),Q(2,5),Q(3,4),Q(1,4)),Q(3,400),3,2),((Q(1,2),Q(3,4),Q(5,8),Q(1,2)),Q(225,4096),2,1)]:
 f=build(8,gate(8,ps[:2]),gate(8,ps[2:]));g,_,cs=f['local']
 ck(f['P'][8]==mass and f['j'][8]==jf)
 ck(g['j'][2]+cs[1]['j'][2]==jlocal and f['C1']>=mass)
 controls.append({'biases':[str(p) for p in ps],'singleton_mass':str(mass),'final_j':jf,'local_j':jlocal,'C1':str(f['C1'])})
near=[]
for r in range(1,13):
 p=1-Q(1,2**r);f=gate(8,(p,p));B=2*f['D']-f['R']-f['J1']
 ck(not f['L1'] if r==1 else f['J1']==0)
 ck(vint(f['L1'])[1]<=2*B or not f['L1'])
 if r>1:near.append({'r':r,'L1_over_2Delta_interval':[str(z/(2*f['D'])) for z in vint(f['L1'])]})
towers=[]
for d in range(1,13):
 D=Q(3,2)**d-1;Rt=D/2;J1=Q(d)*Q(3,4)**d;T=Q(3,2)*D-J1
 ck(T+J1==2*D-Rt);ck(T>=0)
 towers.append({'d':d,'Delta':str(D),'Rtree':str(Rt),'J1_units':str(J1),'T_units':str(T)})
lit=literal(Q(1,3));ind=gate(8,(Q(1,3),Q(1,3)))
ck(lit['P'][0]==Q(1,9) and ind['P'][0]==Q(49,81) and lit['P'][0]!=ind['P'][0])
fair=gate(8,(Q(1,2),Q(1,2)));restricted=gate(0,(Q(1,2),))
absence=fair['P'][0]/(fair['P'][0]+fair['P'][2])
ck(absence==Q(1,2) and restricted['P'][0]==1 and absence!=restricted['P'][0])
out={'status':'PASS','flat_cases':flat,'formula_cases':formulas,'chains':chains,'positive_low_carry_formulas':positive_carry,'AND4_controls':controls,'Maj3_depths':12,'nearconstant_AND2_controls':12,'physical_exclusions':2,'assertions':ns['assertions'],'runtime_seconds':time.monotonic()-start,'scope':'full scoped A045 reconstruction and new sharp joint singleton envelope; prime Jhi and FEI remain open'}
(O/('PILOT_CHECKS.json' if pilot else 'CHECKS.json')).write_bytes((json.dumps(out,indent=2)+'\n').encode('utf-8'))
(O/('PILOT_SHARPNESS.json' if pilot else 'SHARPNESS.json')).write_bytes((json.dumps({'nearconstant_AND2':near,'Maj3_towers':towers},indent=2)+'\n').encode('utf-8'))
print(json.dumps(out))
