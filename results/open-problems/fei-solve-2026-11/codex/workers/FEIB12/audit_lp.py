"""Recheck primal/dual LPs without BLAS; test fitted potentials on fresh descendants."""
import json,math
from pathlib import Path
from induction_lp import *

def audit():
    saved=json.load(open('induction_lp.json'));raw=np.load('induction_constraints.npz');A=raw['A'];rhs=raw['rhs'];out=[]
    for r in saved['results']:
        cols=[features.index(x) for x in r['features']];x=np.array([r['c'],*r['G_coefficients']]);aa=A[:,[0]+[i+1 for i in cols]]
        # Python math.fsum is a different residual calculation from NumPy.
        residual=[math.fsum(float(a)*float(b) for a,b in zip(row,x))-float(h) for row,h in zip(aa,rhs)]
        out.append(dict(label=r['label'],rechecked_max_violation=max(0,max(residual)),duality_gap=abs(r['objective']-r['dual_objective'])))
    # Replay every four-variable local row from the explicit J formula.
    roots=from_tt(np.fromfile('npn4.bin',dtype='<u4'),4)
    keys=[tuple((f.astype(int)*int(SCALE)).tolist()) for f in roots]
    aa,bb,meta4,nodes4=constraints(keys)
    recerr=0.;ierr=0.
    for rr in meta4:
        key=tuple(rr['g']);a,d=split(key,rr['coordinate'])
        va=np.array(a)/SCALE;vd=np.array(d)/SCALE
        ma=fwht(va)**2;md=fwht(vd)**2;upa=noise_polys(ma,1.);upd=noise_polys(md,1.)
        direct=float(sum(ma[t]*math.log2(1+upd[t]/upa[t]) for t in range(len(ma)) if ma[t]))
        recerr=max(recerr,abs(direct-rr['J']))
        bg,ig,mg,fg=stat(key);ba,ia,mmaa,fa=stat(a);bd,id,mmd,fd=stat(d)
        ierr=max(ierr,abs(ig-ia-id-mmd))
    locindex={(tuple(r['g']),r['coordinate']):i for i,r in enumerate(meta4)}
    dualchecks=[]
    for r in saved['results']:
        cols=[features.index(x) for x in r['features']];mat=aa[:,[0]+[i+1 for i in cols]]
        dual=np.zeros(len(bb))
        for z in r['forcing']:dual[locindex[(tuple(z['g']),z['coordinate'])]]=z['dual']
        obj=np.zeros(len(cols)+1);obj[0]=1
        if cols and cols[-1]==5:obj[-1]=1/np.log(2)
        grad=np.array([math.fsum(float(v)*float(w) for v,w in zip(mat[:,j],dual)) for j in range(len(obj))])
        errors=[]
        for j in range(len(obj)):
            free=r['signed'] and j>0 and cols[j-1]!=5
            errors.append(abs(grad[j]-obj[j]) if free else max(0,grad[j]-obj[j]))
        dualchecks.append(dict(label=r['label'],dual_max_positive=max(0,float(dual.max())),dual_constraint_max_violation=max(errors),duality_gap=abs(float((bb*dual).sum())-r['objective'])))
    assert recerr<1e-12 and ierr<1e-12
    assert max(z['dual_constraint_max_violation'] for z in dualchecks)<1e-9
    held=[]
    for n in [5,6]:
        F=sample(n,128,20261110+100+n);roots=[tuple((f.astype(int)*int(SCALE)).tolist()) for f in F]
        a,b,meta,nodes=constraints(roots)
        for r in saved['results']:
            cols=[features.index(x) for x in r['features']];x=np.array([r['c'],*r['G_coefficients']]);aa=a[:,[0]+[i+1 for i in cols]]
            residual=(aa*x).sum(axis=-1)-b;ix=int(residual.argmax());held.append(dict(n=n,label=r['label'],root_draws=len(F),unique_nodes=len(nodes),constraints=len(b),violating_rows=int((residual>1e-9).sum()),max_violation=float(max(0,residual.max())),witness=meta[ix]))
    # Counterexample family for local constant-payment and the nonnegative cone.
    spread=[]
    for N in [4,16,64,256,1024]:
        # a=sum x_i/(2N), d=parity/(2sqrt N); J/Dmass=log2(N+1).
        spread.append(dict(N=N,Dmass=1/(4*N),J=math.log2(N+1)/(4*N),J_over_Dmass=math.log2(N+1),M_over_Dmass=2))
    # Direct spectral check at N=4 (five-variable real g).
    N=4;x=np.arange(1<<(N+1));a=(N-2*pc(N)[x>>1])/(2*N);d=(-1.)**pc(N)[x>>1]/(2*math.sqrt(N));g=a+(1-2*(x&1))*d
    from numerics import data
    B=data(g)['B'][0];assert abs(B-spread[0]['J'])<1e-12
    Path('induction_audit.json').write_text(json.dumps(dict(primal_replay=out,dual_replay=dualchecks,recursion_explicit_J_max_error=recerr,influence_recursion_max_error=ierr,held_out=held,spread_parity=spread,spread_direct_error=abs(B-spread[0]['J'])),indent=2));print(json.dumps(dict(primal_replay=out,held_out_summary=[{k:v for k,v in r.items() if k!='witness'} for r in held],spread_parity=spread),indent=2),flush=True)
if __name__=='__main__':audit()
