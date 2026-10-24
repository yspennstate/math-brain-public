import audit as a
import exact as e
from exact import Q,check,add,logform,entropy,nonnegative
from pathlib import Path
import itertools,json,time,sys
R=Path(__file__).resolve().parents[1];START=time.perf_counter();LATE=0;ORIGINAL=a.local
def local(c,us,ids,kind,i):
    global LATE
    out=ORIGINAL(c,us,ids,kind,i)
    if kind=='c' and i==3 and 0 not in ids:
        qs,U,RR=a.pots(c,us);aa=qs[0]
        if aa==1:check(out[3],Q(0));return out
        q=qs[1]/(1-aa);mu=a.mean(us[0]);nu=a.mean(us[1]);b=1-nu;d=(1-aa)*q*b
        check(out[3],d);check(out[2],add((qs[1]*(1-nu*nu),logform(Q(2)))))
        P=a.spec(a.table(c,us))[1];ix=ids.index(i);fold=[Q(0)]*(len(P)//2)
        for s,v in enumerate(P):fold[e.compressed(s,[j for j in range(a.dim(a.table(c,us))) if j!=ix])]+=v
        B=add((1,entropy(P)),(-1,entropy(tuple(fold))))
        ex=add(((q-2*q*q)*b*b*(1-aa),logform(Q(2))),(aa*(1-aa),a.phi((mu-1+q*b)**2,(q*b)**2)),(1,a.phi((1-aa*(1-mu)-d)**2,d*d)))
        check(add((1,B),(-1,out[2])),ex);nonnegative(ex)
        a.bounded(ex,(4-4*q+4*aa,4-4*q+4*aa),d)
        a.bounded(add((1,out[1]),(-1,out[2])),e.plus((Q(6),Q(6)),e.scale(2,a.CI)),d)
        LATE+=1
    return out
a.local=local
def main():
    pilot='--pilot' in sys.argv;lo=int(sys.argv[sys.argv.index('--start')+1]) if '--start' in sys.argv else 0
    hi=int(sys.argv[sys.argv.index('--end')+1]) if '--end' in sys.argv else (2 if pilot else 22)
    cores=[e.tab(m,n) for n in (0,1,2) for m in range(1<<(1<<n))]
    if pilot:cores=cores[:6]
    for u in cores[lo:hi]:
        for v in cores:
            for opposite in (0,1):
                c=a.controller(2,1,opposite);us=(u,v);a.STATS['roots']+=1
                for perm in itertools.permutations((1,2,3)):
                    for data in (None,0,1):
                        ops=[('c',0),('c',perm[0])]+([] if data is None else [('d',data)])+[('c',i) for i in perm[1:]]
                        a.tree(c,us,(0,1,2,3),ops);a.STATS['trees']+=1
        a.coeff.cache_clear();a.spec.cache_clear()
        assert time.perf_counter()-START<(55 if pilot else 180)
    out={'status':'PASS','pilot':pilot,'slice':[lo,hi],'stats':a.STATS,'later_test_exact_formula_checks':LATE,'exact_assertions':e.COUNT,'runtime_seconds':time.perf_counter()-START}
    (R/'out'/('UNORDERED_PILOT.json' if pilot else f'UNORDERED_{lo}_{hi}.json')).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
