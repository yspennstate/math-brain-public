"""Independent A031 audit; only stdlib, exact finite algebra, bounded domain."""
from fractions import Fraction as F
from pathlib import Path
import json, math, sys, time, hashlib

ROOT = Path(__file__).resolve().parents[1]
checks = nodes = trees = ghosts = biased = calibrations = 0
started = time.monotonic()
def ok(x):
    global checks
    checks += 1
    assert x, (checks, nodes)
    if checks % 4096 == 0:
        assert time.monotonic()-started < (55 if MODE=='pilot' else 120)

def spectrum(table):
    a=list(table); n=len(a); step=1
    while step<n:
        for k in range(0,n,2*step):
            for j in range(k,k+step):
                u,v=a[j],a[j+step]; a[j],a[j+step]=u+v,u-v
        step*=2
    return [F(x*x,n*n) for x in a]

def marginal(v,bit):
    out=[F(0)]*(len(v)//2)
    for j,x in enumerate(v):
        k=(j & ((1<<bit)-1)) | ((j>>(bit+1))<<bit)
        out[k]+=x
    return out

def entropy(p): return -sum(float(x)*math.log2(float(x)) for x in p if x)
def div(p,q): return sum(float(x)*math.log2(float(x/y)) for x,y in zip(p,q) if x)

def inherit(p,children,q,bit,split):
    global ghosts,biased
    m=marginal(p,bit); r=marginal(q,bit); s=sum(q)
    raw=[]
    for b,pb in enumerate(children):
        raw.append([rr*pp/mm if mm else 2*rr*(split if b==0 else 1-split)
                    for mm,rr,pp in zip(m,r,pb)])
    z=[sum(row) for row in raw]
    ok(sum(z)==2*s); ok(all(zz>0 for zz in z))
    if z[0]!=z[1]: biased+=1
    ghosts += sum(mm==0 and rr>0 for mm,rr in zip(m,r))
    out=[[s*x/zz for x in row] for row,zz in zip(raw,z)]
    for b,pb in enumerate(children):
        ok(sum(out[b])==s)
        for k,pp in enumerate(pb):
            if pp: ok(out[b][k]*m[k]*z[b]==s*r[k]*pp)
    # Independently track EACH original witness through its stochastic kernel.
    beta=min(qq/pp for pp,qq in zip(p,q) if pp)/2
    c=[qq-beta*pp for pp,qq in zip(p,q)]
    ok(all(x>=0 for x in c)); ok(sum(c)+beta==s)
    cm=marginal(c,bit)
    for b,pb in enumerate(children):
        normal=z[b]/(2*s)
        new_beta=beta/(2*normal)
        for k,pp in enumerate(pb):
            kernel=pp/(2*m[k]) if m[k] else (split if b==0 else 1-split)
            ok(new_beta*pp+cm[k]*kernel/normal==out[b][k])
    pair=div(p,q)-div(m,r)
    outcome=-math.log2(float(z[0]*z[1]/s**2))/2
    loss=div(p,q)-sum(div(pb,qb) for pb,qb in zip(children,out))/2
    ok(abs(loss-pair-outcome)<1e-9)
    ok(pair>=-1e-10 and outcome>=-1e-10 and loss>=-1e-10)
    return out,loss

def calibrate(p,q):
    global calibrations
    calibrations+=1
    s=sum(q); r=p[0]; z=q[0]/s
    if r==1: out=[s*x for x in p]
    else:
        ok(z<1)
        out=[s*r]+[x*(1-r)/(1-z) for x in q[1:]]
    ok(sum(out)==s and out[0]==s*r)
    if len(out)>1:
        for k in range(1,len(out)):
            for j in range(1,k): ok(out[k]*q[j]==out[j]*q[k])
    charge=div(p,out)-div(p,q)
    binary=div([r,1-r],[z,1-z])
    ok(abs(charge+binary)<1e-9); ok(charge<=1e-10)
    if r==1: ok(abs(div(p,out)+math.log2(float(s)))<1e-9)
    return out,charge

def walk(table,q,policy,split,depth=0):
    global nodes
    nodes+=1
    p=spectrum(table); n=(len(table)).bit_length()-1
    # Early stop is an actual full frontier, not omitted terminal debt.
    if n==0 or (policy==2 and depth>0 and table[0]<0):
        return div(p,q),0.0,0.0,entropy(p)
    bit=0 if policy==0 else n-1 if policy==1 else (sum(x<0 for x in table)+depth)%n
    childtables=[[table[x] for x in range(len(table)) if (x>>bit)&1==b] for b in (0,1)]
    children=[spectrum(t) for t in childtables]
    m=marginal(p,bit)
    ok(all(children[0][j]+children[1][j]==2*m[j] for j in range(len(m))))
    inh,loss=inherit(p,children,q,bit,split)
    erasure=entropy(p)-entropy(m)
    js=entropy(m)-sum(entropy(pb) for pb in children)/2
    results=[]; charge=0
    for pb,qb,tb in zip(children,inh,childtables):
        new,e=calibrate(pb,qb); charge+=e/2
        results.append(walk(tb,new,policy,split,depth+1))
    d=sum(x[0] for x in results)/2
    e=charge+sum(x[1] for x in results)/2
    l=loss+sum(x[2] for x in results)/2
    h=sum(x[3] for x in results)/2
    ok(abs(d-(div(p,q)+e-l))<1e-8)
    ok(abs((entropy(p)+div(p,q)+e)-(entropy(p)+d+l))<1e-8)
    ok(l<=div(p,q)+1e-8); ok(e<=1e-8)
    ok(abs(erasure+js-(entropy(p)-sum(entropy(pb) for pb in children)/2))<1e-9)
    return d,e,l,h

MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
maxn=2 if MODE=='pilot' else 3
for n in range(maxn+1):
    N=1<<n
    for truth in range(1<<N):
        table=[1-2*((truth>>x)&1) for x in range(N)]
        p=spectrum(table); ok(sum(p)==1)
        refs=[p,[(x+F(1,N))/2 for x in p],[(x+(j==0))/2 for j,x in enumerate(p)]]
        for ref in refs:
            for mass in [F(1),F(1,2)]:
                q=[mass*x for x in ref]
                for policy in range(3):
                    for split in [F(1,2),F(1,3)]:
                        walk(table,q,policy,split); trees+=1

# Independent exact recomputation of SAME-owner constants and scalar boundaries.
ok(4*F(4081,4096)-F(135,92)-1==F(35751,23552))
ok(15*F(4081,4096)-320*F(151,8192)-F(37,8)==F(18111,4096))
ok(F(24,23)*F(45,32)==F(135,92))
ok(F(24,23)*256<320)
ok(F(9*12+43,2**13)==F(151,8192))
ok(F(12+3,2**12)==F(15,4096))
for b in range(12,65):
    ok(F(9*(b+1)+43,2**(b+2))<=F(9*b+43,2**(b+1)))
    ok(F(b+4,2**(b+1))<=F(b+3,2**b))
    eps=F(1,2**(b+1)); den=(1+3*eps)*(1-2*eps+2*eps*eps)
    z=(1+3*eps*eps)/den
    ok(den-(1+3*eps*eps)==eps*(1-eps)*(1-6*eps))
    ok(0<z<1); ok(0<z*(2-z)<1)
for j in range(3,257):
    A=1+j*(j+1); B=1+4*j*(j+1)
    ok(B<=4*A); ok(5+16*j*(j+1)<=2**(j+5))
    ok(F(1,8*j*(j+1))==F(1,8)*(F(1,j)-F(1,j+1)))
# Young domination using all attainable signed Walsh values of 1..4-bit tables.
# Every Walsh coefficient is an even multiple of 1/2^n; all such values occur.
for n in range(1,5):
    for numerator in range(-(1<<n), (1<<n)+1,2):
        a=F(numerator,1<<n)
        for sign in [-1,1]:
            for r in [1,2,4]:
                t=F(1,2**(n+12)); p=F(1,2**r); rho=p*t
                val=a*a-4*rho*sign*a+4*p*t*t
                for j in [1,2,3,4,5,6,7,8,9,10,16,32]:
                    eta=F(1,8) if j==1 else F(1,4) if j==2 else F(1,8*j*(j+1))
                    gamma=4*rho*(1+1/eta)
                    ok(val<=(1+eta)*a*a+gamma*t)

result=dict(status='PASS',mode=MODE,checks=checks,trees=trees,nodes=nodes,
            ghost_fibers=ghosts,biased_normalizers=biased,calibrations=calibrations,
            runtime_seconds=time.monotonic()-started,
            helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            arithmetic='Fraction identities and signs; floating log equalities diagnostics only; universal proof separate')
(ROOT/'out'/('PILOT.json' if MODE=='pilot' else 'MAIN.json')).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
