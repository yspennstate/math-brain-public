"""Numerical stress tests for proposed proof lemmas (not proofs)."""
from q1_core import *
import json, time
from pathlib import Path
start=time.monotonic(); rng=np.random.default_rng(9182)
worst=0; witness=None; tests=0
for n in (3,4,5,6,8):
    for rep in range(1000):
        w=np.exp(rng.uniform(-7,7,(n,n))); w=np.triu(w); w=w+w.T-np.diag(np.diag(w))
        t,F=numeric(w,True)
        for pair in combinations(range(n),2):
            bs=blocks(n,pair); th,C=numeric(np.array(lump(w,bs)),True)
            rest=[i for i in range(n) if i not in pair]
            for a,i in enumerate(rest):
                for b,j in enumerate(rest):
                    val=C[a,b]-np.max(F[i,:]+F[j,:]); tests+=1
                    if val>worst:
                        worst=val; witness={'n':n,'w':w,'pair':pair,'ij':(i,j),'gap':val,'t':t}
        if witness and worst>1e-6: break
    print('n',n,'worst',worst,flush=True)
    if witness and worst>1e-6: break
Path('candidate_inequalities_results.json').write_text(json.dumps(serialize(witness),indent=2))
print('tests',tests,'seconds',time.monotonic()-start)
