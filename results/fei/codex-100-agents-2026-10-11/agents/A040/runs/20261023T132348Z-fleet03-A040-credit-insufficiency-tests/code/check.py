from model import *
import arithmetic as ar
from functools import lru_cache

def exact(v): return (v,v)
def chi(p,q): return sum(((y-x)**2/x for x,y in zip(p,q) if x),F(0))
def geometry(g,q,i):
    aa=spectrum(g);eta=infl(g,i);cs,qs,rr,pp,qq=branch(g,q,i)
    ss=[]
    for t,p in enumerate(pp):
        lo=t%(1<<i)+(t>>i)*(1<<(i+1)); hi=lo+(1<<i)
        ss.append(aa[lo]*aa[hi]/p if p else F(0))
    ck(sum(p*s for p,s in zip(pp,ss))==0)
    V=sum((p*s*s for p,s in zip(pp,ss)),F(0));t=sum(q*s for q,s in zip(qq,ss));X=chi(pp,qq)
    ck(rr==[F(1,2)+t,F(1,2)-t]);ck(V<=eta*(1-eta));ck(t*t<=X*V)
    ratios=[q/p for p,q in zip(pp,qq) if p];beta=min(ratios);upper=max(ratios)
    ck(X<=(upper-1)*(1-beta))
    O=scale(log(1/(1-4*t*t)),F(1,2))
    cap=scale(exact(2*X*eta*(1-eta)/(beta*(2-beta))),1/L2[0])
    ck(O[0]<=cap[1])
    fw=kl(qq,pp);full=kl(q,law(g));ck(fw[0]<=full[1])
    theta=min(eta,1-eta)
    if theta:
        barrier=sub(scale(log(1/theta),2*abs(t)),log(F(5)))
        ck(fw[1]>=barrier[0])
    else:ck(t==0 and O==Z)
    return {'eta':str(eta),'t':str(t),'V':str(V),'chi2_erased':str(X),'floor':str(beta),'upper':str(upper),'outcome_KL':fmt(O),'forward_full_KL':fmt(full)}

def grouped(r,alpha):
    d=F(1,2**r);m=d*d;beta=1-alpha;n=2**(r-1)
    old=scale(Fmix(m,alpha),F(1,2))
    q=alpha+beta*m
    fw=scale(add(scale(log(q/m),q),scale(log(beta),beta*(1-m))),F(1,2))
    kap=scale(log(1/(1-F(9,100)*alpha*alpha)),F(1,2))
    correction=scale(sub(add(Fmix(4*m,alpha),Fmix(16*m,alpha)),scale(Fmix(10*m,alpha),2)),F(1,4))
    sig=add(kap,correction)
    ck(kap[0]>0);ck(sig[1]>=kap[0]);ck(old[1]<1 and fw[1]<2) if alpha==F(1,r) else None
    X=alpha*alpha*(1/(10*m)-1)/2
    t=-3*alpha/20;eta=d/2
    barrier=sub(scale(log(1/eta),2*abs(t)),log(F(5)))
    ck(fw[1]>=barrier[0]);ck(X>0)
    hv=add(add(phi((1-3*d)**2),scale(phi(9*m),n-1)),scale(phi(m),3*n))
    h0=add(phi((1-2*d)**2),scale(phi(4*m),2**r-1));h1=add(phi((1-4*d)**2),scale(phi(16*m),n-1))
    he=add(add(phi(1-6*d+10*m),scale(phi(10*m),n-1)),scale(phi(2*m),n))
    credits=[scale(sub(Fmix(m,alpha),Fmix(10*m,alpha)),F(1,2)),scale(sub(he,scale(add(h0,h1),F(1,2))),F(1,2)),sub(bern(d/2),scale(sub(hv,he),F(1,2))),scale(sub(bern(3*d/2),scale(add(bern(d),bern(2*d)),F(1,2))),r),sub(add(bern(d/2),scale(bern(3*d/2),r)),scale(hv,F(1,2)))]
    if r<=32:ck(all(x[0]>0 for x in credits));ck(correction[0]>0)
    return {'r':r,'alpha':str(alpha),'reverse_KL':fmt(old),'forward_KL':fmt(fw),'outcome_KL':fmt(kap),'sigma':fmt(sig),'sigma_over_Inf_lower':str(sig[0]/eta),'r2_sigma':fmt(scale(sig,r*r)),'chi2_erased':str(X),'five_credits':list(map(fmt,credits))}

def tensor_core(k,r):
    out=[]
    for x in range(2**(1+k*(r+1))):
        y=1-2*(x&1)
        for b in range(k):
            row=(x>>(1+b*(r+1)))&((1<<(r+1))-1)
            j=row&1;w=row>>1;y*=1-2*(w==0 or(j and w==3))
        out.append(y)
    return tuple(out)

def tensor_policy(k,r):
    v=tensor_core(k,r);f=priority(v);q0=lifted(f,v,F(1,8),3)
    A0=kl(law(f),q0);H0=entropy(law(f));I0=influence(f);M0=sub(exact(4*I0),add(H0,A0))
    ck(I0==F(3,2)+k*(3*r+1)*F(1,2**r)/4)
    ck(spectrum(v)[-1]**2==F(1,2**(2*r*k)))
    bc,bq,_,_,_=branch(f,q0,2);ac,aq,_,_,_=branch(bc[1],bq[1],1)
    terms=[(F(1,2),bc[0],bq[0])];states=[];sigma1=Z;later=Z;records=[]
    for g,q in zip(ac,aq):
        fresh=lifted(g,v,F(1,6),1)
        sigma1=add(sigma1,scale(sub(kl(law(g),fresh),kl(law(g),q)),F(1,4)))
        states.append((F(1,4),g,fresh,v))
    mroot=F(1,2**(2*r*k));same(sigma1,scale(sub(Fmix(mroot,F(1,6)),Fmix(mroot,F(1,8))),F(1,4)))
    kap=scale(log(F(400,399)),F(1,2));ck(sigma1[0]>0)
    for level in range(k):
        new=[];generation=Z
        for reach,g,q,h in states:
            idx=2+level*r;gc,old,rr,pp,qq=branch(g,q,idx)
            ck(rr==[F(19,40),F(21,40)])
            m=law(h)[-1];sig=Z
            for b in (0,1):
                hc=restrict(h,idx-1,b);fresh=lifted(gc[b],hc,F(1,6),1)
                sig=add(sig,scale(sub(kl(law(gc[b]),fresh),kl(law(gc[b]),old[b])),F(1,2)))
                ck(law(hc)[-1]==m*(4 if b==0 else 16))
                new.append((reach/2,gc[b],fresh,hc))
            formula=add(kap,scale(sub(add(Fmix(4*m,F(1,6)),Fmix(16*m,F(1,6))),scale(Fmix(10*m,F(1,6)),2)),F(1,4)))
            same(sig,formula);ck(sig[0]>kap[1]);generation=add(generation,scale(sig,reach))
            records.append({'level':level,'reach':str(reach),'full_mass':str(m),'outcomes':list(map(str,rr)),'sigma':fmt(sig)})
        ck(sum(x[0] for x in new)==F(1,2));ck(generation[0]>kap[1]/2)
        later=add(later,generation);states=new
    terms.extend((w,g,q) for w,g,q,h in states)
    S=Z;Af=Z;Hf=Z;If=F(0)
    for w,g,q in terms:
        hp=entropy(law(g));ii=influence(g);S=add(S,scale(sub(exact(4*ii),hp),w));Hf=add(Hf,scale(hp,w));If+=w*ii;Af=add(Af,scale(kl(law(g),q),w))
    e=sub(sub(H0,Hf),exact(4*(I0-If)))
    paid=add(add(A0,e),add(sigma1,later))
    signed=sub(S,(max(F(0),paid[0]),max(F(0),paid[1])))
    other=sub(M0,add(sigma1,later));mini=(min(S[0],other[0]),min(S[1],other[1]));same(signed,mini)
    return {'k':k,'r':r,'M0':fmt(M0),'sigma1':fmt(sigma1),'sigma_later':fmt(later),'terminal_S':fmt(S),'signed_before_old_quarter':fmt(signed),'terminal_full_KL':fmt(Af),'local_records':records}

pilot='--pilot' in sys.argv
tables=range(8) if pilot else range(256)
geo=[]
for table in tables:
    g=tuple(1-2*((table>>x)&1) for x in range(8));p=law(g);target=max(t for t,x in enumerate(p) if x)
    q=tuple(F(5,6)*x+F(1,6)*(t==target) for t,x in enumerate(p))
    for i in range(3):geo.append(geometry(g,q,i))
rare=[]
for r in ((3,) if pilot else (3,4)):
    for alpha in (F(1,6),F(1,r)):
        for eps in (-1,1):
            h=core(r);g=G(h,eps);q=lifted(g,h,alpha,1);rec=geometry(g,q,1);gc,old,rr,pp,qq=branch(g,q,1)
            ck(rr==[F(1,2)-3*alpha/20,F(1,2)+3*alpha/20]);ck(chi(pp,qq)==alpha*alpha*(1/F(10*F(1,2**(2*r))))/2-alpha*alpha/2)
            sig=Z
            for b in (0,1):
                hc=restrict(h,0,b);fresh=lifted(gc[b],hc,alpha,1)
                sig=add(sig,scale(sub(kl(law(gc[b]),fresh),kl(law(gc[b]),old[b])),F(1,2)))
            same(sig,tuple(F(x) for x in grouped(r,alpha)['sigma']));rec.update({'r':r,'alpha':str(alpha),'epsilon':eps,'sigma':fmt(sig)});rare.append(rec)
rs=[3,8,32] if pilot else list(range(3,17))+[24,32,64,128]
groups=[grouped(r,a) for r in rs for a in (F(1,6),F(1,r))]
policies=[tensor_policy(k,r) for k,r in ([(1,3)] if pilot else [(1,3),(2,3),(1,4)])]
scalar=[]
for s in range(12,33):
    k=2**s;r=2*s+8;d=F(1,2**r)
    ck(k*(3*r+1)*d<F(1,16));ck(16*k*(r+1)*d<=F(1,1024));ck(16*k*r*d<=F(1,2048));ck(F(49,16)-F(k,1200)<=-F(421,1200))
    scalar.append({'s':s,'final_margin_upper':str(F(49,16)-F(k,1200))})
ck(400**300>2*399**300);ck(F(49,16)-F(4096,1200)==-F(421,1200))
out={'status':'PASS','checks':ar.checks,'runtime_seconds':time.perf_counter()-start,'universal_geometry_cases':len(geo),'geometry':geo,'rare_dense':rare,'grouped':groups,'A037_policies':policies,'A037_scalar':scalar,'formal_verification':'not attempted'}
dest=ROOT/'out'/('PILOT.json' if pilot else 'CHECK.json');dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:out[k] for k in ('status','checks','runtime_seconds','universal_geometry_cases')}))
