#!/usr/bin/env python3
from itertools import combinations

# State order for connectivity on the three clique terminals:
# D=1|2|3, P12=12|3, P13=13|2, P23=23|1, T=123.
M = [
    [4,1,1,1,1],
    [0,4,0,0,2],
    [0,0,4,0,2],
    [0,0,0,4,2],
    [0,0,0,0,4],
]
E1 = [
    [1,1,1,0,1],
    [0,1,0,0,1],
    [0,0,1,0,1],
    [0,0,0,1,2],
    [0,0,0,0,1],
]
E2 = [
    [1,1,0,1,1],
    [0,1,0,0,1],
    [0,0,1,0,2],
    [0,0,0,1,1],
    [0,0,0,0,1],
]
E3 = [
    [1,0,1,1,1],
    [0,1,0,0,2],
    [0,0,1,0,1],
    [0,0,0,1,1],
    [0,0,0,0,1],
]
E12 = [
    [0,1,0,0,1],
    [0,0,0,0,0],
    [0,0,0,0,1],
    [0,0,0,0,1],
    [0,0,0,0,0],
]

u = [1,1,1,1,3]      # all forests of the initial K3, by terminal partition
wt = [0,1,0,0,2]     # forests of K3 containing fixed triangle edge 12
wtt = [0,0,0,0,1]    # forests of K3 containing fixed triangle edges 12 and 13
ones = [1,1,1,1,1]

def row_mat(v, A):
    return [sum(v[i]*A[i][j] for i in range(len(v))) for j in range(len(A[0]))]

def mat_mul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def mat_pow(A, n):
    size=len(A)
    R=[[int(i==j) for j in range(size)] for i in range(size)]
    B=[row[:] for row in A]
    while n:
        if n&1:
            R=mat_mul(R,B)
        B=mat_mul(B,B)
        n//=2
    return R

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def count(v, ops, tail_power):
    r=v[:]
    for A in ops:
        r=row_mat(r,A)
    if tail_power:
        r=row_mat(r, mat_pow(M, tail_power))
    return dot(r, ones)

def formulas(n):
    q=4**n
    return {
      "Z": q*(3*n*n+37*n+112)//16,
      "Zt": q*(n+6)//2,
      "Ztt": q,
      "Zs": q*(3*n*n+47*n+174)//64,
      "Zts_inc": q*(n+7)//8,
      "Zts_non": q*(n+9)//8,
      "Zss_R": q*(n+7)//8,
      "Zss_L": q*(3*n*n+57*n+242)//256,
      "Zss_D": q*3*(n*n+19*n+86)//256,
    }

def delta_formulas(n):
    q=16**n
    return {
      "tt": q*(n*n+11*n+32)//16,
      "ts_inc": q*(7*n*n+85*n+260)//128,
      "ts_non": q*(n*n+11*n+36)//128,
      "ss_R": q*(9*n**4+186*n**3+1397*n*n+4484*n+5188)//4096,
      "ss_L": q*(41*n*n+509*n+1586)//2048,
      "ss_D": q*(17*n*n+213*n+690)//2048,
    }

def transfer_counts(n):
    out={}
    out["Z"]=count(u, [], n)
    out["Zt"]=count(wt, [], n)
    out["Ztt"]=count(wtt, [], n)
    out["Zs"]=count(u, [E1], n-1)
    out["Zts_inc"]=count(wt, [E1], n-1)
    out["Zts_non"]=count(wt, [E3], n-1)
    out["Zss_R"]=count(u, [E12], n-1)
    if n>=2:
        out["Zss_L"]=count(u, [E1,E1], n-2)
        out["Zss_D"]=count(u, [E1,E2], n-2)
    return out

def rayleigh_from_counts(c):
    Z=c["Z"]; Zt=c["Zt"]; Zs=c["Zs"]
    out={
      "tt": Zt*Zt-Z*c["Ztt"],
      "ts_inc": Zt*Zs-Z*c["Zts_inc"],
      "ts_non": Zt*Zs-Z*c["Zts_non"],
      "ss_R": Zs*Zs-Z*c["Zss_R"],
    }
    if "Zss_L" in c:
        out["ss_L"]=Zs*Zs-Z*c["Zss_L"]
        out["ss_D"]=Zs*Zs-Z*c["Zss_D"]
    return out

def complete_split_edges(n):
    E=[(0,1),(0,2),(1,2)]
    for j in range(n):
        v=3+j
        for a in range(3):
            E.append((a,v))
    return E

def is_forest(vcount, edge_list):
    p=list(range(vcount))
    def find(x):
        while p[x]!=x:
            p[x]=p[p[x]]
            x=p[x]
        return x
    for a,b in edge_list:
        ra,rb=find(a),find(b)
        if ra==rb:
            return False
        p[rb]=ra
    return True

def brute(n):
    E=complete_split_edges(n)
    m=len(E)
    fs=[]
    for mask in range(1<<m):
        chosen=[E[i] for i in range(m) if (mask>>i)&1]
        if is_forest(n+3, chosen):
            fs.append(mask)
    Z=len(fs)
    single=[sum((mask>>i)&1 for mask in fs) for i in range(m)]
    pair={}
    for i in range(m):
        for j in range(i+1,m):
            pair[(i,j)]=sum(((mask>>i)&1) and ((mask>>j)&1) for mask in fs)
    c={
      "Z":Z,
      "Zt":single[0],
      "Ztt":pair[(0,1)],
      "Zs":single[3],
      "Zts_inc":pair[(0,3)],
      "Zts_non":pair[(0,5)],
      "Zss_R":pair[(3,4)],
    }
    if n>=2:
        c["Zss_L"]=pair[(3,6)]
        c["Zss_D"]=pair[(3,7)]
    return c

print("COMPLETE_SPLIT_Sn_CHECK")
for n in range(1,13):
    c=transfer_counts(n)
    f=formulas(n)
    keys=list(c.keys())
    assert all(c[k]==f[k] for k in keys), (n,c,f)
    d=rayleigh_from_counts(c)
    df=delta_formulas(n)
    assert all(d[k]==df[k] for k in d), (n,d,df)
    assert all(x>0 for x in d.values()), (n,d)
    print("n=%d Z=%d min_orbit_delta=%d transfer_formula=PASS" %
          (n,c["Z"],min(d.values())))

print("BRUTE_FORCE_SMALL_N")
for n in range(1,4):
    b=brute(n)
    f=formulas(n)
    assert all(b[k]==f[k] for k in b), (n,b,f)
    d=rayleigh_from_counts(b)
    assert all(x>0 for x in d.values()), (n,d)
    print("n=%d edges=%d forests=%d min_orbit_delta=%d brute=PASS" %
          (n,3+3*n,b["Z"],min(d.values())))

print("ALL_EXACT_CHECKS_PASS")
