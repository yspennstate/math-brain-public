"""Stress-test proposed stronger one-merge inequalities."""
from q1_core import *
from pathlib import Path
import time,json
rng=np.random.default_rng(82342); start=time.monotonic()
worst=[0.,0.,0.,0.,0.]; examples=[None,None,None,None,None]; count=0
for n in (4,5,6,8):
    for rep in range(700):
        w=np.exp(rng.uniform(-8,8,(n,n))); w=np.triu(w); w=w+w.T-np.diag(np.diag(w))
        T,F=numeric(w,True)
        pi=w.sum(axis=1)/w.sum()
        for pair in combinations(range(n),2):
            u,v=pair; bs=blocks(n,pair); rest=[i for i in range(n) if i not in pair]
            _,C=numeric(np.array(lump(w,bs)),True)
            # c*s_i = F_vi-F_ui; c>0, so this determines the signs.
            s=F[v,:]-F[u,:]
            for a,i in enumerate(rest):
                for b,j in enumerate(rest[:a]):
                    if s[i]*s[j]<=0: continue
                    low=v if s[i]>0 else u
                    proposed=[T+max(F[i,low],F[j,low],0),
                              max(F.max(axis=1)[i],F.max(axis=1)[j])+T,
                              T+max(C[a,-1],C[b,-1],0),
                              F.max(axis=1)[i]+F.max(axis=1)[j],
                              2*min(F.max(axis=1)[i],F.max(axis=1)[j])]
                    for k,p in enumerate(proposed):
                        gap=(C[a,b]-p)/T
                        if gap>worst[k]:
                            worst[k]=gap; examples[k]={'n':n,'w':w,'pair':pair,'ij':(i,j),
                                  'T':T,'gap_over_T':gap,'Cij':C[a,b],'proposed':p}
                    count+=1
    print(n,'worst',worst,flush=True)
Path('test_bound_variants_results.json').write_text(json.dumps(serialize(examples),indent=2))
print('tests',count,'seconds',time.monotonic()-start)
