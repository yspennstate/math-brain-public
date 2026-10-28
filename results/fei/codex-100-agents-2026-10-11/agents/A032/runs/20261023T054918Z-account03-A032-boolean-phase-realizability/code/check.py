from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import json, time, sys
R=Path(__file__).resolve().parents[1]; O=R/'out'
t0=time.perf_counter(); checks=0
def ck(b):
 global checks
 checks+=1
 assert b,checks
 assert time.perf_counter()-t0 < (55 if '--pilot' in sys.argv else 60)
def enc(v):
 if isinstance(v,Q):return str(v)
 if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
 if isinstance(v,(list,tuple)):return [enc(x) for x in v]
 return v
def save(n,v):(O/n).write_text(json.dumps(enc(v),indent=2)+'\n',encoding='utf-8')
def fw(a):
 a=list(a);j=1
 while j<len(a):
  for s in range(0,len(a),2*j):
   for k in range(s,s+j):a[k],a[k+j]=a[k]+a[k+j],a[k]-a[k+j]
  j*=2
 return a
def coeff(a):return [Q(x,len(a)) for x in fw(a)]
def law(a):return [x*x for x in coeff(a)]
@lru_cache(None)
def factor(n):
 r=[];p=2
 while p*p<=n:
  e=0
  while n%p==0:n//=p;e+=1
  if e:r.append((p,e))
  p+=1
 if n>1:r.append((n,1))
 return r
@lru_cache(None)
def lr(x):
 ans={}
 for n,s in [(x.numerator,1),(x.denominator,-1)]:
  for p,e in factor(n):ans[p]=ans.get(p,Q(0))+s*e
 return {p:v for p,v in ans.items() if v}
def add(*terms):
 ans={}
 for c,x in terms:
  for p,v in x.items():ans[p]=ans.get(p,Q(0))+c*v
 return {p:v for p,v in ans.items() if v}
def ce(p,q):
 ck(len(p)==len(q));ck(all(y>0 or x==0 for x,y in zip(p,q)))
 return add(*[(-x,lr(y)) for x,y in zip(p,q) if x])
def H(p):return ce(p,p)
def D(p,q):return add((1,ce(p,q)),(-1,H(p)))
def ln(v):
 x=(v-1)/(v+1);s=Q(0);power=x
 for j in range(24):s+=2*power/(2*j+1);power*=x*x
 return s,s+2*power/(49*(1-x*x))
LN2=ln(Q(2))
@lru_cache(None)
def lb(p):
 k=p.bit_length()-1;l,u=ln(Q(p,1<<k))
 return k+l/LN2[1],k+u/LN2[0]
def bounds(x):
 l=u=Q(0)
 for p,c in x.items():
  a,b=lb(p);l+=c*(a if c>=0 else b);u+=c*(b if c>=0 else a)
 return l,u
def below(x,y):ck(bounds(add((1,x),(-1,{2:Q(y)})))[1]<0)
def marginal(p,bit):
 low=(1<<bit)-1;n=len(p)//2
 return [p[(x&low)|((x&~low)<<1)]+p[(x&low)|((x&~low)<<1)|(1<<bit)] for x in range(n)]
def restrict(f,bit,value):
 low=(1<<bit)-1
 return [f[(x&low)|((x&~low)<<1)|(value<<bit)] for x in range(len(f)//2)]
def erasure(p,bit):return add((1,H(p)),(-1,H(marginal(p,bit))))
a=[1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1];b=[1-x*x for x in a]
A=coeff(a);B=coeff(b);beta=Q(3,8)
def wrap(h,sig):return [x+sig*y*v for v in h for x,y in zip(a,b)]
def coherent(h,M,sig):
 m=Q(sum(h),len(h));r=m*m
 ans=[(x+sig*m*y)**2 for x,y in zip(A,B)]
 for t in M[1:]:ans.extend(y*y*(1-r)*t for y in B)
 ck(sum(ans)==1)
 return ans
def normalized(v):ck(sum(v)==1);ck(all(x>=0 for x in v))
cores=[list(k) for n in [1,2] for k in product([-1,1],repeat=1<<n)]
cores += [[1]*8,[-1]+[1]*7,[1,-1]*4,[1,1,1,-1,1,1,1,-1]]
fixture=None;count=0;thirds=0;strict=[]
for k in cores[:4] if '--pilot' in sys.argv else cores:
 count+=1;nk=len(k);d=nk.bit_length()-1
 # i is bit0, j bit1; x starts at bit2; +1 means input bit0.
 h=[1 if not (x&1) else (1 if not(x&2) else -1)*k[x>>2] for x in range(4*nk)]
 ph=law(h);ck(ph[0]==Q(1,4));ck(ph[1]==Q(1,4))
 pk=law(k);r=pk[0];mu=Q(sum(k),nk)
 U=[Q(0)]+[Q(6,7*(2*nk-2))]*(2*nk-1);U[1]=Q(1,7);normalized(U)
 S1=[Q(0)]*len(h);S1[1]=Q(1,15)
 for v in range(1,2*nk):S1[2*v]=S1[2*v+1]=Q(7,15)*U[v]
 normalized(S1)
 oldtail=[Q(0)]+[x/Q(3,4) for x in ph[1:]]
 M=[Q(7,8)*x+Q(1,8)*y for x,y in zip(oldtail,S1)];normalized(M)
 ck(M[1]==Q(3,10))
 ref=[Q(1,2)]+[x*Q(1,2) for x in oldtail[1:]]
 tagged=[x*x*(t==0) for t in range(len(h)) for x in A]+[y*y*v for v in ref for y in B]
 root=[x+z*y*v for z in [1,-1] for v in h for x,y in zip(a,b)]
 proot=law(root);normalized(proot);normalized(tagged)
 ck(add((1,H(ph)),(-Q(1,2),H(pk)))=={2:Q(2)})
 ck(add((1,H(proot)),(-Q(3,16),H(pk)))=={2:Q(23,4),3:-Q(9,16)})
 Ik=sum(t.bit_count()*v for t,v in enumerate(pk))
 ck(sum(t.bit_count()*v for t,v in enumerate(ph))==1+Ik/2)
 ck(sum(t.bit_count()*v for t,v in enumerate(proot))==Q(5,2)+Q(3,16)*Ik)
 # tag is the highest physical bit (4+d+2).
 Bz=erasure(proot,4+d+2);oldce=ce(proot,tagged)
 signed=[];ce1={};q1={};p1={}
 for sig in [1,-1]:
  f=wrap(h,sig);p1[sig]=law(f);q1[sig]=coherent(h,M,sig);ce1[sig]=ce(p1[sig],q1[sig]);signed.append(f)
 taginc=add((1,Bz),(Q(1,2),ce1[1]),(Q(1,2),ce1[-1]),(-1,oldce));below(taginc,-Q(1,64))
 ck(all(v in [-1,1] for v in root))
 L=[Q(0)]+[(M[2*v]+M[2*v+1])/(1-M[1]) for v in range(1,2*nk)]
 expected=[Q(1,6)*v for v in U]
 for t,p in enumerate(pk):expected[2*t+1]+=Q(5,6)*p
 ck(L==expected);normalized(L)
 N=[Q(7,8)*v for v in L];N[1]+=Q(1,8);normalized(N)
 tj=N[1];ck(tj==(35*r+7)/48)
 terminal=[];constants=[];cost2={};cost3={};be_i={};be_j={};ce_const={};ce_j={}
 for sig in [1,-1]:
  fi=signed[0 if sig==1 else 1];bi=erasure(p1[sig],4);qi=marginal(q1[sig],4)
  be_i[sig]=bi
  ich=[]
  for val in [0,1]:
   hh=restrict(h,0,val);ff=restrict(fi,4,val);pp=law(ff)
   ck(ff==wrap(hh,sig));qq=coherent(hh,N,sig);ich.append(ce(pp,qq))
   if val==0:
    ck(all(v==1 for v in hh));ce_const[sig]=ich[-1]
    constants.append({'sigma':sig,'reach':Q(1,4),'truth_table':ff,'spectrum':pp,'reference':qq,'CE':ich[-1]})
    continue
   ck(Q(sum(hh),len(hh))==0)
   bj=erasure(pp,4);qj=marginal(qq,4);jces=[]
   be_j[sig]=bj
   # third prescribed target alternatives on the retained arbitrary core.
   targetlist=[[Q(0)]+[Q(1,nk-1)]*(nk-1),[Q(0)]*(nk-1)+[Q(1)], [Q(0)]+[Q(t,nk*(nk-1)//2) for t in range(1,nk)]]
   L3=[Q(0)]+[(N[2*t]+N[2*t+1])/(1-tj) for t in range(1,nk)];normalized(L3)
   for target_index,target in enumerate(targetlist):
    normalized(target);T=[Q(511,512)*x+Q(1,512)*y for x,y in zip(L3,target)];normalized(T)
    newces=[];coarseD=[];ends=[]
    for jval in [0,1]:
     hk=restrict(hh,0,jval);fk=restrict(ff,4,jval);ppk=law(fk);qk=coherent(hk,T,sig)
     ck(fk==wrap(hk,sig));ck(law(hk)==pk)
     pco=ppk[:16]+[beta*(1-r)];qco=qj[:16]+[beta*(1-tj)];normalized(pco);normalized(qco)
     rd=D(pco,qco);ck(bounds(rd)[0]>Q(1,512))
     delta=[x-y for x,y in zip(pco,qco)];l1=sum(abs(x) for x in delta)
     ck(l1>=Q(1,16));ck(l1>=abs(mu)/4);ck(l1>=Q(3,4)*abs(r-tj))
     newces.append(ce(ppk,qk));coarseD.append(rd);ends.append({'seed':hk,'truth_table':fk,'spectrum':ppk,'reference':qk,'coarse_refund':rd,'L1':l1})
    inc3=add((1,bj),(Q(1,2),newces[0]),(Q(1,2),newces[1]),(-1,ce(pp,qq)))
    cost3[sig,target_index]=inc3;ce_j[sig,target_index]=newces
    below(inc3,-Q(1,2048));thirds+=1
    # Exact chain identity, including inherited occupancy KL and fresh CE changes.
    rho=add((1,D(pp,qq)),(-1,D(marginal(pp,4),qj)))
    resetdiff=add((Q(1,2),newces[0]),(Q(1,2),newces[1]),(-Q(1,2),ce(law(restrict(ff,4,0)),qj)),(-Q(1,2),ce(law(restrict(ff,4,1)),qj)))
    ck(inc3==add((-1,rho),(1,resetdiff)))
    if count==6 and target==targetlist[1]:terminal.append({'sigma':sig,'third_increment':inc3,'terminals':ends,'current_tail':N,'third_tail':T})
  inc2=add((1,bi),(Q(1,2),ich[0]),(Q(1,2),ich[1]),(-1,ce1[sig]));below(inc2,-Q(1,10))
  cost2[sig]=inc2
 totalcert=[]
 for target_index in range(3):
  total=add((1,taginc),*[ (Q(1,2),cost2[sig]) for sig in [1,-1]],*[ (Q(1,4),cost3[sig,target_index]) for sig in [1,-1]])
  literal=add((1,Bz),(-1,oldce),*[(Q(1,2),be_i[sig]) for sig in [1,-1]],*[(Q(1,4),be_j[sig]) for sig in [1,-1]],*[(Q(1,4),ce_const[sig]) for sig in [1,-1]],*[(Q(1,8),cc) for sig in [1,-1] for cc in ce_j[sig,target_index]])
  ck(total==literal);below(total,-Q(1,64)-Q(1,10)-Q(1,4096));totalcert.append(total)
 if count==6:fixture={'core':k,'selector_seed':h,'root_truth_table':root,'incoming_reference':tagged,'first_tail':M,'second_tail':N,'tag_increment':taginc,'constant_terminals':constants,'third_branches':terminal,'complete_tree_increments':totalcert,'terminal_reaches':'two constant terminals at1/4 each; four core terminals at1/8 each'}
 save('CHECKPOINT.json',{'status':'RUNNING_NOT_CERTIFICATE','completed_cores':count,'checks':checks})
ck(320**40*7**15>2**8*257**40*8**15)
ck(512**256<2*511**256)
ck(21**18>2**79)
result={'PASS':True,'pilot':'--pilot' in sys.argv,'cores':count,'third_resets':thirds,'checks':checks,'seconds':time.perf_counter()-t0,'arithmetic':'rational laws, exact prime-log identities and rational proven log intervals','formal_status':'NOT_CLAIMED'}
save('pilot.json' if '--pilot' in sys.argv else 'validation.json',result)
if fixture:save('fixture.json',fixture)
print(json.dumps(result))
