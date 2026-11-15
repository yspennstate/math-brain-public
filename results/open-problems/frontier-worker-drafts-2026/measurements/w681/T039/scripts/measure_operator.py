"""Uncertified Nyström instrument for Appendix A (145)--(152).

No random numbers. Every row is saved immediately. This is not an interval
bound or a proof of an infinite-dimensional operator norm.
"""
import argparse, ast, datetime, hashlib, json, math, os, pathlib, sys, time
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import psutil
psutil.Process().cpu_affinity([2,3])
if psutil.virtual_memory().available < 2*2**30:
    raise SystemExit('Not started: available memory below 2 GiB.')
import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.optimize import brentq
from scipy.special import roots_legendre, erfc, erfcx, ive, i0e

ROOT=pathlib.Path(__file__).resolve().parents[1]
tree=ast.parse((ROOT/'cut_bounds/plur_cert_positive.py').read_text(encoding='utf-8'))
CENTER=np.array(next(ast.literal_eval(n.value) for n in tree.body
                     if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='CENTER' for t in n.targets)))
J1=(9-math.pi*math.sqrt(3))/(4*math.pi**2)

def legendre(n,lo,hi):
    z,w=roots_legendre(n)
    return lo+(z+1)*(hi-lo)/2, w*(hi-lo)/2

def jtilde(rho,x,nv=128):
    """Equation (148), with exp(-q²) absorbed before erfc evaluation."""
    d=1-rho*rho
    alpha=rho/math.sqrt(d)
    q=alpha*np.asarray(x)
    v,wv=legendre(nv,0,2/3)
    c=np.cos(math.pi*v)
    s=np.sin(math.pi*v)
    qq=q[:,None]
    cc=c[None,:]
    ss=s[None,:]
    damp=np.exp(-q*q)
    # exp(-q²) [-psi'(-q c)], avoiding erfcx of a large negative argument.
    neg_dpsi=(math.sqrt(math.pi)*(1+2*(qq*cc)**2)
              *np.exp(-(qq*ss)**2)*erfc(-qq*cc)
              +2*qq*cc*damp[:,None])
    h=math.pi/2 * (neg_dpsi @ (wv*v*(1-1.5*v)*s))
    sq=math.sqrt(math.pi)*(1+2*q*q)*erfcx(q)-2*q
    ans=alpha*(h+J1/2*damp*sq)
    if not np.all(np.isfinite(ans)) or np.min(ans)<=0:
        raise ArithmeticError('Jtilde must be positive and finite')
    return ans

def center(rho,x):
    return np.polynomial.polynomial.polyval(x,CENTER @ np.array([rho**i for i in range(5)]))

def matrix(rho,n=256,cutoff=20,nv=128,centered=True):
    """Symmetric dx kernel after t=x² and weighted normalization.

    A_ij = sqrt(w_i w_j) 2 exp(-(x_i²+x_j²)/2)
           [K_+(x_i²,x_j²)-ell(x_i)-ell(x_j)] / sqrt(Jtilde_i Jtilde_j).
    Mean-zero vector is sqrt(2 w_i) exp(-x_i²/2)/sqrt(Jtilde_i).
    """
    x,wx=legendre(n,0,cutoff)
    v,wv=legendre(nv,0,2/3)
    d=1-rho*rho
    kappa=rho*rho/d
    ss=x[:,None]**2+x[None,:]**2
    a=(2*rho/d)*(x[:,None]*x[None,:])
    exbase=-(0.5+kappa)*ss
    kernel=np.zeros((n,n))
    for u,w in zip(v,wv):
        kernel+=w*(1+1.5*u)*np.exp(exbase+a*math.cos(math.pi*u))
    kernel*=2/d
    kernel-=4*J1/d*a*np.exp(exbase-a)
    jt=jtilde(rho,x,nv)
    if centered:
        ell=center(rho,x)
        kernel-=2*np.exp(-ss/2)*(ell[:,None]+ell[None,:])
    scale=np.sqrt(wx/jt)
    A=kernel*(scale[:,None]*scale[None,:])
    u=np.sqrt(2*wx)*np.exp(-x*x/2)/np.sqrt(jt)
    u/=np.linalg.norm(u)
    Au=A@u
    compressed=A-np.outer(u,Au)-np.outer(Au,u)+(u@Au)*np.outer(u,u)
    return A,compressed,u,x,wx,jt

def measure(rho,n=256,cutoff=20,nv=128,extra=False):
    start=time.perf_counter()
    A,PAP,u,x,wx,jt=matrix(rho,n,cutoff,nv)
    low=float(eigh(PAP,subset_by_index=[0,0],eigvals_only=True,check_finite=False)[0])
    high=float(eigh(PAP,subset_by_index=[n-1,n-1],eigvals_only=True,check_finite=False)[0])
    norm=max(abs(low),abs(high))
    row={'rho':float(rho),'n':n,'cutoff':cutoff,'angular_n':nv,
         'hs_squared':float(np.sum(A*A)),'hs':float(np.linalg.norm(A,'fro')),
         'lambda_min':low,'lambda_max':high,'operator_norm':norm,
         'projection_residual':float(np.linalg.norm(PAP@u)),
         'min_Jtilde':float(np.min(jt)),'elapsed_seconds':time.perf_counter()-start}
    if extra:
        _,Praw,_,_,_,_=matrix(rho,n,cutoff,nv,False)
        row['centering_projection_difference_max']=float(np.max(np.abs(Praw-PAP)))
        vals,vecs=eigh(PAP,subset_by_index=[n-1,n-1],check_finite=False)
        f=vecs[:,0]
        row['top_eigenvector_mean_constraint']=float(abs(u@f))
        row['top_eigenvector_residual']=float(np.linalg.norm(PAP@f-vals[0]*f))
    return row

def save(row,dest='logs/operator_rows.jsonl'):
    row['at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    with (ROOT/dest).open('a',encoding='utf-8') as f:
        f.write(json.dumps(row,allow_nan=False)+'\n')
    print(json.dumps(row,allow_nan=False),flush=True)

def direct_j(rho,x,n=400,nv=192,cutoff=30):
    """Independent radial marginal of (144)+(102), not erfc formula (148)."""
    y,wy=legendre(n,0,cutoff)
    v,wv=legendre(nv,0,2/3)
    d=1-rho*rho
    k=rho*rho/d
    a=2*rho*x*y/d
    ex=-k*x*x-(1+k)*y*y
    integrand=np.zeros(n)
    for u,w in zip(v,wv):
        integrand+=w*.5*(1-3*u)*np.exp(ex+a*math.cos(math.pi*u))
    integrand+=J1/2*a*np.exp(ex-a)
    return float(np.dot(2*y*wy,integrand)/d/x)

def control():
    for rho in (.4,.6,.8,.95):
        for x in (.1,.5,1,2,4):
            analytic=float(jtilde(rho,np.array([x]),256)[0])
            marginal=direct_j(rho,x)
            save({'control':'independent_J_marginal','rho':rho,'x':x,
                  'formula_148':analytic,'radial_marginal':marginal,
                  'absolute_difference':abs(analytic-marginal),
                  'relative_difference':abs(analytic-marginal)/analytic},'logs/operator_controls.jsonl')
            if not math.isclose(analytic,marginal,rel_tol=2e-10,abs_tol=2e-12):
                raise AssertionError('Independent J normalization control failed')
    for rho in (.4,.95):
        save(measure(rho,256,20,128,True),'logs/operator_controls.jsonl')

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['control','sweep','refine','roots'])
    parser.add_argument('--n',type=int,default=256)
    parser.add_argument('--cutoff',type=float,default=20)
    parser.add_argument('--angular-n',type=int,default=128)
    parser.add_argument('--rho',type=float,nargs='*')
    args=parser.parse_args()
    reproduction=json.loads((ROOT/'logs/reproduction_result.json').read_text(encoding='utf-8'))
    if not reproduction['reproduced']:
        raise SystemExit('Target 1(a) did not reproduce: no extension permitted.')
    route='Target 1(b,c): published-center weighted HS and mean-zero compressed positive radial operator, Nystrom refinement.'
    with (ROOT/'ROUTES.jsonl').open('a',encoding='utf-8') as f:
        f.write(json.dumps({'row':'T039','route':route,'status':'live','why':'Target 1 instrument; no certified extension or new theorem claimed.','evidence':'logs/route_bc_check.txt','at':datetime.datetime.now(datetime.timezone.utc).isoformat()})+'\n')
    metadata={'command':sys.argv,'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,
              'script_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
              'positive_source_sha256':hashlib.sha256((ROOT/'cut_bounds/plur_cert_positive.py').read_bytes()).hexdigest(),
              'paper_sha256':hashlib.sha256((ROOT/'papers/2608.00333.pdf').read_bytes()).hexdigest(),
              'rng':'none','seed':None,'cpu_affinity':psutil.Process().cpu_affinity(),
              'thread_caps':'BLAS, OMP, MKL, Numexpr = 1','arithmetic':'IEEE-754 binary64, uncertified',
              'memory_estimate_bytes':args.n**2*8*24,'reproduction':'refinement comparison, not a rigorous tolerance'}
    (ROOT/f'logs/operator_{args.mode}_{args.n}_{args.cutoff:g}_metadata.json').write_text(json.dumps(metadata,indent=2),encoding='utf-8')
    if args.mode=='control':
        control()
    elif args.mode=='sweep':
        for rho in (args.rho if args.rho else np.linspace(.4,.95,56)):
            save(measure(float(rho),args.n,args.cutoff,args.angular_n))
    elif args.mode=='refine':
        for rho in (args.rho if args.rho else [.4,.5,.6,.7,.8,.9,.95]):
            save(measure(rho,args.n,args.cutoff,args.angular_n,True))
    elif args.mode=='roots':
        rows=[json.loads(s) for s in (ROOT/'logs/operator_rows.jsonl').read_text(encoding='utf-8').splitlines()]
        grid=sorted({r['rho']:r for r in rows if r['n']==256 and r['cutoff']==20}.values(),key=lambda r:r['rho'])
        for label,key in [('rho_HS','hs'),('rho_op','operator_norm')]:
            brackets=[(a['rho'],b['rho']) for a,b in zip(grid,grid[1:]) if (a[key]-2)*(b[key]-2)<0]
            if not brackets:
                save({'root':label,'status':'no crossing on sweep','range':[.4,.95]},'logs/operator_roots.jsonl')
                continue
            for lo,hi in brackets:
                def objective(r):
                    row=measure(r,args.n,args.cutoff,args.angular_n)
                    save(row,'logs/operator_root_evaluations.jsonl')
                    return row[key]-2
                root=brentq(objective,lo,hi,xtol=2e-10)
                save({'root':label,'rho':root,'bracket':[lo,hi],'n':args.n,'cutoff':args.cutoff,
                      'angular_n':args.angular_n,'status':'uncertified double precision root'},'logs/operator_roots.jsonl')

if __name__=='__main__': main()
