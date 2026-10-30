from check_radial import *
start=time.perf_counter();count=0
for tt0,tt1 in [((1,1),(1,-1)),((1,1),(-1,-1)),((1,-1),(-1,1)),((1,1),(1,1))]:
    a0,a1=c.walsh(tt0),c.walsh(tt1)
    for Q0 in bernref(c.probs(a0)):
        for Q1 in bernref(c.probs(a1)):
            ah,Qh=c.lift(a0,a1,Q0,Q1);beta=(a0[0]+a1[0])/2;r=(a0[0]**2+a1[0]**2)/2;nu=beta*beta/r if r else F(1)
            dc=add(sc(F(1,2),add(c.kl(c.probs(a0),Q0),c.kl(c.probs(a1),Q1))),sc(-1,c.kl(c.probs(ah),Qh)));E=Dempty(a0[0],a1[0],Q0,Q1)
            for ts,kind in [((1,),0),((-1,),0),((1,-1),0),((1,-1),1)]:
                ss=c.walsh(ts);Qs=c.probs(ss) if kind==0 else c.refs(c.probs(ss))[2]
                C,D=c.activation(ah,Qh,ss,Qs);_,D0=c.activation(a0,Q0,ss,Qs);_,D1=c.activation(a1,Q1,ss,Qs)
                m=ss[0]**2;t=Qs[0];p=m*r;z=t*(Q0[0]+Q1[0])/2
                L=add(sc(F(1,2),add(D0,D1)),sc(-1,D),sc(-F(1,2),dc));G=add(c.refund(p,z),sc(-1,c.refund(nu*p,nu*z)))
                K=Kplus((m*a0[0]**2,m*a1[0]**2),(t*Q0[0],t*Q1[0]))
                ck(L==add(G,sc(-F(1,2),add(dc,sc(-m,E),K))))
                ck(nonneg(K));ck(nonneg(G));ck(nonneg(add(G,sc(-1,L))))
                if p<=z:ck(nonneg(add(sc(F(1,2),lg((1+z)/(1+nu*z))),sc(-1,G))))
                count+=1
result={'status':'PASS','cases':count,'assertions':c.checks,'seconds':time.perf_counter()-start,'scope':'Actual Boolean m0/t0/p0/nu0/nu1/constant-mask boundary cases'}
(ROOT/'out/BOUNDARIES.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
