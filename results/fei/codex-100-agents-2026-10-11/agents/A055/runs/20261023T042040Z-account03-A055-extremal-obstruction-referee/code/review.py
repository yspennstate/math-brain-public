from exact import Q,fw,entropy,add,mul,sgn,put,enc,bounds
from pathlib import Path
import sys,time,json,hashlib
start=time.perf_counter(); checks=0
def ck(b):
    global checks
    assert b
    checks+=1
    assert time.perf_counter()-start<55,'frozen time cap'
def coefficients(v): return [Q(w,len(v)) for w in fw(v)]
def stat(v):
    a=coefficients(v);H=entropy(a)
    n=len(v).bit_length()-1
    I=Q(sum(v[x]!=v[x^(1<<j)] for x in range(len(v)) for j in range(n)),len(v))
    ck(I==sum(s.bit_count()*q*q for s,q in enumerate(a)))
    return H,I,a[0],a
def hh(u):return entropy([u])
def rem(u,k):
    p=Q(1,1<<k)
    r=add(hh(1-p*(1-u)),hh(u),-p)
    r=add(r,hh(1-u),p*(1-p))
    return add(r,{2:2*k*p*((1-u*u)+(1-p)*(1-u)**2)})
def rank(vs):
    piv={}
    for v in vs:
        while v:
            b=v.bit_length()-1
            if b in piv:v^=piv[b]
            else:piv[b]=v;break
    return len(piv)
def affine_test(v,a):
    # Walsh-transform squared integer coefficients independently computes all biases.
    N=len(v);W=fw(v);bias=fw([w*w for w in W]);n=N.bit_length()-1
    costs=[min(Q(N*N-b,2*N*N),Q(N*N+b,2*N*N)) for b in bias]
    p=[Q(sum(a[x]*a[x] for x in range(N) if x&(1<<j))) for j in range(n)]
    minimal=all(p[j]<=Q(1,2) for j in range(n)) and all(costs[s]>=max([p[j] for j in range(n) if s&(1<<j)],default=0) for s in range(1,N))
    supp=[s for s,q in enumerate(a) if q]
    span=rank([s^supp[0] for s in supp])==n
    return minimal,span
pilot='--pilot' in sys.argv
profiles=[];qualified=0
for n in range(3):
  N=1<<n
  for mask in range(1<<N):
    seed=[(-1 if mask&(1<<x) else 1) for x in range(N)]
    H,q,mu,a=stat(seed); eligible=affine_test(seed,a)
    for t,k in ([(1,2)] if pilot else [(1,2),(1,3),(2,2),(2,3)]):
      nc=n*t;data=nc+4;size=1<<(data+k);p=Q(1,1<<k);v=mu**t
      root=[]
      for x in range(size):
        if x>>data:root.append(1);continue
        aa,bb,cc,zz=[(x>>j)&1 for j in range(4)]
        value=(-1)**(aa*bb+aa*cc+bb*cc+zz*aa)
        for j in range(t):value*=seed[(x>>(4+n*j))&(N-1)]
        root.append(value)
      Hr,Ir,mur,ar=stat(root)
      ck(mur==1-p*(1-v/4))
      ck(Hr==add(mul(add(mul(H,t),{2:4}),p),rem(v/4,k)))
      ck(Ir==p*(t*q+2+k*(1-v/4)))
      if all(eligible):
        ck(all(affine_test(root,ar)));qualified+=1
      physical=[];reset=[];release=[]
      for b in range(4):
        ch=[root[(y<<2)|b] for y in range(size//4)]
        sh=[]
        for y in range(len(ch)):
          # y bits zero and one are c,z; substitute old c=c+z only on b=1.
          old=y^(2*((y>>1)&1)) if False else y
          if b==1:old=y^((y>>1)&1)
          sh.append(ch[old])
        Hc,Ic,mc,ac=stat(ch);Hs,Is,ms,as_=stat(sh)
        ck(sorted(x*x for x in ac)==sorted(x*x for x in as_))
        ck(Hs==Hc);ck(mc==ms)
        ck(Ic-Is==(p if b==1 else 0));release.append(Ic-Is)
        targetmu=v if b==0 else Q(0)
        ck(Hs==add(mul(H,t*p),rem(targetmu,k)))
        ck(Is==p*(t*q+(0 if b==0 else 1)+k*(1-targetmu)))
        ck(all(sum(x*x for s,x in enumerate(as_) if s&(1<<j))<=Q(1,2) for j in range(data+k-2)))
        physical.append((Hc,Ic));reset.append((Hs,Is))
      rho=sum(release)/4
      ck(rho==p/4)
      ck(Ir-sum(x[1] for x in physical)/4==p)
      ck(Ir-sum(x[1] for x in reset)/4==5*p/4)
      L=Hr
      for h,i in reset:L=add(L,h,-Q(1,4))
      expected=add({2:4*p},rem(v/4,k))
      expected=add(expected,rem(v,k),-Q(1,4));expected=add(expected,rem(0,k),-Q(3,4))
      ck(L==expected)
      # Enclose absolute mean-profile error via two exact inequalities, no float.
      error=add(mul(L,1/p),{2:-4});bound=(13+6*k)*abs(v)
      ck(sgn(add({2:bound},error))>=0);ck(sgn(add({2:bound},error,-1))>=0)
      for K in [Q(16,5),Q(15,4),Q(8)]:
        D=add(Hr,{2:-K*Ir});S={}
        for h,i in reset:S=add(S,add({2:K*i},h,-1),Q(1,4))
        ck(add(D,S)==add(L,{2:-5*K*p/4}))
      profiles.append({'n':n,'mask':mask,'t':t,'k':k,'qualified_root':all(eligible),'mean_power':str(v),'L':enc(L),'release':str(rho)})
    put('CHECKPOINT_REPLAY.json',{'seeds_completed':sum(1 for _ in profiles),'assertions':checks})
# Scalar certificate reconstructed using the own-stage exact interval helper.
g=[-1]+[1]*255;Hg,Ig,mug,ag=stat(g)
ck(Ig==Q(1,16));ck(mug==Q(127,128));ck(all(affine_test(g,ag)))
K=Q(15,4);d=add(Hg,{2:-K*Ig});ck(sgn(add(d,{2:-Q(1,256)}))>0)
t=100000000;k=10000;vbound=Q(128,128+t)
margin=5*K/4-4-(13+6*k)*vbound
term=Q(t,256)-K*(1+2*k)-10*k-20
rootbound=Q(t,256)+4-K*2-K*2*k-10*k-20
ck(margin==Q(7633553,12500016));ck(term==Q(862405,4));ck(margin>0 and term>0 and rootbound>0)
put('PILOT.json' if pilot else 'CHECK.json',{'status':'PASS','pilot':pilot,'assertions':checks,'roots':len(profiles),'physical_terminals':4*len(profiles),'reset_terminals':4*len(profiles),'qualified_root_profiles':qualified,'elapsed_seconds':time.perf_counter()-start,'scalar_certificate':{'margin_over_p':str(margin),'terminal_deficit_over_p':str(term),'root_deficit_over_p_lower':str(rootbound),'huge_power_or_truth_table_evaluated':False},'profiles':profiles})
print(json.dumps({'status':'PASS','assertions':checks,'roots':len(profiles),'qualified':qualified,'seconds':time.perf_counter()-start}))
