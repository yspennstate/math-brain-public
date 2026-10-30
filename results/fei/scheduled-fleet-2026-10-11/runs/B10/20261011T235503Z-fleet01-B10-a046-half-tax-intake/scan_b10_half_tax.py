import math

def h(ps):
    return -sum(x*math.log2(x) for x in ps if x>0)

def basis(x,p):
    return (-math.sqrt(p/(1-p)) if x==0 else math.sqrt((1-p)/p))

def ledger(vals,p,q,reveal=0):
    # vals indexed by x*2+y, each +-1.
    coeff=[]
    for mask in range(4):
        s=0.0
        for x in (0,1):
          for y in (0,1):
            pr=(p if x else 1-p)*(q if y else 1-q)
            z=vals[2*x+y]
            if mask&1: z*=basis(x,p)
            if mask&2: z*=basis(y,q)
            s+=pr*z
        coeff.append(s)
    mass=[z*z for z in coeff]
    if reveal==0:
        # R=X, T=Y
        qT=[mass[0]+mass[1],mass[2]+mass[3]]
        M=h(mass)-h(qT)
        children=[]
        for x in (0,1):
            m=0.0
            for y in (0,1): m+=(q if y else 1-q)*vals[2*x+y]
            children.append(h([m*m,1-m*m]))
        J=h(qT)-((1-p)*children[0]+p*children[1])
        d=p*math.log2((1-p)/p) if p<=0.5 else (1-p)*math.log2(p/(1-p))
    else:
        qT=[mass[0]+mass[2],mass[1]+mass[3]]
        M=h(mass)-h(qT)
        children=[]
        for y in (0,1):
            m=0.0
            for x in (0,1): m+=(p if x else 1-p)*vals[2*x+y]
            children.append(h([m*m,1-m*m]))
        J=h(qT)-((1-q)*children[0]+q*children[1])
        d=q*math.log2((1-q)/q) if q<=0.5 else (1-q)*math.log2(q/(1-q))
    return M,J,d,mass

biases=sorted(set([i/400 for i in range(1,200)]+[2.0**(-k) for k in range(2,41)]))
best=(-1,None)
tested=0
violations=[]
for truth in range(16):
 vals=[1 if (truth>>i)&1 else -1 for i in range(4)]
 for p in biases:
  for q in biases:
   for reveal in (0,1):
    M,J,d,mass=ledger(vals,p,q,reveal)
    ratio=(J-M)/d if d>0 else -1
    tested += 1
    if ratio > 0.5 + 2e-6:
        violations.append((ratio,truth,p,q,reveal))
    if ratio>best[0]: best=(ratio,(truth,p,q,reveal,M,J,d,mass))
print("candidate=J_A <= M_A + (1/2) Delta_A")
print("scope=all 16 two-bit truth tables; both singleton reveals; displayed bias grid")
print("bias_count=",len(biases))
print("instances=",tested)
print("violations=",len(violations))
print("max_ratio=",best[0])
print("maximizer=",best[1])
print("status=NUMERICAL_ONLY_NOT_CONTINUUM_CERTIFICATE")
