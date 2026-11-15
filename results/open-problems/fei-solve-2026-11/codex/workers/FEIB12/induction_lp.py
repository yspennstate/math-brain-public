"""Finite E/D-node induction experiment, with homogeneous, root-controlled G.
G=a Ent(g^2)+b(||g||2^2-||g||1^2)+c M log2(M/||g||1^2)
 +d M log2(1/p)+e M log2(||g||inf^2/M)+z mean(g)^2 log2(M/mean(g)^2).
First five vanish at Boolean roots and constants. Last is <=Var/ln2 at roots.
"""
import warnings,json,itertools,time
from pathlib import Path
from functools import lru_cache
from numerics import *
from scipy.optimize import linprog
SCALE=256.
features=['Ent_g2','L1_deficit','L1_log_deficit','support_surprise','sup_surprise','bias_entropy']
@lru_cache(None)
def stat(key):
    v=np.array(key,dtype=float)/SCALE;N=len(v);n=N.bit_length()-1;hat=fwht(v);mu=hat**2;M=float(mu.sum());I=float((mu*pc(n)).sum());up=noise_polys(mu,1.)
    B=float((mu*np.log2(np.maximum(up,1e-300)/np.maximum(mu,1e-300))).sum())
    if not M:return B,I,M,(0.,)*6
    sq=v*v;ab=abs(v).mean();p=(v!=0).mean();m=hat[0]**2
    feat=(float(np.mean(sq*np.log2(np.maximum(sq,1e-300)/M))),M-ab*ab,M*mathlog(M/(ab*ab)),M*mathlog(1/p),M*mathlog(max(sq)/M),m*mathlog(M/m) if m else 0.)
    return B,I,M,feat

def mathlog(x):return float(np.log2(x))
def split(key,i):
    a=np.array(key);h=1<<i;b=a.reshape(-1,2*h);v=b[:,:h];w=b[:,h:]
    assert np.all((v+w)%2==0) and np.all((v-w)%2==0)
    return tuple(((v+w)//2).ravel().tolist()),tuple(((v-w)//2).ravel().tolist())

def constraints(roots):
    pending=list(roots);seen=set();rows=[];meta=[]
    while pending:
        key=pending.pop()
        if key in seen:continue
        seen.add(key);n=len(key).bit_length()-1
        if not n:continue
        B,I,M,phi=stat(key)
        for i in range(n):
            a,d=split(key,i);pending.extend([a,d]);ba,ia,ma,fa=stat(a);bd,id,md,fd=stat(d)
            J=B-ba-bd;delta=np.array(fa)+np.array(fd)-np.array(phi)
            rows.append(np.r_[-md,delta]);meta.append(dict(n=n,g=list(key),coordinate=i,J=J,Dmass=md))
    return np.array(rows),np.array([-r['J'] for r in meta]),meta,seen

def solve(A,rhs,meta,cols,label,signed=False,include_bias=False):
    c=np.zeros(len(cols)+1);c[0]=1
    if include_bias:c[-1]=1/np.log(2)
    aa=A[:,[0]+[i+1 for i in cols]]
    bounds=[(0,None)]+([(None,None)]*len(cols) if signed else [(0,None)]*len(cols))
    # Bias coefficient must be nonnegative for the stated root bound/objective.
    if include_bias:bounds[-1]=(0,None)
    with warnings.catch_warnings():
        warnings.simplefilter('ignore');r=linprog(c,A_ub=aa,b_ub=rhs,bounds=bounds,method='highs',options={'threads':1,'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    out=dict(label=label,features=[features[i] for i in cols],signed=signed,status=int(r.status),message=r.message,rows=len(rhs),variables=len(c))
    if r.success:
        residual=(aa*r.x).sum(axis=-1)-rhs;dual=r.ineqlin.marginals
        active=np.argsort(dual)[:8]
        out.update(objective=float(r.fun),c=float(r.x[0]),G_coefficients=r.x[1:].tolist(),max_violation=float(max(0,residual.max())),dual_objective=float((rhs*dual).sum()),forcing=[dict(meta[k],dual=float(dual[k]),slack=float(-residual[k])) for k in active])
    return out

def main():
    roots=from_tt(np.fromfile('npn4.bin',dtype='<u4'),4);keys=[tuple((f.astype(int)*int(SCALE)).tolist()) for f in roots]
    A,rhs,meta,nodes=constraints(keys);out=[]
    for name,cols,signed,bias in [('none',[],False,False),('entropy',[0],False,False),('nonnegative_root_zero',list(range(5)),False,False),('signed_root_zero',list(range(5)),True,False),('nonnegative_with_bias',list(range(6)),False,True),('signed_with_bias',list(range(6)),True,True)]:
        ans=solve(A,rhs,meta,cols,name,signed,bias);out.append(ans);print({k:v for k,v in ans.items() if k!='forcing'},flush=True)
    # Fixed output is the entire finite LP; never extrapolate these inequalities.
    np.savez_compressed('induction_constraints.npz',A=A,rhs=rhs)
    Path('induction_lp.json').write_text(json.dumps(dict(root_classes=len(keys),unique_nodes=len(nodes),constraints=len(rhs),features=features,results=out),indent=2))
    # A root-only necessary LP is deliberately distinguished from node induction.
    rootA=[];rootrhs=[]
    for key in keys:
        B,I,M,phi=stat(key);rootA.append([-I,*(-np.array(phi))]);rootrhs.append(-B)
    res=linprog([1,0,0,0,0,0,1/np.log(2)],A_ub=rootA,b_ub=rootrhs,bounds=[(0,None)]*7,method='highs',options={'threads':1})
    Path('root_only_lp.json').write_text(json.dumps(dict(status=int(res.status),objective=float(res.fun),x=res.x.tolist(),max_violation=float(max(0,((np.array(rootA)*res.x).sum(axis=-1)-np.array(rootrhs)).max()))),indent=2))
if __name__=='__main__':main()
