from pathlib import Path
from fractions import Fraction as F
import json,sys,time
import arithmetic as A
RUN=Path(__file__).resolve().parents[1]
def plus(*xs):
    z=(F(0),F(0))
    for x in xs:z=A.add(z,x)
    return z
def overlapzero(x):A.ck(x[0]<=0<=x[1])
def neglog(q):return A.scale(A.lg(q),F(-1))
def source(w,narrow=2):
    return [(1-2*((x&((1<<w)-1))==0))*(1-2*((x>>w)==0)) for x in range(1<<(w+narrow))]
def model(g,m):
    k=(len(g)-1).bit_length();n=k+m;eps=F(1,1<<n)
    gg=[g[x&((1<<k)-1)] for x in range(1<<n)]
    v=gg+gg;v[1<<n]*=-1
    p=A.law(g);s=sum(x!=0 for x in p);W=2*eps-s*eps**2
    Q=[(1-W)*p[t] if t<len(p) and p[t] else eps**2 for t in range(len(v))]
    A.ck(sum(Q)==1);P=A.law(v);A.ck(min(P)>0);A.ck(min(Q)>0)
    ac=A.fw(g);rc=A.fw(v)
    for t,x in enumerate(rc):
        if t<len(ac) and ac[t]:A.ck(x==ac[t]-g[0]*eps)
        else:A.ck(abs(x)==eps)
    return v,Q,p,eps
def product_boundary(p0,p1,q0,q1):
    # Constant true terminal with a deliberately nonmatching full reference.
    terminalP=[F(1),F(0)]; terminalR=[F(1,3),F(2,3)]
    for p,q in [(p0,q0),(p1,q1)]:
        productP=[a*b for b in terminalP for a in p]
        productQ=[a*b for b in terminalR for a in q]
        A.ck(sum(productQ)==1)
        overlapzero(A.sub(A.ce(productP,productQ),plus(A.ce(p,q),A.ce(terminalP,terminalR))))
        # Neither reference-only terminal atom nor core mass is discarded.
        A.ck(sum(productQ[len(q):])==F(2,3))
def root_case(w,m,pilot=False):
    g=source(w);v,Q,p,delta=model(g,m);rootv=v;rootQ=Q
    Iroot=A.total(v); Croot=A.ce(A.law(v),Q);q=F(1,1<<(w-1))
    A.ck(Iroot==1+w*q+delta*(m-w-1))
    A.ck(4*Iroot-Croot[1]>F(395,256))
    # Independently check exact profile reconstruction and the original full theorem bounds.
    aa=A.fw(g);ProfileA=plus(*(A.scale(neglog(x*x),x) for x in aa if x))
    ProfileB=plus(*(neglog(x*x) for x in aa if x));c=A.ce(p,p)
    W=2*delta-len(p)*delta*delta
    formula=plus(c,A.scale(ProfileA,-2*delta),A.scale(ProfileB,delta*delta),
                 A.scale(neglog(1-W),1-W),(2*(w+2+m)*W,)*2)
    overlapzero(A.sub(formula,Croot));A.ck(Croot[1]<F(1005,256))
    gamma=(F(0),F(0));rho=F(1);siblings=[];spend=F(0);rows=[]
    for d in range(w+1):
        t=w-d; P=A.law(v); C=A.ce(P,Q)
        leavesBefore=plus(*(A.scale(cc,reach) for reach,_,cc in siblings),A.scale(C,rho))
        overlapzero(A.sub(plus(gamma,leavesBefore),Croot))
        remwide=sum(reach*ii for reach,ii,_ in siblings)+rho*A.total(v)
        A.ck(remwide>=F(63,64));A.ck(Iroot==spend+remwide)
        vv,qq=A.inherit(v,Q,t,True)
        pp=[A.law(x) for x in vv];cc=[A.ce(pp[b],qq[b]) for b in [0,1]]
        release=A.sub(C,A.scale(plus(*cc),F(1,2)))
        A.ck(release[1]>=0)
        gamma_after=plus(gamma,A.scale(release,rho));lam=rho/2
        canonicalv,canonicalQ,_,eps=model(source(t,1),m)
        A.ck(canonicalv==vv[0]); Ccan=A.ce(pp[0],canonicalQ)
        A.ck(Ccan[1]<4)
        if t>=4:A.ck(Ccan[1]<F(245,128))
        remain=sum(reach*ii for reach,ii,_ in siblings)+lam*(A.total(vv[0])+A.total(vv[1]))
        queryspend=spend+rho*A.inf(v,t)
        A.ck(Iroot==queryspend+remain)
        for eta in [F(0),F(1,4)]:
            fresh=[(1-eta)*x+eta/F(len(canonicalQ)) for x in canonicalQ]
            A.ck(sum(fresh)==1);A.ck(min(fresh)>0)
            Cnew=A.ce(pp[0],fresh); excess=A.scale(A.sub(Cnew,cc[0]),lam)
            total=plus(gamma_after,*(A.scale(cost,reach) for reach,_,cost in siblings),A.scale(plus(Cnew,cc[1]),lam))
            overlapzero(A.sub(total,plus(Croot,excess)))
            margin=(4*Iroot-total[1],4*Iroot-total[0])
            A.ck(lam*Cnew[1]<F(5,4));A.ck(margin[0]>F(75,256))
            if eta==0:A.ck(lam*Cnew[1]<1);A.ck(margin[0]>F(139,256))
            if t>=1:A.ck(len(set(vv[0]))==2);A.ck(len(set(vv[1]))==2)
            rows.append({'w':w,'m':m,'d':d,'remaining_wide':t,'eta':str(eta),'reach':str(lam),
                         'query_influence':str(A.inf(v,t)),'cumulative_actual_query_influence':str(queryspend),
                         'remaining_physical_I':str(remain),'root_unused_margin_interval':[str(4*Iroot-Croot[1]),str(4*Iroot-Croot[0])],
                         'signed_reset_excess_interval':[str(x) for x in excess],
                         'whole_paid_margin_interval':[str(x) for x in margin],
                         'positive_reset_excess':excess[0]>0,'negative_reset_excess':excess[1]<0,
                         'fresh_full_CE_interval':[str(x) for x in Cnew]})
            if w==4 and m==0 and d==0:product_boundary(pp[0],pp[1],fresh,qq[1])
        if d<w:
            vv,qq=A.inherit(v,Q,0,True); pp=[A.law(x) for x in vv]
            cc=[A.ce(pp[b],qq[b]) for b in [0,1]]
            release=A.sub(C,A.scale(plus(*cc),F(1,2)))
            gamma=plus(gamma,A.scale(release,rho));spend+=rho*A.inf(v,0)
            siblings.append((rho/2,A.total(vv[1]),cc[1]))
            v,Q=vv[0],qq[0];rho/=2
    return rows
mode=sys.argv[1];start=time.perf_counter()
domain=[(4,0)] if mode=='pilot' else [(4,0),(4,1),(5,0),(5,1),(6,0)]
rows=[]
for w,m in domain:rows+=root_case(w,m,mode=='pilot')
out={'status':'PASS','mode':mode,'root_cases':len(domain),'physical_prefix_query_cases':len(rows)//2,'reset_cases':len(rows),
     'positive_reset_cases':sum(r['positive_reset_excess'] for r in rows),
     'negative_reset_cases':sum(r['negative_reset_excess'] for r in rows),'assertions':A.checks,'seconds':time.perf_counter()-start,'rows':rows}
(RUN/'out'/f'{mode.upper()}_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
