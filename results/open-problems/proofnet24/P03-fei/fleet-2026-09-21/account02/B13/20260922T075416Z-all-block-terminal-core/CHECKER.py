import itertools, math

def h2(x):
    if x == 0 or x == 1: return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def jfun(q):
    if q == 0: return 0.0
    if q == 0.5: return 1.0
    s=math.sqrt(q*(1-q)); x=0.5+s
    return 1-h2(x)

def jprime(q):
    if q == 0: return 2/math.log(2)
    if q == 0.5: return 0.0
    s=math.sqrt(q*(1-q)); x=0.5+s
    return math.log2(x/(1-x))*(1-2*q)/(2*s)

def walsh(vals):
    a=[float(x) for x in vals]; N=len(a); step=1
    while step<N:
        for b in range(0,N,2*step):
            for r in range(b,b+step):
                x,y=a[r],a[r+step]; a[r],a[r+step]=x+y,x-y
        step*=2
    return [x/N for x in a]

def influences(vals,n):
    N=1<<n
    return [sum(vals[x]!=vals[x^(1<<i)] for x in range(N))/N for i in range(n)]

def char_mult(vals,n,T):
    return [v*(-1 if ((x&T).bit_count()&1) else 1) for x,v in enumerate(vals)]

def centered(vals,n):
    p=influences(vals,n); T=sum((1<<i) for i,x in enumerate(p) if x>0.5)
    return char_mult(vals,n,T)

def entropy_spec(vals):
    p=[x*x for x in walsh(vals)]
    H=-sum(float(x)*math.log2(float(x)) for x in p if x>0)
    return H,p

def restrict(vals,n,A,z):
    A=sorted(A); R=[i for i in range(n) if i not in A]; out=[]
    for y in range(1<<len(R)):
        x=0
        for k,i in enumerate(A): x|=((z>>k)&1)<<i
        for k,i in enumerate(R): x|=((y>>k)&1)<<i
        out.append(vals[x])
    return out,R

def J(vals,n): return sum(min(x,1-x) for x in influences(vals,n))

def F(vals,n):
    v=centered(vals,n); H,_=entropy_spec(v); q=[min(x,1-x) for x in influences(vals,n)]
    P=sum(jfun(x) for x in q); return H-P,H,sum(q),P

def B_A(vals,n,A):
    v=centered(vals,n); H,p=entropy_spec(v); B=[i for i in range(n) if i not in A]; marg={}
    for S,x in enumerate(p):
        key=tuple((S>>i)&1 for i in B); marg[key]=marg.get(key,0.0)+float(x)
    HB=-sum(x*math.log2(x) for x in marg.values() if x>0)
    return H-HB

def block(vals,n,A):
    v=centered(vals,n); A=tuple(sorted(A)); p=influences(v,n); q=p; J0=sum(q)
    EJ=0.0
    for z in range(1<<len(A)):
        ch,R=restrict(v,n,A,z); EJ += J(ch,len(R))/(1<<len(A))
    D=J0-EJ; IA=sum(q[i] for i in A); C=D-IA; W=0.0
    for j in range(n):
        if j in A: continue
        eabs=0.0
        for z in range(1<<len(A)):
            ch,R=restrict(v,n,A,z); pj=influences(ch,len(R))[R.index(j)]
            eabs += abs(pj-0.5)/(1<<len(A))
        cj=eabs-abs(q[j]-0.5); W += jprime(q[j])*cj
    U=sum(h2(q[i]) for i in A)-W
    return U,D,C,W,q

def tensor(v1,n1,v2,n2):
    return [v1[x&((1<<n1)-1)]*v2[x>>n1] for x in range(1<<(n1+n2))]

max_source_excess=0.0; cosingleton_errors=0; source_checks=0
for n in range(1,4):
    N=1<<n
    for mask in range(1<<(N-1)):
        vals=[1]+[1 if (mask>>(x-1))&1 else -1 for x in range(1,N)]
        F0,_,_,_=F(vals,n); v=centered(vals,n)
        for r in range(1,n+1):
            for A in itertools.combinations(range(n),r):
                U,D,C,W,q=block(vals,n,A); BA=B_A(vals,n,A); EF=0.0
                for z in range(1<<r):
                    ch,R=restrict(v,n,A,z); EF += F(ch,len(R))[0]/(1<<r)
                max_source_excess=max(max_source_excess,(F0-EF)-(BA-W)); source_checks+=1
                if n>=2 and r==n-1:
                    j=next(iter(set(range(n))-set(A)))
                    if abs(C-q[j])>1e-12: cosingleton_errors+=1

max_gauge=0.0; gauge_checks=0
for n in range(1,4):
    N=1<<n
    for mask in range(min(1<<(N-1),64)):
        vals=[1]+[1 if (mask>>(x-1))&1 else -1 for x in range(1,N)]
        for T in range(1<<n):
            vv=char_mult(vals,n,T)
            for r in range(1,n+1):
                for A in itertools.combinations(range(n),r):
                    x=block(vals,n,A); y=block(vv,n,A)
                    max_gauge=max(max_gauge,max(abs(x[k]-y[k]) for k in range(4))); gauge_checks+=1

funcs=[]
for mask in range(8): funcs.append([1]+[1 if (mask>>(x-1))&1 else -1 for x in range(1,4)])
max_tensor=0.0; tensor_checks=0
for v1 in funcs[:5]:
  for v2 in funcs[:5]:
    tv=tensor(v1,2,v2,2)
    for a1 in range(4):
      for a2 in range(4):
        if not (a1 or a2): continue
        A1=[i for i in range(2) if (a1>>i)&1]; A2=[i for i in range(2) if (a2>>i)&1]
        A=A1+[2+i for i in A2]; U,D,C,W,_=block(tv,4,A)
        parts=[0.0]*4
        if A1:
            x=block(v1,2,A1)
            for k in range(4): parts[k]+=x[k]
        if A2:
            x=block(v2,2,A2)
            for k in range(4): parts[k]+=x[k]
        for got,want in zip((U,D,C,W),parts): max_tensor=max(max_tensor,abs(got-want))
        tensor_checks+=1

print('source_checks',source_checks)
print('max_curvature_inequality_excess',format(max_source_excess,'.3e'))
print('cosingleton_C_equals_q_errors',cosingleton_errors)
print('gauge_checks',gauge_checks,'max_error',format(max_gauge,'.3e'))
print('tensor_checks',tensor_checks,'max_error',format(max_tensor,'.3e'))
print('RESULT', 'PASS' if max_source_excess<1e-12 and cosingleton_errors==0 and max_gauge<1e-12 and max_tensor<1e-12 else 'FAIL')
