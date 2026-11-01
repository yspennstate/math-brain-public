from verify import *
import random
def maskof(a,m,fun):
    return sum((fun(x,y)==-1)<<(x+(y<<a)) for y in range(1<<m) for x in range(1<<a))
def ledger(mask,a,m):
    v=table(mask,a+m);w=walsh(v);N=len(v)
    return dict(walsh=w,influences=[str(Q(sum(w[t]**2 for t in range(N) if t&(1<<i)),N*N)) for i in range(a+m)],
                entropy_nats_interval=[str(Q(t,SCALE)) for t in ent(tuple(sorted(z*z for z in w)),N*N)])
def run():
    started=time.perf_counter();rows=[]; best=None
    for a in range(1,5):
        for m in [2,4]:
            def bent(y):return (-1)**sum(((y>>(2*i))&1)*((y>>(2*i+1))&1) for i in range(m//2))
            fs=[('coincident_parity_cells',lambda x,y:(-1)**(x.bit_count()+(y&1))),
                ('unequal_nested_affine_cells',lambda x,y:((-1)**(x.bit_count()) if x<2 else 1)*(-1)**(y&1)),
                ('nearly_identical_bent_rare_cell',lambda x,y:bent(y)*(-1 if x==0 and y==0 else 1)),
                ('nearly_identical_bent_parity_cell',lambda x,y:bent(y)*(-1 if x.bit_count()%2 and y==0 else 1))]
            for name,fun in fs:
                mask=maskof(a,m,fun);r=analyze(mask,a,m);r.update(name=name,ledger=ledger(mask,a,m));rows.append(r)
    rng=random.Random(20261012020)
    for _ in range(1024):
        mask=rng.getrandbits(64);r=analyze(mask,2,4)
        if Q(1,4)<=Q(r['density'])<=Q(3,4) and (best is None or r['ratio_float']>best['ratio_float']):best=r
    out=dict(named_cases=32,random_cases=1024,named_fixtures=rows,moderate_random_best=best,runtime_seconds=time.perf_counter()-started)
    (ROOT/'out'/'fixtures.json').write_text(json.dumps(out,indent=2))
    print('PASS 1056 targeted cases',json.dumps(best),out['runtime_seconds'])
if __name__=='__main__':run()
