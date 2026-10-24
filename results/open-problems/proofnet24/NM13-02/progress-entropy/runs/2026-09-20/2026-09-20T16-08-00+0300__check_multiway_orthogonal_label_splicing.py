#!/usr/bin/env python3
import itertools, math, json
import numpy as np

TOL = 1e-10

def entropy_probs(probs):
    return -sum(float(p)*math.log2(float(p)) for p in probs if p > 0)

def fwht(arr):
    a = np.array(arr, dtype=float).copy()
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2*h):
            x = a[i:i+h].copy()
            y = a[i+h:i+2*h].copy()
            a[i:i+h] = x+y
            a[i+h:i+2*h] = x-y
        h *= 2
    return a / n

def flip_index(i,j):
    return i ^ (1 << j)

def influence(vals, coords):
    N = len(vals)
    total = 0.0
    for j in coords:
        total += sum(vals[i] != vals[flip_index(i,j)] for i in range(N)) / N
    return total

def spectral_joint(vals, nA):
    n = int(round(math.log2(len(vals))))
    nY = n - nA
    hat = fwht(vals)
    mat = np.zeros((1 << nA, 1 << nY))
    for idx, prob in enumerate(hat*hat):
        u = idx & ((1 << nA)-1)
        t = idx >> nA
        mat[u,t] += prob
    return mat

def cond_entropy_rows_given_cols(mat):
    col = mat.sum(axis=0)
    return entropy_probs(mat.flatten()) - entropy_probs(col)

def label_boundary(q, nY):
    N = 1 << nY
    return sum(sum(q[y] != q[flip_index(y,j)] for y in range(N))/N
               for j in range(nY))

def make_character_label_F(nA,nY,q,s):
    vals=[]
    for idx in range(1 << (nA+nY)):
        a = idx & ((1 << nA)-1)
        y = idx >> nA
        parity = ((a & q[y]).bit_count() & 1)
        vals.append(s[y] * (-1 if parity else 1))
    return vals

def truth_from_code(code,n):
    return [1 if (code >> i) & 1 else -1 for i in range(1 << n)]

def make_general_controller_F(u_list,nA,nY,q,s):
    vals=[]
    for idx in range(1 << (nA+nY)):
        a = idx & ((1 << nA)-1)
        y = idx >> nA
        vals.append(s[y] * u_list[q[y]][a])
    return vals

def latent_cond_entropy(q,s,nY,nlabels):
    mat=np.zeros((nlabels,1 << nY))
    for z in range(nlabels):
        c=[s[y] if q[y]==z else 0 for y in range(1 << nY)]
        hc=fwht(c)
        mat[z,:]=hc*hc
    return cond_entropy_rows_given_cols(mat)

def cycle_q(d):
    q=[]
    for y in range(1 << d):
        z=0
        for j in range(d):
            if ((y >> j)&1) and ((y >> ((j+1)%d))&1):
                z |= 1 << j
        q.append(z)
    return q

def block_B_from_cells(q,nY,nA):
    mat=np.zeros((1 << nA,1 << nY))
    for z in range(1 << nA):
        c=[1 if q[y]==z else 0 for y in range(1 << nY)]
        hc=fwht(c)
        mat[z,:]=hc*hc
    return cond_entropy_rows_given_cols(mat)

def cycle_phase_vals(d):
    vals=[]
    for idx in range(1 << (2*d)):
        a=idx & ((1 << d)-1)
        y=idx >> d
        p=0
        for j in range(d):
            p ^= (((a>>j)&1) & ((y>>j)&1) & ((y>>((j+1)%d))&1))
        vals.append(-1 if p else 1)
    return vals

def signed_translation_count(vals):
    N=len(vals)
    count=0
    for v in range(1,N):
        first=vals[0]*vals[v]
        if all(vals[x]*vals[x^v]==first for x in range(N)):
            count += 1
    return count

def cycle_hitting_number(d):
    edges=[{j,d+j,d+((j+1)%d)} for j in range(d)]
    for r in range(2*d+1):
        for comb in itertools.combinations(range(2*d),r):
            S=set(comb)
            if all(S & e for e in edges):
                return r
    raise RuntimeError

out={}

# Exhaustive character-controller theorem, A=Y=2.
nA=nY=2
v_B_H=v_H_L=v_L_I=v_IA=0.0
cases=0
for qtuple in itertools.product(range(1 << nA), repeat=1 << nY):
    q=list(qtuple)
    beta=[q.count(z)/(1 << nY) for z in range(1 << nA)]
    Hb=entropy_probs(beta)
    L=label_boundary(q,nY)
    for smask in range(1 << (1 << nY)):
        s=[1 if (smask>>y)&1 else -1 for y in range(1 << nY)]
        vals=make_character_label_F(nA,nY,q,s)
        BA=cond_entropy_rows_given_cols(spectral_joint(vals,nA))
        IY=influence(vals,range(nA,nA+nY))
        IA=influence(vals,range(nA))
        IA_formula=sum(beta[z]*z.bit_count() for z in range(1 << nA))
        v_B_H=max(v_B_H, BA-Hb)
        v_H_L=max(v_H_L, Hb-L)
        v_L_I=max(v_L_I, L-2*IY)
        v_IA=max(v_IA, abs(IA-IA_formula))
        cases += 1
assert max(v_B_H,v_H_L,v_L_I,v_IA) <= TOL
out["character_exhaustive"]={
    "cases":cases,
    "max_B_minus_Hlabel":v_B_H,
    "max_Hlabel_minus_boundary":v_H_L,
    "max_boundary_minus_2IY":v_L_I,
    "max_IA_identity_error":v_IA,
}

# Non-character disjoint Fourier-support controller pair in dimension 3.
u0=truth_from_code(3,3)
u1=truth_from_code(86,3)
h0=fwht(u0); h1=fwht(u1)
supp0={i for i,x in enumerate(h0) if abs(x)>TOL}
supp1={i for i,x in enumerate(h1) if abs(x)>TOL}
assert supp0.isdisjoint(supp1)
H0=entropy_probs(h0*h0); H1=entropy_probs(h1*h1)
v_exact=v_L_I=0.0
cases2=0
for qmask in range(1 << (1 << 2)):
    q=[(qmask>>y)&1 for y in range(4)]
    beta=[q.count(z)/4 for z in [0,1]]
    for smask in range(16):
        s=[1 if (smask>>y)&1 else -1 for y in range(4)]
        vals=make_general_controller_F([u0,u1],3,2,q,s)
        BA=cond_entropy_rows_given_cols(spectral_joint(vals,3))
        Bz=latent_cond_entropy(q,s,2,2)
        exact=beta[0]*H0+beta[1]*H1+Bz
        L=label_boundary(q,2)
        IY=influence(vals,range(3,5))
        v_exact=max(v_exact,abs(BA-exact))
        v_L_I=max(v_L_I,L-2*IY)
        cases2 += 1
assert max(v_exact,v_L_I) <= TOL
out["noncharacter_pair"]={
    "cases":cases2,
    "support0":sorted(supp0),
    "support1":sorted(supp1),
    "controller_entropies":[H0,H1],
    "max_factorization_error":v_exact,
    "max_boundary_minus_2IY":v_L_I,
}

# Connected signed-rigid cycle family.
cycle=[]
for d in range(3,8):
    q=cycle_q(d)
    beta=[q.count(z)/(1 << d) for z in range(1 << d)]
    Hb=entropy_probs(beta)
    L=label_boundary(q,d)
    BA=block_B_from_cells(q,d,d)
    IY=L/2
    IA=sum(beta[z]*z.bit_count() for z in range(1 << d))
    ratio=(BA+IY)/(IA+IY)
    assert BA <= Hb + TOL
    assert Hb <= L + TOL
    hit=cycle_hitting_number(d)
    assert hit == math.ceil(d/2)
    rigid=None
    if d <= 5:
        rigid = signed_translation_count(cycle_phase_vals(d))
        assert rigid == 0
    cycle.append({
        "d":d,
        "B_A":BA,
        "H_label":Hb,
        "label_boundary":L,
        "I_Y":IY,
        "I_A":IA,
        "certificate_ratio_using_exact_BA":ratio,
        "cubic_vertex_cover":hit,
        "signed_translation_symmetries":rigid,
    })
out["cycle_family"]=cycle
out["status"]="PASS"
print(json.dumps(out, indent=2, sort_keys=True))
