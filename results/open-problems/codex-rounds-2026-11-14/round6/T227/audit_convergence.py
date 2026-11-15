"""Independent Decimal forward-mode AD audit through escape and continuation."""
import json
import os
import resource
import time
from decimal import Decimal as D, localcontext

resource.setrlimit(resource.RLIMIT_CPU,(120,120))
start=time.monotonic()
assert os.environ['OMP_NUM_THREADS']=='1'
assert os.getpriority(os.PRIO_PROCESS,0)>=15

class Dual:
    def __init__(self,v,d=0): self.v,self.d=D(v),D(d)
    def __add__(self,y):
        if not isinstance(y,Dual): y=Dual(y)
        return Dual(self.v+y.v,self.d+y.d)
    __radd__=__add__
    def __mul__(self,y):
        if not isinstance(y,Dual): y=Dual(y)
        return Dual(self.v*y.v,self.d*y.v+self.v*y.d)
    __rmul__=__mul__
    def tanh(self):
        e=(2*self.v).exp()
        v=(e-1)/(e+1)
        # Stable sech², independent of subtracting v² from one.
        q=4*e/(e+1)**2
        return Dual(v,self.d*q)

def forward(x,m):
    a,b,c=x[:m],x[m:m+m*m],x[m+m*m:]
    u=[cj.tanh() for cj in c]
    v=[(sum((b[i*m+j]*u[j] for j in range(m)),Dual(0))
        * (1/D(m).sqrt())).tanh() for i in range(m)]
    f=sum((a[i]*v[i] for i in range(m)),Dual(0))*(1/D(m))
    return f,[vi.v for vi in v]

def all_gradients(x,m):
    f,v=forward([Dual(xi) for xi in x],m)
    g=[]
    for k in range(len(x)):
        fk,_=forward([Dual(xi,int(k==j)) for j,xi in enumerate(x)],m)
        assert fk.v==f.v
        g.append(fk.d)
    return f.v,v,g

audits=[]
for precision in (80,110):
    with localcontext() as ctx:
        ctx.prec=precision
        m=4
        x0=([D(8)]*m+
            [D(-1 if (j-i)%m<2 else 1)/2 for i in range(m) for j in range(m)]
            +[D(2)]*m)
        x0[m]+=D('1e-25')
        for hs in ('.9','1.1','1.99'):
            h=D(hs)
            x=x0[:]
            e0=sum(ai*ai for ai in x[:m])/m
            weighted=sumsq=D(0)
            maxerr=D(0)
            exit_t=None
            residuals=[]
            for t in range(60):
                f,v,g=all_gradients(x,m)
                residuals.append(str(f))
                if exit_t is None and abs(f)>=D('.02'): exit_t=t
                q=sum(vi*vi for vi in v)/m
                e=sum(ai*ai for ai in x[:m])/m
                y=[xi-m*h*f*gi for xi,gi in zip(x,g)]
                ep=sum(ai*ai for ai in y[:m])/m
                decrement=h*(2-h*q)*f*f
                err=abs(ep-e+decrement)
                maxerr=max(maxerr,err)
                tol=D(10)**(-precision+6)
                assert err<tol
                assert ep<=e+tol
                weighted+=decrement
                sumsq+=f*f
                assert abs(e0-ep-weighted)<100*tol
                assert sumsq<=e0/(h*(2-h))+100*tol
                x=y
            assert exit_t is not None
            audits.append(dict(precision=precision,h=hs,exit_t=exit_t,
                               initial_F=residuals[0],last_F=residuals[-1],
                               max_identity_error=str(maxerr),sum_F2=str(sumsq),
                               residuals=residuals))

comparisons=[]
with localcontext() as ctx:
    ctx.prec=110
    for low in audits[:3]:
        high=next(a for a in audits if a['precision']==110 and a['h']==low['h'])
        assert low['exit_t']==high['exit_t']
        discrepancy=max(abs(D(x)-D(y)) for x,y in zip(low['residuals'],high['residuals']))
        assert discrepancy<D('1e-40')
        comparisons.append(dict(h=low['h'],max_residual_discrepancy=str(discrepancy)))

# In a native tanh state, a nonzero label can increase output energy.
with localcontext() as ctx:
    ctx.prec=80
    m=2
    x=[D(0)]*m+[D(1)]*(m*m)+[D(2)]*m
    f,v,g=all_gradients(x,m)
    assert f==0
    y=[xi-D(m)*(f-1)*gi for xi,gi in zip(x,g)]
    label_counterexample=sum(ai*ai for ai in y[:m])/m
    assert label_counterexample>0

summary=dict(status='PASS',method='Decimal forward-mode AD in all Euclidean coordinates',
             trajectories=len(audits),steps_per_trajectory=60,
             precision_comparisons=comparisons,
             nonzero_label_energy_increase=str(label_counterexample),
             nice=os.getpriority(os.PRIO_PROCESS,0),
             rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
             seconds=time.monotonic()-start)
assert summary['rss_bytes']<1_000_000_000
with open('convergence_audit.json','w') as out:
    json.dump(dict(summary=summary,audits=audits),out,indent=2)
print(json.dumps(summary,indent=2))
