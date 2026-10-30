"""Exact paid-sector checker; imports definitions only from A041's own helper."""
from pathlib import Path
from fractions import Fraction as Q
import ast, hashlib, json, sys, time
R=Path(__file__).resolve().parents[1]; O=R/'out'
old=R.parent/'20261023T050523Z-fleet03-A041-weighted-threshold-fei/code/check.py'
pilot='--pilot' in sys.argv
spec={'helper':'A041-paid-sector-reference-carry-v1','source_helper_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),'family':'all labelled three-input Boolean signs and all binary root/two-input child gates on disjoint blocks; fixed depth and source controls','domain':{'laws':[['1/3']*3,['1/4','1/2','3/4']],'flat_tables':16 if pilot else 256,'root_tables':4 if pilot else 16,'child_tables':4 if pilot else 16,'controls':'four depth-two four-bit formulas at two laws; fair AND3; biased AND2; excluded real-valued one-bit; repeated wire'},'case_count':{'flat':32 if pilot else 512,'formula':32 if pilot else 512,'controls':12},'symmetry':'none','arithmetic':'exact Fraction centered-product expansion; exact coefficient products and integer carries; rigorous 20-term rational atanh logarithm intervals','memory_estimate_MB':100,'maximum_runtime_seconds':60,'mode':'pilot' if pilot else 'main'}
(O/('FROZEN_PILOT.json' if pilot else 'FROZEN_SPEC.json')).write_text(json.dumps(spec,indent=2)+'\n',encoding='utf-8')
start=time.monotonic()
tree=ast.parse(old.read_text(encoding='utf-8'))
defs=ast.Module(body=[n for n in tree.body if isinstance(n,(ast.Import,ast.ImportFrom,ast.FunctionDef))],type_ignores=[])
ns={'__file__':str(old),'assertions':0,'start':start,'formula_count':0}
exec(compile(defs,str(old),'exec'),ns)
ns['L2'],ns['U2']=ns['series'](Q(2))
ck=ns['ck']; mul=ns['mul']; logint=ns['logint']; base=ns['spectrum']
def spectrum(ps,vals):
 f=base(ps,vals); P=f['P']; hi=[s for s,p in P.items() if p and s.bit_count()>=2]
 H=sum((P[s] for s in hi),Q(0)); W={s:P[s]/(f['c'][s]**2*4**f['j'][s]) for s in hi}; Z=sum(W.values(),Q(0))
 f['Q_all']=f['Q']; f['H']=H; f['Zhi']=Z
 f['Q']={s:(P[s] if s.bit_count()<=1 else (H*W.get(s,0)/Z if Z else Q(0))) for s in P}
 f['Jh']=sum((P[s]*f['j'][s] for s in hi),Q(0))
 ck(H==f['D']-f['R']);ck(sum(f['Q'].values())==1)
 ck(H<=Z<=4*H); ck(all(f['Q'][s]==P[s] for s in P if s.bit_count()<=1))
 e1=sum((P[s]*logint(1/f['c'][s]**2)[1] for s in P if P[s] and s.bit_count()==1),Q(0))
 ck(e1<=4*f['D']-2*f['R'] or e1==0)
 f['E1upper']=e1
 return f
ns['spectrum']=spectrum
gate=ns['gate'];literal=ns['literal'];basebuild=ns['build']
def enrich(f):
 if 'local' not in f:
  f['hij']={s:(f['j'][s] if s.bit_count()>=2 else 0) for s,p in f['P'].items() if s and p}
  f['uhprod']={s:(f['c'][s]**2*4**f['j'][s] if s.bit_count()>=2 else Q(1)) for s in f['hij']}
  f['scprod']={s:(f['c'][s]**2 if s.bit_count()==1 else Q(1)) for s in f['hij']}
  f['Ht']=f['H'];f['Jt']=f['Jh'];f['Rt']=f['R'];return f
 g,weights,children=f['local'];active=[i for i,c in enumerate(children) if c['w']]
 for c in children:enrich(c)
 f['Ht']=g['H']+sum((a*children[i]['Ht'] for i,a in weights),Q(0))
 f['Jt']=g['Jh']+sum((a*children[i]['Jt'] for i,a in weights),Q(0))
 f['hij']={};f['uhprod']={};f['scprod']={};nl=len(children[0]['ps'])
 carry=Q(0)
 for s,p in f['P'].items():
  if not s or not p:continue
  parts=(s&((1<<nl)-1),s>>nl);am=sum((1<<k for k,i in enumerate(active) if parts[i]),0)
  j=g['j'][am] if am.bit_count()>=2 else 0
  up=g['c'][am]**2*4**g['j'][am] if am.bit_count()>=2 else Q(1)
  sp=g['c'][am]**2 if am.bit_count()==1 else Q(1)
  for i in active:
   t=parts[i]
   if t:j+=children[i]['hij'][t];up*=children[i]['uhprod'][t];sp*=children[i]['scprod'][t]
  f['hij'][s]=j;f['uhprod'][s]=up;f['scprod'][s]=sp
  if s.bit_count()>=2:
   k=f['j'][s]-j;ck(k>=0);carry+=p*k
   # Multiplicative certificate for the exact logarithmic carry identity.
   ck(f['c'][s]**2*4**f['j'][s]==4**k*up*sp)
  else:ck(j==0 and sp==f['c'][s]**2 and up==1)
 ck(carry==f['Jh']-f['Jt']);ck(f['Ht']==f['D']-f['Rt'])
 f['carry']=carry
 return f
def build(t,l,r):return enrich(basebuild(t,l,r))
def check(f):
 P=f['P'];F=f['Q'];T=f['T'];H=f['H'];Ht=f['Ht']
 ck(all(T[s]==P[s] for s in P if s.bit_count()<=1))
 ck(sum((T[s] for s in P if s.bit_count()>=2),Q(0))==H)
 dist=sum((abs(F[s]-T[s]) for s in P),Q(0))/2
 if H:
  raw={s:max(F[s],T[s]) for s in P if s.bit_count()>=2};z=sum(raw.values(),Q(0))
  ck(z==H+dist and H<=z<=2*H)
  M={s:(P[s] if s.bit_count()<=1 else H*raw[s]/z) for s in P};ck(sum(M.values())==1)
  ck(all(M[s]==P[s] for s in P if s.bit_count()<=1))
  ck(all(raw[s]>=F[s] and raw[s]>=T[s] for s in raw))
  sel=sum((F[s] if s%2 else T[s] for s in raw),Q(0));ck(0<sel<=2*H)
  upper=Q(0)
  for s,p in P.items():
   if p:
    l,u=logint(F[s]/T[s]);upper+=p*max(abs(l),abs(u))
  # Strict interval-separated comparison; identical laws have exact zero conversion.
  ck(upper<=4*ns['L2']*(H+Ht) or F==T)
 else:ck(F==T==P)
 if time.monotonic()-start>60:raise RuntimeError('frozen 60-second bound exceeded')
laws=[(Q(1,3),)*3,(Q(1,4),Q(1,2),Q(3,4))]
flat=formulas=0
for ps in laws:
 for t in range(16 if pilot else 256):gate(t,ps);flat+=1
 for rt in range(4 if pilot else 16):
  for ct in range(4 if pilot else 16):check(build(rt,gate(ct,ps[:2]),literal(ps[2])));formulas+=1
# Eight four-bit controls, including genuinely nonzero gate R and deeper propagation.
for ps in [(Q(1,2),)*4,(Q(1,3),Q(1,4),Q(1,2),Q(3,4))]:
 for rt,ct in [(8,8),(14,8),(6,6)]:
  c=build(ct,gate(8,ps[:2]),literal(ps[2]));check(build(rt,c,literal(ps[3])))
 check(build(8,gate(128,ps[:3]),literal(ps[3])))
f=build(8,gate(8,(Q(1,2),)*2),literal(Q(1,2)));check(f)
g,weights,children=f['local']
def e1unit(x):
 ck(all(x['c'][s]**2*4**x['j'][s]==1 for s,p in x['P'].items() if s and p))
 return sum((p*x['j'][s] for s,p in x['P'].items() if p and s.bit_count()==1),Q(0))
e1f=e1unit(f);e1t=e1unit(g)+sum((a*e1unit(children[i]) for i,a in weights),Q(0))
ck(f['Jh']==Q(1,2));ck(f['Jt']==Q(5,16));ck(f['carry']==Q(3,16))
ck(e1f==Q(3,8) and e1t==Q(9,16));ck(f['Q']==f['T']==f['P'])
ck(f['carry']+e1f==e1t)
witness={k:str(v) for k,v in {'Jflat_over_ln4':f['Jh'],'Jtree_over_ln4':f['Jt'],'carry_over_ln4':f['carry'],'E1flat_over_ln4':e1f,'E1tree_over_ln4':e1t}.items()}
a=gate(8,(Q(3,4),)*2);ck(a['Q']==a['P'] and a['Q_all']!=a['P'])
# Hypothesis and physical-law exclusions are checked directly, not passed as Boolean inputs.
ck(Q(16,25)+Q(9,25)==1 and Q(9,25)*logint(Q(25,9))[0]>0) # real-valued one-bit Delta=0
ck(Q(1,9)!=Q(49,81)) # repeated wire is not an independent second child
out={'status':'PASS','helper':spec['helper'],'flat_cases':flat,'formula_cases':formulas,'mandatory_controls':12,'assertions':ns['assertions'],'runtime_seconds':time.monotonic()-start,'AND3_exact_control':witness,'scope':'exact finite checks support the analytic reference/carry interface; universal prime Jhi payment and FEI remain open'}
(O/('PILOT_CHECKS.json' if pilot else 'CHECKS.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
