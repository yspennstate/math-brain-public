"""Constrained local searches in structured families, n<=6.

Reports feasible maxima found, never certified global suprema.
"""
import json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from common import tables,quantities,check,mv
from repair_small import repair

def optimize_family(n,groups,starts=10):
    pc,z,L,fac,meta=tables(n); rr=np.array([r for r,k in meta]); m=1<<n
    P=np.zeros((m,len(groups)))
    for j,g in enumerate(groups): P[g,j]=1/len(g)
    Z=np.einsum('ij,jk->ik',z[rr],P,optimize=False)
    LL=np.einsum('ij,jk->ik',L,P,optimize=False)
    def objective(y):
        x=mv(P,y); q=quantities(x,pc,z)
        return -q['A_I']
    def con(y): return np.maximum(mv(Z,y),0)**1.5-mv(LL,y)/fac
    def jac(y): return 1.5*np.sqrt(np.maximum(mv(Z,y),0))[:,None]*Z-LL/fac[:,None]
    rng=np.random.default_rng(20261110+n+len(groups)); best=None
    for j in range(starts):
        y=rng.dirichlet(np.ones(len(groups))); y*=.7; y[-1]+=.3
        sol=minimize(objective,y,method='SLSQP',bounds=[(0,1)]*len(y),
                     constraints=[{'type':'eq','fun':lambda y:y.sum()-1},
                                  {'type':'ineq','fun':con,'jac':jac}],
                     options={'maxiter':400,'ftol':2e-11})
        x=mv(P,np.maximum(sol.x,0)); x/=x.sum()
        if check(x,n)['max_violation']>1e-7: continue
        x,eps,ratio=repair(x,n); q=quantities(x,pc,z)
        if best is None or q['A_I']>best['quantities']['A_I']:
            best={'quantities':q,'mu':x.tolist(),'max_C_left_right':ratio,'repair_mix':eps,
                  'groups':groups,'orbit_weights':sol.x.tolist()}
    return best

def product_search(n,starts=12):
    pc,z,L,fac,meta=tables(n); rr=np.array([r for r,k in meta]);m=1<<n
    sizes=[2]*(n//2)+([1] if n%2 else []); widths=[1<<b for b in sizes]
    offsets=np.cumsum([0]+widths); shift=np.cumsum([0]+sizes)
    def law(y):
        x=np.ones(m)
        for j,b in enumerate(sizes):
            x*=y[offsets[j]+((np.arange(m)>>shift[j])&((1<<b)-1))]
        return x
    def obj(y): return -quantities(law(y),pc,z)['A_I']
    def con(y):
        x=law(y); return mv(z[rr],x)**1.5-mv(L,x)/fac
    cons=[{'type':'eq','fun':lambda y,j=j:y[offsets[j]:offsets[j+1]].sum()-1} for j in range(len(sizes))]
    cons.append({'type':'ineq','fun':con})
    rng=np.random.default_rng(100+n); best=None
    for j in range(starts):
        y=np.concatenate([rng.dirichlet(np.ones(w)) for w in widths])
        sol=minimize(obj,y,method='SLSQP',bounds=[(1e-8,1)]*len(y),constraints=cons,
                     options={'maxiter':600,'ftol':1e-11})
        xx=sol.x.copy()
        # Mix each factor toward its full-set atom, retaining a product law.
        eps=1e-12
        while eps<1:
            for k in range(len(sizes)):
                v=sol.x[offsets[k]:offsets[k+1]].clip(0);v/=v.sum()
                xx[offsets[k]:offsets[k+1]]=(1-eps)*v
                xx[offsets[k+1]-1]+=eps
            x=law(xx); up=mv(z[rr],x); left=mv(L,x);right=fac*up**1.5
            ratio=float(np.max(left/right))
            if ratio<1-1e-11: break
            eps*=2
        if eps>=1:continue
        q=quantities(x,pc,z)
        if best is None or q['A_I']>best['quantities']['A_I']:
            best={'quantities':q,'mu':x.tolist(),'factor_sizes':sizes,'factor_probabilities':xx.tolist(),
                  'max_C_left_right':ratio,'factor_mix':eps}
    return best

if __name__=='__main__':
    start=time.time(); out=[]
    for n in range(1,7):
        m=1<<n; fam={}
        for name,groups in [
            ('nested_chain',[[0]]+[[ (1<<j)-1 ] for j in range(1,n+1)]),
            ('exchangeable',[[i for i in range(m) if i.bit_count()==r] for r in range(n+1)])]:
            fam[name]=optimize_family(n,groups)
        candidates=[]
        if n>=2:
            for s in range(1,n):
                candidates.append(optimize_family(n,[[0],[i for i in range(m) if i.bit_count()==s],[m-1]]))
            fam['two_scale']=max((x for x in candidates if x),key=lambda x:x['quantities']['A_I'])
        else:fam['two_scale']=fam['nested_chain']
        blockc=[]
        for length in range(1,n):
            orbit=sorted({sum(1<<((i+j)%n) for j in range(length)) for i in range(n)})
            blockc.append(optimize_family(n,[[0],orbit,[m-1]],starts=6))
        fam['cyclic_block_design']=max((x for x in blockc if x),key=lambda x:x['quantities']['A_I']) if blockc else fam['nested_chain']
        fam['products_of_1_or_2_bit_measures']=product_search(n)
        out.append({'n':n,'families':fam})
        print(n,{k: v['quantities']['A_I'] if v else None for k,v in fam.items()},flush=True)
        Path('families_output.json').write_text(json.dumps({'results':out,'seconds':time.time()-start},indent=2)+'\n')
