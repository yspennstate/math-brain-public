from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
R=Path(__file__).resolve().parents[1];mode=sys.argv[1] if len(sys.argv)>1 else 'pilot';start=time.monotonic();checks=0;states=0;edges=0;dummy_guards=[]
def ck(x):
 global checks
 checks+=1;assert x,checks;assert time.monotonic()-start<(55 if mode=='pilot' else 180)
def wal(v):
 a=list(v);h=1
 while h<len(a):
  for k in range(0,len(a),2*h):
   for j in range(k,k+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
@lru_cache(None)
def sp(v):return tuple(F(x*x,len(v)**2) for x in wal(v))
def rest(v,j,b):return tuple(v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(v)//2))
def marg(q,j):return tuple(a+b for a,b in zip(rest(q,j,0),rest(q,j,1)))
def inf(v,j):return F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
def TI(v):return sum((inf(v,j) for j in range(len(v).bit_length()-1)),F(0))
@lru_cache(None)
def cleanH(v):
 p=sp(v);s=[x for x in p if x];ck(all(x==s[0] for x in s));n=len(s);ck(n&(n-1)==0)
 h=n.bit_length()-1;ck(h%2==0);return F(h)
@lru_cache(None)
def bell(v):
 global states,edges
 states+=1;h=cleanH(v);opt=F(0)
 for j in range(len(v).bit_length()-1):
  edges+=1;a,b=rest(v,j,0),rest(v,j,1);e=h-(cleanH(a)+cleanH(b))/2-3*inf(v,j)
  val=e+(bell(a)+bell(b))/2;opt=max(opt,val)
  ck(val<=h/4)
 ck(opt==h/4);return opt
def ln(x):
 z=(x-1)/(x+1);s=sum((2*z**(2*j+1)/(2*j+1) for j in range(28)),F(0))
 return s,s+2*z**57/(57*(1-z*z))
L2=ln(F(2))
@lru_cache(None)
def lg(x):
 k=0
 while x<1:x*=2;k-=1
 while x>=2:x/=2;k+=1
 a,b=ln(x);return F(k)+a/L2[1],F(k)+b/L2[0]
def pt(x):return F(x),F(x)
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,t):return (a[0]*t,a[1]*t) if t>=0 else (a[1]*t,a[0]*t)
def sub(a,b):return add(a,mul(b,-1))
def overlaps(a,b):return a[0]<=b[1] and b[0]<=a[1]
@lru_cache(None)
def CE(p,q):
 out=pt(0)
 for pp,qq in zip(p,q):
  if pp:ck(qq>0);out=add(out,mul(lg(1/qq),pp))
 return out
def enc(x):return {'lo':str(x[0]),'hi':str(x[1]),'approx':float(sum(x)/2)}
def seed(k,l,d):
 return tuple((-1)**(sum(((x>>(2*j))&3)==3 for j in range(k))+sum((x>>(2*k+j))&1 for j in range(l))) for x in range(1<<(2*k+l+d)))
clean_rows=[];cap=3 if mode=='pilot' else 6
for k in range(cap//2+1):
 for l in range(cap-2*k+1):
  for d in range(cap-2*k-l+1):
   v=seed(k,l,d);ck(bell(v)==F(k,2));clean_rows.append({'k':k,'l':l,'dummy':d,'optimal_rate3_debit':str(F(k,2))})
# Frontier entries: actual truth table, inherited Q, original G reach, clean flag.
def query(active,j):
 v,q,a,_=active;qr=marg(q,j)
 return (rest(v,j,0),qr,a/2,False),(rest(v,j,1),qr,a/2,True),a*inf(v,j)
def oldfront(m,H,T):
 b=seed(m,0,1);c=tuple(x-2*(i==0) for i,x in enumerate(b));leaves=[(b,sp(b),F(1,2),True)];active=(c,sp(c),F(1,2),False);J=F(0)
 for s in range(T+1):
  if s==H:
   active,exit,jj=query(active,len(active[0]).bit_length()-2);leaves.append(exit);J+=jj
  if s<T:
   active,exit,jj=query(active,0);leaves.append(exit);J+=jj
   active,exit,jj=query(active,0);leaves.append(exit);J+=jj
 leaves.append(active);return b,c,leaves,J
def attain(v,q):
 # Query only first-hit intact coordinates; retain every branch and inherited reference.
 for j in range(len(v).bit_length()-1):
  if inf(v,j)==F(1,2):
   qr=marg(q,j);a,b=rest(v,j,0),rest(v,j,1)
   ha,ka,ja=attain(a,qr);hb,kb,jb=attain(b,qr)
   return mul(add(ha,hb),F(1,2)),mul(add(ka,kb),F(1,2)),F(1,2)+(ja+jb)/2
 p=sp(v);h=pt(cleanH(v));return h,sub(CE(p,q),h),F(0)
frontrows=[];queried_clean_nodes=0
for m in ([2] if mode=='pilot' else [2,3,4]):
 for H in range(m+1):
  for T in range(H,m+1):
   b,c,leaves,J=oldfront(m,H,T);hc=CE(sp(c),sp(c));hb=pt(2*m);hinit=mul(add(hb,hc),F(1,2))
   g=b+c;hg=CE(sp(g),sp(g));IX=(TI(b)+TI(c))/2;r3=sub(pt(3*IX),hg)
   EHleaf=pt(0);CQleaf=pt(0);Kold=pt(0);Hnew=pt(0);Knew=pt(0);Jnew=F(0);kbar=F(0);Fnew=F(0)
   ck(sum(a for v,q,a,cl in leaves)==1)
   for v,q,a,cl in leaves:
    p=sp(v);hh=pt(cleanH(v)) if cl else CE(p,p);cc=CE(p,q);kl=sub(cc,hh)
    EHleaf=add(EHleaf,mul(hh,a));CQleaf=add(CQleaf,mul(cc,a));Kold=add(Kold,mul(kl,a))
    if not cl:Hnew=add(Hnew,mul(hh,a));Knew=add(Knew,mul(kl,a));continue
    k=cleanH(v)/2;kbar+=a*k
    for j in range(len(v).bit_length()-1):
     queried_clean_nodes+=1;v0,v1=rest(v,j,0),rest(v,j,1);qr=marg(q,j)
     eH=cleanH(v)-(cleanH(v0)+cleanH(v1))/2-3*inf(v,j)
     ck(eH in [F(1,2),F(-3),F(0)])
     c0,c1=CE(sp(v0),qr),CE(sp(v1),qr);eq=sub(sub(cc,mul(add(c0,c1),F(1,2))),pt(3*inf(v,j)))
     kl0=sub(c0,pt(cleanH(v0)));kl1=sub(c1,pt(cleanH(v1)))
     ck(overlaps(add(eq,sub(mul(add(kl0,kl1),F(1,2)),kl)),pt(eH)))
     if eH==0 and inf(v,j)==0 and eq[0]>0:
      if len(dummy_guards)<4:dummy_guards.append({'m':m,'H':H,'T':T,'reach':str(a),'query':j,'source_debit':enc(eq),'actual_debit':'0','full_KL_change':enc(sub(mul(add(kl0,kl1),F(1,2)),kl))})
    hn,kn,jn=attain(v,q);Hnew=add(Hnew,mul(hn,a));Knew=add(Knew,mul(kn,a));Jnew+=a*jn
    cost=sub(sub(hh,hn),pt(3*jn));ck(overlaps(cost,pt(k/2)));Fnew+=a*k/2
   oldEH=sub(sub(hinit,EHleaf),pt(3*J));oldEQ=sub(sub(hinit,CQleaf),pt(3*J))
   ck(oldEH[1]<F(71,96));ck(oldEQ[1]<F(7,48));ck(Kold[1]<F(19,32));ck(overlaps(oldEH,add(oldEQ,Kold)))
   ck(kbar<=m);ck(Fnew==kbar/2)
   newEH=sub(sub(hinit,Hnew),pt(3*(J+Jnew)));ck(overlaps(newEH,add(oldEH,pt(Fnew))))
   remain=sub(r3,newEH);ck(remain[0]>F(m,2)-F(71,96));ck(remain[0]>F(25,96))
   # FULL new reference invoice from terminal H+KL, not a reset spectrum.
   newCE=add(Hnew,Knew);newEQ=sub(sub(hinit,newCE),pt(3*(J+Jnew)));ck(overlaps(newEH,add(newEQ,Knew)))
   legacy=sub(sub(hinit,Hnew),pt(2*(J+Jnew)));ck(overlaps(sub(legacy,newEH),pt(J+Jnew)))
   frontrows.append({'m':m,'H':H,'T':T,'old_entropy_debit':enc(oldEH),'old_J':str(J),'clean_weighted_pairs':str(kbar),'sharp_added_actual_debit':str(Fnew),'new_J':str(J+Jnew),'new_full_KL':enc(Knew),'total_entropy_debit':enc(newEH),'original_remaining_reserve':enc(remain)})
ck(bool(dummy_guards))
result={'status':'PASS','mode':mode,'checks':checks,'runtime_seconds':time.monotonic()-start,'clean_representatives':len(clean_rows),'unique_Bellman_truth_tables':states,'Bellman_query_edges':edges,'inherited_frontiers':len(frontrows),'clean_physical_query_checks':queried_clean_nodes,'clean':clean_rows,'frontiers':frontrows,'positive_dummy_source_guards':dummy_guards}
(R/'out').mkdir(exist_ok=True);(R/'out'/('PILOT.json' if mode=='pilot' else 'CHECK.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['clean','frontiers','positive_dummy_source_guards']}))
