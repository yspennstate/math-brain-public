from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import time,json,sys
from arithmetic import fw,influences,tables,ent,ce,kl,add,reference,lograt
RUN=Path(__file__).resolve().parents[1];COUNT=0;START=time.perf_counter();MODE=sys.argv[1]
def check(v):
    global COUNT
    assert v;COUNT+=1
def checkpoint(obj):
    obj.update(assertions=COUNT,elapsed_seconds=time.perf_counter()-START)
    (RUN/'out'/f'{MODE.upper()}_CHECKPOINT.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    if obj['elapsed_seconds']>=55:raise RuntimeError('Frozen internal cutoff; completed checkpoint saved')
GRID=2**100
def floorq(q):return F(q.numerator*GRID//q.denominator,GRID)
def ceilq(q):return -floorq(-q)
@lru_cache(None)
def lnq(q):
    q=F(q);assert q>0
    if q==1:return F(0),F(0)
    e=q.numerator.bit_length()-q.denominator.bit_length()
    x=q/F(2)**e
    if x<1:e-=1;x*=2
    assert 1<=x<2
    z=(x-1)/(x+1);s=sum((2*z**(2*j+1)/F(2*j+1) for j in range(36)),F(0));rem=2*z**73/(73*(1-z*z))
    if e:
        l,u=lnq(F(2))
        s0=s+(e*l if e>=0 else e*u);s1=s+rem+(e*u if e>=0 else e*l)
    else:s0,s1=s,s+rem
    return floorq(s0),ceilq(s1)
# Separate base case avoids binary range reduction recursively calling itself.
z=F(1,3);ss=sum((2*z**(2*j+1)/F(2*j+1) for j in range(36)),F(0));rr=2*z**73/(73*(1-z*z))
lnq.cache_clear()
LN2=(floorq(ss),ceilq(ss+rr))
lnq_raw=lnq
def lnq(q):return LN2 if F(q)==2 else lnq_raw(F(q))
def mul(interval,a):return (interval[0]*a,interval[1]*a) if a>=0 else (interval[1]*a,interval[0]*a)
def plus(*ivs):return sum((x[0] for x in ivs),F(0)),sum((x[1] for x in ivs),F(0))
def divpositive(a,b):
    assert b[0]>0
    combos=[a[i]/b[j] for i in [0,1] for j in [0,1]];return min(combos),max(combos)
def L(q):
    if not q:return F(0),F(0)
    return divpositive(mul(lnq(q),-q),LN2)
def prime_interval(v):return divpositive(plus(*(mul(lnq(p),a) for p,a in v.items())),LN2)
def bounds_str(iv):return [str(x) for x in iv]
def base_values(k,m):
    return [(-1)**sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(k//2)) for x in range(1<<(k+m))]
def structural(k,m):
    n=k+m;d=F(1,2**n);e=F(1,2**(k//2));N=2**k;pluscount=(N+2**(k//2))//2
    hh=plus(mul(L((e-2*d)**2),pluscount),mul(L((e+2*d)**2),N-pluscount),mul(L(4*d*d),2**n-N))
    hm=plus(mul(L((e-d)**2),pluscount),mul(L((e+d)**2),N-pluscount),mul(L(d*d),2**(n+1)-N))
    massh=pluscount*(e-2*d)**2+(N-pluscount)*(e+2*d)**2+(2**n-N)*4*d*d
    massm=pluscount*(e-d)**2+(N-pluscount)*(e+d)**2+(2**(n+1)-N)*d*d
    check(massh==massm==1)
    return hh,hm
def compressed():
    rows=[]
    h4,hM4=structural(4,0);C=mul(hM4,F(16,29));check(C[0]>F(34,15));check(C[0]>F(17,8));check(C[1]<F(37,16))
    _,hM5=structural(4,1);ratio5=mul(hM5,F(16,31));check(ratio5[1]<F(34,15));check(ratio5[1]<C[0])
    for k in [4,6,8,10,12]:
        for m in range(25):
            n=k+m;d=F(1,2**n);hh,hm=structural(k,m);I0=F(k,2)+(n+1)*d;Iw=I0-2*k*d
            check(hm[1]<F(17,8)*I0-F(1,64))
            # The entropy sector estimate as an outward interval sign.
            cap=F(k+2,2**k)+F(1,2**k)/LN2[1]
            check(hh[1]-k<=cap)
            if n==4:check(hm[0]==C[0]*Iw and hm[1]==C[1]*Iw)
            else:check(hm[1]<C[0]*Iw)
            if n>=6:check(hm[1]/Iw<F(34,15))
            rows.append({'k':k,'m':m,'I_zero':str(I0),'I_all_pivotal':str(Iw),'entropy_M_interval':bounds_str(hm),'price17over8_margin_interval':bounds_str((F(17,8)*I0-hm[1],F(17,8)*I0-hm[0]))})
            checkpoint({'status':'COMPLETED_PREFIX','cases':len(rows)})
    _,hm22=structural(4,18);d=F(1,2**22);I=2+23*d;lower=d*(44-42-88*F(1,2**18))
    check(lower==F(65525,137438953472));check(hm22[0]-2*I>=lower)
    exactH=add({2:F(8)},add({3:F(180,256)},{5:F(300,256)}),F(-1))
    check(prime_interval(exactH)[0]<=hM4[1] and prime_interval(exactH)[1]>=hM4[0])
    witness={'actual_family':'k4,m0,flip active vertex 1111; fresh selector','dimension':5,'incident_original_pivotal_edges':4,'I_G':'2','I_H':'3/2','I_M':'29/16','H_M_prime_log':{str(p):str(a) for p,a in exactH.items()},'H_M_interval':bounds_str(hM4),'H_minus_17over8_I_lower':str(hM4[0]-F(17,8)*F(29,16)),'sharp_all_vertex_constant_expression':'(16/29)*(8-(180 log2 3+300 log2 5)/256)','sharp_constant_interval':bounds_str(C),'n5_worst_ratio_interval':bounds_str(ratio5),'large_domain_upper':'34/15','price2_padded_n22_lower':str(lower)}
    check(F(witness['H_minus_17over8_I_lower'])>0)
    (RUN/'out/SHARP_VERTEX_CERTIFICATE.json').write_text(json.dumps(witness,indent=2)+'\n',encoding='utf-8')
    return {'cases':len(rows),'compressed_rows':rows,'sharp_constant_interval':bounds_str(C)}
def vertices():
    cases=0;types=[]
    for k in [4,6]:
        for m in [0,1,2]:
            n=k+m;d=F(1,2**n);g=base_values(k,m);ag=fw(g);ig=influences(g)
            zero=g.copy();zero[0]*=-1;reference_h_multiset=sorted(x*x for x in fw(zero).values());reference_m_multiset=sorted(x*x for x in fw(g+zero).values())
            for a in range(1<<n):
                h=g.copy();h[a]*=-1;ah=fw(h);w=(a&((1<<k)-1)).bit_count()
                ih=influences(h);actual=g+h;am=fw(actual);im=influences(actual)
                check(sum(ig)==F(k,2));check(sum(ih)==F(k,2)+2*d*(n-2*w));check(sum(im)==F(k,2)+d*(n+1-2*w));check(im[n]==d)
                for j in range(n):
                    was_pivotal=g[a]!=g[a^(1<<j)]
                    check(ih[j]-ig[j]==2*d*(1-2*int(was_pivotal)))
                for t,x in ag.items():
                    shift=g[a]*d*(-1 if (t&a).bit_count()%2 else 1)
                    check(ah[t]==x-2*shift);check(am[t]==x-shift);check(am[t|(1<<n)]==shift)
                check(sorted(x*x for x in ah.values())==reference_h_multiset);check(sorted(x*x for x in am.values())==reference_m_multiset)
                cases+=1
            types.append({'k':k,'m':m,'all_vertices':1<<n})
            checkpoint({'status':'COMPLETED_PREFIX','actual_vertices':cases,'domains_completed':types})
    return {'actual_vertices':cases,'domains_completed':types,'symmetry_quotient':False}
def product(p,q,n):return {a|(b<<n):x*y for a,x in p.items() for b,y in q.items()}
def composition():
    cases=refcases=actcases=0
    for m in [0,1]:
        k=4;n=k+m;g=base_values(k,m);h=g.copy();h[15]*=-1;base=g+h;nb=n+1
        pb={t:x*x for t,x in fw(base).items()};ib=sum(influences(base))
        for q in tables(2):
            pq={t:x*x for t,x in fw(q).items()};iq=sum(influences(q));data=[a*b for a in q for b in base];ng=nb+2
            coeff=fw(data);pd={t:x*x for t,x in coeff.items()};mu=coeff[0]
            check(pd==product(pb,pq,nb));check(sum(influences(data))==ib+iq)
            hg=ent(pd);hb=ent(pb);hq=ent(pq);check(add(hg,add(hb,hq),F(-1))=={})
            # Each activation truth spectrum and influence computed once per physical root.
            activations={}
            for r in [1,2]:
                p=F(1,2**r);vals=[]
                for ctrl in range(1<<r):vals.extend(data if ctrl==0 else [1]*len(data))
                out={t:x*x for t,x in fw(vals).items()};I=sum(influences(vals))
                check(I==p*(ib+iq+r*(1-mu)));activations[r]=out
            for variant in range(3):
                rq=reference(pq,variant);rd=product(pb,rq,nb)
                check(sum(rd.values())==1);check(add(ce(pd,rd),add(ce(pq,rq),hb),F(-1))=={})
                check(kl(pd,rd)==kl(pq,rq));refcases+=1
                v=1-pd[0];den=1-rd[0];cal={t:(pd[0] if t==0 else rd[t]*v/den) for t in pd}
                catp={0:pd[0],1:v};catr={0:rd[0],1:den}
                debt=add(kl(pq,rq),kl(catp,catr),F(-1));check(kl(pd,cal)==debt)
                for r,out in activations.items():
                    p=F(1,2**r);Q={}
                    for t in range(1<<ng):
                        for u in range(1<<r):
                            a=t|(u<<ng)
                            if t:Q[a]=p*p*cal[t];check(out[a]==p*p*pd[t])
                            elif u:Q[a]=p*p*(1-mu)**2;check(out[a]==Q[a])
                            else:Q[a]=(1-p*(1-mu))**2;check(out[a]==Q[a])
                    check(sum(Q.values())==1);check(add(kl(out,Q),debt,-p)=={})
                    check(add(add(ce(out,Q),ent(out),F(-1)),debt,-p)=={})
                    actcases+=1
            cases+=1;checkpoint({'status':'COMPLETED_PREFIX','tensors':cases,'tensor_reference_cases':refcases,'activation_reference_cases':actcases})
    return {'tensors':cases,'tensor_reference_cases':refcases,'activation_reference_cases':actcases}
result={'compressed':compressed,'vertices':vertices,'composition':composition}[MODE]()
result.update(status='PASS',assertions=COUNT,runtime_seconds=time.perf_counter()-START,mode=MODE,arithmetic='exact fractions and prime-log identities; outward rational intervals; actual physical edges')
(RUN/'out'/f'{MODE.upper()}_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['compressed_rows']}))
