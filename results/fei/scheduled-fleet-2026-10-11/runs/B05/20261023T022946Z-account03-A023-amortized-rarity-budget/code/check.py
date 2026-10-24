"""Frozen exact mixed-history reference validation; see out/FROZEN_SPEC.json."""
import sys,time,json,itertools,importlib.util
from pathlib import Path
from fractions import Fraction as Q
sys.dont_write_bytecode=True
RUN=Path(__file__).resolve().parents[1]
old=RUN.parents[1]/'runs/20261014T022245Z-account05-A023-amortized-rarity-budget/code/check_block.py'
spec=importlib.util.spec_from_file_location('arithmetic',old); h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
START=time.perf_counter();CHECKS=0;CACHE={};ROWS=[]
def ck(ok):
 global CHECKS
 assert ok
 CHECKS+=1
 if time.perf_counter()-START>60:raise RuntimeError('Frozen 60-second cap')
def vec(v):return {str(k):str(x) for k,x in sorted(v.items())}
def save(name,x):(RUN/'out'/name).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def fw(t):
 a=list(t);s=1
 while s<len(a):
  for j in range(0,len(a),2*s):
   for k in range(j,j+s):a[k],a[k+s]=a[k]+a[k+s],a[k]-a[k+s]
  s*=2
 return a
def law(t):
 w=fw(t);N=len(t);ck(sum(a*a for a in w)==N*N)
 return {k:Q(a*a,N*N) for k,a in enumerate(w) if a}
def ent(p):
 v={}
 for x in p.values():h.lg(v,x,-x)
 return v
def ce(p,q):
 v={}
 for s,x in p.items():ck(q[s]>0);h.lg(v,q[s],-x)
 return v
def influence(t,i):return Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
def expand(x,active,fixed):
 y=sum(v<<i for i,v in fixed.items())
 for j,i in enumerate(active):y|=((x>>j)&1)<<i
 return y
def bent(x,m):return -1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2))%2 else 1
def state(m,w,fixed):
 key=(m,w,tuple(sorted(fixed.items())))
 if key in CACHE:return CACHE[key]
 da=[i for i in range(m) if i not in fixed];ca=[i for i in [m+1,m+2] if i not in fixed];act=da+[m]+ca
 def value(x):
  y=expand(x,act,fixed);core=y% (1<<m);A=(y>>(m+1))&1;B=(y>>(m+2))&1
  return bent(core,m)*(-1 if (y>>m)&1 else 1)*(-1 if A and core==(w if B else 0) else 1)
 t=tuple(value(x) for x in range(1<<len(act)));p=law(t);H=ent(p)
 base=tuple(bent(expand(x,da,{i:v for i,v in fixed.items() if i<m}),m) for x in range(1<<len(da)))
 pb=law(base);qd={s:(pb.get(s,Q(0))+Q(1,1<<len(da)))/2 for s in range(1<<len(da))}
 delta=Q(1,1<<m);nu0=[1-3*delta/2]+[delta/2]*3;nu={s:Q(0) for s in range(1<<len(ca))}
 for s,a in enumerate(nu0):
  z=sum(((s>>(i-m-1))&1)<<j for j,i in enumerate(ca));nu[z]+=a
 ctrl={s:Q(0) for s in nu};data={s:Q(0) for s in qd};ref={}
 for s,x in p.items():
  ck((s>>len(da))&1==1);ds=s% (1<<len(da));cs=s>>(len(da)+1);ctrl[cs]+=x;data[ds]+=x;ref[s]=qd[ds]*nu[cs]
 C=ce(p,ref);CY=ce(ctrl,nu);K=h.add((1,C),(-1,H));ck(h.sign(K)>=0)
 ii={i:influence(t,j) for j,i in enumerate(act)};ID=sum((ii[i] for i in da+[m]),Q(0));IC=sum((ii[i] for i in ca),Q(0))
 pi=[Q(0)]*3
 for x in range(1<<len(ca)):
  y=expand(x,ca,{i:v for i,v in fixed.items() if i>m});A=(y>>(m+1))&1;B=(y>>(m+2))&1;pi[0 if not A else 1+B]+=Q(1,1<<len(ca))
 cores=[tuple(b*(-1 if j and expand(x,da,{i:v for i,v in fixed.items() if i<m})==(0 if j==1 else w) else 1) for x,b in enumerate(base)) for j in range(3)]
 R=Q(0);T={};mix={s:Q(0) for s in qd}
 for j in range(3):
  pj=law(cores[j]);T=h.add((1,T),(pi[j],ent(pj)))
  for s,a in pj.items():mix[s]+=pi[j]*a
  for k in range(j):
   prod=tuple(a*b for a,b in zip(cores[j],cores[k]));R+=2*pi[j]*pi[k]*sum((influence(prod,i) for i in range(len(da))),Q(0))
 ck(mix==data);J=h.add((1,ent(mix)),(-1,T));L=h.add((1,H),(-1,ent(mix)));ck(h.add((1,C),(-1,T),(-1,J),(-1,L),(-1,K))=={})
 U=Q(m,8);B=h.add((1,h.rational(4*ID-U-R)),(-1,C));ck(h.sign(h.add((1,C),(-1,h.rational(len(da)+1)),(-1,CY)))<=0)
 s=dict(m=m,w=w,fixed=fixed,d=m-len(da),p=p,H=H,C=C,CY=CY,K=K,ID=ID,IC=IC,R=R,B=B,ii=ii,pi=pi,qd=qd,nu=nu)
 CACHE[key]=s
 row={'m':m,'w':w,'fixed':{str(i):a for i,a in fixed.items()},'d':s['d'],'ID':str(ID),'IC':str(IC),'R':str(R),'pi':list(map(str,pi))}
 for n in ['H','C','CY','K','B']:row[n]=vec(s[n])
 ROWS.append(row);return s
def transition(s,i):
 children=[state(s['m'],s['w'],dict(s['fixed'],**{} )|{i:a}) for a in [0,1]]
 a,b=children;data=i<s['m'];ck(s['ID']-(a['ID']+b['ID'])/2==(s['ii'][i] if data else 0));r=s['R']-(a['R']+b['R'])/2;ck(r>=0)
 cy=h.add((1,s['CY']),(-Q(1,2),a['CY']),(-Q(1,2),b['CY']));ck(h.sign(cy)==0 if data else h.sign(cy)>=0)
 c=h.add((1,s['C']),(-Q(1,2),a['C']),(-Q(1,2),b['C']))
 diff=h.add((1,s['B']),(-Q(1,2),a['B']),(-Q(1,2),b['B']))
 ck(diff==h.add((1,h.rational(4*s['ii'][i] if data else 0)),(-1,c),(-1,h.rational(r))))
 # Full KL, full physical influence, full entropy and same remaining R.
 def total(x):return h.add((1,x['B']),(1,x['K']),(1,h.rational(4*x['IC']+x['R'])))
 dh=h.add((1,s['H']),(-Q(1,2),a['H']),(-Q(1,2),b['H']))
 ck(h.add((1,total(s)),(-Q(1,2),total(a)),(-Q(1,2),total(b)))==h.add((1,h.rational(4*s['ii'][i])),(-1,dh)))
 return children
def main():
 roots=[];DP={}
 def worst(s):
  key=(s['m'],s['w'],tuple(sorted(s['fixed'].items())))
  if key in DP:return DP[key]
  best=s['B']
  allowed=[i for i in [s['m']+1,s['m']+2] if i not in s['fixed']]
  if s['d']==0:allowed+=list(range(s['m']))
  for i in allowed:
   a,b=transition(s,i);v=h.add((Q(1,2),worst(a)),(Q(1,2),worst(b)))
   if h.sign(h.add((1,v),(-1,best)))<0:best=v
  DP[key]=best;return best
 for m,ws in [(4,range(1,16)),(6,[1,3])]:
  for w in ws:
   root=state(m,w,{});worstB=worst(root);ck(h.sign(h.add((1,worstB),(-1,h.rational(1+Q(m,32)))))>=0)
   delta=Q(1,1<<m);ck(root['R']==(Q(3*m,2)-Q(int(w.bit_count()==1),2))*delta)
   ck(root['IC']==2*delta);ck(root['ID']>=1+Q(m,2)-m*delta)
   roots.append({'m':m,'w':w,'worst_frontier_B':vec(worstB)})
   save('checkpoint.json',{'completed_roots':len(roots),'checks':CHECKS,'states':len(ROWS)})
 ck(len(ROWS)==1449)
 m=8;w=1;root=state(m,w,{});front=[];expected={};depth=Q(0)
 for j in range(m):
  parent=state(m,w,{i:0 for i in range(j)});a,b=transition(parent,j);reach=Q(1,1<<(j+1));front.append((reach,b));depth+=reach*(j+1)
 last=state(m,w,{i:0 for i in range(m)});front.append((Q(1,1<<m),last));depth+=Q(m,1<<m)
 for reach,s in front:expected=h.add((1,expected),(reach,s['B']))
 ck(depth==2*(1-Q(1,1<<m)));ck(h.sign(last['B'])<0);ck(last['ID']==1 and last['R']==0);ck(h.sign(h.add((1,expected),(-1,h.rational(1+Q(m,32)))))>=0)
 save('deep_frontier.json',{'m':m,'expected_depth':str(depth),'expected_B':vec(expected),'negative_leaf_B':vec(last['B']),'negative_leaf_KL':vec(last['K']),'leaf_reaches':[str(r) for r,s in front]})
 save('rows.json',ROWS);save('roots.json',roots);save('sign_certificates.json',list(h.SIGNS.values()))
 result={'status':'PASS','states':len(ROWS),'shallow_states':1449,'deep_states':17,'roots':17,'checks':CHECKS,'sign_certificates':len(h.SIGNS),'elapsed_seconds':time.perf_counter()-START,'scope':'Exact declared finite validation; all-m theorem is author proof, not independently reviewed.'}
 save('validation.json',result);print(json.dumps(result))
if __name__=='__main__':main()
