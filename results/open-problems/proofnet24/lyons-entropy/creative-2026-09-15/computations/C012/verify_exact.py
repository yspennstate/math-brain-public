"""Standard-library exact verification of the C012 certificate.

No LP solver, floating-point determinant, or saved numerical array is used.
"""
from exact_core import *
from coupling import CERT, VERTEX_WEIGHTS, barycentric, weights_at_coordinates
from pathlib import Path
from itertools import product
import json

ROOT=Path(__file__).resolve().parent
assert CERT['ground_set']==list(E)
assert CERT['sets']==[list(X) for X in SETS]
assert CERT['diamonds']==[[list(A),list(B)] for A,B in AB]
# Exact unitarity of the unnormalized Fourier columns.
for i in E:
    for j in E:
        ip=(F(0),F(0))
        for k in E: ip=add(ip,mul(conj(FOURIER[k][i]),FOURIER[k][j]))
        assert ip==(F(6*(i==j)),F(0))
# These coefficients follow by multilinearity under an arbitrary complex row
# rotation; no evaluations of angles are needed.
C=contrast_coefficients()
assert [[str(a) for a in row] for row in C]==[[str(F(a,72)) for a in row] for row in CERT['contrast_coefficient_numerators']]
assert all(probability_coefficients(A,(4,5))==C[SIX[A]] for A in LEVELS[0])
for j in range(4):
    v=[row[j] for row in C]
    assert sum(v)==0
    assert all(sum(v[k] for k,X in enumerate(SETS) if i in X)==0 for i in E)
    assert sum(v[:15])==(j==0)
# Three commuting symmetries flip the three contrast coordinates independently.
for perm,swap,signs in [(SIGMA,False,(1,-1,1,1)),(IDENTITY,True,(1,1,-1,1)),(TAU,False,(1,1,1,-1))]:
    for j in range(4):
        assert act_sets([row[j] for row in C],perm,swap)==[signs[j]*row[j] for row in C]
    for k in range(90):
        atom=[F(i==k) for i in range(90)]
        assert matvec(D,act_weights(atom,perm,swap))==act_sets(matvec(D,atom),perm,swap)
assert tuple(SIGMA[TAU[i]] for i in E)==tuple(TAU[SIGMA[i]] for i in E)
# The two supplied seeds generate all ten exact vertex certificates.
for point,w in VERTEX_WEIGHTS.items():
    assert len(w)==90 and min(w)>=0 and sum(w)==1
    assert matvec(D,w)==at(C,point)
# The report proves the global barycentric formula algebraically. These exact
# evaluations check the implementation, including both pieces and the seam.
points=[(F(1),F(0),F(0)),(F(3,5),F(4,5),F(0)),
        (F(5,13),F(6,13),F(18,13)),(F(1,2),F(0),F(3,2)),
        (F(0),F(1,2),F(-3,2)),(F(1),F(-1),F(1)),(F(0),F(0),F(2))]
for point in points:
    masses=barycentric(*point)
    assert min(masses.values())>=0 and sum(masses.values())==1
    assert tuple(sum(mass*vertex[j] for vertex,mass in masses.items()) for j in range(3))==point
    w=weights_at_coordinates(*point)
    assert min(w)>=0 and sum(w)==1 and matvec(D,w)==at(C,point)
# Recheck C004's right inverse independently, then verify the new exchange-flow
# corrections for both vertices, including all 90 entries of each correction.
Rn=right_inverse_numerators()
for i,X in enumerate(SETS):
    for j,Y in enumerate(SETS):
        p=sum(D[i][k]*Rn[k][j] for k in range(90))
        pinum=42+70*(len(X)-3)*(len(Y)-3)+150*len(set(X)&set(Y))-25*len(X)*len(Y)
        assert p==6*(2100*(i==j)-pinum)
flows,labels=exchange_flows()
assert len(flows)==120 and all(not any(matvec(D,v)) for v in flows)
oriented_flows={tuple(v) for v in flows}|{tuple(-a for a in v) for v in flows}
for perm,swap in [(SIGMA,False),(IDENTITY,True),(TAU,False)]:
    for j in range(50):
        unit=[F(i==j) for i in range(50)]
        image=act_sets(unit,perm,swap)
        k=next(i for i,v in enumerate(image) if v)
        assert act_weights([row[j] for row in Rn],perm,swap)==[row[k] for row in Rn]
    assert all(tuple(act_weights(v,perm,swap)) in oriented_flows for v in flows)
columns=CERT['flow_basis_columns'];rows=CERT['flow_basis_rows']
assert CERT['flow_basis_labels']==[list(labels[j]) for j in columns]
for name in ['cube','tip']:
    rec=CERT[name]
    w=[F(v,rec['denominator']) for v in rec['numerators']]
    theta=[F(v,rec['flow_correction_denominator']) for v in rec['flow_correction_numerators']]
    b=at(C,rec['point']);Rb=[v/F(12600) for v in matvec(Rn,b)]
    assert all(Rb[i]+sum(flows[j][i]*t for j,t in zip(columns,theta))==w[i] for i in range(90))
# Exact witness for the no-affine-lift theorem.
affected=[A for A in LEVELS[0] if len(set(A)&{0,3})==1]
assert len(affected)==8
for A in affected:
    c,h,g,j=C[SIX[A]]
    assert c==F(1,18) and abs(h)==abs(j)==F(1,36) and g==0
    assert c*c==h*h+g*g+3*j*j
assert C[SIX[(0,1,2)]][2]==F(1,24)
assert C[SIX[(1,2,3)]][2]==F(-1,24)
# The sole edge at these two middles whose A and B both avoid singleton
# intersection with {0,3} is their common diamond (12,45).
for M in [(0,1,2),(1,2,3)]:
    exceptional=[]
    for k,(A,B) in enumerate(AB):
        if D[SIX[M]][k] and len(set(A)&{0,3})!=1 and len(set(B)&{0,3})!=1:
            exceptional.append((A,B))
    assert exceptional==[((1,2),(4,5))]
report={'all_exact_checks_passed':True,'unitary_frame':'Fourier-6 with arbitrary complex SU(2) rotation of rows 0 and 3',
        'coefficient_denominator':72,'vertex_count':10,'seed_weight_denominators':[36,72],
        'new_flow_correction_denominators':[288,288],'verified_vertex_marginal_equations':500,
        'verified_right_inverse_identities':2500,'verified_exchange_flows':120,
        'right_inverse_and_flow_symmetry_checks':True,
        'exact_implementation_points':len(points),'nonaffine_obstruction':'rank-one bottom/top faces force incompatible y coefficients at 012 and 123'}
(ROOT/'verified_output.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
