"""Small exact enumerations and numerical hostile-referee checks; no proof by simulation."""
import itertools, math, json, pathlib, time
import numpy as np
ROOT=pathlib.Path(__file__).resolve().parent
started=time.monotonic()
def rank(vectors):
    piv={}
    for x in vectors:
        while x:
            b=x.bit_length()-1
            if b in piv: x^=piv[b]
            else: piv[b]=x; break
    return len(piv)
out={'periodicity':[], 'matrix_moments':[], 'hypercube':[]}
for d,k in [(1,1),(1,2),(2,2),(2,3),(2,4),(3,3),(3,4),(3,5)]:
    gen=per=0
    for gs in itertools.product(range(2**d),repeat=k):
        if rank(gs)!=d: continue
        gen+=1
        odd=any(all((f&g).bit_count()%2==1 for g in gs) for f in range(1,2**d))
        per+=odd
    expected_gen=math.prod(2**k-2**j for j in range(d))
    assert gen==expected_gen
    assert per*(2**k-1)==gen*(2**d-1)
    out['periodicity'].append({'d':d,'k':k,'generating':gen,'periodic':per,'total':2**(d*k)})
# S3: independent uniform right translations, all tuples, no commutation assumption.
els=list(itertools.permutations(range(3))); index={g:i for i,g in enumerate(els)}
def mul(g,h): return tuple(g[h[i]] for i in range(3))
R=[]
for g in els:
    T=np.zeros((6,6))
    for x in els: T[index[x],index[mul(x,g)]]=1
    R.append(T)
J=np.ones((6,6))/6
Y=[(T+T.T)/2-J for T in R]
assert np.linalg.norm(sum(Y))<1e-12
assert max(np.linalg.norm(a@b-b@a) for a in Y for b in Y)>0.1
for k in [1,2,3]:
    mats=[sum((Y[i] for i in inds),np.zeros((6,6)))/k for inds in itertools.product(range(6),repeat=k)]
    for m in range(1,k+1):
        moment=float(np.mean([np.sum(np.linalg.eigvalsh(A)**(2*m)) for A in mats]))
        bound=5*m*m**(2*m)/(math.factorial(m)*k**m)
        assert moment<=bound+1e-10
        for a in [.5,.8]:
            tail=sum(np.max(np.abs(np.linalg.eigvalsh(A)))>=a-1e-12 for A in mats)/len(mats)
            assert tail <= bound/a**(2*m)+1e-10
        out['matrix_moments'].append({'group':'S3','k':k,'m':m,'exact_enumeration_float_moment':moment,'bound':bound})
# Exact lumped transition recursion on Hamming weight; floating-point arithmetic.
for d in [16,64,256]:
    w=np.arange(d+1,dtype=float)
    pi=np.array([math.exp(math.lgamma(d+1)-math.lgamma(j+1)-math.lgamma(d-j+1)-d*math.log(2)) for j in range(d+1)])
    assert abs(pi.sum()-1)<1e-10
    law=np.zeros(d+1); law[0]=1
    center=d/2*math.log(d)
    targets={max(1,int(round(center+c*d))):c for c in [-1,0,1]}
    times={}; profiles=[]
    for t in range(1,int(center+5*d)+1):
        new=.5*law
        new[1:]+=law[:-1]*(d-w[:-1])/(2*d)
        new[:-1]+=law[1:]*w[1:]/(2*d)
        law=new
        assert abs(law.sum()-1)<1e-10
        tv=.5*np.abs(law-pi).sum()
        upper=.5*math.sqrt(math.expm1(d*math.exp(-2*t/d))) if d*math.exp(-2*t/d)<700 else float('inf')
        b=d*(1-1/d)**t
        lower=max(0,1-8*d/b**2)
        assert tv<=upper+1e-9 and tv>=lower-1e-9
        for eps in [.75,.5,.25,.1]:
            if eps not in times and tv<=eps: times[eps]=t
        if t in targets: profiles.append({'c':targets[t],'t':t,'tv':float(tv),'lower':lower,'upper':upper})
    out['hypercube'].append({'d':d,'center':center,'mixing_times':times,'profiles':profiles})
out['elapsed_seconds']=time.monotonic()-started
out['memory_design']='Largest arrays are 257 entries; S3 stores at most 216 matrices of size 6x6. No large jobs.'
(ROOT/'checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
