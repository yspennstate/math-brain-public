"""Exact-rational stochastic optimization: every objective is an exact solve.
One process/thread, wall-time budget 175 s; saved incumbent on every improvement.
"""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,time,random,json,math,resource
from fractions import Fraction as Q
import q2_search as s
from q1_core import exact,lump,serialize
n=int(sys.argv[1]);seed=int(sys.argv[2]);rng=random.Random(seed)
start=time.monotonic();best=s.loadbest();count=accepted=0;trials=[]
with open('q2_shape_results.json') as f:shapes=json.load(f)['best']

def assess(w,bs):
    global count
    x=exact(w);h=s.correction(x['F'],bs);count+=1
    return max(map(max,h))/x['t'],x['t'],max(map(max,h))

for shape in ((3,),(2,2)):
    key=str((n,2,shape));z=shapes[key]
    initial=[[Q(x) for x in row] for row in z['w']];bs=z['partition']
    incumbent=Q(z['ratio']);saved=initial
    end=start+(82 if shape==(3,) else 170)
    restart=0
    while time.monotonic()<end:
        w=[row[:] for row in saved] if restart%3 else [row[:] for row in initial]
        # Rescale huge weights to permit exploring a more moderate hierarchy.
        if restart%3==0:
            # shrink the integer exponents towards the origin while keeping zeros
            w=[[Q(0) if not x else Q(10)**round(math.log10(float(x))*(.25 if restart%2 else .5)) for x in row] for row in w]
        val,T,Th=assess(w,bs)
        for k in range(200):
            if time.monotonic()>end:break
            v=[row[:] for row in w];i=rng.randrange(n);j=rng.randrange(n)
            if i>j:i,j=j,i
            old=v[i][j]
            if old:
                fac=rng.choice((Q(1,10),Q(1,2),Q(2),Q(10)))
                x=old*fac
                if i==j and rng.random()<.08:x=Q(0)
                if x and (x>Q(10)**60 or x<Q(10)**-60):continue
            else:
                nz=[a for a in w[i]+w[j] if a]
                x=rng.choice(nz)*rng.choice((Q(1,100),Q(1,10),Q(1),Q(10)))
            v[i][j]=v[j][i]=x
            try:rat,t,th=assess(v,bs)
            except (StopIteration,ZeroDivisionError):continue
            # Cooling within a restart, objective itself always rational.
            temperature=.025*(1-k/200)**2
            delta=float(rat-val)
            if rat>=val or (temperature>0 and rng.random()<math.exp(max(-700,delta/temperature))):
                w=v;val=rat;accepted+=1
            if rat>incumbent:
                incumbent=rat;saved=[row[:] for row in v]
                trials.append(serialize(dict(n=n,shape=shape,w=v,partition=bs,T=t,That=th,ratio=rat,evaluation=count)))
                with open(f'q2_exact_opt_{n}_{seed}_results.json','w') as f:json.dump(dict(records=trials),f,indent=2)
                s.record(best,n,2,v,bs,t,th,f'exact_opt_seed{seed}_shape{shape}_eval{count}')
                s.log(f'Exact optimizer n={n}, shape={shape}, improved to {float(rat):.15g}; exact witness saved (evaluation {count}).')
            if rat>3:raise RuntimeError('EXACT Q2 COUNTEREXAMPLE')
        restart+=1
    s.log(f'Exact optimizer completed n={n}, shape={shape}, best {float(incumbent):.15g}, {count} cumulative exact evaluations.')
s.log(f'Exact optimization n={n}, seed={seed}: {count} exact objectives, {accepted} accepted proposals, {time.monotonic()-start:.3f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss} bytes.')
with open('q2_counts.jsonl','a') as f:f.write(json.dumps(dict(mode='exact_opt',n=n,seed=seed,evaluations=count,accepted=accepted,seconds=time.monotonic()-start))+'\n')
