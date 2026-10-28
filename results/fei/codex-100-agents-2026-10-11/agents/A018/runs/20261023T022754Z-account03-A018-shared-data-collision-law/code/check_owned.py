from check_radial import *
def influence(tt):
    n=(len(tt)).bit_length()-1;N=len(tt)
    return F(sum(tt[x]!=tt[x^(1<<i)] for x in range(N) for i in range(n)),N)
def run():
    start=time.perf_counter();cases=[];ss=c.walsh((-1,1,1,1));Qs=c.probs(ss)
    ck(145**4<2*128**4);ck(72**65>2**7*65**65);ck(290**8<2*273**8)
    for k in range(1,6):
        eps=F(1,2**k);N=2**(k+1)
        plus=tuple(1 if x//2==0 else 1-2*(x%2) for x in range(N))
        minus=tuple(-1 if x//2==0 else 1-2*(x%2) for x in range(N))
        char=tuple(1-2*(x%2) for x in range(N))
        for name,t0,t1 in [('opposite',plus,minus),('one-balanced',char,plus)]:
            a0,a1=c.walsh(t0),c.walsh(t1);P0,P1=c.probs(a0),c.probs(a1)
            Q0,Q1=c.refs(P0)[1],c.refs(P1)[1];ah,Qh=c.lift(a0,a1,Q0,Q1)
            r=(a0[0]**2+a1[0]**2)/2;beta=(a0[0]+a1[0])/2;nu=beta*beta/r
            ck(nu==(0 if name=='opposite' else F(1,2)))
            dc=add(sc(F(1,2),add(c.kl(P0,Q0),c.kl(P1,Q1))),sc(-1,c.kl(c.probs(ah),Qh)))
            E=Dempty(a0[0],a1[0],Q0,Q1)
            C,D=c.activation(ah,Qh,ss,Qs);C0,D0=c.activation(a0,Q0,ss,Qs);C1,D1=c.activation(a1,Q1,ss,Qs)
            L=add(sc(F(1,2),add(D0,D1)),sc(-1,D),sc(-F(1,2),dc))
            z=Qs[0]*(Q0[0]+Q1[0])/2;p=ss[0]**2*r;G=add(c.refund(p,z),sc(-1,c.refund(nu*p,nu*z)))
            bound=sc(F(1,2),lg((1+z)/(1+nu*z)));ck(nonneg(add(bound,sc(-1,L))))
            I0,I1=influence(t0),influence(t1);ck(I0==sum(F(j.bit_count())*v for j,v in enumerate(P0)));ck(I1==sum(F(j.bit_count())*v for j,v in enumerate(P1)))
            bank=add(sc(2*(I0+I1)/2,lg(F(2))),sc(-F(1,4),add(c.ce(P0,Q0),c.ce(P1,Q1))))
            # bank=average(4I-c)/2, with original supplied references.
            spent=L if c.interval(L)[0]>0 else {}
            remain=add(bank,sc(-F(1,8),lg(F(2))),sc(-1,spent))
            if k>=2:
                ck(nonneg(add(sc(F(1,8) if name=='opposite' else F(1,16),lg(F(2))),sc(-1,bound))))
                floor=F(1,4) if name=='opposite' else F(13,16)
                ck(c.interval(add(remain,sc(-floor,lg(F(2)))))[0]>0)
                if name=='one-balanced':
                    # Complete physical rate4 query excess, including core entropy and profile.
                    T=add(C,sc(-F(1,2),add(C0,C1)),sc(-eps,lg(F(2))))
                    ck(c.interval(add(sc(F(1,4),lg(F(2))),sc(-1,T)))[0]>0)
                    used=T if c.interval(T)[0]>0 else {}
                    full_remaining=add(bank,sc(-F(1,8),lg(F(2))),sc(-1,used))
                    ck(c.interval(add(full_remaining,sc(-F(5,8),lg(F(2)))))[0]>0)
            if name=='one-balanced' and k==1:ck(c.interval(L)[1]<0)
            if name=='opposite':ck(dc=={});ck(c.interval(L)[0]>0)
            if k<=3:
                th=tuple(v for pair in zip(t0,t1) for v in pair)
                tf=tuple(v for s in (-1,1,1,1) for h in th for v in (1,h*s))
                af=c.walsh(tf)
                ck(c.ent(c.probs(af))==add(sc(F(1,2),add(c.ent(c.probs(ah)),c.ent(Qs))),c.psi(beta*ss[0])))
            cases.append({'k':k,'family':name,'nu':str(nu),'bank':{str(p):str(v) for p,v in bank.items()},'remaining':{str(p):str(v) for p,v in remain.items()},'Lambda_sign':'positive' if c.interval(L)[0]>0 else 'negative','complete_rate4_excess_paid_from_same_bank':name=='one-balanced' and k>=2})
        if time.perf_counter()-start>175:raise RuntimeError('Frozen owned-review deadline')
    result={'status':'PASS','cases':len(cases),'assertions':c.checks,'seconds':time.perf_counter()-start,'details':cases,'strict_integer_certificates':['145^4<2*128^4','72^65>2^7*65^65','290^8<2*273^8']}
    (ROOT/'out/OWNED_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in result.items() if k!='details'}))
if __name__=='__main__':run()
