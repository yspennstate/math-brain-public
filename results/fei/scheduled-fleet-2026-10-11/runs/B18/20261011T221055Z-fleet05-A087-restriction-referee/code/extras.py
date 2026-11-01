import sys,json,time
sys.argv=[sys.argv[0],'library']
import check as c
from fractions import Fraction as F
start=time.perf_counter();before=c.assertions;points=adjacent=labels=activations=0
for n in [1,2]:
    N=1<<n;delta=F(1,N)
    for mask in range(1<<N):
        f=tuple(1-2*((mask>>x)&1) for x in range(N));a=[F(w,N) for w in c.walsh(f)];iv=c.influence(f)
        ds=[(v,) for v in range(N)]+[(v,v^(1<<j)) for j in range(n) for v in range(N) if not ((v>>j)&1)]
        for D in ds:
            g=tuple(-f[x] if x in D else f[x] for x in range(N));b=[F(w,N) for w in c.walsh(g)]
            t=[delta*sum(f[v]*(1-2*((v&s).bit_count()%2)) for v in D) for s in range(N)]
            c.check(all(bb==aa-2*tt for aa,bb,tt in zip(a,b,t)))
            e=[tt*tt for tt in t];m=[(aa-tt)**2 for aa,tt in zip(a,t)];q=[aa+bb for aa,bb in zip(e,m)]
            c.check(sum(e)==len(D)*delta);c.check(sum(q)==1)
            selector=f+g;p=c.spectrum(selector)
            c.check(p==m+e)
            L=c.add(*(c.scale(c.ent([ee/qq,mm/qq]),qq) for ee,mm,qq in zip(e,m,q) if qq))
            J=c.add(*(c.scale(c.log(qq/ee),ee) for ee,qq in zip(e,q) if ee));R=c.add(*(c.scale(c.log(qq/mm),mm) for mm,qq in zip(m,q) if mm))
            c.check(L==c.add(J,R));c.check(c.ent(p)==c.add(c.ent(q),L))
            ig=c.influence(g)
            for i in range(n):
                expected=sum(2*delta*f[v]*f[v^(1<<i)] for v in D if (v^(1<<i)) not in D)
                c.check(ig[i]-iv[i]==expected)
            if len(D)==1:c.check(all(ee<=mm for ee,mm in zip(e,m)));points+=1
            else:adjacent+=1
for mask in range(16):
    u=tuple(1-2*((mask>>x)&1) for x in range(4));mu=F(sum(u),4);delta=(1-mu)/2;v=1-mu*mu
    su=c.spectrum(u);L=c.ent([p/v for p in su[1:]]) if v else {}
    for k in [1,2,3]:
        p=F(1,1<<k);f=tuple(u[x>>k] if x%(1<<k)==0 else 1 for x in range(1<<(k+2)));sf=c.spectrum(f)
        q=[F(0)]*(1<<k)
        for s,ps in enumerate(sf):q[s% (1<<k)]+=ps
        B=c.add(c.ent(sf),c.scale(c.ent(q),-1));R0=1-4*p*delta+4*p*p*delta
        rhs=c.add(c.scale(L,p*v),c.scale(c.ent([delta,1-delta]),4*delta*p*(1-p)))
        if v:rhs=c.add(rhs,c.scale(c.ent([p*p*v/R0,1-p*p*v/R0]),R0))
        c.check(B==rhs)
        ci=[c.restrict(f,[k,k+1],z) for z in range(4)]
        terminalI=sum(sum(c.influence(g)) for g in ci)/4
        c.check(terminalI==k*p*(1-mu));c.check(sum(c.influence(f))==p*sum(c.influence(u))+terminalI)
        activations+=1
for n in range(4):
    N=1<<n
    for mask in range(1<<N):
        f=tuple(1-2*((mask>>x)&1) for x in range(N));iv=c.influence(f)
        for um in range(1,1<<n):
            U=[i for i in range(n) if (um>>i)&1];V=[i for i in range(n) if i not in U]
            ci=[c.influence(c.restrict(f,U,z)) for z in range(1<<len(U))]
            for j in V:c.check(iv[j]==sum(a[V.index(j)] for a in ci)/len(ci));labels+=1
for k in range(1,11):
    p=F(1,1<<k);coreI=(1<<(k-1))+1;coreH=1<<k
    c.check(p*coreI==F(1,2)+p);c.check(p*coreH==1);c.check(p*(coreI+k)<=F(3,2))
# The posterior-on-empty-packet is 4/5 versus a fair physical branch.
f=(1,1,1,-1,1,1,1,1) # use constructed activation below for convention clarity
f=tuple((1 if (x>>2)==0 else -1) if x%4==0 else 1 for x in range(8))
g=[c.restrict(f,[0],z) for z in [0,1]];p0=[c.spectrum(h)[0] for h in g]
c.check(sorted(p0)==[F(1,4),F(1)]);c.check(max(p0)/sum(p0)==F(4,5))
result={'status':'PASS','assertions':c.assertions-before,'point_surgeries':points,'adjacent_surgeries':adjacent,'proper_core_activations':activations,'labelled_survival_checks':labels,'terminal_family_parameters':10,'posterior_empty_packet':'4/5','physical_branch_probability':'1/2','runtime_seconds':time.perf_counter()-start}
c.ROOT.joinpath('out/extra_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result,indent=2))
