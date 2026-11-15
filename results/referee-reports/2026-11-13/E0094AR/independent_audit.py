"""Independent checks. No imports or executable inputs from claim_files."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import itertools, math, json, time, hashlib
import resource
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.linalg import eigvalsh

OUT=Path('independent_results')
OUT.mkdir(exist_ok=True)

def save(name,data):
    (OUT/name).write_text(json.dumps(data,indent=2)+'\n')

def inv(p):
    return tuple(np.argsort(p).tolist())

def generators(n,sigma=None):
    identity=tuple(range(n)); t=list(identity); t[0],t[1]=1,0
    c=tuple((i+1)%n for i in identity)
    moves={tuple(t),c,inv(c)}
    if sigma is not None: moves.update((tuple(sigma),inv(sigma)))
    return sorted(moves-{identity})

def rank_rows(a):
    out=np.zeros(len(a),dtype=np.int32)
    for i in range(a.shape[1]-1):
        out+=np.sum(a[:,i+1:]<a[:,i,None],axis=1,dtype=np.int32)*math.factorial(a.shape[1]-1-i)
    return out

def transitions(perms,moves):
    return [rank_rows(perms[:,s]) for s in moves]

def tv_run(trans,thresholds=(.25,.01),keep=False):
    N=len(trans[0]); p=np.zeros(N); p[0]=1
    rows=[]; hits={}; weight=.5/len(trans)
    for t in range(10001):
        tv=float(np.abs(p-1/N).sum()/2)
        if keep: rows.append([t,tv,float(p.sum())])
        for eps in thresholds:
            if eps not in hits and tv<=eps: hits[eps]=t
        if len(hits)==len(thresholds): return hits,rows
        new=.5*p
        for index in trans: new+=weight*p[index]
        p=new
    raise RuntimeError('time limit')

def walks():
    summary=[]
    for n in range(3,10):
        start=time.time()
        perms=np.array(list(itertools.permutations(range(n))),dtype=np.int16)
        sigma=tuple((2*i)%n for i in range(n)) if n%2 else tuple((2*i)%(n-1) for i in range(n-1))+(n-1,)
        row={'n':n,'sigma':sigma}
        for label,s in [('base',None),('double',sigma)]:
            trans=transitions(perms,generators(n,s))
            hits,curve=tv_run(trans,keep=True)
            row[label]={'t25':hits[.25],'t01':hits[.01], 'move_count':len(trans)}
            np.savetxt(OUT/f'tv_{n}_{label}.csv',curve,delimiter=',',header='time,tv,mass',comments='')
            if n<=5:
                P=np.eye(len(perms))*.5
                for ix in trans: P[np.arange(len(perms)),ix]+=.5/len(trans)
                row[label]['gap']=float(1-eigvalsh(P,subset_by_index=[len(perms)-2,len(perms)-2])[0])
        if n<=7:
            # Enumerate EVERY sigma, including identity, coincidences and inverses.
            base=generators(n)
            cache={s:ix for s,ix in zip(base,transitions(perms,base))}
            best=10001; optimizers=[]; values=[]
            for s0 in perms:
                s=tuple(map(int,s0)); moves=generators(n,s)
                for a in moves:
                    if a not in cache: cache[a]=rank_rows(perms[:,a])
                hits,_=tv_run([cache[a] for a in moves],thresholds=(.25,))
                t=hits[.25]; values.append(t)
                if t<best: best=t; optimizers=[s]
                elif t==best: optimizers.append(s)
            row['exhaustive']={'count':len(perms),'best_t25':best,'optimizer_count':len(optimizers),'optimizers':optimizers}
            save(f'exhaustive_{n}.json',{'times_in_lexicographic_sigma_order':values,'optimizers':optimizers})
        row['seconds']=time.time()-start
        summary.append(row); save('walks.json',summary)
        print('walk',n,row,flush=True)

def reduce_word(word):
    stack=[]
    for a in word:
        if stack and (a==-stack[-1] or a==stack[-1]==3): stack.pop()
        else: stack.append(a)
    return stack

def iw(w): return [-a if abs(a)!=3 else 3 for a in w[::-1]]
def power_word(i):
    if i==0: return []
    if i==1: return [1]
    return [2]+power_word(i//2)+[-2]+([1] if i%2 else [])

def trans_word(i,j):
    d=j-i; bits=[b for b in range(d.bit_length()) if (d>>b)&1]
    B=[2]*bits[0]
    for a,b in zip(bits,bits[1:]): B += [3,1]+[2]*(b-a)
    w=power_word(i)+B+[3]+iw(B)+iw(power_word(i))
    return reduce_word(w)

def words():
    results=[]
    for n in [5,7,9,11,15,17,31,33,63,65,101,127,129,255,257]:
        c=np.array([(i+1)%n for i in range(n)])
        d=np.array([(2*i)%n for i in range(n)])
        t=np.arange(n); t[0],t[1]=1,0
        maps={1:c,-1:np.argsort(c),2:d,-2:np.argsort(d),3:t}
        maximum=0; count=0
        for i in range(n):
            for j in range(i+1,n):
                w=trans_word(i,j); p=np.arange(n)
                # Evaluate composition rightmost argument first.
                for letter in reversed(w): p=maps[letter][p]
                expected=np.arange(n); expected[i],expected[j]=j,i
                assert np.array_equal(p,expected),(n,i,j,w)
                assert len(w)<=12*math.ceil(math.log2(n))
                maximum=max(maximum,len(w)); count+=1
        results.append({'n':n,'pairs':count,'maximum_reduced_length':maximum,'bound':12*math.ceil(math.log2(n))})
        print('words',results[-1],flush=True)
    save('words.json',results)

def variations(poly,at):
    seq=sp.sturm(poly.as_expr(),poly.gens[0]); signs=[]
    for p in seq:
        value=p.subs(poly.gens[0],at)
        if value: signs.append(sp.sign(value))
    return sum(a!=b for a,b in zip(signs,signs[1:]))

def graphs():
    x,z=sp.symbols('x z')
    edges=[(0,4),(0,6),(0,7),(1,5),(1,7),(1,8),(2,5),(2,8),(2,9),(3,6),(3,8),(3,9),(4,7),(4,9),(5,6)]
    A=sp.zeros(10)
    for i,j in edges: A[i,j]=A[j,i]=1
    assert list(map(sum,A.tolist()))==[3]*10
    L=3*sp.eye(10)-A
    basepoly=L.charpoly(x).as_poly()
    f=sp.Matrix([2,z*z-z-2,2-z*z,-1,z,-1,0,z,2-z*z,z*z-z-2])
    assert all(sp.rem(a,z**3-3*z-1,z)==0 for a in A*f-z*f)
    assert sp.rem(sum(f),z**3-3*z-1,z)==0
    eigenvalues=basepoly.intervals(eps=sp.Rational(1,10**12))
    records=[]
    for i in range(10):
        for j in range(i+1,10):
            if A[i,j]: continue
            Ap=A.copy(); Ap[i,j]=Ap[j,i]=1
            D=sp.diag(*map(sum,Ap.tolist())); Lp=D-Ap
            # Rational generalized characteristic polynomial; independent of Bareiss/inertia code.
            primitive=sp.Poly((D.inv()*Lp).charpoly(x).as_expr(),x).clear_denoms()[1].primitive()[1]
            p=sp.Poly(primitive.as_expr()/x,x)
            roots=p.intervals(eps=sp.Rational(1,10**12))
            low,high=roots[0][0]
            assert low>0
            rec={'edge':[i,j],'polynomial':str(sp.factor(primitive.as_expr())), 'gap_interval':[str(low),str(high)],'gap':float((low+high)/2)}
            if (i,j) in [(0,2),(0,8),(2,4)]:
                l,u=(sp.Rational(47694,100000),sp.Rational(47695,100000)) if i==0 else (sp.Rational(48117,100000),sp.Rational(48118,100000))
                rec['sturm']=[variations(p,a) for a in [0,l,u]]
                assert rec['sturm']==[9,9,8]
            records.append(rec)
    best=max(records,key=lambda r:r['gap'])
    winners=[]
    bp=sp.Poly(sp.sympify(best['polynomial'])/x,x)
    bl,bh=map(sp.Rational,best['gap_interval'])
    for r in records:
        lo,hi=map(sp.Rational,r['gap_interval'])
        if hi<bl: continue
        common=sp.gcd(bp,sp.Poly(sp.sympify(r['polynomial'])/x,x))
        assert common.count_roots(max(lo,bl),min(hi,bh))==1
        winners.append(r['edge'])
    save('counterexample.json',{'base_polynomial':str(sp.factor(basepoly.as_expr())),'base_intervals':[(list(map(str,r)),m) for r,m in eigenvalues], 'candidates':records,'certified_optimizers':winners})
    cycle=[]
    for n in range(4,42,2):
        A=np.zeros((n,n))
        for i in range(n): A[i,(i+1)%n]=A[(i+1)%n,i]=1
        original=1-math.cos(2*math.pi/n)
        for w in [.01,.5,1,5,1000]:
            for k in range(2,n//2+1):
                Ap=A.copy(); Ap[0,k]=Ap[k,0]=w
                d=Ap.sum(axis=1); norm=Ap/np.sqrt(d[:,None]*d[None,:])
                gap=float(1-eigvalsh(norm)[-2])
                bound=original/(1+2*w/(n+w)*math.cos(math.pi*k/n)**2)
                assert gap<=bound+1e-12
                if k==n//2: assert abs(gap-original)<1e-12
                cycle.append([n,w,k,gap,bound])
    save('cycles.json',cycle)
    print('graphs certified',winners,'cycle cases',len(cycle),flush=True)

def final_checks():
    """Cross-check numerical output and certify selected thresholds with integers."""
    summary=json.loads((OUT/'walks.json').read_text())
    curves=[]; witnesses=[]
    for row in summary:
        n=row['n']
        if n>=5:
            for label in ['base','double']:
                a=np.loadtxt(OUT/f'tv_{n}_{label}.csv',delimiter=',',skiprows=1)
                b=np.genfromtxt(f'claim_files/data/walk_n{n}_{label}.csv',delimiter=',',names=True)
                assert np.array_equal(a[:,0],b['t'])
                error=float(np.max(np.abs(a[:,1]-b['tv'])))
                assert error<1e-10
                curves.append({'n':n,'label':label,'max_tv_discrepancy':error,'max_own_mass_error':float(np.max(np.abs(a[:,2]-1)))})
        if n<=7:
            perms=np.array(list(itertools.permutations(range(n))),dtype=np.int16)
            s=tuple(row['exhaustive']['optimizers'][0]); best=row['exhaustive']['best_t25']
            trans=transitions(perms,generators(n,s)); N=len(perms); m=len(trans)
            # Integer transition weights: m for holding, one for each distinct move.
            counts=np.zeros(N,dtype=object); counts[0]=1; den=1; exact=[]
            for t in range(best+1):
                if t>=best-1:
                    numerator=sum(abs(N*v-den) for v in counts)
                    tv=sp.Rational(numerator,2*N*den)
                    assert (tv<=sp.Rational(1,4))==(t==best)
                    exact.append({'time':t,'tv_numerator':str(tv.p),'tv_denominator':str(tv.q),'tv':float(tv)})
                new=m*counts
                for ix in trans: new+=counts[ix]
                counts=new;den*=2*m
            hits,_=tv_run(trans)
            witnesses.append({'n':n,'sigma':s,'t25':best,'t01':hits[.01],'integer_certificate':exact})
    save('cross_checks.json',{'curves':curves,'exact_optimal_witnesses':witnesses})
    print('final checks',len(curves),'curves;',len(witnesses),'integer witnesses',flush=True)

if __name__=='__main__':
    import sys
    for name in sys.argv[1:] or ['words','graphs','walks','final_checks']:
        globals()[name]()
    from threadpoolctl import threadpool_info
    save('last_run_resources.json',{'nice':os.getpriority(os.PRIO_PROCESS,0),
         'maxrss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         'numerical_threadpools':threadpool_info(),
         'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'claim_sha256':hashlib.sha256(Path('CLAIM.md').read_bytes()).hexdigest()})
