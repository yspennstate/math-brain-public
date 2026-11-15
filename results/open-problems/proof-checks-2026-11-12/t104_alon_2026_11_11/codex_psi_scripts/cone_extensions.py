"""Small exact extension experiments. Each invocation has a 240 second alarm."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'): os.environ[k]='1'
import sympy as sp
import time, signal, sys, json, resource
from cone_certificate import rays,log

def timeout(*args):raise TimeoutError('240-second limit')
signal.signal(signal.SIGALRM,timeout);signal.alarm(240)
try:resource.setrlimit(resource.RLIMIT_DATA,(750*1024**2,750*1024**2))
except (ValueError,OSError) as exc:print('Memory rlimit unavailable:',str(exc),flush=True)
n=int(sys.argv[1]); start=time.monotonic()
log(f'## Exact cone extension n={n} (cone_extensions.py {n})')
try:
    rr,labels=rays(n); z=sp.symbols('z:'+str(len(rr)))
    xx=[sp.Poly(sum(v[i]*t for v,t in zip(rr,z)),*z,domain=sp.ZZ) for i in range(n)]
    a=xx[0];T=sum(v*v for v in xx);P=sum(v**3 for v in xx);Q=sum(v**4 for v in xx)
    K=(n*n-6*n+6)*T*T+2*n*Q
    H=K*(n*(n-1)*(T*T-Q+2*a*P-2*a*a*T)+T*T)+2*(n-3)*(n*(n-1)*a*a-T)*(n*Q*T-T**3-n*P*P)
    neg=[(m,int(c)) for m,c in H.terms() if c<0]
    print('rays',len(rr),'terms',len(H.terms()),'negative',len(neg),'seconds',time.monotonic()-start,'peak RSS bytes (macOS)',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,flush=True)
    print('negative examples',neg[:5],flush=True)
    with open(f'cone_extension_{n}.json','w') as f:json.dump({'n':n,'rays':[[int(v) for v in r] for r in rr],'negative':neg,'terms':len(H.terms())},f)
    log(f'EXACT n={n}: {len(rr)} generating rays, {len(H.terms())} nonzero coefficients, {len(neg)} negative. Elapsed {time.monotonic()-start:.2f} s. '+('Coefficient certificate succeeds.' if not neg else 'This coefficient certificate fails.'))
except TimeoutError:
    log(f'Exact cone extension n={n} FAILED to finish within 240 seconds; no conclusion.')
