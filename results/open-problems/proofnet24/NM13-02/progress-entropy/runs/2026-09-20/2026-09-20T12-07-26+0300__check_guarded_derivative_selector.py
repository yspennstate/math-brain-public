import json, math, random
from itertools import product
import numpy as np

def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p*math.log2(p) - (1.0-p)*math.log2(1.0-p)

K_GUARD = 4.0*h2(0.25)
C_DIRECT = K_GUARD + 2.0/math.log(2.0)

class Node:
    __slots__ = ("x","y","z","left","right")
    def __init__(self,x,y,z,left=None,right=None):
        self.x=x; self.y=y; self.z=z; self.left=left; self.right=right

def build_balanced(depth,start=0):
    if depth == 0:
        return None,start
    x,y,z = start,start+1,start+2
    left,nxt = build_balanced(depth-1,start+3)
    right,nxt = build_balanced(depth-1,nxt)
    return Node(x,y,z,left,right),nxt

def core_poly(node,bits):
    if node is None:
        return 0
    p0 = core_poly(node.left,bits)
    p1 = core_poly(node.right,bits)
    return p0 ^ (bits[node.x] & (p0 ^ p1 ^ (bits[node.y] & bits[node.z])))

def q_eval(bits,q):
    c,lin,edges=q
    v=c
    for i,a in enumerate(lin):
        if a and bits[i]:
            v ^= 1
    for i,j in edges:
        if bits[i] and bits[j]:
            v ^= 1
    return v

def q_from_mask(n,mask):
    pos=0
    c=(mask>>pos)&1; pos+=1
    lin=[]
    for i in range(n):
        lin.append((mask>>pos)&1); pos+=1
    edges=[]
    for i in range(n):
        for j in range(i+1,n):
            if (mask>>pos)&1:
                edges.append((i,j))
            pos+=1
    return c,lin,edges

def random_q(n,rng):
    c=rng.randrange(2)
    lin=[rng.randrange(2) for _ in range(n)]
    edges=[]
    for i in range(n):
        for j in range(i+1,n):
            if rng.randrange(2):
                edges.append((i,j))
    return c,lin,edges

def restricted_vals(root,n,q,assignment):
    free=[i for i in range(n) if i not in assignment]
    vals=[]
    for tup in product([0,1], repeat=len(free)):
        bits=[0]*n
        for i,v in assignment.items():
            bits[i]=v
        for i,v in zip(free,tup):
            bits[i]=v
        phase=core_poly(root,bits)^q_eval(bits,q)
        vals.append(1.0 if phase==0 else -1.0)
    return free,np.array(vals,dtype=float)

def fwht(vals):
    a=np.array(vals,dtype=float).copy()
    N=len(a); h=1
    while h<N:
        for i in range(0,N,2*h):
            x=a[i:i+h].copy(); y=a[i+h:i+2*h].copy()
            a[i:i+h]=x+y
            a[i+h:i+2*h]=x-y
        h*=2
    return a/N

def entropy_fourier(vals):
    p=fwht(vals)**2
    return float(sum(-x*math.log2(x) for x in p if x>1e-15))

def inf_coord(vals,j):
    N=len(vals); m=int(round(math.log2(N)))
    stride=2**(m-1-j)
    cnt=0
    for idx in range(N):
        if ((idx//stride)%2)==0 and vals[idx]!=vals[idx+stride]:
            cnt+=1
    return cnt/(N/2)

def total_influence(vals):
    m=int(round(math.log2(len(vals))))
    return sum(inf_coord(vals,j) for j in range(m))

def B_coord(vals,j):
    N=len(vals); m=int(round(math.log2(N)))
    p=fwht(vals)**2
    bit=1<<(m-1-j)
    ans=0.0
    for mask in range(N):
        if mask & bit:
            continue
        p0=float(p[mask]); p1=float(p[mask|bit]); q=p0+p1
        if q>1e-15:
            ans += q*h2(p1/q)
    return ans

def restrict_local(vals,j,b):
    N=len(vals); m=int(round(math.log2(N)))
    stride=2**(m-1-j)
    out=[]
    for idx in range(N):
        if ((idx//stride)%2)==b:
            out.append(vals[idx])
    return np.array(out,dtype=float)

def Delta_coord(vals,j):
    return entropy_fourier(vals) - 0.5*(entropy_fourier(restrict_local(vals,j,0))+entropy_fourier(restrict_local(vals,j,1)))

def hereditary_R(root,current,n,q,assignment,stats):
    free,vals=restricted_vals(root,n,q,assignment)
    if not free:
        return 0.0
    if current is not None:
        coord=current.x
        loc=free.index(coord)
        alpha=inf_coord(vals,loc)
        jj=min(alpha,1.0-alpha)
        B=B_coord(vals,loc)
        Delta=Delta_coord(vals,loc)
        stats["selector_count"] += 1
        stats["min_j"] = min(stats["min_j"],jj)
        if alpha>0:
            stats["max_B_over_inf"] = max(stats["max_B_over_inf"],B/alpha)
            stats["max_Delta_over_inf"] = max(stats["max_Delta_over_inf"],Delta/alpha)
        if jj < 0.25-1e-10 or B > K_GUARD*alpha+1e-9 or Delta > C_DIRECT*alpha+1e-9:
            stats["local_violations"] += 1
        a0=dict(assignment); a0[coord]=0
        a1=dict(assignment); a1[coord]=1
        return B + 0.5*hereditary_R(root,current.left,n,q,a0,stats) + 0.5*hereditary_R(root,current.right,n,q,a1,stats)
    coord=free[0]
    loc=0
    B=B_coord(vals,loc)
    a0=dict(assignment); a0[coord]=0
    a1=dict(assignment); a1[coord]=1
    return B + 0.5*hereditary_R(root,None,n,q,a0,stats) + 0.5*hereditary_R(root,None,n,q,a1,stats)

def check_one(root,n,q):
    free,vals=restricted_vals(root,n,q,{})
    I=total_influence(vals)
    stats={"selector_count":0,"min_j":1.0,"max_B_over_inf":0.0,"max_Delta_over_inf":0.0,"local_violations":0}
    R=hereditary_R(root,root,n,q,{},stats)
    ratio=0.0 if I==0 else R/I
    return I,R,ratio,stats

guard=np.array([1.0,1.0,1.0,-1.0])
guard_spec=[float(x) for x in fwht(guard)]
guard_ok=all(abs(abs(x)-0.5)<1e-12 for x in guard_spec)

root1,n1=build_balanced(1)
count_q1=2**(1+n1+n1*(n1-1)//2)
depth1={"twists":count_q1,"violations":0,"min_j":1.0,"max_R_over_I":0.0,"max_B_over_inf":0.0,"max_Delta_over_inf":0.0,"selector_visits":0}
for mask in range(count_q1):
    q=q_from_mask(n1,mask)
    I,R,ratio,s=check_one(root1,n1,q)
    depth1["violations"] += s["local_violations"] + (1 if ratio>K_GUARD+1e-9 else 0)
    depth1["min_j"]=min(depth1["min_j"],s["min_j"])
    depth1["max_R_over_I"]=max(depth1["max_R_over_I"],ratio)
    depth1["max_B_over_inf"]=max(depth1["max_B_over_inf"],s["max_B_over_inf"])
    depth1["max_Delta_over_inf"]=max(depth1["max_Delta_over_inf"],s["max_Delta_over_inf"])
    depth1["selector_visits"] += s["selector_count"]

root2,n2=build_balanced(2)
rng=random.Random(20260920)
samples=80
depth2={"samples":samples,"violations":0,"min_j":1.0,"max_R_over_I":0.0,"max_B_over_inf":0.0,"max_Delta_over_inf":0.0,"selector_visits":0}
for _ in range(samples):
    q=random_q(n2,rng)
    I,R,ratio,s=check_one(root2,n2,q)
    depth2["violations"] += s["local_violations"] + (1 if ratio>K_GUARD+1e-9 else 0)
    depth2["min_j"]=min(depth2["min_j"],s["min_j"])
    depth2["max_R_over_I"]=max(depth2["max_R_over_I"],ratio)
    depth2["max_B_over_inf"]=max(depth2["max_B_over_inf"],s["max_B_over_inf"])
    depth2["max_Delta_over_inf"]=max(depth2["max_Delta_over_inf"],s["max_Delta_over_inf"])
    depth2["selector_visits"] += s["selector_count"]

out={
    "status":"PASS" if guard_ok and depth1["violations"]==0 and depth2["violations"]==0 else "FAIL",
    "constants":{
        "kappa_guard":K_GUARD,
        "C_direct":C_DIRECT,
        "kappa_guard_exact":"8 - 3 log2(3)",
        "C_direct_exact":"8 - 3 log2(3) + 2/ln(2)"
    },
    "guard_walsh":guard_spec,
    "depth1_exhaustive":depth1,
    "depth2_sampled":depth2,
    "scope_note":"Finite checks only; theorem is analytic. Depth-2 sampling uses seed 20260920."
}
print(json.dumps(out,indent=2,sort_keys=True))
