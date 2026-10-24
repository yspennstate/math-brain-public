from fractions import Fraction as F
from itertools import product, combinations

# Exact n=2 checker for the candidate heat-bath Bakry-Emery bound
#     Gamma_2 >= 2*delta_* Gamma
# on every positive integer target weight table w in {1,...,12}^4.
# Source normalization: heat-bath flip rate c_i(x)=(2/n) w(x^i)/(w(x)+w(x^i)); n=2,
# so the prefactor 2/n equals 1.

states = [(0,0),(0,1),(1,0),(1,1)]
idx = {x:k for k,x in enumerate(states)}
n = 2

def flip(x,i):
    y=list(x); y[i]=1-y[i]; return tuple(y)

def mat_add(A,B):
    m=len(A); return [[A[i][j]+B[i][j] for j in range(m)] for i in range(m)]

def mat_sub(A,B):
    m=len(A); return [[A[i][j]-B[i][j] for j in range(m)] for i in range(m)]

def mat_scale(a,A):
    return [[a*v for v in row] for row in A]

def outer(v):
    return [[v[i]*v[j] for j in range(len(v))] for i in range(len(v))]

def det(M):
    M=[row[:] for row in M]
    n=len(M)
    out=F(1)
    for k in range(n):
        p=next((r for r in range(k,n) if M[r][k]),None)
        if p is None: return F(0)
        if p!=k:
            M[k],M[p]=M[p],M[k]; out=-out
        piv=M[k][k]; out*=piv
        for r in range(k+1,n):
            if M[r][k]:
                q=M[r][k]/piv
                for c in range(k+1,n): M[r][c]-=q*M[k][c]
    return out

def principal_minors_psd(M):
    d=len(M)
    mins=[]
    for r in range(1,d+1):
        for S in combinations(range(d),r):
            D=det([[M[i][j] for j in S] for i in S])
            mins.append(D)
            if D < 0:
                return False, min(mins)
    return True, min(mins) if mins else F(0)

# Gauge f(00)=0; variables correspond to states 01,10,11.
var_states=states[1:]
vid={x:i for i,x in enumerate(var_states)}
d=3

def linvec_for_value(x):
    v=[F(0)]*d
    if x!=(0,0): v[vid[x]]=F(1)
    return v

def vsub(a,b): return [x-y for x,y in zip(a,b)]

def local_forms(weights, x):
    def c(z,i):
        a=F(weights[idx[flip(z,i)]])
        b=F(weights[idx[z]])
        return a/(a+b) # 2/n=1 for n=2

    def Lvec(z):
        vz=linvec_for_value(z)
        out=[F(0)]*d
        for i in range(n):
            diff=vsub(linvec_for_value(flip(z,i)),vz)
            ci=c(z,i)
            for k in range(d): out[k]+=ci*diff[k]
        return out

    def GammaMat(z):
        vz=linvec_for_value(z)
        G=[[F(0)]*d for _ in range(d)]
        for i in range(n):
            diff=vsub(linvec_for_value(flip(z,i)),vz)
            G=mat_add(G,mat_scale(F(1,2)*c(z,i),outer(diff)))
        return G

    def GammaMixedMat(z):
        vz=linvec_for_value(z); Lz=Lvec(z)
        M=[[F(0)]*d for _ in range(d)]
        for i in range(n):
            di=vsub(linvec_for_value(flip(z,i)),vz)
            dL=vsub(Lvec(flip(z,i)),Lz)
            term=[[F(1,2)*(di[a]*dL[b]+dL[a]*di[b]) for b in range(d)] for a in range(d)]
            M=mat_add(M,mat_scale(F(1,2)*c(z,i),term))
        return M

    Gx=GammaMat(x)
    LG=[[F(0)]*d for _ in range(d)]
    for i in range(n):
        LG=mat_add(LG,mat_scale(c(x,i),mat_sub(GammaMat(flip(x,i)),Gx)))
    G2=mat_sub(mat_scale(F(1,2),LG),GammaMixedMat(x))
    return Gx,G2

def delta_star(weights):
    def c(z,i):
        return F(weights[idx[flip(z,i)]], weights[idx[z]]+weights[idx[flip(z,i)]])
    vals=[]
    for x in states:
        for i in range(n):
            s=c(x,i)
            for j in range(n):
                if j==i: continue
                diff=c(flip(x,i),j)-c(x,j)
                if diff>0: s-=diff
            vals.append(s)
    return min(vals)

total=0; eligible=0; counterexamples=0; global_min=None
for weights in product(range(1,13), repeat=4):
    total += 1
    ds=delta_star(weights)
    if ds < 0:
        continue
    eligible += 1
    for x in states:
        G,G2=local_forms(weights,x)
        M=mat_sub(G2,mat_scale(2*ds,G))
        ok,mn=principal_minors_psd(M)
        if global_min is None or mn < global_min:
            global_min=mn
        if not ok:
            counterexamples += 1
            print('FAIL witness=',(weights,x,ds,mn))
            raise SystemExit(1)

print(f'tested_total={total}')
print(f'eligible_delta_nonnegative={eligible}')
print(f'counterexamples={counterexamples}')
print(f'min_principal_minor={global_min}')
print('PASS exact rational search: Gamma2 >= 2*delta_* Gamma for all eligible n=2 weight tables in {1,...,12}^4')
