from pathlib import Path
import sys,time,json
P=Path(__file__).resolve();A={'__name__':'reuse','__file__':str(P.with_name('check.py'))}
exec(compile(P.with_name('check.py').read_text(),str(P.with_name('check.py')),'exec'),A)
Q=A['Q'];add=A['add'];scale=A['scale'];const=A['const'];sign=A['sign'];entropy=A['entropy'];fwht=A['fwht'];total=A['total'];influence=A['influence'];ROOT=P.parents[1]
erasure=A['A']['scope']['scope']['erasure'];packet_js=A['A']['scope']['packet_js']
def maximum(a,b):return a if sign(add(a,scale(b,-1)))>=0 else b
def minimum(v):
    r=v[0]
    for x in v[1:]:r=r if sign(add(r,scale(x,-1)))<=0 else x
    return r
def run(mode):
    start=time.perf_counter();checks=cases=0;transitions=[]
    def eq(a,b):
        nonlocal checks
        checks+=1;assert a==b,(a,b)
    domains=[(n,b,t,C) for n in ([1] if mode=='pilot' else [1,2]) for b in range(1<<(1<<n)) for t in ([1,2] if mode=='pilot' else [1,2,3]) for C in [Q(0),Q(1),Q(8,3),Q(4)]]
    if mode=='full':domains.extend((3,254,t,Q(8,3)) for t in [1,2,3])
    for n,b,t,C in domains:
        assert time.perf_counter()-start<50
        cases+=1;f=A['seed'](n,b);a=fwht(f);v=A['tensor'](f,t);c=fwht(v);N=n*t
        delta=add(entropy(a),const(-C*total(a,n)));rootdelta=add(entropy(c),const(-C*total(c,N)))
        eq(rootdelta,scale(delta,t));corrected=[];predicted=[];slacks=[]
        for i in range(N):
            children=[fwht(A['restrict'](v,N,[i],z)) for z in [0,1]]
            sigma=add(const(C*sum((total(ch,N-1) for ch in children),Q(0))/2),scale(add(*(entropy(ch) for ch in children)),-Q(1,2)))
            seedchildren=[fwht(A['restrict'](f,n,[i%n],z)) for z in [0,1]]
            seedsigma=add(const(C*sum((total(ch,n-1) for ch in seedchildren),Q(0))/2),scale(add(*(entropy(ch) for ch in seedchildren)),-Q(1,2)))
            eq(sigma,add(seedsigma,scale(delta,-(t-1))))
            d=influence(c,i);eq(d,influence(a,i%n));eq(erasure(c,i),erasure(a,i%n));eq(packet_js(c,i),packet_js(a,i%n))
            if not d:continue
            q=scale(add(erasure(c,i),maximum(scale(sigma,-1),{})),1/d)
            pred=maximum(scale(erasure(a,i%n),1/d),add(const(C),scale(add(scale(delta,t),scale(packet_js(a,i%n),-1)),1/d)))
            eq(q,pred);corrected.append(q);predicted.append(pred);slacks.append(sign(sigma))
        if corrected:eq(minimum(corrected),minimum(predicted))
        if n==3:
            transitions.append({'t':t,'all_average_children_certified':all(s>=0 for s in slacks),'Q_interval':[str(x) for x in A['evaluate'](minimum(corrected))]})
    elapsed=time.perf_counter()-start;assert elapsed<55
    result={'mode':mode,'cases':cases,'assertions':checks,'failures':0,'elapsed_seconds':elapsed,'point_seed_transitions':transitions,'source_claim':'A002-SIGNED-PRICE-SAME-C-COMPLETENESS@1'}
    (ROOT/'out'/f'REVIEW_{mode.upper()}.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':run(sys.argv[1])
