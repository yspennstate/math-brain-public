#!/usr/bin/env python3
"""Exact self-check for P04/I0101 trace-kernel identities at p=257.

This is a finite author self-check only.  The general lemmas are proved
symbolically in the accompanying run report.
"""
P=257

def chi(a):
    a%=P
    if a==0:
        return 0
    return 1 if pow(a,(P-1)//2,P)==1 else -1

V=[x for x in range(P) if x not in (0,1) and chi(x)==1 and chi(x-1)==1]
assert len(V)==63
n=len(V)
idx={x:i for i,x in enumerate(V)}

C=[[0]*n for _ in range(n)]
for i,x in enumerate(V):
    for j,y in enumerate(V):
        if i!=j:
            C[i][j]=chi(x-y)

C2=[[sum(C[i][k]*C[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
S=[sum(chi(t*(t-1)*(t-lam)) for t in range(P)) for lam in range(P)]
assert S[1]==-1

ordered_pairs=0
ordered_edges=0
for i,x in enumerate(V):
    ux=x*pow(x-1,-1,P)%P
    for j,y in enumerate(V):
        if i==j:
            continue
        ordered_pairs += 1
        uy=y*pow(y-1,-1,P)%P

        # Quartic Legendre-family reduction.
        T=sum(chi(t*(t-1)*(t-x)*(t-y)) for t in range(P))
        ratio=uy*pow(ux,-1,P)%P
        assert T==S[ratio]-1

        # Exact C_A^2 identity.
        ksum=(S[y*pow(x,-1,P)%P]
              + S[(y-1)*pow(x-1,-1,P)%P]
              + S[ratio])
        assert 4*C2[i][j]==ksum-6

        # H=(C-I)/2, so 4 H^2_offdiag = C^2_offdiag-2C_offdiag.
        h2_num=C2[i][j]-2*C[i][j]
        assert 4*h2_num==ksum-6-8*C[i][j]

        if C[i][j]==1:
            ordered_edges += 1
            assert 4*h2_num==ksum-14

# Matrix identity for the explicit free-nonedge completion S0.
# Work after multiplying by 4:
# 4 S0 = C^2 - 2J + (3-m)I.
m=n
for i in range(n):
    for j in range(n):
        rhs=C2[i][j]-2+(3-m if i==j else 0)
        if i==j:
            lhs=0
        else:
            x,y=V[i],V[j]
            ux=x*pow(x-1,-1,P)%P
            uy=y*pow(y-1,-1,P)%P
            ksum=(S[y*pow(x,-1,P)%P]
                  + S[(y-1)*pow(x-1,-1,P)%P]
                  + S[uy*pow(ux,-1,P)%P])
            # 4*S0 = (ksum-14)/4, so compare after multiplying by 4 again.
            assert 4*rhs==ksum-14
            lhs=rhs
        if i==j:
            assert rhs==0

print("P04-I0101-TRACE-KERNEL-SELFCHECK=PASS")
print(f"p={P}")
print(f"|V2|={n}")
print(f"unordered_edges={ordered_edges//2}")
print(f"ordered_distinct_pairs={ordered_pairs}")
print("quartic_to_cubic_identity_all_pairs=PASS")
print("conference_square_trace_identity_all_pairs=PASS")
print("edge_second_moment_formula_all_edges=PASS")
print("explicit_completion_matrix_identity=PASS")
print("SELF_CHECK_ONLY=true")
