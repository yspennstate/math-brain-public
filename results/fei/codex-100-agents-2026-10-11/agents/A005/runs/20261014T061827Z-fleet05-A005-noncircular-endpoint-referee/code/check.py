from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import combinations
import json,sys,time
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent/'20261014T001325Z-fleet05-A005-noncircular-endpoint-referee/code/check.py'
reuse={'__name__':'reuse','__file__':str(BASE)}
exec(compile(BASE.read_text(),str(BASE),'exec'),reuse)
add,scale,phi,fwht,influence,total,seed,evaluate,sign,const,physical_i=(reuse[k] for k in ['add','scale','phi','fwht','influence','total','seed','evaluate','sign','const','physical_i'])
def H(a):
    return add(*(scale(phi(p),m) for p,m in Counter(u*u for u in a).items()))
def restrict(v,n,coords,b):
    kept=[i for i in range(n) if i not in coords]
    fixed=sum(((b>>j)&1)<<i for j,i in enumerate(coords))
    return [v[fixed+sum(((x>>j)&1)<<i for j,i in enumerate(kept))] for x in range(1<<len(kept))]
def stats(v,n):
    a=fwht(v)
    return {'a':a,'H':H(a),'I':total(a,n),'d':[influence(a,i) for i in range(n)]}
def block(v,n,coords,s):
    a=s['a']; children=[stats(restrict(v,n,coords,b),n-len(coords)) for b in range(1<<len(coords))]
    EH=scale(add(*(c['H'] for c in children)),Q(1,len(children)))
    EI=sum((c['I'] for c in children),Q(0))/len(children)
    rows=Counter()
    for x in range(1<<n):
        if any(x>>i&1 for i in coords):continue
        row=tuple(a[x|sum(((b>>j)&1)<<i for j,i in enumerate(coords))]**2 for b in range(1<<len(coords)))
        rows[row]+=1
    B={}
    beta=Q(0)
    for row,m in rows.items():
        B=add(B,scale(add(*(phi(p) for p in row),scale(phi(sum(row)), -1)),m))
        if len(coords)==1:beta+=m*min(row)
    return {'children':children,'L':add(s['H'],scale(EH,-1)),'IA':s['I']-EI,'B':B,'J':add(s['H'],scale(EH,-1),scale(B,-1)),'beta':beta,'rows':rows,'EH':EH,'EI':EI}
def referenceKL(b,rho):
    ans={};m=(len(next(iter(b['rows'])))-1).bit_length()
    for row,multiplicity in b['rows'].items():
        q=sum(row)
        if not q:continue
        for x,p in enumerate(row):
            if not p:continue
            ref=rho**x.bit_count()*(1-rho)**(m-x.bit_count())
            ans=add(ans,scale(phi(ref),multiplicity*p/ref))
    return add(ans,scale(b['B'],-1))
def minorityKL(b,rho):
    ans={}
    for row,m in b['rows'].items():
        x,y=sorted(row)
        ans=add(ans,scale(phi(rho),m*x/rho),scale(phi(1-rho),m*y/(1-rho)))
    return add(ans,scale(b['B'],-1))
def interval(x):return [str(z) for z in evaluate(x)]
def run(mode):
    started=time.perf_counter();checks=0;roots=singles=pairs=0
    def eq(a,b):
        nonlocal checks
        checks+=1
        assert a==b,(a,b)
    def positive(a,strict=False):eq(sign(a)>=int(strict),True)
    if mode in ('pilot','full'):
        for n in range((2 if mode=='pilot' else 3)+1):
            for truth in range(1<<(1<<n)):
                assert time.perf_counter()-started<55,'Frozen runtime guard'
                v=seed(n,truth);s=stats(v,n);roots+=1
                eq(sum((u*u for u in s['a']),Q(0)),1)
                bs=[block(v,n,(i,),s) for i in range(n)]
                for i,b in enumerate(bs):
                    singles+=1;eq(b['IA'],s['d'][i]);eq(b['IA'],physical_i(v,n,i))
                    positive(b['L']);positive(add(const(2),scale(b['L'],-1)))
                    for K in (4,8):
                        lam=3;rho=Q(1,1+(1<<(K-lam)));r=scale(phi(1-rho),1/(1-rho))
                        D=add(s['H'],const(-K*s['I']));S=add(scale(b['EH'],-1),const(K*b['EI']))
                        O=b['IA']-b['beta'];La=minorityKL(b,rho);Ac=add(const(lam*b['beta']),scale(b['J'],-1))
                        eq(add(D,S,const(K*O),La,Ac),r)
                        positive(La);positive(Ac)
                for i,j in combinations(range(n),2):
                    pairs+=1;b=block(v,n,(i,j),s);bi,bj=bs[i],bs[j]
                    eq(b['IA'],s['d'][i]+s['d'][j])
                    Z=add(b['B'],scale(bi['B'],-1),scale(bj['B'],-1))
                    Om=add(b['L'],scale(bi['L'],-1),scale(bj['L'],-1))
                    eq(Om,add(Z,b['J'],scale(bi['J'],-1),scale(bj['J'],-1)))
                    positive(Z);positive(add(const(2),Om));positive(add(const(2),scale(Om,-1)))
                    for K in (4,8):
                        lam=3;rho=Q(1,1+(1<<(K-lam)));r=scale(phi(1-rho),1/(1-rho))
                        G=referenceKL(b,rho);Di=add(s['H'],const(-K*s['I']))
                        Si=add(scale(bi['EH'],-1),const(K*bi['EI']));Sj=add(scale(bj['EH'],-1),const(K*bj['EI']))
                        Sp=add(scale(b['EH'],-1),const(K*b['EI']))
                        eq(add(minorityKL(bi,rho),minorityKL(bj,rho),const((K-lam)*(bi['IA']-bi['beta']+bj['IA']-bj['beta']))),add(G,Z))
                        eq(add(Di,Sp,G,const(lam*b['IA']),scale(b['J'],-1)),scale(r,2))
                        eq(add(G,const(lam*b['IA']),scale(b['J'],-1),scale(r,-2)),add(const(K*b['IA']),scale(b['L'],-1)))
                        eq(add(Sp,scale(Si,-1),scale(Sj,-1),scale(Di,-1)),Om)
                        positive(G);positive(add(const(lam*b['IA']),scale(b['J'],-1)))
        sharp=[]
        for v,n,want in [(seed(2,14),2,-2),([(-1)**(((x&1)^((x>>1)&1))*((x>>2)&1)) for x in range(8)],3,2)]:
            s=stats(v,n);bi=block(v,n,(0,),s);bj=block(v,n,(1,),s);bp=block(v,n,(0,1),s)
            Om=add(bp['L'],scale(bi['L'],-1),scale(bj['L'],-1));eq(Om,const(want));eq(s['H'],const(2))
            sharp.append({'n':n,'Omega':want,'I':str(s['I']),'L_pair':interval(bp['L'])})
        result={'mode':mode,'roots':roots,'singleton_cuts':singles,'pair_cuts':pairs,'K':[4,8],'lambda':3,'sharp_witnesses':sharp}
    elif mode=='fixture':
        seedv=seed(3,254);base=[]
        for x in range(1<<12):
            core=seedv[x&7]*seedv[(x>>3)&7]*(-1 if ((x>>6)&3)==0 else 1)*(-1 if x>>8&1 else 1)
            base.append(core if ((x>>9)&7)==0 else 1)
        edited=[base[x&4095] for x in range(1<<14)];edited[1<<9]*=-1
        results=[]
        for label,v,n in [('activated',base,12),('prime_point_edit',edited,14)]:
            assert time.perf_counter()-started<55,'Frozen runtime guard'
            s=stats(v,n);b=block(v,n,(6,7),s);rho=Q(1,2);G=referenceKL(b,rho)
            D=add(s['H'],const(-3*s['I']));S=add(scale(b['EH'],-1),const(3*b['EI']))
            surplus=add(G,const(3*b['IA']),scale(b['J'],-1),const(-2))
            childDs=[add(c['H'],const(-3*c['I'])) for c in b['children']]
            eq(sum((u*u for u in s['a']),Q(0)),1);eq(b['IA'],s['d'][6]+s['d'][7]);positive(D,True);positive(surplus,True)
            eq(sign(S),-1);eq(max(s['d'])<Q(1,4),True)
            for cD in childDs:positive(cD,True)
            eq(surplus,add(const(3*b['IA']),scale(b['L'],-1)));eq(add(D,S,G,const(3*b['IA']),scale(b['J'],-1)),const(2))
            if label=='activated':
                eq(b['IA'],Q(1,8));eq(b['L'],const(Q(1,4)));eq(b['J'],{})
            else:
                eq(all(u!=0 for u in s['a']),True);eq(sum(z==-1 for z in v)%2,1)
                for i in range(n):eq(s['d'][i],physical_i(v,n,i))
            results.append({'label':label,'n':n,'K':3,'lambda':3,'rho':'1/2','r':1,'I':str(s['I']),'mean':str(s['a'][0]),'max_influence':str(max(s['d'])),'negative_count':sum(z==-1 for z in v),'nonzero_fourier':sum(u!=0 for u in s['a']),'root_deficit':interval(D),'pair_influence':str(b['IA']),'pair_rate':interval(scale(b['L'],1/b['IA'])),'Gibbs_surplus':interval(surplus),'child_deficits':[interval(c) for c in childDs],'actual_child_reserve':interval(S)})
        result={'mode':mode,'roots':2,'results':results}
    else:raise ValueError(mode)
    result.update(assertions=checks,failures=0,seconds=time.perf_counter()-started,arithmetic='exact rational Walsh; prime-log symbolic equality; outward 48-bit atanh log intervals')
    (ROOT/'out'/f'{mode}.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':run(sys.argv[1])
