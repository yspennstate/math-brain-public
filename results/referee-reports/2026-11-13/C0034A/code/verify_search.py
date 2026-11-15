"""Audit saved duals/control with Fractions, and objectives with scalar complex determinants."""
import json,itertools,math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def det(A):
    A=[row[:] for row in A];answer=1+0j;n=len(A)
    for i in range(n):
        k=max(range(i,n),key=lambda k:abs(A[k][i]))
        if abs(A[k][i])<1e-30:return 0j
        if k!=i:A[k],A[i]=A[i],A[k];answer=-answer
        pivot=A[i][i];answer*=pivot
        for j in range(i+1,n):
            ratio=A[j][i]/pivot
            for k in range(i+1,n):A[j][k]-=ratio*A[i][k]
    return answer

def run():
    control=json.loads((ROOT/'data/positive_control_farkas.json').read_text())
    y=list(map(F,control['dual']));b=list(map(F,control['rhs']))
    assert sum((v*w for v,w in zip(y,b)),F(0))==F(control['rhs_dot_y'])==-1
    def slacks(n,p,q,y):
        As=list(itertools.combinations(range(n),p));Bs=list(itertools.combinations(range(n),q));Cs=list(itertools.combinations(range(n),p+q))
        ia={A:i for i,A in enumerate(As)};ib={B:i+len(As) for i,B in enumerate(Bs)};ic={C:i+len(As)+len(Bs) for i,C in enumerate(Cs)}
        result=[]
        for A in As:
            for B in Bs:
                if set(A).isdisjoint(B):result.append(y[ia[A]]+y[ib[B]]+y[ic[tuple(sorted(A+B))]])
        return result
    assert min(slacks(3,1,1,y))>=0
    search=json.loads((ROOT/'data/adversarial_results.json').read_text())
    eqs=0;maxerror=0.;minslack=F(100);maxorth=0.
    for row in search['records']:
        n,p,q=row['n'],row['p'],row['q'];y=list(map(F,row['dual_exact']))
        ss=slacks(n,p,q,y);assert min(ss)>=0;minslack=min(minslack,min(ss));eqs+=len(ss)
        Q=[[complex(re,im) for re,im in zip(r,i)] for r,i in zip(row['final_Q_real'],row['final_Q_imag'])]
        err=max(abs(sum(Q[k][i].conjugate()*Q[k][j] for k in range(n))-int(i==j)) for i in range(n) for j in range(n))
        maxorth=max(maxorth,err);assert err<1e-12
        groups=[list(range(p)),list(range(p,p+q)),list(range(p+q))]
        rhs=[abs(det([[Q[i][j] for j in cols] for i in B]))**2 for cols in groups for B in itertools.combinations(range(n),len(cols))]
        value=math.fsum(float(v)*mass for v,mass in zip(y,rhs))
        maxerror=max(maxerror,abs(value-row['optimized_functional']))
        assert abs(value-row['optimized_functional'])<1e-10
    from verify_certificates import check
    check(ROOT/'data/rank_one_flow.json',{})
    record={'exact_dual_inequalities_checked':eqs,'minimum_exact_slack':str(minslack),
            'positive_control_exact_pairing':'-1','positive_control_exact_slacks_nonnegative':True,
            'runs_checked':len(search['records']),'max_independent_functional_discrepancy':maxerror,
            'max_independent_orthogonality_error':maxorth,'rank_one_flow_independently_verified':True,
            'max_primal_L1_residual':max(r['final_primal_L1_residual'] for r in search['records']),
            'max_absolute_raw_dual_L1_value':max(abs(r['final_min_L1_violation_raw']) for r in search['records'])}
    (ROOT/'data/search_verification.json').write_text(json.dumps(record,indent=2)+'\n')
    print(record)
if __name__=='__main__':run()
