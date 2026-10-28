"""Exact fixed-orientation matching-pair stopping trees; frozen specification."""
import sys,time,json,itertools,importlib.util
from fractions import Fraction as Q
from pathlib import Path
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
hp=ROOT/'runs/20261014T022245Z-account05-A023-amortized-rarity-budget/code/check_block.py'
sp=importlib.util.spec_from_file_location('exact_arithmetic',hp);h=importlib.util.module_from_spec(sp);sp.loader.exec_module(h)
START=time.perf_counter();CHECKS=0;CACHE={};ROWS=[]
def ck(ok):
 global CHECKS
 assert ok
 CHECKS+=1
 if time.perf_counter()-START>60:raise RuntimeError('Frozen60second cap')
def save(n,x):(RUN/'out'/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def vector(v):return {str(p):str(c) for p,c in sorted(v.items())}
def fw(t):
 a=list(t);k=1
 while k<len(a):
  for j in range(0,len(a),2*k):
   for i in range(j,j+k):a[i],a[i+k]=a[i]+a[i+k],a[i]-a[i+k]
  k*=2
 return a
def law(t):
 w=fw(t);N=len(t);ck(sum(a*a for a in w)==N*N)
 return {s:Q(a*a,N*N) for s,a in enumerate(w) if a}
def ent(p):
 out={}
 for a in p.values():h.lg(out,a,-a)
 return out
def ce(p,q):
 out={}
 for s,a in p.items():ck(q[s]>0);h.lg(out,q[s],-a)
 return out
def inf(t,i):return Q(sum(a!=t[x^(1<<i)] for x,a in enumerate(t)),len(t))
def scatter(x,active,fix):
 y=sum(v<<i for i,v in fix.items())
 for j,i in enumerate(active):y|=((x>>j)&1)<<i
 return y
def seed(x,m,mask):return -1 if (sum(((x>>i)&1)*((x>>(i+1))&1) for i in range(0,m,2))+(x&mask).bit_count())%2 else 1
def state(m,w,mask,fix,z=None):
 key=(m,w,mask,tuple(sorted(fix.items())),z)
 if key in CACHE:return CACHE[key]
 data=[i for i in range(m) if i not in fix];ctrl=[i for i in [m+1,m+2] if i not in fix];active=data+([m] if z is None else [])+ctrl
 cf={i:v for i,v in fix.items() if i<m};k=len(data);r=2*sum(i not in cf and i+1 not in cf for i in range(0,m,2));ell=sum(i in cf and i+1 not in cf and cf[i]!=((mask>>(i+1))&1) for i in range(0,m,2))
 base=tuple(seed(scatter(x,data,cf),m,mask) for x in range(1<<k));pb=law(base);ck(len(pb)==1<<r and set(pb.values())=={Q(1,1<<r)})
 IS=sum((inf(base,j) for j in range(k)),Q(0));ck(IS==Q(r,2)+ell);Z=4*IS-r
 cores=[tuple(b*(-1 if j and scatter(x,data,cf)==(0 if j==1 else w) else 1) for x,b in enumerate(base)) for j in range(3)]
 pi=[Q(0)]*3
 for x in range(1<<len(ctrl)):
  y=scatter(x,ctrl,{i:v for i,v in fix.items() if i>m});A=(y>>(m+1))&1;B=(y>>(m+2))&1;pi[0 if not A else 1+B]+=Q(1,1<<len(ctrl))
 survive=[all(((v>>i)&1)==a for i,a in cf.items()) for v in [0,w]];M=Q(1,1<<k)*sum((pi[j+1]*int(survive[j]) for j in range(2)),Q(0))
 table=[]
 for x in range(1<<len(active)):
  y=scatter(x,active,fix);core=y% (1<<m);A=(y>>(m+1))&1;B=(y>>(m+2))&1;zz=((y>>m)&1) if z is None else z
  table.append(seed(core,m,mask)*(-1 if zz else 1)*(-1 if A and core==(w if B else 0) else 1))
 p=law(table);H=ent(p);pd={s:Q(0) for s in range(1<<k)};py={s:Q(0) for s in range(1<<len(ctrl))}
 q={s:(pb.get(s,Q(0))+Q(1,1<<k))/2 for s in pd};nu={s:Q(0) for s in py};delta=Q(1,1<<m)
 for s,a in enumerate([1-3*delta/2]+[delta/2]*3):nu[sum(((s>>(i-m-1))&1)<<j for j,i in enumerate(ctrl))]+=a
 ref={}
 for s,a in p.items():
  if z is None:ck((s>>k)&1==1)
  ds=s% (1<<k);cs=s>>(k+int(z is None));pd[ds]+=a;py[cs]+=a;ref[s]=q[ds]*nu[cs]
 C=ce(p,ref);CX=ce(pd,q);CY=ce(py,nu);ck(C==h.add((1,CX),(1,CY)));K=h.add((1,C),(-1,H));ck(h.sign(K)>=0)
 eps=sum((a for s,a in pd.items() if s not in pb),Q(0));ck(eps==4*M*(1-Q(1,1<<(k-r))))
 mix={s:Q(0) for s in pd};R=Q(0)
 for j in range(3):
  for s,a in law(cores[j]).items():mix[s]+=pi[j]*a
  for l in range(j):
   prod=tuple(a*b for a,b in zip(cores[j],cores[l]));R+=2*pi[j]*pi[l]*sum((inf(prod,i) for i in range(k)),Q(0))
 ck(pd==mix);ck(h.sign(h.add((1,CX),(-1,h.rational(r+1+4*(k-r)*M))))<=0)
 ii={i:inf(table,j) for j,i in enumerate(active)};ID=sum((ii[i] for i in active if i<=m),Q(0));IC=sum((ii[i] for i in ctrl),Q(0));ck(ID>=IS-2*k*M)
 B=h.add((1,h.rational(4*ID-Q(m,8)-R)),(-1,C))
 lower=h.add((1,h.rational(Z-1-Q(m,8)-R-(8*k+4*(k-r))*M)),(-1,CY));ck(h.sign(h.add((1,B),(-1,lower)))>=0)
 out=dict(m=m,w=w,mask=mask,fix=fix,z=z,k=k,r=r,ell=ell,IS=IS,Z=Z,M=M,pi=pi,H=H,C=C,CX=CX,CY=CY,K=K,R=R,ID=ID,IC=IC,B=B,ii=ii)
 CACHE[key]=out;row={n:out[n] for n in ['m','w','mask','z','k','r','ell']};row['fix']={str(i):a for i,a in fix.items()}
 for n in ['IS','Z','M','R','ID','IC']:row[n]=str(out[n])
 for n in ['H','C','CX','CY','K','B']:row[n]=vector(out[n])
 ROWS.append(row);return out
def allowed(s):
 m=s['m'];fix=s['fix'];out=[i for i in [m+1,m+2] if i not in fix]
 if s['z'] is None:out+=[m]
 for a in range(0,m,2):
  if a not in fix:out.append(a)
  elif a+1 not in fix and fix[a]==((s['mask']>>(a+1))&1):out.append(a+1)
 return out
def children(s,i):
 a,b=[state(s['m'],s['w'],s['mask'],s['fix'],z) if i==s['m'] else state(s['m'],s['w'],s['mask'],s['fix']|{i:z},s['z']) for z in [0,1]]
 ck(s['Z']==(a['Z']+b['Z'])/2);ck(s['M']==(a['M']+b['M'])/2);ck(s['R']>=(a['R']+b['R'])/2)
 cy=h.add((1,s['CY']),(-Q(1,2),a['CY']),(-Q(1,2),b['CY']));ck(h.sign(cy)>=0 if i>s['m'] else not cy)
 pivot=s['ii'][i] if i<=s['m'] else Q(0);ck(s['ID']-(a['ID']+b['ID'])/2==pivot)
 dc=h.add((1,s['C']),(-Q(1,2),a['C']),(-Q(1,2),b['C']));dr=s['R']-(a['R']+b['R'])/2
 ck(h.add((1,s['B']),(-Q(1,2),a['B']),(-Q(1,2),b['B']))==h.add((1,h.rational(4*pivot)),(-1,dc),(-1,h.rational(dr))))
 for c in [a,b]:ck(c['K']==h.add((1,c['C']),(-1,c['H'])))
 return a,b
def main():
 pilot='--pilot' in sys.argv;families=[(4,1,0)] if pilot else [(4,w,a) for w in [1,3] for a in [0,15]]+[(6,1,0)]
 roots=[];DP={};edges=0
 def worst(s):
  nonlocal edges
  key=(s['m'],s['w'],s['mask'],tuple(sorted(s['fix'].items())),s['z'])
  if key in DP:return DP[key]
  best=s['B']
  for i in allowed(s):
   a,b=children(s,i);edges+=1;v=h.add((Q(1,2),worst(a)),(Q(1,2),worst(b)))
   if h.sign(h.add((1,v),(-1,best)))<0:best=v
  DP[key]=best;return best
 for m,w,mask in families:
  options=[]
  for a in range(0,m,2):
   beta=(mask>>(a+1))&1;options.append([{}, {a:0},{a:1},{a:beta,a+1:0},{a:beta,a+1:1}])
  for pieces in itertools.product(*options):
   cf={i:v for piece in pieces for i,v in piece.items()}
   for ctrl in itertools.product([None,0,1],repeat=2):
    fix=cf|{m+1+j:a for j,a in enumerate(ctrl) if a is not None}
    for z in [None,0,1]:state(m,w,mask,fix,z)
  root=state(m,w,mask,{});ck(root['Z']==m and root['M']==Q(1,1<<(m+1)))
  optimum=worst(root);bound=Q(7*m,8)-1-(9*m+Q(15,4))*Q(1,1<<m);ck(h.sign(h.add((1,optimum),(-1,h.rational(bound))))>0)
  if m>=6:ck(h.sign(h.add((1,optimum),(-1,h.rational(Q(m,2)))))>0)
  terminal_options=[]
  for a in range(0,m,2):
   beta=(mask>>(a+1))&1;terminal_options.append([{a:1-beta},{a:beta,a+1:0},{a:beta,a+1:1}])
  EB={};D=Q(0);negative_mass=Q(0);EM=Q(0)
  for pieces in itertools.product(*terminal_options):
   cf={i:v for piece in pieces for i,v in piece.items()};s=state(m,w,mask,cf,0);reach=Q(1,1<<len(cf));D+=reach*len(cf);EM+=reach*s['M'];EB=h.add((1,EB),(reach,s['B']))
   if s['IS']==0:ck(h.sign(s['B'])<0);negative_mass+=reach
  ck(D==Q(3*m,4));ck(negative_mass==Q(1,1<<(m//2)));ck(EM==root['M']);ck(h.sign(h.add((1,EB),(-1,h.rational(bound))))>0)
  roots.append({'m':m,'w':w,'mask':mask,'worst_all_policy_B':vector(optimum),'complete_pair_B':vector(EB),'complete_expected_depth':str(D),'negative_branch_mass':str(negative_mass),'analytic_bound':str(bound)})
  save('pilot_checkpoint.json' if pilot else 'checkpoint.json',{'families':len(roots),'states':len(ROWS),'checks':CHECKS})
 ck(len(ROWS)==(675 if pilot else 6075))
 suffix='pilot_' if pilot else ''
 save(suffix+'rows.json',ROWS);save(suffix+'roots.json',roots);save(suffix+'sign_certificates.json',list(h.SIGNS.values()))
 result={'status':'PASS','pilot':pilot,'families':len(roots),'states':len(ROWS),'checks':CHECKS,'query_states':edges,'sign_certificates':len(h.SIGNS),'elapsed_seconds':time.perf_counter()-START,'scope':'Exact declared fixed-orientation states/policies; all-dimensional matching-quadratic theorem is analytic author proof, independent-person review pending.'}
 save(suffix+'validation.json',result);print(json.dumps(result))
if __name__=='__main__':main()
