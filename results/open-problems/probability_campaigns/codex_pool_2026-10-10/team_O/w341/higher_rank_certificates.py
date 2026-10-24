"""Obtain float LP supports, then certify rank-2 + rank-2 couplings exactly.

Float output is only a suggested support. The certificate is a rational point
whose nonnegativity and all three determinantal marginals are rechecked.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
import random
import time
from scipy.optimize import linprog

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'measurements'

def determinant(a):
    a=[row[:] for row in a]
    value=F(1)
    n=len(a)
    for j in range(n):
        choices=[i for i in range(j,n) if a[i][j]]
        if not choices:
            return F(0)
        k=choices[0]
        if k!=j:
            a[j],a[k]=a[k],a[j]; value=-value
        pivot=a[j][j]; value*=pivot
        for i in range(j+1,n):
            fac=a[i][j]/pivot
            for k in range(j+1,n):
                a[i][k]-=fac*a[j][k]
    return value

def dpp_mass(u,columns,subset):
    # Fixed-cardinality projection law: Gram determinant of the chosen rows.
    a=[[sum((u[i][k]*u[j][k] for k in columns),F(0)) for j in subset] for i in subset]
    return determinant(a)

def basis_minor_mass(u,columns,subset):
    return determinant([[u[i][k] for k in columns] for i in subset])**2

def orthogonal(n,seed):
    rng=random.Random(seed)
    u=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    for _ in range(2):
        w=[rng.choice([-2,-1,1,2]) for _ in range(n)]
        norm=sum(x*x for x in w)
        h=[[F(int(i==j))-F(2*w[i]*w[j],norm) for j in range(n)] for i in range(n)]
        u=[[sum((h[i][k]*u[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]
    assert all(sum(u[i][k]*u[i][j] for i in range(n))==int(k==j) for k in range(n) for j in range(n))
    return u

def exact_solve_support(matrix,rhs,support):
    rows=[[F(row[i]) for i in support]+[b] for row,b in zip(matrix,rhs)]
    r=0; pivots=[]
    for j in range(len(support)):
        choices=[i for i in range(r,len(rows)) if rows[i][j]]
        if not choices:
            continue
        i=choices[0]; rows[r],rows[i]=rows[i],rows[r]
        z=rows[r][j]; rows[r]=[x/z for x in rows[r]]
        for k in range(len(rows)):
            if k!=r and rows[k][j]:
                z=rows[k][j]; rows[k]=[x-z*y for x,y in zip(rows[k],rows[r])]
        pivots.append((r,j)); r+=1
    assert all(any(row[:-1]) or row[-1]==0 for row in rows), 'floating support does not solve the exact equations'
    result=[F(0)]*len(support)
    for i,j in pivots:
        result[j]=rows[i][-1]
    assert all(x>=0 for x in result), 'floating support did not yield a nonnegative exact point'
    return result

def certify(n,seed):
    u=orthogonal(n,seed)
    pairs=list(combinations(range(n),2)); unions=list(combinations(range(n),4))
    qa={a:basis_minor_mass(u,[0,1],a) for a in pairs}
    qb={b:basis_minor_mass(u,[2,3],b) for b in pairs}
    qc={c:basis_minor_mass(u,[0,1,2,3],c) for c in unions}
    assert sum(qa.values())==sum(qb.values())==sum(qc.values())==1
    variables=[]
    for c in unions:
        for a in combinations(c,2):
            b=tuple(i for i in c if i not in a)
            variables.append((a,b,c))
    constraints=[(0,a) for a in pairs]+[(1,b) for b in pairs]+[(2,c) for c in unions]
    maps=[qa,qb,qc]
    matrix=[[int(var[k]==subset) for var in variables] for k,subset in constraints]
    rhs=[maps[k][subset] for k,subset in constraints]
    rng=random.Random(seed+1000)
    costs=[rng.randrange(-100,101) for _ in variables]
    guess=linprog(costs,A_eq=matrix,b_eq=list(map(float,rhs)),bounds=(0,None),method='highs')
    assert guess.success
    support=[i for i,x in enumerate(guess.x) if x>0]
    point=exact_solve_support(matrix,rhs,support)
    full=[F(0)]*len(variables)
    for i,x in zip(support,point): full[i]=x
    assert all(sum((F(a)*x for a,x in zip(row,full)),F(0))==b for row,b in zip(matrix,rhs))
    cert={'n':n,'seed':seed,'ranks':[2,2],'orthogonal_matrix':[[str(x) for x in row] for row in u],
          'positive_masses':[[list(variables[i][0]),list(variables[i][1]),str(x)] for i,x in enumerate(full) if x],
          'label':'exact rational feasibility certificate; not a general theorem'}
    return cert

def replay(cert):
    u=[[F(x) for x in row] for row in cert['orthogonal_matrix']]
    n=cert['n']
    assert all(sum(u[i][k]*u[i][j] for i in range(n))==int(k==j) for k in range(n) for j in range(n))
    pairs=list(combinations(range(n),2)); unions=list(combinations(range(n),4))
    marg=[{a:F(0) for a in pairs},{b:F(0) for b in pairs},{c:F(0) for c in unions}]
    for ar,br,raw in cert['positive_masses']:
        a,b=tuple(ar),tuple(br); x=F(raw); c=tuple(sorted(a+b))
        assert len(a)==len(b)==2 and len(set(a+b))==4 and x>0
        marg[0][a]+=x; marg[1][b]+=x; marg[2][c]+=x
    for k,cols in enumerate(([0,1],[2,3],[0,1,2,3])):
        assert sum(marg[k].values())==1
        for subset,mass in marg[k].items():
            assert mass==dpp_mass(u,cols,subset)

def main():
    start=time.perf_counter(); count=0
    path=OUT/'C0034_higher_rank_certificates.jsonl'
    with path.open('w',encoding='utf-8') as f:
        for n in [5,6]:
            for seed in range(4):
                cert=certify(n,seed); replay(cert)
                f.write(json.dumps(cert)+'\n'); f.flush(); count+=1
                print('EXACT',n,seed,'support',len(cert['positive_masses']),flush=True)
    replayed=0
    with path.open(encoding='utf-8') as f:
        for line in f:
            replay(json.loads(line)); replayed+=1
    assert replayed==count==8
    result={'label':'exact rational certificates','before_exact_higher_rank_certificates':0,'after_exact_higher_rank_certificates':count,'replayed':replayed,'ranks':[2,2],'dimensions':[5,6],'all_three_marginal_residuals':'0 exactly','seconds':round(time.perf_counter()-start,3),'status':'PASS'}
    (OUT/'C0034_higher_rank_summary.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result),flush=True)

if __name__=='__main__':
    main()
