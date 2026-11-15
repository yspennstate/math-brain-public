"""Independent exact integration and direct Haar quadrature for PROOF.md."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import json, math, resource, signal, sys, time
from fractions import Fraction as F
from pathlib import Path
signal.alarm(120)
START=time.monotonic()
assert os.getpriority(os.PRIO_PROCESS,0)>=15
import numpy as np
np.seterr(all="raise")

def matmul(a,b):
    return np.einsum("...ij,...jk->...ik",a,b,optimize=False)

def avg(weights, values):
    return math.fsum(float(w)*float(v) for w,v in zip(weights,values))

# Polynomials in cos(theta),sin(theta), with exact rational coefficients.
class P:
    def __init__(self, x=0):
        self.d=x if isinstance(x,dict) else {(0,0):F(x)}
    def __add__(self,b):
        b=b if isinstance(b,P) else P(b)
        d=self.d.copy()
        for k,v in b.d.items(): d[k]=d.get(k,F(0))+v
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({k:-v for k,v in self.d.items()})
    def __sub__(self,b): return self+-as_p(b)
    def __rsub__(self,b): return as_p(b)+-self
    def __mul__(self,b):
        b=as_p(b);d={}
        for (i,j),v in self.d.items():
            for (k,l),w in b.d.items():
                z=(i+k,j+l);d[z]=d.get(z,F(0))+v*w
        return P(d)
    __rmul__=__mul__
    def integral(self):
        ans=F(0)
        for (i,j),v in self.d.items():
            if i%2 or j%2: continue
            num=math.prod(range(1,i,2))*math.prod(range(1,j,2))
            den=math.prod(range(2,i+j+1,2))
            ans+=v*F(num,den)
        return ans

def as_p(x): return x if isinstance(x,P) else P(x)
def tr(x): return sum(x[i][i] for i in range(len(x)))
def transpose(x): return list(map(list,zip(*x)))
def mm(x,y): return [[sum(a*b for a,b in zip(row,col)) for col in zip(*y)] for row in x]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]

def prediction(X,e,u,A):
    """Formulas (3)-(5), using rational arithmetic."""
    n=len(e);m=n-1;T=tr(X);Q=tr(mm(X,X))
    xe=[sum(x*y for x,y in zip(row,e)) for row in X]
    alpha=sum(x*y for x,y in zip(e,xe));gamma=sum(x*x for x in xe)
    beta=gamma-alpha*alpha;t=T-alpha;q=Q-alpha*alpha-2*beta
    c=((m+1)*t*t-2*q)/F(m*(m-1)*(m+2))
    d=(m*q-t*t)/F(m*(m-1)*(m+2))
    k=sum(A);h=sum(x*x for x in A)
    s=sum(a*x*x for a,x in zip(A,u));r=sum(a*a*x*x for a,x in zip(A,u))
    p=k-s;w=h-2*r+s*s;z=r-s*s
    return (alpha*s+t*p/m,
            alpha*alpha*s*s+2*((beta+alpha*t)*z+beta*s*p)/m+(c+d)*w+d*p*p,
            alpha*alpha*s*s+2*alpha*t*s*p/m+4*beta*z/m+c*p*p+2*d*w)

def exact_circle():
    e=[F(0),F(0),F(1)]
    u=[F(2,3),F(1,3),F(2,3)]
    v=[x-y for x,y in zip(e,u)];vv=sum(x*x for x in v)
    H=[[F(i==j)-2*v[i]*v[j]/vv for j in range(3)] for i in range(3)]
    M=[[F(1),F(1,3),F(-1,4)],[F(0),F(3,2),F(1,5)],[F(1,2),F(0),F(4,3)]]
    generic=mm(M,transpose(M))
    cases=[('generic',generic),('identity',eye(3)),('zero',[[F(0)]*3 for _ in range(3)]),
           ('aligned_rank_one',[[a*b for b in e] for a in e]),
           ('transverse_rank_one',[[F(i==0 and j==0) for j in range(3)] for i in range(3)])]
    records=[]
    for name,X in cases:
        for A in ([F(2),F(1,2),F(3,4)],[F(1)]*3,[F(0),F(2),F(0)]):
            vals=[F(0)]*3
            for sign in (-1,1):
                co=P({(1,0):F(1)});si=P({(0,1):F(1)})
                rot=[[sign*co,-si,P(0)],[sign*si,co,P(0)],[P(0),P(0),P(1)]]
                O=mm(H,rot);B=mm(mm(O,X),transpose(O))
                t=sum(A[i]*B[i][i] for i in range(3))
                q=sum(A[i]*A[j]*B[i][j]*B[j][i] for i in range(3) for j in range(3))
                for j,z in enumerate((t,q,t*t)): vals[j]+=z.integral()/2
            pred=prediction(X,e,u,A)
            assert tuple(vals)==pred,(name,vals,pred)
            records.append({'case':name,'A':list(map(str,A)),'moments':list(map(str,vals))})
    return records

def sphere_grid(nt,nphi):
    t,w=np.polynomial.legendre.leggauss(nt)
    phi=2*np.pi*np.arange(nphi)/nphi
    t=np.repeat(t,nphi);weights=np.repeat(w/2/nphi,nphi)
    phi=np.tile(phi,nt)
    u=np.column_stack((np.sqrt(1-t*t)*np.cos(phi),np.sqrt(1-t*t)*np.sin(phi),t))
    return t,phi,u,weights

def conditional_average(X,qs,nt,nphi):
    t,phi,u,weights=sphere_grid(nt,nphi)
    n=3;m=2;T=np.trace(X);Q=np.sum(X*X);alpha=X[2,2];gamma=np.sum(X[:,2]**2)
    beta=gamma-alpha*alpha;T0=T-alpha;Q0=Q-alpha*alpha-2*beta
    c=((m+1)*T0*T0-2*Q0)/(m*(m-1)*(m+2));d=(m*Q0-T0*T0)/(m*(m-1)*(m+2))
    out=[]
    for q in qs:
        raw=np.cosh(np.sqrt(n*q)*u)**-4
        mu=avg(weights,raw[:,2]);A=raw/mu
        k=A.sum(1);h=(A*A).sum(1);s=(u*u*A).sum(1);r=(u*u*A*A).sum(1)
        p=k-s;w=h-2*r+s*s;z=r-s*s
        pred=np.array((avg(weights,alpha*s+T0*p/m),
            avg(weights,alpha*alpha*s*s+2*((beta+alpha*T0)*z+beta*s*p)/m+(c+d)*w+d*p*p),
            avg(weights,alpha*alpha*s*s+2*alpha*T0*s*p/m+4*beta*z/m+c*p*p+2*d*w)))
        # Independent first-trace formula (13): 1D sphere marginal only.
        y=3*u[:,2]**2;x=np.sqrt(q*y)
        ratio=np.divide(np.tanh(x),x,out=np.ones_like(x),where=x!=0)
        kappa=4*q/((n-1)*mu)*(avg(weights,y*(1-y/n)*np.cosh(x)**-4*ratio))
        assert abs(pred[0]-(T-kappa*(n*alpha-T)))<5e-12
        assert 0<=kappa<=8*q/(n+2)+1e-14
        lin=np.array((-4*(n*alpha-T)/(n+2),-8*(n*gamma-Q)/(n+2),-8*T*(n*alpha-T)/(n+2)))
        base=np.array((T,Q,T*T));rem=np.abs(pred-base-q*lin)
        limits=q*q*np.array((72*abs(n*alpha-T)/(n+2),1344*Q,1344*T*T))
        assert np.all(rem<=limits+1e-11),(q,rem,limits)
        out.append({'q':q,'mu':mu,'predicted':pred.tolist(),'kappa':kappa,'linear_coefficients':lin.tolist(),
                    'remainders':rem.tolist(),'remainder_bounds':limits.tolist()})
    return out

def direct_haar(X,q,mu,nt,nphi,npsi=8):
    """Direct Euler O(3) integration; no conditional tensor formulas."""
    t,phi,u,weights=sphere_grid(nt,nphi)
    # O=Rz(phi)Ry(theta)Rz(psi)diag(sign,1,1), theta=acos(t).
    ct=t;st=np.sqrt(1-t*t);cp=np.cos(phi);sp=np.sin(phi)
    base=np.zeros((len(t),3,3))
    base[:,0,0]=cp*ct;base[:,0,1]=-sp;base[:,0,2]=cp*st
    base[:,1,0]=sp*ct;base[:,1,1]=cp;base[:,1,2]=sp*st
    base[:,2,0]=-st;base[:,2,2]=ct
    A=np.cosh(np.sqrt(3*q)*u)**-4/mu
    total=np.zeros(3)
    for psi in 2*np.pi*np.arange(npsi)/npsi:
        c=math.cos(psi);s=math.sin(psi)
        R=np.array([[c,-s,0],[s,c,0],[0,0,1.]])
        for sign in (-1,1):
            O=matmul(base,R);O[:,:,0]*=sign
            B=matmul(matmul(O,X),O.transpose(0,2,1))
            trace=(A*np.diagonal(B,axis1=1,axis2=2)).sum(1)
            second=(A[:,:,None]*A[:,None,:]*B*B).sum((1,2))
            total+=np.array((avg(weights,trace),avg(weights,second),avg(weights,trace*trace)))/(2*npsi)
    return total

def sphere_marginal_quadrature(n, nodes):
    # Symmetric Gegenbauer Jacobi matrix, lambda=(n-2)/2.
    lam=(n-2)/2
    k=np.arange(1,nodes,dtype=float)
    off=np.sqrt(k*(k+2*lam-1)/(4*(k+lam)*(k+lam-1)))
    jac=np.diag(off,1)+np.diag(off,-1)
    t,vec=np.linalg.eigh(jac);w=vec[0]**2
    assert abs(avg(w,t*t)-1/n)<1e-14
    assert abs(avg(w,t**4)-3/(n*(n+2)))<1e-14
    return t,w


def accumulation_check():
    rng=np.random.default_rng(2473003)
    records=[]
    # Ordinary tanh, gain 1: q_l <= initial radius / n deterministically.
    # This tests the genuinely dependent multi-layer model, with only a scalar
    # post-normalization of its Jacobian (no change to its forward propagation).
    samples=1200;depth=30;epsilon=.001
    for n in (4,8,16):
        t,sphere_w=sphere_marginal_quadrature(n,24)
        t2,w2=sphere_marginal_quadrature(n,48)
        mu24=avg(sphere_w,np.cosh(math.sqrt(n*epsilon)*t)**-4)
        mu48=avg(w2,np.cosh(math.sqrt(n*epsilon)*t2)**-4)
        assert abs(mu24-mu48)<1e-13
        h=np.zeros((samples,n));h[:,0]=math.sqrt(n*epsilon)
        J=np.broadcast_to(np.eye(n),(samples,n,n)).copy();scalar=np.ones(samples)
        max_q=0.
        for layer in range(depth):
            q=(h*h).sum(1)/n;max_q=max(max_q,float(q.max()))
            assert max_q<=epsilon*(1+1e-12)
            mu=(np.cosh(np.sqrt(n*q[:,None])*t[None,:])**-4*sphere_w[None,:]).sum(1)
            O,R=np.linalg.qr(rng.standard_normal((samples,n,n)))
            signs=np.where(np.diagonal(R,axis1=1,axis2=2)>=0,1.,-1.)
            O*=signs[:,None,:]
            z=np.einsum('bij,bj->bi',O,h)
            gates=1/np.cosh(z)**2
            J=gates[:,:,None]*(matmul(O,J))
            h=np.tanh(z);scalar*=mu
        X=(matmul(J,J.transpose(0,2,1)))/scalar[:,None,None]
        obs=((X-np.eye(n))**2).sum((1,2))/n
        bound=(6*depth*epsilon/(n+2)+2904*depth*epsilon**2)*math.exp(12*depth*epsilon/(n+2)+2760*depth*epsilon**2)
        se=obs.std(ddof=1)/math.sqrt(samples)
        assert obs.mean()+6*se<bound
        records.append({'n':n,'L':depth,'samples':samples,'epsilon':epsilon,'max_q':max_q,
                        'normalized_distortion_mean':float(obs.mean()),'standard_error':float(se),
                        'theorem_bound':bound,'marginal_quadrature_difference':abs(mu24-mu48),'scalar_gain_mean':float(scalar.mean())})
        print(f'Actual tanh n={n}, L={depth}: mean normalized Z={obs.mean():.6g}, bound {bound:.6g}, mean S={scalar.mean():.6g}')
    return records


def main():
    exact=exact_circle()
    print(f'Exact residual O(2) polynomial integrations: {len(exact)} passed')
    M=np.array([[1.,1/3,-1/4],[0.,1.5,.2],[.5,0.,4/3]])
    X=matmul(M,M.T)
    qs=[0.,1e-5,2e-5,1e-4,.001,.01,.1,.25]
    low=conditional_average(X,qs,24,48);high=conditional_average(X,qs,48,96)
    quadrature=max(np.max(np.abs(np.array(a['predicted'])-b['predicted'])) for a,b in zip(low,high))
    assert quadrature<1e-9,quadrature
    direct=[]
    for record in high:
        val=direct_haar(X,record['q'],record['mu'],32,64)
        err=np.max(np.abs(val-record['predicted']))
        assert err<1e-9,err
        direct.append({'q':record['q'],'direct':val.tolist(),'max_error':err})
    print(f'Direct Haar O(3) tanh quadrature: {len(direct)} cases passed; max error {max(x["max_error"] for x in direct):.3g}')
    print(f'24x48 versus 48x96 sphere quadrature: max difference {quadrature:.3g}')
    # Extrapolated first derivative cancels the O(q^2) term of each moment.
    base=np.array(high[0]['predicted']);q=high[1]['q']
    der=(4*np.array(high[1]['predicted'])-np.array(high[2]['predicted'])-3*base)/(2*q)
    theory=np.array(high[1]['linear_coefficients']);derr=np.max(np.abs(der-theory))
    assert derr<2e-6,(der,theory)
    print('Extrapolated derivatives:',der.tolist())
    print('Exact linear coefficients:',theory.tolist())
    print(f'Max derivative difference: {derr:.3g}; all explicit remainder bounds passed')
    # Test every dimension entering the tensor formula by residual Haar Monte Carlo.
    rng=np.random.default_rng(2470315);mc=[]
    for n in (4,7):
        m=n-1;N=10000
        u=rng.normal(size=n);u/=np.linalg.norm(u);e=np.eye(n)[-1]
        v=e-u;H=np.eye(n)-2*np.outer(v,v)/(v@v)
        M=rng.normal(size=(n,n));X=matmul(M,M.T)/n
        A=np.cosh(np.sqrt(.1*n)*u)**-4
        R,tri=np.linalg.qr(rng.normal(size=(N,m,m)))
        signs=np.where(np.diagonal(tri,axis1=1,axis2=2)>=0,1.,-1.)
        R*=signs[:,None,:]
        O=np.zeros((N,n,n));O[:,:m,:m]=R;O[:,-1,-1]=1;O=matmul(H,O)
        B=matmul(matmul(O,X),O.transpose(0,2,1))
        t=(A*np.diagonal(B,axis1=1,axis2=2)).sum(1)
        s=(A[:,None]*A[None,:]*B*B).sum((1,2))
        obs=np.column_stack((t,s,t*t));mean=obs.mean(0);se=obs.std(0,ddof=1)/math.sqrt(N)
        pred=np.asarray(prediction(X.tolist(),e.tolist(),u.tolist(),A.tolist()),dtype=float)
        err=np.abs(mean-pred)/se
        assert max(err)<6,err
        mc.append({'n':n,'samples':N,'predicted':pred.tolist(),'mean':mean.tolist(),'se':se.tolist(),'error_in_se':err.tolist()})
        print(f'Residual Haar O({m}) simulation: max discrepancy {max(err):.3f} SE')
    accumulation=accumulation_check()
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak=peak if sys.platform=='darwin' else 1024*peak
    assert peak<1024**3
    results={'exact_circle':exact,'tanh':high,'direct_haar':direct,'quadrature_difference':quadrature,
             'derivative_estimate':der.tolist(),'derivative_max_error':derr,'monte_carlo':mc,
             'actual_network_accumulation':accumulation,'runtime_seconds':time.monotonic()-START,'peak_rss_bytes':peak,
             'niceness':os.getpriority(os.PRIO_PROCESS,0),'numpy_version':np.__version__,
             'thread_environment':{k:os.environ[k] for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS')}}
    Path('results.json').write_text(json.dumps(results,indent=2)+'\n')
    print(f'Niceness {results["niceness"]}; peak RSS {peak/1024**2:.1f} MiB; runtime {results["runtime_seconds"]:.2f} s')
    print('All dependent-gate verification checks passed')
if __name__=='__main__': main()
