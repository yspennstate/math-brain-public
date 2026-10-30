from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent/'20261012T044149Z-fleet05-A005-noncircular-endpoint-referee/code/check.py'
scope={'__name__':'arithmetic_reuse','__file__':str(BASE)}
exec(compile(BASE.read_text(),str(BASE),'exec'),scope)
add,scale,phi,L,fwht,entropy,influence,total,seed,evaluate,sign,const,physical_i=(scope[k] for k in ['add','scale','phi','L','fwht','entropy','influence','total','seed','evaluate','sign','const','physical_i'])
# Cached results are never mutated: add/scale construct fresh dictionaries.
scope['scope']['phi']=lru_cache(None)(scope['scope']['phi'])
phi=scope['scope']['phi']
scope['scope']['L']=lru_cache(None)(scope['scope']['L'])
L=scope['scope']['L']
def dummy_B(a,eta,n,N):
    al=Q(2,1<<N)
    return add(const(2*al*al*((1<<(N-1))-(1<<n))),*(L(u-eta*al,al) for u in a))
def core_B(a,eta,n,N,i):
    al=Q(2,1<<N)
    return add(const(2*al*al*((1<<(N-1))-(1<<(n-1)))),*(L(u-eta*al,a[s|(1<<i)]-eta*al) for s,u in enumerate(a) if not s>>i&1))
def edited_stats(f,N):
    n=(len(f)-1).bit_length();a=fwht(f);eta=f[0];al=Q(2,1<<N)
    H=add(*(phi((u-eta*al)**2) for u in a),scale(phi(al*al),(1<<N)-(1<<n)))
    I=total(a,n)+(N-n)*al+sum((al if f[0]==f[1<<i] else -al for i in range(n)),Q(0))
    return H,I
def run(mode):
    start=time.perf_counter(); assertions=0; cases=0
    def eq(a,b):
        nonlocal assertions
        assertions+=1
        assert a==b,(a,b)
    if mode in ['pilot','full']:
        nmax=2 if mode=='pilot' else 3
        for n in range(nmax+1):
            for b in range(1<<(1<<n)):
                f=seed(n,b);a=fwht(f);eta=f[0]
                for r in [2,3]:
                    assert time.perf_counter()-start<55,'In-loop frozen runtime guard'
                    N=n+r;al=Q(2,1<<N);cases+=1
                    v=[f[x&((1<<n)-1)] for x in range(1<<N)];v[0]*=-1
                    c=fwht(v)
                    for s,u in enumerate(c):
                        eq(u,(a[s] if s<(1<<n) else 0)-eta*al)
                        eq(u!=0,True)
                    eq(sum((u*u for u in c),Q(0)),1)
                    grouped=add(*(phi((u-eta*al)**2) for u in a),scale(phi(al*al),(1<<N)-(1<<n)))
                    eq(entropy(c),grouped)
                    for i in range(N):
                        di=influence(c,i);eq(di,physical_i(v,N,i))
                        eq(di,al if i>=n else influence(a,i)+(al if f[0]==f[1<<i] else -al))
                        eq(scope['scope']['erasure'](c,i),dummy_B(a,eta,n,N) if i>=n else core_B(a,eta,n,N,i))
        result={'mode':mode,'cases':cases,'assertions':assertions,'failures':0,'max_dimension':nmax+3}
    elif mode=='witness':
        n=3;N=12;al=Q(1,2048);f=seed(3,254);eta=f[0];a=fwht(f)
        eq(eta,-1);eq(a[0],Q(3,4));eq(set(a[1:]),{Q(-1,4)})
        c=[u-eta*al for u in a];dc=Q(511,2048);dd=al
        eq(sum((u*u for u in c),Q(0))+((1<<N)-(1<<n))*al*al,1)
        eq(all(u!=0 for u in c) and al!=0,True)
        eq(3*dc+9*dd,Q(771,1024))
        eq(dc<Q(1,4) and dd<Q(1,4),True)
        bs=scope['scope']['erasure'](a,0);bo=core_B(a,eta,n,N,0);bd=dummy_B(a,eta,n,N)
        for i in [1,2]:eq(core_B(a,eta,n,N,i),bo)
        eq(sign(add(bs,const(-Q(5,2)*Q(1,4)))),1)
        eq(sign(add(bo,const(-Q(5,2)*dc))),1)
        eq(sign(add(bd,const(-Q(5,2)*dd))),-1)
        H=add(*(phi(u*u) for u in c),scale(phi(al*al),(1<<N)-(1<<n)))
        C=Q(8,3);delta=add(H,const(-C*Q(771,1024)))
        eq(sign(delta),1)
        # Physical children: clean child is padded seed; edited child has one fewer bit.
        dh,di=edited_stats(f,N-1)
        ds=add(const(C*(total(a,n)+di)/2),scale(add(entropy(a),dh),-Q(1,2)))
        cs=[];child_signs=[]
        for i in range(n):
            clean=scope['restricted'](f,n,i,1);edit=scope['restricted'](f,n,i,0)
            ch=entropy(fwht(clean));ci=total(fwht(clean),n-1)
            eh,ei=edited_stats(edit,N-1)
            slack=add(const(C*(ci+ei)/2),scale(add(ch,eh),-Q(1,2)))
            cs.append(slack)
            child_signs.append([sign(add(const(C*ci),scale(ch,-1))),sign(add(const(C*ei),scale(eh,-1)))])
            eq(sign(slack),1)
        eq(sign(ds),-1)
        for s in cs[1:]:eq(s,cs[0])
        decrement=add(H,scale(add(entropy(a),dh),-Q(1,2)))
        eq(add(delta,ds,const(C*dd)),decrement)
        result={'mode':mode,'cases':1,'assertions':assertions,'failures':0,'dimension':N,'nonzero_coefficient_count':1<<N,
                'I':'771/1024','original_influences':'511/2048','dummy_influences':'1/2048',
                'seed_ratio_interval':[str(x) for x in evaluate(scale(bs,4))],
                'original_ratio_interval':[str(x) for x in evaluate(scale(bo,1/dc))],
                'dummy_ratio_interval':[str(x) for x in evaluate(scale(bd,1/dd))],
                'HI_interval':[str(x) for x in evaluate(scale(H,Q(1024,771)))],
                'C':'8/3','root_delta_interval':[str(x) for x in evaluate(delta)],
                'original_average_child_slack_interval':[str(x) for x in evaluate(cs[0])],
                'dummy_average_child_slack_interval':[str(x) for x in evaluate(ds)],
                'original_individual_child_slack_signs':child_signs,
                'dummy_individual_child_slack_signs':[sign(add(const(C*total(a,n)),scale(entropy(a),-1))),sign(add(const(C*di),scale(dh,-1)))],
                'dummy_entropy_decrement_per_influence_interval':[str(x) for x in evaluate(scale(decrement,1/dd))],
                'compressed_coefficient_classes':[[str(c[0]),1],[str(c[1]),7],[str(al),4088]],
                'entropy_logprime_vector':{str(k):str(v) for k,v in H.items()},
                'original_B_logprime_vector':{str(k):str(v) for k,v in bo.items()},
                'dummy_B_logprime_vector':{str(k):str(v) for k,v in bd.items()}}
    else:raise ValueError(mode)
    result['elapsed_seconds']=time.perf_counter()-start
    assert result['elapsed_seconds']<60,'Frozen runtime exceeded'
    (ROOT/'out'/f'{mode.upper()}_VALIDATION.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':run(sys.argv[1])
