"""Independent integer path counts for small n and trace-based roundoff checks."""
import csv
from fractions import Fraction
from itertools import permutations
import json
from math import factorial
from pathlib import Path


def small_check(n, model, steps):
    states=list(permutations(range(n)))
    ranks={p:i for i,p in enumerate(states)}
    ident=list(range(n))
    tau=[1,0]+list(range(2,n))
    c=[(i+1)%n for i in ident];ci=[(i-1)%n for i in ident]
    gs=[tau,c,ci]
    if model=='double':
        m=n if n%2 else n-1
        sig=[2*i%m if i<m else i for i in ident]
        si=[0]*n
        for i,j in enumerate(sig):si[j]=i
        gs += [sig,si]
    trs=[[ranks[tuple(p[g[i]] for i in ident)] for p in states] for g in gs]
    den=2*len(gs);hold=len(gs)
    counts=[0]*len(states);counts[0]=1
    original=list(csv.DictReader(open(f'data/walk_n{n}_{model}.csv')))
    maximum=0.
    power=1;N=factorial(n)
    for t in range(steps+1):
        exact=Fraction(sum(abs(N*v-power) for v in counts),2*N*power)
        error=abs(float(exact)-float(original[t]['tv']));maximum=max(maximum,error)
        assert error<1e-12
        if t<steps:
            counts=[hold*counts[i]+sum(counts[tr[i]] for tr in trs) for i in range(N)]
            power*=den
    return dict(n=n,model=model,steps=steps,max_error=maximum)


def main():
    rows=[small_check(n,m,20) for n in [5,6,7] for m in ['base','double']]
    summary=[]
    for n in range(5,12):
        for m in ['base','double']:
            p=Path(f'data/walk_n{n}_{m}.csv')
            if not p.exists():continue
            data=list(csv.DictReader(p.open()))
            assert all(float(r['tv'])<=1+1e-8 for r in data)
            assert max(abs(float(r['mass'])-1) for r in data)<1e-7
            assert all(float(b['tv'])<=float(a['tv'])+1e-8 for a,b in zip(data,data[1:]))
            summary.append(dict(n=n,model=m,states=factorial(n),steps=len(data)-1,
                  max_mass_error=max(abs(float(r['mass'])-1) for r in data),
                  thresholds={str(e):next((int(r['t']) for r in data if float(r['tv'])<=e),None)
                              for e in [.5,.25,.1,.01]}))
    Path('data/walk_audit.json').write_text(json.dumps(dict(integer_checks=rows,full_state=summary),indent=2)+'\n')
    print(json.dumps(dict(integer_checks=rows,full_state=summary),indent=2))


if __name__=='__main__':main()
