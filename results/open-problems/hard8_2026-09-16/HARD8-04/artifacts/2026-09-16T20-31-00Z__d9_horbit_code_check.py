from collections import Counter
P=523
# order-9 subgroup K=<2^58>
h=pow(2,58,P)
K=[]
x=1
for _ in range(9):
    K.append(x); x=x*h%P
assert x==1 and len(set(K))==9
assert P-1 not in K

# K-orbits on nonzero residues
orb_id=[None]*P
orbits=[]
for a in range(1,P):
    if orb_id[a] is None:
        O=sorted({a*k%P for k in K})
        assert len(O)==9
        j=len(orbits)
        for y in O:
            assert orb_id[y] is None
            orb_id[y]=j
        orbits.append(O)
assert len(orbits)==58

# Negation pairs the 58 K-orbits into 29 distinct pairs.
neg_mate=[]
for j,O in enumerate(orbits):
    m=orb_id[(-O[0])%P]
    assert m!=j
    assert all(orb_id[(-x)%P]==m for x in O)
    neg_mate.append(m)
assert all(neg_mate[neg_mate[j]]==j for j in range(58))
pairs=[]; seen=set()
for j in range(58):
    if j not in seen:
        m=neg_mate[j]; pairs.append((j,m)); seen.add(j); seen.add(m)
assert len(pairs)==29 and len(seen)==58

H4=((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))
label_to_code=[]
for lab in range(8):
    i=lab//2; sg=1 if lab%2==0 else -1
    vals=[sg*H4[r][i] for r in range(4)]
    assert vals[3]==vals[0]*vals[1]*vals[2]
    code=sum((vals[b]<0)<<b for b in range(3))
    label_to_code.append(code)
assert label_to_code==[0,7,4,3,2,5,6,1]

# Best heuristic candidate found in this run. It is NOT a solution/certificate.
labels=[7,3,2,7,6,3,1,6,1,7,3,6,2,5,4,3,7,0,6,6,6,7,2,7,6,1,7,2,6,7,0,6,6,6,7,4,3,7,6,6,0,6,5,5,4,7,6,7,7,0,2,7,0,2,6,7,4,7]
assert len(labels)==58
cnt=Counter(labels)
# component plus-minus imbalances at nonzero orbits: (2,1,1,0)
assert tuple(cnt[2*i]-cnt[2*i+1] for i in range(4))==(2,1,1,0)
# m profile = minus counts
m=tuple(cnt[2*i+1] for i in range(4))
assert m==(3,5,3,16) and sum(m)==27

q=[0]*P
for j,O in enumerate(orbits):
    for x in O: q[x]=labels[j]
# q(0)=+e0 fixed
r=[0]*4
for x in range(P):
    lab=q[x]; r[lab//2]+=1 if lab%2==0 else -1
assert tuple(r)==(19,9,9,0)

# transformed 3-bit code g for (A,B,C); D=ABC is implicit.
g=[label_to_code[qx] for qx in q]

def t_corr(s):
    c=0
    for x in range(P):
        a=q[x]; b=q[(x+s)%P]
        if a//2==b//2:
            c += 1 if (a%2)==(b%2) else -1
    return c

def code_balance(s):
    n0=n7=0
    for x in range(P):
        d=g[x]^g[(x+s)%P]
        if d==0: n0+=1
        elif d==7: n7+=1
    return n0,n7,n0-n7

# The theorem-level identity: for every shift, T aggregate correlation equals
# (# equal three-bit codes) - (# bitwise-complementary three-bit codes).
Cs=[]
for s in range(1,P):
    c=t_corr(s)
    n0,n7,b=code_balance(s)
    assert c==b
    assert c==t_corr((-s)%P)
    Cs.append(c)

# K invariance makes C constant on each K shift orbit; negation halves to 29 H=<K,-1> classes.
C_orb=[]
for j,O in enumerate(orbits):
    vals={t_corr(s) for s in O}
    assert len(vals)==1
    C_orb.append(next(iter(vals)))
for j,mate in enumerate(neg_mate):
    assert C_orb[j]==C_orb[mate]

reduced=[C_orb[a] for a,b in pairs]
assert sum(c*c for c in C_orb)==172
assert sum(c*c for c in reduced)==86
assert max(abs(c) for c in reduced)==4
assert any(c!=0 for c in reduced)
assert sum(reduced)==0

# Re-expand the 29 reduced constraints to all 522 nonzero shifts.
for s in range(1,P):
    j=orb_id[s]
    rep_pair=next((idx for idx,(a,b) in enumerate(pairs) if j==a or j==b),None)
    assert rep_pair is not None
    assert t_corr(s)==reduced[rep_pair]

print('P',P)
print('K',K)
print('K_orbits',len(orbits),'negation_pairs',len(pairs))
print('label_to_code',label_to_code)
print('candidate_m_profile',m)
print('candidate_rowsums',tuple(r))
print('reduced_29_correlations',reduced)
print('reduced_energy',sum(c*c for c in reduced))
print('full_58_energy',sum(c*c for c in C_orb))
print('max_abs_reduced',max(abs(c) for c in reduced))
print('candidate_is_solution',all(c==0 for c in reduced))
print('THEOREM_CHECK: C(s)=N_delta000(s)-N_delta111(s) for all 522 nonzero shifts')
print('THEOREM_CHECK: 58 K-shift equations collapse exactly to 29 <K,-1>-shift equations')
print('ALL_EXACT_D9_HORBIT_CODE_CHECKS_PASSED')
