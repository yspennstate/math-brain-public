from pathlib import Path
from fractions import Fraction as Q
import sys, importlib.util, json, time, argparse
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
old=R.parents[1]/'runs/20261022T231605Z-account03-A020-selector-boundary-tests/code/check.py'
spec=importlib.util.spec_from_file_location('arithmetic',old)
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
# Only the saved endpoints are rounded; no large rational is converted to decimal.
a.show=lambda v:[str(a.floorq(v[0])),str(a.ceilq(v[1]))]
N=0
def ck(v):
 global N
 N+=1
 assert v
def overlap(x,y):ck(x[0]<=y[1] and y[0]<=x[1])
def old_debit(p):
 z=p/2;t=(1+z)**2/(2*(1+z*z))
 E=a.scale(a.sub(a.con(1),a.add(a.eta(t),a.eta(1-t))),(1+z*z)/2)
 L=a.add(a.scale(a.log2((9+p*p)/8),Q(1,2)),a.scale(a.log2((9+p*p)/(1+p*p)),p*p/8))
 U=a.add(L,E);ck(U[0]>=0 and U[1]<Q(5,8))
 return U
def root_eligibility(k,r):
 rho=Q(1,1<<k);m=r+1;mu=Q(3,4)**m;beta=(1-mu)/2;p=rho*beta
 H0=a.sub(a.con(4),a.scale(a.log2(3),Q(9,8)))
 LB=a.add(a.add(a.eta(beta*beta),a.scale(a.sub(a.scale(H0,m),a.eta(mu*mu)),Q(1,4))),a.con((1-mu*mu)/2))
 HP=a.add(a.sub(a.eta((1-p)**2),a.eta(p*p)),a.add(a.con(4*k*p),a.scale(LB,2*rho)))
 c=a.add(HP,a.sub(a.con(1),a.scale(a.log2((1+p*p)/(p*p)),p*p)))
 JA=2*k*p+rho*Q(3*m,4)
 rootCE=a.add(a.scale(c,Q(1,2)),a.con(3))
 margin=a.sub(a.con(6+JA),rootCE)
 ck(margin[0]>Q(291,128));ck(c[1]<4*(1-p+JA/2))
 ck(a.sub(a.con(2-2*p+JA),a.scale(c,Q(1,2)))[0]>Q(159,128))
 return {'k':k,'r':r,'root_rate4_margin':a.show(margin),'core_rate4':True,'original_half_bank_positive':True}
def terminal(k,r,clean=False):
 rho=Q(1,1<<k);mu=Q(3,4)**(r+1);p=rho*(1-mu)/2
 d=Q(1) if clean else Q(5,8)**r;mass=rho/8
 # True small terminal core, with every killed block physically fixed to +1.
 core=[]
 for y in range(1<<(k+4)):
  u=y&1;pad=(y>>1)&((1<<k)-1);live=y>>(k+1)
  active=(pad==0 and live==0)
  core.append(1 if active else (-1 if u else 1))
 pc=a.law(core)
 # Slice of ORIGINAL reference at zero Fourier frequency in all dummy bits.
 # Ghost rows are retained in the ambient product reference, not renormalized.
 qc=[]
 for T in range(len(core)):
  u=T&1;pad=(T>>1)&((1<<k)-1);live=T>>(k+1)
  b=(d*(Q(9,16) if live==0 else Q(1,16))+(1-2*mu if live==0 else 0))/4
  pb=rho*rho*b+(1-2*p if u and pad==0 and live==0 else 0)
  qc.append((pb+int(T==0))/2)
 ck(all(q>=0 for q in qc));ck(0<sum(qc)<=1)
 # Ambient normalization independent of the support slice:
 # projected B has beta mass since every projected seed law sums to one.
 beta=(1-mu)/2;ck((1+1-2*mu)/4==beta)
 ck(2*rho*beta+1-2*p==1)
 expected_row_mass=7*rho/32
 rows=[i for i in range(len(core)) if (i>>(k+1))!=0]
 ck(sum(pc[i] for i in rows)==expected_row_mass)
 ck(all(qc[i]==rho*rho*d/128 for i in rows))
 qf=a.fullref(qc)
 profiles=[]
 for sign in [1,-1]:
  h=[sign if (((y>>1)&((1<<k)-1))==0 and (y>>(k+1))==0) else (-1 if y&1 else 1) for y in range(len(core))]
  f=a.full(h);pf=a.law(f);I=a.influence(f)
  expected4=6+(2*k+4-sign)*mass
  ck(4*I==expected4)
  ce=a.ce(pf,qf);U=old_debit(p)
  W=a.sub(a.sub(a.con(4*I),ce),U)
  selected=[j for j in range(len(pf)) if (((j>>1)%len(core))>>(k+1))!=0]
  ck(sum(pf[j] for j in selected)==7*rho/64)
  ck(all(qf[j]==rho*rho*d/2048 for j in selected))
  selectedCE=a.scale(a.log2(2048/(rho*rho*d)),7*rho/64)
  ck(ce[0]>=selectedCE[0])
  if not clean:ck(ce[0]>7*rho*r/128)
  if not clean and r==4096 and k==5:
   ck(ce[0]>7);ck(W[1]<Q(-241,256))
  if clean:
   ck(all(qc[t]>=pc[t]/4 for t in range(len(pc))))
   if k>=5:ck(W[0]>Q(5,4))
  profiles.append({'q_sign':sign,'4I':str(4*I),'CE_interval':a.show(ce),'CE_selected_interval':a.show(selectedCE),'old_U':a.show(U),'signed_reserve_after_U':a.show(W)})
 return {'k':k,'r':r,'m':r+1,'cleaned':clean,'physical_history_reach':'2^(-'+str(r)+') (two q outcomes each half this)','original_p':'(1-(3/4)^'+str(r+1)+')/2^'+str(k+1),'slice_Q_core_mass_interval':a.show(a.con(sum(qc))),'ambient_Q_normalized':True,'row_true_full_mass':str(7*rho/64),'row_Q_full_atom':'2^(-'+str(2*k+11)+')'+('' if clean else '*(5/8)^'+str(r)),'profiles':profiles},qc

def literal(k,r):
 m=r+1;act=[]
 for y in range(1<<(k+3*m)):
  z=y>>k;g=1
  for j in range(m):g*=(-1 if ((z>>(3*j))&7)==0 else 1)
  act.append(int((y&((1<<k)-1))==0 and g==-1))
 h=[(-1 if t&1 else 1) if act[t>>2] else (-1 if (t>>1)&1 else 1) for t in range(4*len(act))]
 f=a.full(h);ph=a.law(h);qh=[(v+int(i==1))/2 for i,v in enumerate(ph)];qf=a.fullref(qh)
 ck(sum(qf)==1)
 # Average ALL actual histories, not just distinguished all-ones history.
 qi=a.marginal(qf,1);ff=[a.restrict(f,1,b) for b in [0,1]]
 for j in reversed(range(r)):
  bit=k+2+3*j
  qi=a.marginal(qi,bit)
  ff=[a.restrict(v,bit,b) for v in ff for b in [0,1]]
 ck(sum(qi)==1)
 projected=a.marginal(a.law(f),1)
 for j in reversed(range(r)):projected=a.marginal(projected,k+2+3*j)
 pp=[a.law(v) for v in ff]
 ck([sum(vals,Q(0))/len(pp) for vals in zip(*pp)]==projected)
 # Independently literal restrictions versus compressed formula on both q signs.
 data,small_qc=terminal(k,r);smallq=a.fullref(small_qc)
 for q in [0,1]:
  v=a.restrict(f,1,q);qr=a.marginal(qf,1)
  for j in reversed(range(r)):
   v=a.restrict(v,k+2+3*j,1);qr=a.marginal(qr,k+2+3*j)
  p=a.law(v)
  for t in range(len(p)):
   dummy=(t>>(k+2))&((1<<(2*r))-1)
   if dummy:ck(p[t]==0)
   else:
    compact=(t&((1<<(k+2))-1))|((t>>(k+2+2*r))<<(k+2))
    ck(qr[t]==smallq[compact])
  ce=a.ce(p,qr);overlap(ce,tuple(Q(x) for x in data['profiles'][q]['CE_interval']))
  ck(4*a.influence(v)==Q(data['profiles'][q]['4I']))
  # Complete zero-influence cleanup of all remaining killed-block bits.
  for bit in reversed(range(k+2,k+2+2*r)):
   z0=a.restrict(v,bit,0);z1=a.restrict(v,bit,1)
   ck(z0==z1);ck(a.influence(v)==a.influence(z0))
   v=z0;qr=a.marginal(qr,bit)
  cleaned,cqc=terminal(k,r,True)
  ck(qr==a.fullref(cqc));ck(sum(qr)==1)
  overlap(a.ce(a.law(v),qr),tuple(Q(x) for x in cleaned['profiles'][q]['CE_interval']))
 # Signed transition identity across every query, every complementary terminal.
 parent=[f];reference=qf;debit=a.con(0);Iremoved=Q(0)
 for bit in [1]+[k+2+3*j for j in reversed(range(r))]:
  nextref=a.marginal(reference,bit);nxt=[];charge=a.con(0);removed=Q(0)
  for v in parent:
   pv=a.law(v)
   local=a.con(0)
   for t,w in enumerate(pv):
    if w:
     erased=(t&((1<<bit)-1))|((t>>(bit+1))<<bit)
     local=a.add(local,a.scale(a.log2(nextref[erased]/reference[t]),w))
   charge=a.add(charge,a.scale(local,Q(1,len(parent))))
   children=[a.restrict(v,bit,b) for b in [0,1]]
   removed+=(a.influence(v)-sum(a.influence(c) for c in children)/2)/len(parent)
   nxt+=children
  ck(charge[0]>=0);debit=a.add(debit,charge);Iremoved+=removed
  parent=nxt;reference=nextref
 orig=a.ce(a.law(f),qf)
 end=a.con(0)
 for v in parent:end=a.add(end,a.scale(a.ce(a.law(v),reference),Q(1,len(parent))))
 overlap(orig,a.add(end,debit))
 ck(a.influence(f)==Iremoved+sum(a.influence(v) for v in parent)/len(parent))
 return {'k':k,'r':r,'original_dimension':len(f).bit_length()-1,'all_histories_checked':len(parent),'complete_reference_mass':'1','signed_transition':'PASS','support_slice_vs_original':'PASS'}

def main(pilot):
 start=time.perf_counter();out={'status':'RUNNING','compressed':[],'cleanup':[],'root':[],'literal':[]}
 name='PILOT.json' if pilot else 'CHECK.json'
 ck(Q(8,5)**2>2);ck(7*4096*Q(1,32)/128==7)
 ck(6+Q(15,256)-7==Q(-241,256))
 ck(31**31>2**152)
 for r in ([1,4] if pilot else [1,4,16,64,256,1024,4096]):
  out['compressed'].append(terminal(5,r)[0]);ck(time.perf_counter()-start<60)
  out['cleanup'].append(terminal(5,r,True)[0]);ck(time.perf_counter()-start<60)
  out['root'].append(root_eligibility(5,r));ck(time.perf_counter()-start<60)
  (R/'out'/name).write_text(json.dumps(out,indent=2),encoding='utf-8')
 for r in ([1] if pilot else [1,2]):
  out['literal'].append(literal(1,r));ck(time.perf_counter()-start<60)
 out.update(status='PASS',assertions=N,runtime_seconds=time.perf_counter()-start)
 (R/'out'/name).write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps({'status':out['status'],'assertions':N,'compressed':len(out['compressed']),'literal':len(out['literal']),'runtime_seconds':out['runtime_seconds']}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
