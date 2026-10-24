# account02/B16 multiplicity-eight replacement, part 2 of 3

Continue from Part 1. We are in the hypothetical no-pivot, s_8>=1, V_3<kappa^3 chamber.

## Robust literal two-anchor

For a physical two-set H define

D_H=sum_{U subset H^c, |U|=2} det A[H,U]^2.

If C_H=A[H,H^c], Cauchy-Binet gives

D_H=det(C_H C_H^T),

and by definition of the ordered disjoint order-two volume,

sum_H D_H=V_2.

Assign to every good seed B=A[S,T] one two-set H supplied by the collar inequality from Part 1, and define

w_H=sum_{good seeds assigned to H} det A[S,T]^2.

Good seeds carry at least V_2/2, so some H_* satisfies

w_H* >= D_H*/2.                             (2)

For this H_*, square the collar inequality and sum over the assigned seeds. Every resulting term belongs to

Xi_H*=
sum_{S,T subset H_*^c, |S|=|T|=2, S cap T=empty}
det A[H_*,S]^2 det A[H_*,T]^2.

Thus

delta_*^2 w_H* <= Xi_H*
<= (sum_{U subset H_*^c, |U|=2} det A[H_*,U]^2)^2
=D_H*^2.

Together with (2),

g:=D_H*=det(CC^T)
>=delta_*^2/2
=0.364944265882702... >8/25,                (3)

where C=A[H_*,H_*^c].

There is no dimension-dependent reciprocal of an individual minor.

## Determinantal leverage

Put L=H_*^c and define the rank-two orthogonal projection

Q_C=C^T(CC^T)^(-1)C,
P_0=I-Q_C,
q_i=(Q_C)_ii,
p_i=1-q_i.

For distinct i,j in L let

omega_ij=det(C_{i,j})^2/g.

Cauchy-Binet makes omega a probability law on two-subsets. Its inclusion marginal is

q_i=sum_{j!=i} omega_ij.

A direct proof: whiten the two rows of C so BB^T=I_2. Then omega_ij=det(b_i,b_j)^2 and
sum_j det(b_i,b_j)^2=||b_i||^2=q_i.

No pivot gives

|A_uv|^2<eta^2+eta=101/10000  for u!=v.

Therefore every two-column minor of C satisfies

|det C_{i,j}|<2(eta^2+eta)=101/5000.

By (3),

omega_ij<0.00112<0.02.

If distinct i,j both had q_i,q_j>0.51, inclusion-exclusion for the two-set probability law would give

omega_ij=P(i and j)>=q_i+q_j-1>0.02,

a contradiction. Hence at most one complement coordinate e has q_e>0.51.

Delete that one coordinate, or delete any one if none exists, and put L'=L\{e}. Then

p_i>=0.49 for every i in L'.                (4)

## Exact anchored disjoint third-minor identity

Write D_out=A[L,L]. For i in L let d_i be row i of D_out and set

r_i=d_i P_0.

For i in L' define

W_i=
sum_{T subset L\{i}, |T|=3}
det A[H_* union {i},T]^2.                   (5)

Every term in (5) is an ordinary disjoint 3-by-3 minor: its row set is H_* union {i}, and its column set lies in L\{i}.

The exact identity is

W_i=g( p_i ||r_i||_2^2-r_ii^2 ).           (6)

Proof of (6): subtract from d_i its projection onto row(C), leaving the row r_i and preserving all 3-by-3 minors with the two anchor rows. Remove column i. The anchor Gram determinant changes from g to g p_i by the matrix determinant lemma. Since C r_i^T=0, the Schur complement of the reduced three-row Gram matrix equals ||r_i||^2-r_ii^2/p_i. Multiplication gives (6).

Let

W'=sum_{i in L'} W_i.

Part 3 proves W'>0.0098, which contradicts V_3<kappa^3 because W' is literally a sub-sum of V_3.
