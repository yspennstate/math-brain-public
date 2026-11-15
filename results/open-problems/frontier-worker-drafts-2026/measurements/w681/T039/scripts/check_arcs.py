"""Uncertified grids for the stronger scalar bound, (139), and (142).

Equation (139) itself is rho-independent. For each requested rho the a grid
spans all a induced by x,y in [0,7], plus logarithmic small-a coverage.
"""
import argparse, datetime, hashlib, json, math, os, pathlib, sys, time
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import psutil
psutil.Process().cpu_affinity([2,3])
if psutil.virtual_memory().available < 2*2**30:
    raise SystemExit('Not started: available memory below 2 GiB.')
import numpy as np
import scipy
from scipy.special import ive,i0e
ROOT=pathlib.Path(__file__).resolve().parents[1]
J1=(9-math.pi*math.sqrt(3))/(4*math.pi**2)

def arc_matrix(a,p,multiplier=1):
    m=np.arange(1,int(math.ceil(10*math.sqrt(max(a,1))+30))*multiplier+1,dtype=float)
    ratio=ive(m,a)/i0e(a)
    s=np.sin(math.pi*p[:,None]*m[None,:])
    U=s*np.sqrt(2*ratio)/(math.pi*m)
    L=np.outer(p,p)+U@U.T
    b=1/3
    sb=np.sin(math.pi*b*m)
    k=b*b+float(np.sum(2*ratio*sb*sb/(math.pi*m)**2))
    P=b+float(np.sum(ratio*np.sin(2*math.pi*b*m)/(math.pi*m)))
    tau=4*P-3*k
    w=3*k-P
    return L,k,tau,w,len(m)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--rho',type=float,nargs='+',default=[.45,.5,.6,.7,.8,.9])
    parser.add_argument('--p-panels',type=int,default=600)
    parser.add_argument('--simplex-denominator',type=int,default=30)
    args=parser.parse_args()
    baseline=json.loads((ROOT/'logs/reproduction_result.json').read_text(encoding='utf-8'))
    if not baseline['reproduced']: raise SystemExit('1(a) failed; do not extend.')
    route='Target 1(d): rho-independent aligned-arc scalar and simplex grids, including sharpened bound (142).'
    with (ROOT/'ROUTES.jsonl').open('a',encoding='utf-8') as f:
        f.write(json.dumps({'row':'T039','route':route,'status':'live','why':'Instrument only; grid is not a proof for all a,p,q. Lemma A.2 states all a>=0, independently of rho.','evidence':'logs/route_d_check.txt','at':datetime.datetime.now(datetime.timezone.utc).isoformat()})+'\n')
    metadata={'command':sys.argv,'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,
              'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'paper_sha256':hashlib.sha256((ROOT/'papers/2608.00333.pdf').read_bytes()).hexdigest(),
              'rng':'none','seed':None,'cpu_affinity':[2,3],'threads':1,'status':'numerical evidence',
              'a_grid':'81 per rho: zero, 40 uniform positive values to 98*rho/(1-rho²), 40 geometric values from 1e-7 to same maximum',
              'p_grid':'uniform scalar grid plus 1/3 and symmetric near-1/3 perturbations 1e-8 through .02; all simplex grid coordinates',
              'hypotheses':'p,q in [0,1] for stronger scalar inequality; p,q in Delta_3 for equations 139 and 142',
              'tolerance':1e-10,'reproduction':'double precision comparison; no outward rounding, no theorem claim'}
    (ROOT/'logs/arc_metadata.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
    N=args.simplex_denominator
    simplex=np.array([(i,j,N-i-j) for i in range(N+1) for j in range(N+1-i)],dtype=float)/N
    pert=np.array([1e-8,1e-6,1e-4,.001,.005,.02])
    p=np.unique(np.r_[np.linspace(0,1,args.p_panels+1),1/3,1/3-pert,1/3+pert,simplex.ravel()])
    # Use nearest coordinate rather than requiring identical binary64 rational division.
    ind=np.argmin(np.abs(simplex[:,:,None]-p[None,None,:]),axis=2)
    xx=simplex-1/3
    inner=xx@xx.T
    norms=np.sum(xx*xx,axis=1)
    normsum=norms[:,None]+norms[None,:]
    existing=set()
    dest=ROOT/'logs/arc_rows.jsonl'
    if dest.exists():
        for s in dest.read_text(encoding='utf-8').splitlines():
            r=json.loads(s); existing.add((r['rho'],r['a'],r['p_panels'],r['simplex_denominator']))
    for rho in args.rho:
        start=time.perf_counter()
        amax=98*rho/(1-rho*rho)
        ag=np.unique(np.r_[0,np.linspace(0,amax,41)[1:],np.geomspace(1e-7,amax,41)])
        worst={'scalar':-math.inf,'139':-math.inf,'142':-math.inf}
        for ia,a in enumerate(ag):
            a=float(a)
            if (rho,a,args.p_panels,N) in existing: continue
            L,k,tau,w,terms=arc_matrix(a,p)
            scalar=L-tau*np.outer(p,p)-w*(p[:,None]*(1-p[:,None])+p[None,:]*(1-p[None,:]))
            si=np.unravel_index(np.argmax(scalar),scalar.shape)
            lhs=sum(L[ind[:,i,None],ind[None,:,i]] for i in range(3))-3*k
            margin139=lhs-tau*inner+w*normsum
            theta=J1/2*a*math.exp(-2*a)/float(i0e(a))
            margin142=lhs-(tau-4*theta)*inner+(w+theta)*normsum
            vi=np.unravel_index(np.argmax(margin139),margin139.shape)
            vv=np.unravel_index(np.argmax(margin142),margin142.shape)
            row={'rho':rho,'a':a,'a_max':amax,'p_panels':args.p_panels,'scalar_coordinates':len(p),
                 'simplex_denominator':N,'simplex_vectors':len(simplex),'fourier_terms':terms,
                 'tau':tau,'w':w,'max_scalar_violation':float(scalar[si]),
                 'scalar_argmax':[float(p[si[0]]),float(p[si[1]])],
                 'max_139_violation':float(margin139[vi]),'139_argmax':[simplex[vi[0]].tolist(),simplex[vi[1]].tolist()],
                 'max_142_violation':float(margin142[vv]),'142_argmax':[simplex[vv[0]].tolist(),simplex[vv[1]].tolist()],
                 'status':'numerical evidence','at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
            if ia in (0,len(ag)//2,len(ag)-1):
                doubled,_,_,_,_=arc_matrix(a,p,2)
                row['doubled_fourier_max_difference']=float(np.max(np.abs(L-doubled)))
            with dest.open('a',encoding='utf-8') as f:f.write(json.dumps(row,allow_nan=False)+'\n')
            worst={label:max(worst[label],row[key]) for label,key in [('scalar','max_scalar_violation'),('139','max_139_violation'),('142','max_142_violation')]}
            if max(worst.values())>1e-10:
                (ROOT/'logs/arc_failure.json').write_text(json.dumps(row,indent=2),encoding='utf-8')
                print('FAILURE CANDIDATE',json.dumps(row),flush=True)
                raise SystemExit(1)
        summary={'rho':rho,'a_range':[0,amax],'a_values':len(ag),'scalar_pairs_per_a':len(p)**2,
                 'simplex_pairs_per_a':len(simplex)**2,'worst_violation':worst,
                 'elapsed_seconds':time.perf_counter()-start,'status':'no grid violation above 1e-10'}
        with (ROOT/'logs/arc_summary.jsonl').open('a',encoding='utf-8') as f:f.write(json.dumps(summary)+'\n')
        print(json.dumps(summary),flush=True)

if __name__=='__main__': main()
