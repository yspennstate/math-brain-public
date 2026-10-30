import itertools, json, math, random
import numpy as np

TOL=5e-10
CSTAR=2/math.log(2)

def fwht(a):
    a=np.array(a,dtype=float).copy(); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            x=a[i:i+h].copy(); y=a[i+h:i+2*h].copy()
            a[i:i+h]=x+y; a[i+h:i+2*h]=x-y
        h*=2
    return a

def spec(f):
    a=fwht(f)/len(f); m=a*a; m[m<1e-15]=0.0; return m

def H(v):
    return -sum(float(x)*math.log2(float(x)) for x in v if x>1e-15)

def marg(mu,n):
    return [sum(mu[s] for s in range(1<<n) if (s>>i)&1) for i in range(n)]

def jf(p):
    p=min(p,1-p); u=.5+math.sqrt(max(0.0,p*(1-p)))
    hb=0.0 if u<=1e-15 or u>=1-1e-15 else -u*math.log2(u)-(1-u)*math.log2(1-u)
    return 1-hb

def J(f):
    n=len(f).bit_length()-1
    return sum(min(x,1-x) for x in marg(spec(f),n))

def Phi(f):
    n=len(f).bit_length()-1
    return sum(jf(x) for x in marg(spec(f),n))

def center(f):
    n=len(f).bit_length()-1; p=marg(spec(f),n); A=[i for i,x in enumerate(p) if x>.5+1e-12]
    g=np.array(f,float).copy()
    for x in range(1<<n):
        if sum((x>>i)&1 for i in A)&1: g[x]*=-1
    return g

def transform(f,buckets,anchors):
    n=len(f).bit_length()-1; amap={i:a for b,a in zip(buckets,anchors) for i in b}; g=np.zeros_like(f,float)
    for y in range(1<<n):
        x=0
        for i in range(n):
            bit=(y>>i)&1; a=amap[i]
            if i!=a: bit^=(y>>a)&1
            x|=bit<<i
        g[y]=f[x]
    return g

def restrict_pos(f,pos,val,vars_):
    d=len(vars_); out=[]
    for y in range(1<<(d-1)):
        x=0; k=0
        for i in range(d):
            bit=val if i==pos else ((y>>k)&1)
            if i!=pos: k+=1
            x|=bit<<i
        out.append(f[x])
    return np.array(out,float), vars_[:pos]+vars_[pos+1:]

def cond_H(mu,n,R):
    d={}
    for s,p in enumerate(mu):
        key=tuple((s>>i)&1 for i in R); d[key]=d.get(key,0.0)+float(p)
    return H(mu)-H(d.values())

def check(f,buckets):
    f=center(f); n=len(f).bit_length()-1; mu0=spec(f); p=marg(mu0,n)
    anchors=[max(b,key=lambda i:jf(p[i])) for b in buckets]
    A=[i for b,a in zip(buckets,anchors) for i in b if i!=a]; R=anchors[:]
    ft=transform(f,buckets,anchors); mut=spec(ft); H0=H(mut)
    Bblock=cond_H(mut,n,R)
    states=[(1.0,ft,list(range(n)))]
    for name in A:
        nxt=[]
        for w,cur,vars_ in states:
            pos=vars_.index(name)
            for val in (0,1):
                ch,nv=restrict_pos(cur,pos,val,vars_); nxt.append((w/2,ch,nv))
        states=nxt
    EH=sum(w*H(spec(cur)) for w,cur,_ in states)
    EJ=sum(w*J(cur) for w,cur,_ in states)
    EPh=sum(w*Phi(cur) for w,cur,_ in states)
    JSblock=H0-EH-Bblock
    Bseq=0.0; JSseq=0.0; states2=[(1.0,ft,list(range(n)))]
    for name in A:
        nxt=[]
        for w,cur,vars_ in states2:
            pos=vars_.index(name); muc=spec(cur); hc=H(muc)
            rest=[i for i in range(len(vars_)) if i!=pos]
            b=cond_H(muc,len(vars_),rest)
            kids=[]
            for val in (0,1):
                ch,nv=restrict_pos(cur,pos,val,vars_); kids.append((ch,nv)); nxt.append((w/2,ch,nv))
            dh=hc-sum(H(spec(ch)) for ch,_ in kids)/2
            Bseq+=w*b; JSseq+=w*(dh-b)
        states2=nxt
    J0=J(f); Ph0=Phi(f); Horig=H(mu0); D=J0-EJ
    pt=marg(mut,n); Q=sum(min(pt[a],1-pt[a]) for a in anchors); C=Q-EJ
    M=sum(jf(p[a]) for a in anchors)
    dE=(Horig-Ph0)-sum(w*(H(spec(cur))-Phi(cur)) for w,cur,_ in states)
    rhs=Bseq-M+CSTAR*(J0-D)
    js_cap=sum(jf(p[i]) for i in A)
    return {
      'drift_identity':abs(D-(J0-Q+C)),
      'simultaneous_entropy':abs((Bblock+JSblock)-(H0-EH)),
      'sequential_entropy':abs((Bseq+JSseq)-(H0-EH)),
      'projection_refund_violation':Bseq-Bblock,
      'js_cap_violation':JSseq-js_cap,
      'corrected_charge_violation':dE-rhs,
      'projection_refund':Bblock-Bseq
    }

def truth(mask,n):
    return np.array([1.0 if ((mask>>x)&1) else -1.0 for x in range(1<<n)])

max_abs_identity=0.0; max_pos_violation=0.0; strict=0; max_refund=0.0; cases=0
for n in (2,3):
    for mask in range(1,(1<<(1<<n))-1):
        f=truth(mask,n)
        for colors in itertools.product((0,1),repeat=n):
            if colors[0]!=0 or len(set(colors))<2: continue
            buckets=[[i for i,c in enumerate(colors) if c==b] for b in (0,1)]
            v=check(f,buckets); cases+=1
            max_abs_identity=max(max_abs_identity,v['drift_identity'],v['simultaneous_entropy'],v['sequential_entropy'])
            max_pos_violation=max(max_pos_violation,v['projection_refund_violation'],v['js_cap_violation'],v['corrected_charge_violation'])
            if v['projection_refund']>TOL: strict+=1
            max_refund=max(max_refund,v['projection_refund'])
rng=random.Random(1402)
for _ in range(1000):
    n=4; mask=rng.randrange(1,(1<<(1<<n))-1); f=truth(mask,n)
    if rng.random()<.5:
        buckets=[list(range(4))]
    else:
        colors=[0]+[rng.randrange(2) for _ in range(3)]
        if len(set(colors))<2: colors[-1]=1
        buckets=[[i for i,c in enumerate(colors) if c==b] for b in sorted(set(colors))]
    v=check(f,buckets); cases+=1
    max_abs_identity=max(max_abs_identity,v['drift_identity'],v['simultaneous_entropy'],v['sequential_entropy'])
    max_pos_violation=max(max_pos_violation,v['projection_refund_violation'],v['js_cap_violation'],v['corrected_charge_violation'])
    if v['projection_refund']>TOL: strict+=1
    max_refund=max(max_refund,v['projection_refund'])
out={
  'status':'PASS' if max_abs_identity<=TOL and max_pos_violation<=TOL else 'FAIL',
  'scope':'exhaustive Boolean truth tables n<=3 over canonical surjective 2-colourings, plus deterministic seed-1402 sample of 1000 n=4 functions/partitions',
  'cases':cases,
  'tolerance':TOL,
  'max_abs_exact_identity_error':max_abs_identity,
  'max_positive_inequality_violation':max_pos_violation,
  'strict_projection_refund_cases':strict,
  'max_projection_refund_bits':max_refund,
  'diagnostic_only':'floating arithmetic and sampled n=4 cases are not theorem certificates; theorem is proved analytically in REPORT.md'
}
print(json.dumps(out,indent=2,sort_keys=True))
