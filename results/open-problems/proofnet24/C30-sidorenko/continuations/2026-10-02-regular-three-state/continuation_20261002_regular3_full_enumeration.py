"""Correct full-root three-state cone exploration, no theorem claim yet."""
import itertools
import json
from collections import Counter
from pathlib import Path


def multiply(P, Q):
    R = Counter()
    for a, u in P.items():
        for b, v in Q.items():
            R[tuple(a[i]+b[i] for i in range(4))] += u*v
    return {a:u for a,u in R.items() if u}


def power(P,n):
    R={(0,0,0,0):1}
    for _ in range(n):
        R=multiply(R,P)
    return R


def linear(values):
    return {tuple(int(i==j) for i in range(4)):v
            for j,v in enumerate(values) if v}


def substitute(P, forms):
    powers={(j,n):power(form,n) for j,form in enumerate(forms)
            for n in range(16)}
    R=Counter()
    for counts,c in P.items():
        T={(0,0,0,0):c}
        for j,n in enumerate(counts):
            T=multiply(T,powers[j,n])
        R.update(T)
    return {a:u for a,u in R.items() if u}


def encode(P):
    return {','.join(map(str,a)):u for a,u in sorted(P.items()) if u}


def main():
    edges=[(i,5+j) for i in range(5) for j in range(5)
           if (j-i)%5 in(0,1,4)]
    entry={(0,0):0,(1,1):1,(2,2):2,(0,1):3,(0,2):4,(1,2):5}
    histograms=Counter()
    for labels in itertools.product(range(3),repeat=10):
        counts=[0]*6
        for u,v in edges:
            i,j=sorted((labels[u],labels[v]))
            counts[entry[i,j]]+=1
        histograms[tuple(counts)]+=1
    assert sum(histograms.values())==3**10
    results={}
    for cone in['I','T']:
        values=([[1,0,0,1],[1,1,0,1],[1,1,1,1],
                 [1,1,1,0],[1,1,0,0],[1,0,0,0]] if cone=='I' else
                [[2,0,0,0],[2,2,0,0],[2,2,2,0],
                 [2,2,2,1],[2,2,0,1],[2,0,0,1]])
        forms=[linear(v) for v in values]
        powers={(j,n):power(form,n) for j,form in enumerate(forms)
                for n in range(16)}
        density=Counter()
        for counts,c in histograms.items():
            T={(0,0,0,0):3**5*c}
            for j,n in enumerate(counts):
                T=multiply(T,powers[j,n])
            density.update(T)
        s=linear([3,2,1,1] if cone=='I' else[6,4,2,2])
        gap=Counter(density)
        gap.subtract(power(s,15))
        gap={a:u for a,u in gap.items() if u}
        record={'density':encode(density),'gap':encode(gap),
                'negative_count':sum(v<0 for v in gap.values())}
        print(cone,'terms',len(gap),'negative',record['negative_count'],flush=True)
        if cone=='I':
            orderings=[[[1,0,0,0],[0,1,0,0],[0,0,1,0],[1,1,1,1]],
                       [[1,0,0,0],[0,1,0,0],[0,0,1,1],[1,1,1,0]],
                       [[1,0,0,0],[0,1,1,0],[0,0,0,1],[1,1,0,0]],
                       [[1,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]]]
            record['relative_identity_weight_orderings']=[]
            for pos,values in enumerate(orderings):
                R=substitute(gap,[linear(v) for v in values])
                negative=sum(v<0 for v in R.values())
                print('I order',pos,'terms',len(R),'negative',negative,flush=True)
                record['relative_identity_weight_orderings'].append(
                    {'position':pos,'gap':encode(R),'negative_count':negative})
        results[cone]=record
    out={'status':'exact full-root cone exploration; analytic audit pending',
         'histogram_count':len(histograms),'assignment_count':3**10,
         'results':results}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))


if __name__=='__main__':
    main()
