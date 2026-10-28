from pathlib import Path
from fractions import Fraction as F
import importlib.util,itertools,json,time,sys
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
old=R.parent/'20261014T053514Z-account05-A083-formal-core/code/reference_rows.py'
sp=importlib.util.spec_from_file_location('old_a083',old);P=importlib.util.module_from_spec(sp);sp.loader.exec_module(P)
E=P.E;START=time.perf_counter();CHECKS=0
def ck(x):
 global CHECKS
 CHECKS+=1
 if not x:raise AssertionError(CHECKS)
 if time.perf_counter()-START>60:raise TimeoutError('frozen60s')
def save(name,v):(R/'out'/name).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8')
def ent(p):return E.entropy_vector(p)
def inf(t):return F(sum(t[x]!=t[x^(1<<i)] for i in range(len(t).bit_length()-1) for x in range(len(t))),len(t))
def gate(h):
 n=len(h).bit_length()-1
 return tuple(h[(s>>1)&((1<<n)-1)] if not s&1 else 2*(s>>(n+2)&1)-1 if s>>(n+1)&1 else 1 for s in range(1<<(n+3)))
def lift(ph,qh):
 n=len(ph).bit_length()-1;q=[F(0)]*(1<<(n+3))
 for s in range(len(q)):
  A=(s>>1)&((1<<n)-1)
  if A:
   if not (s>>(n+1)):q[s]=qh[A]/4
  else:q[s]=F(1,16)
 ck(sum(q)==1)
 return q
def direct(t):
 N=len(t)
 return tuple(F(sum(v*(-1)**((s&x).bit_count()) for x,v in enumerate(t)),N)**2 for s in range(N))
def ivadd(a,b):return a[0]+b[0],a[1]+b[1]
def entropy_atom(a):return E.scale(E.log2_interval(1/a),a) if a else (F(0),F(0))
def occupancy_ref(t,c):
 p=P.spectral(t);n=len(t).bit_length()-1;v=1-p[0]
 marg=[sum(a for s,a in enumerate(p) if s>>j&1) for j in range(n)]
 w=[]
 for s in range(len(p)):
  a=F(1)
  for j,z in enumerate(marg):a*=c*z/v if s>>j&1 else 1-c*z/v
  w.append(a)
 return [p[0]]+[v*a/(1-w[0]) for a in w[1:]]
def history(h):
 t=gate(h);n=len(h).bit_length()-1;qb=occupancy_ref(t,F(3,4))
 row,data=P.query(t,n+1,1<<(n+1),qb,'fair')
 pcs=data[3];joint=data[5];out=[sum(z) for z in joint]
 refs=[[a/out[b] for a in joint[b]] for b in (0,1)]
 tb=P.child(t,n+1,1)
 row2,d2=P.query(tb,n+1,(1<<(n+1))-1,refs[1],'fair')
 ck(d2[3][0]==d2[3][1]);ck(all(k==F(1,2) for rowk in d2[4] for k in rowk));ck(not row2['outcome_KL'])
 C=E.mul(P.vec_log(F(5,4)),F(1,2))
 ck(row['conditional_child_KL']==P.serial(C))
 DL=E.mul(E.add(*(P.kl(d2[3][b],[a/sum(d2[5][b]) for a in d2[5][b]]) for b in (0,1))),F(1,2))
 ck(E.add(P.kl(pcs[1],refs[1]),E.mul(DL,-1))==C)
 ghost=sum(a for s,a in enumerate(d2[2]) if not d2[1][s])
 bad,bd=P.query(tb,n+1,(1<<(n+1))-1,refs[1],'0')
 if ghost:ck(bool(bad['outcome_KL']))
 else:ck(not bad['outcome_KL'])
 return {'core':list(h),'reference_only_erased_mass':str(ghost),'fair_second_outcome_KL':row2['outcome_KL'],'adversarial_second_outcome_KL':bad['outcome_KL'],'old_conditional_booking':P.serial(C)}
def main():
 count=0;fixtures=[]
 for n in [1,2,3]:
  N=1<<n
  for neg in itertools.combinations(range(N),N//2):
   h=tuple(-1 if s in neg else 1 for s in range(N));ph=P.spectral(h);ck(ph[0]==0)
   t=gate(h);p=P.spectral(t);ck(p==direct(t))
   Hh=ent(ph);H=ent(p);Ih=inf(h)
   ck(H==E.add({2:F(3)},E.mul(Hh,F(1,2))))
   ck(inf(t)==1+Ih/2)
   b=[P.child(t,n+1,j) for j in (0,1)];tb=b[1];ls=[b[0],P.child(tb,n+1,0),P.child(tb,n+1,1)]
   ck(all(ent(P.spectral(l))==E.add({2:F(2)},E.mul(Hh,F(1,2))) for l in ls))
   ck(inf(b[0])==F(1,2)+Ih/2 and inf(b[1])==1+Ih/2)
   ck(all(inf(l)==F(1,2)+Ih/2 for l in ls))
   ck(P.spectral(ls[1])==P.spectral(ls[2]))
   # Genuine nonmatching supplied joint reference; balance calibrates its empty atom to zero.
   qh=[F(0)]+[(ph[s]+F(1,N-1))/2 for s in range(1,N)]
   Q=lift(ph,qh);Dh=P.kl(ph,qh);D=P.kl(p,Q)
   ck(D==E.mul(Dh,F(1,2)))
   ck(E.add(H,D)==E.add({2:F(3)},E.mul(E.add(Hh,Dh),F(1,2))))
   count+=1
  save('CENSUS_CHECKPOINT.json',{'status':'PARTIAL','completed_dimension':n,'cases':count,'assertions':CHECKS})
 ck(count==78)
 for h in [(1,-1),(1,-1,-1,1),(1,1,1,-1,1,-1,-1,-1),(1,-1,-1,1,-1,1,1,-1)]:fixtures.append(history(h))
 ck(any(F(d['reference_only_erased_mass'])>0 for d in fixtures))
 # All-r signs: base normalizer bracket; log2(16/15)<1/8, log2(5/4)<1/3, and old C<1/4.
 ck(F(1,4)-(1-F(2,5))**2*(1-F(1,5))**2==F(49,2500))
 ck(16**8<2*15**8);ck(5**3<2*4**3);ck(15**2<2*11**2);ck(8**4<2*7**4)
 family=[]
 for r in [16,32,64]:
  m=(1<<r)//r;d=F(1,1<<r);ck(m*r*d==1);Ih=1+m*2*r*d;ck(Ih==3)
  hp=ivadd(entropy_atom((1-2*d)**2),(8*(r-1)*d*(1-d),)*2)
  Hh=E.scale(hp,m);ck(Hh[1]<8)
  ck(2*Ih-Hh[1]/2>2)
  bound=9-r+F(3,16);ck(bound<0)
  ck(bound+1<0) # Retaining the actual signed whole-history refund1 does not repair this reference.
  # Nonmatching explicit alternative supplier, a comparison of INITIAL laws, not a free reset.
  KLupper=4*d*(1-d)*E.log2_interval(F(8,7))[1]
  CEupper=hp[1]+KLupper;ck(CEupper<8*r*d-d)
  margin=F(1,2)*(12-m*CEupper);ck(margin>2+F(1,2*r))
  family.append({'r':r,'m':m,'root_dimension':(1<<r)+4,'core_I':3,'root_I':'5/2','core_H_interval':E.outward(Hh),'canonical_entropy_strict_lower':str(F(r)-F(3,16)),'original_canonical_owner_remainder_strict_upper':str(bound),'signed_canonical_owner_remainder_strict_upper':str(bound+1),'alternative_initial_lift_remainder_strict_lower':str(2+F(1,2*r))})
 save('RESULT.json',{'status':'PASS','balanced_core_cases':count,'history_fixtures':fixtures,'factored_cases':family,'assertions':CHECKS,'helper_assertions':P.CHECKS,'seconds':time.perf_counter()-START,'formal_scope':'Separate Lean admission result; no compilation inferred','full_FEI':'OPEN'})
 print(json.dumps({'status':'PASS','balanced_core_cases':count,'history_fixtures':len(fixtures),'factored_cases':len(family),'assertions':CHECKS,'helper_assertions':P.CHECKS,'seconds':time.perf_counter()-START}))
if __name__=='__main__':main()
