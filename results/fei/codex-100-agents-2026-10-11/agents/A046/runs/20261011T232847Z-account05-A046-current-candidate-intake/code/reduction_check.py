"""Independent A046 exact reduction checker: rational sources, exact log ledgers."""
from fractions import Fraction as Q
from pathlib import Path
import json
import time

RUN=Path(__file__).resolve().parents[1]

def factors(n):
    assert n>=1
    out={}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1
            n//=d
        d+=1
    if n>1:
        out[n]=out.get(n,0)+1
    return out

def clean(s):
    return {k:v for k,v in s.items() if v}

def plus(*args):
    out={}
    for s in args:
        for k,v in s.items():
            out[k]=out.get(k,Q(0))+v
    return clean(out)

def times(c,s):
    return clean({k:c*v for k,v in s.items()})

def entropy(probs):
    assert sum(probs)==1 and all(x>=0 for x in probs)
    out={}
    for x in probs:
        if not x:
            continue
        for k,v in factors(x.numerator).items():
            out[k]=out.get(k,Q(0))-x*v
        for k,v in factors(x.denominator).items():
            out[k]=out.get(k,Q(0))+x*v
    return clean(out)

def hb(p):
    return entropy([p,1-p])

def walsh(table):
    n=len(table)
    return [Q(sum(v*(-1)**((s&x).bit_count()%2) for x,v in enumerate(table)),n) for s in range(n)]

def pair_check(g,h,p):
    assert len(g)==len(h)
    assert sum(x*x for x in g)==sum(x*x for x in h)==1
    a=[((1-p)*x+p*y)**2 for x,y in zip(g,h)]
    b=[p*(1-p)*(y-x)**2 for x,y in zip(g,h)]
    q=[(1-p)*x*x+p*y*y for x,y in zip(g,h)]
    assert all(x+y==z for x,y,z in zip(a,b,q))
    assert sum(a)+sum(b)==sum(q)==1
    spectral_cond={}
    physical_cond={}
    rare_moment=Q(0)
    for ai,bi,qi,hi in zip(a,b,q,h):
        if not qi:
            assert ai==bi==hi==0
            continue
        u=p*hi*hi/qi
        v=bi/qi
        assert 0<=u<=1 and 0<=v<=1
        rare_moment+=qi*u
        spectral_cond=plus(spectral_cond,times(qi,hb(v)))
        physical_cond=plus(physical_cond,times(qi,hb(u)))
    assert rare_moment==p
    parent=entropy(a+b)
    marg=entropy(q)
    M=plus(parent,times(-1,marg))
    assert M==spectral_cond
    child_average=plus(times(1-p,entropy([x*x for x in g])),times(p,entropy([x*x for x in h])))
    J=plus(marg,times(-1,child_average))
    assert J==plus(hb(p),times(-1,physical_cond))
    debt=plus(J,times(-1,M))
    identity=plus(hb(p),times(-1,plus(spectral_cond,physical_cond)))
    assert debt==identity
    # Independently check the channel's full joint entropy factorization.
    channel_joint=entropy([(1-p)*x*x for x in g]+[p*x*x for x in h])
    assert channel_joint==plus(hb(p),child_average)
    assert channel_joint==plus(marg,physical_cond)
    # Relabeling physical children and p leaves both full spectral law and debt invariant.
    pa=1-p
    swapped_a=[((1-pa)*y+pa*x)**2 for x,y in zip(g,h)]
    swapped_b=[pa*(1-pa)*(x-y)**2 for x,y in zip(g,h)]
    assert swapped_a==a and swapped_b==b
    return {'p':str(p),'dimension':len(g),'q':[str(x) for x in q],
            'parent_masses':[str(x) for x in a+b],
            'exact_debt_log_ledger':{str(k):str(v) for k,v in debt.items()},
            'moment':str(rare_moment),'status':'PASS'}

def main():
    start=time.perf_counter()
    one=walsh([1,1,1,1])
    literal=walsh([1,-1,1,-1])
    andsign=walsh([1,1,1,-1])
    opposite=[-x for x in andsign]
    pairs=[([Q(1)],[Q(1)]),([Q(1)],[Q(-1)]),
           ([Q(1),Q(0)],[Q(0),Q(1)]),
           ([Q(0),Q(1)],[Q(0),Q(1)]),
           ([Q(3,5),Q(4,5)],[Q(1),Q(0)]),
           ([Q(3,5),Q(4,5)],[Q(4,5),Q(-3,5)]),
           (one,andsign),(literal,andsign),(andsign,opposite),
           (andsign,andsign)]
    rows=[pair_check(g,h,p) for g,h in pairs for p in [Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(7,8)]]
    assert len(rows)==50
    # Actual Boolean orientation counterexample, requiring no irrational arithmetic.
    p=Q(3,4)
    correct=pair_check([Q(1)],[Q(1)],p)
    assert correct['exact_debt_log_ledger']=={}
    wrong_v=(2*p-1)**2
    assert wrong_v==Q(1,4)
    wrong_debt=times(-1,hb(wrong_v))
    assert wrong_debt=={2:Q(-2),3:Q(3,4)}
    # Its magnitude is strictly positive: 1/4 and 3/4 are both interior probabilities.
    # A direct exact bound is h2(1/4)>=1/2, from its first nonnegative entropy summand.
    regression={'p':'3/4','children':'G=H=1','actual_debt':'0',
                'wrong_beta_convention_debt':'-h2(1/4)',
                'exact_wrong_debt_log_ledger':{str(k):str(v) for k,v in wrong_debt.items()},
                'wrong_debt_strict_upper_bound':'-1/2 bits',
                'correction':'use beta=arcsin sqrt(p), or swap children before using min(p,1-p)'}
    result={'status':'PASS','case_count':50,'arithmetic':'Fraction and exact prime-exponent log ledgers',
            'float_mathematics':False,'seconds':time.perf_counter()-start,
            'rows':rows,'orientation_regression':regression}
    (RUN/'out').mkdir(exist_ok=True)
    (RUN/'out'/'REDUCTION_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))

if __name__=='__main__':
    main()
