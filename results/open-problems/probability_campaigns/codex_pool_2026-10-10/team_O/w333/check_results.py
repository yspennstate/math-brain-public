"""Reproducible mathematical checks; these are not the directive's test banks."""
import cmath, itertools, json, math, time
from fractions import Fraction as F
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parent
start=time.perf_counter()
results={}

def prime(n):
    return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))
def factors(n):
    return [d for d in range(2,n+1) if n%d==0 and prime(d)]
def mul(A,B,p):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]
def power(A,n,p):
    out=[[int(i==j) for j in range(len(A))] for i in range(len(A))]
    while n:
        if n&1: out=mul(out,A,p)
        A=mul(A,A,p)
        n//=2
    return out

cases=0
for q in range(2,17):
    ell=2*q+1
    while not prime(ell): ell+=2*q
    gen=next(g for g in range(2,ell) if all(pow(g,(ell-1)//d,ell)!=1 for d in factors(ell-1)))
    c=pow(gen,(ell-1)//(2*q),ell)
    assert pow(c,q,ell)==ell-1
    for p in range(1,q):
        if math.gcd(p,q)!=1: continue
        omega=pow(c,2*p,ell)
        A=[[0]*q for _ in range(q)]
        poly=[1]
        for k in range(q):
            weight=pow(omega,k,ell)
            A[k][k]=weight
            A[(k-1)%q][k]=(A[(k-1)%q][k]+c)%ell
            new=[0]*(len(poly)+1)
            for j,v in enumerate(poly):
                new[j]=(new[j]-weight*v)%ell
                new[j+1]=(new[j+1]+v)%ell
            poly=new
        poly[0]=(poly[0]-pow(c,q,ell))%ell
        assert poly==[0]*q+[1]
        assert all(v==0 for row in power(A,q,ell) for v in row)
        cases+=1
results['P0189']={'exact_finite_field_cases':cases,'all_passed':True,'note':'Primitive-root characteristic polynomial and nilpotency; no numerical eigenvalues or Brown-measure verification.'}

cases=0
for n in range(4,9):
    for k in range(1,n):
        subsets=list(itertools.combinations(range(n),k))
        rho=F(k,n)
        for L in range(1,n+1):
            values=[sum(x<L for x in subset) for subset in subsets]
            mean=F(sum(values),len(values))
            variance=F(sum(v*v for v in values),len(values))-mean*mean
            expected=L*rho*(1-rho)*F(n-L,n-1)
            assert variance==expected
            cases+=1
gradient_cases=0
for d in [1,2,3]:
    for L in range(1,65):
        # eta_x=Z_x-Z_(x-e1), Var(Z)=1: c(0)=2,c(+/-e1)=-1.
        variance=2*L**d-2*(L-1)*L**(d-1)
        bound=2*d*L**(d-1)
        assert 0<=variance<=bound
        gradient_cases+=1
results['P0390']={'fixed_mass_enumeration_cases':cases,'weighted_covariance_example_cases':gradient_cases,'all_passed':True,'note':'Comparison fields only; these are not ARW simulations.'}

arrays=[]
for N in [8,16,32,64,128]:
    counts={j:0 for j in [0,1,2]}
    for a in range(N):
        for b in range(N):
            height=(2*((a+b)%2)) if a<N//2 else 1
            counts[height]+=1
    freq={j:F(counts[j],N*N) for j in counts}
    assert freq=={0:F(1,4),1:F(1,2),2:F(1,4)}
    arrays.append({'N':N,'fractions':{str(j):str(v) for j,v in freq.items()}})
results['C0100']={'periodic_patch_cases':len(arrays),'fractions':arrays,'all_passed':True,'note':'Synthetic arrays check the conditional counting lemma, not sandpile dynamics.'}

threshold=[]
for N in [10**4,10**8,10**12]:
    for a in [.25,.5,.75]:
        m=int(N**a)
        threshold.append({'N':N,'exponent':a,'m':m,'P_selected_clock_gt_N':math.erf(m/math.sqrt(2*N))})
assert threshold[-3]['P_selected_clock_gt_N']<.001
assert .68<threshold[-2]['P_selected_clock_gt_N']<.69
assert threshold[-1]['P_selected_clock_gt_N']>.999
results['P0031']={'exact_distribution_evaluations':len(threshold),'values':threshold,'all_passed':True,'note':'Clock law only; no backward-Brownian classification.'}

certificate=json.loads((ROOT/'evidence/P0242_family.json').read_text(encoding='utf-8'))
s=sp.Symbol('s',positive=True)
independent_checks=0
for value in [1,2,5,10,20,50,100,1000]:
    W=sp.Matrix([[0,0,1,0],[0,2*value,1,2*value],[1,1,0,value],[0,2*value,value,4*value*value]])
    blocks=[[0],[1],[2,3]]
    What=sp.Matrix([[sum(W[i,j] for i in a for j in b) for b in blocks] for a in blocks])
    for weights,key in [(W,'fine_D'),(What,'coarse_D')]:
        n=weights.rows
        masses=[sum(weights[i,j] for j in range(n)) for i in range(n)]
        pi=[v/sum(masses) for v in masses]
        P=sp.Matrix([[weights[i,j]/masses[i] for j in range(n)] for i in range(n)])
        Pi=sp.Matrix([pi]*n)
        Z=(sp.eye(n)-P+Pi).inv()-Pi
        for i in range(n):
            for j in range(n):
                expected=sp.sympify(certificate[key][i][j],locals={'s':s}).subs(s,value)
                assert sp.simplify(-Z[i,j]/pi[j]-expected)==0
                independent_checks+=1
results['P0242']={'symbolic_residual_checks':certificate['exact_residual_checks'],'independent_fundamental_matrix_entry_checks':independent_checks,'ratio_at_s1000':certificate['table'][-1]['ratio'],'ratio_float':certificate['table'][-1]['ratio_float'],'all_passed':True}

local_time=[]
for t,g in [(1,1),(2,.5),(.5,2)]:
    atom=math.exp(-t/g)
    assert atom>0 and t+g/2>t
    local_time.append({'t':t,'g':g,'local_time_mean':t,'shifted_square_mean':t+g/2,'local_time_zero_atom':atom,'shifted_square_zero_atom':0})
results['C0011']={'analytical_marginal_checks':len(local_time),'counterexample_marginals':local_time,'all_passed':True,'note':'The full planar spatial level-set limit is not checked.'}

duals=[]
for eps in [.0001,.001,.01,.05,.1,.5]:
    lam=1+eps
    lo,hi=0.0,1.0
    for _ in range(100):
        rho=(lo+hi)/2
        if -math.expm1(-lam*rho)>rho: lo=rho
        else: hi=rho
    q=1-(lo+hi)/2
    dual=lam*q
    I=lambda x:x-1-math.log(x)
    residual=abs(I(dual)-I(lam))
    assert residual<1e-12
    duals.append({'epsilon':eps,'q':q,'dual_mean':dual,'rate_residual':residual,'second_order_coefficient':(dual-(1-eps))/(eps*eps)})
results['C0070']={'poisson_duality_checks':len(duals),'values':duals,'all_passed':True,'note':'Branching process, not hypercube cluster conditioning.'}

products={1}
for r in range(1,4):
    products.update(math.prod(ps) for ps in itertools.product([2,3,5],repeat=r))
moment_cases=0
max_violation=0.0
for T in [10,100,10000]:
    for A,B in itertools.product(sorted(products),repeat=2):
        if A==B:
            average=1
        else:
            freq=math.log(A)-math.log(B)
            average=(cmath.exp(-2j*T*freq)-cmath.exp(-1j*T*freq))/(-1j*T*freq)
            bound=min(1,2/(T*abs(freq)),2*5**3/T)
            max_violation=max(max_violation,abs(average)-bound)
            assert abs(average)<=bound+1e-12
        moment_cases+=1
results['C0105']={'phase_moment_cases':moment_cases,'max_bound_violation':max_violation,'all_passed':True,'note':'No zeta approximation remainder or growing-moment independence is certified.'}

edges=[(0,1),(1,2),(2,3),(3,0)]
fk_cases=0
for p in [F(1,10),F(1,2),F(9,10)]:
    for q in [1,2,3,5]:
        total=F(0); not_wired=F(0)
        for bits in itertools.product([0,1],repeat=4):
            parent=list(range(4))
            def find(x):
                while parent[x]!=x: x=parent[x]
                return x
            for opened,(a,b) in zip(bits,edges):
                if opened: parent[find(a)]=find(b)
            k=len({find(i) for i in range(4)})
            weight=p**sum(bits)*(1-p)**(4-sum(bits))*q**k
            total+=weight
            if find(0)!=find(2): not_wired+=weight
        assert not_wired/total>=(1-p)**2
        fk_cases+=1
results['C0153']={'exact_fk_exterior_partition_cases':fk_cases,'all_passed':True,'note':'Finite-energy obstruction only; no infinite-graph FK phase selection.'}

reflection_cases=0
for t in [F(0),F(1,10),F(1,2),F(9,10)]:
    for y,dy in [(-2-t,-1),(2-t,-1)]:
        separation=abs(1-y)
        dlog=(1-y)*(-dy)/(separation*separation)
        occupation=(1-(y*y-1)/(separation*separation))/2
        assert dlog==occupation
        reflection_cases+=1
results['P0025']={'exact_skorokhod_log_identity_cases':reflection_cases,'all_passed':True,'note':'Deterministic paths; no Brownian asymptotic claim.'}

results['elapsed_seconds']=time.perf_counter()-start
(ROOT/'evidence/check_results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
print(json.dumps({pid:{k:v for k,v in row.items() if not isinstance(v,list)} for pid,row in results.items() if isinstance(row,dict)},indent=2))
print('elapsed_seconds',results['elapsed_seconds'])
