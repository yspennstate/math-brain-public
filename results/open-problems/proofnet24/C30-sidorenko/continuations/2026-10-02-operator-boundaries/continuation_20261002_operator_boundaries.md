# Operator-route boundaries for the unrestricted ML10 problem

2 October 2026. These calculations distinguish valid general bounds from
the unresolved spectral step. They are not a proof of unrestricted
Sidorenko and do not claim historical novelty for the elementary bounds.

## 1. A valid global trace/Perron bound

Use Rossman's interpolation, with the parameter convention

    M(t)_(ij),(kl)=(Aij Akl)^t (Ail Akj)^(1-t), 0<=t<=1,

for a nonnegative symmetric matrix A. Its trace is always ||A||_F^2.
Its endpoints are M(0)=(A tensor A)S and
M(1)=vec(A)vec(A)^T, where S exchanges the two tensor factors.
Therefore

    rho(M(0))=rho(A)^2, rho(M(1))=||A||_F^2.

Entrywise geometric interpolation and Hölder give

    rho(M(t)) <= rho(A)^(2(1-t)) ||A||_F^(2t)
               <= ||A||_F^2 = tr(M(t)).                 (1)

For completeness, if positive matrices B,C have positive Perron
eigenvectors x,y and H=B^(1-t) Hadamard C^t, apply Hölder row by row to
v_i=x_i^(1-t)y_i^t:

    (Hv)_i <= (Bx)_i^(1-t)(Cy)_i^t
             =rho(B)^(1-t)rho(C)^t v_i.

The Perron/Collatz bound proves the inequality; zero entries follow by
continuity. This is the classical spectral log-convexity mechanism of
Kingman (1961), not claimed as a new theorem. Primary reference:
https://academic.oup.com/qjmath/article/12/1/283/1534893

Thus the total Perron-excluded tail sum is nonnegative for every member
of Rossman's family. This supplies the last endpoint of his proposed
tail inequalities, but not their essential shorter partial sums.

There is also a direct ladder proof of the special bound
rho(M_W)<=sum_ij W_ij^3. A bipartite ladder splits into three perfect
matchings. Hölder on their three products, followed by independence
within each matching, gives

    t(BL_(2m),W) <= (E_(x,y) W(x,y)^3)^m.

Rossman's prior identity hom(BL_(2m),W)=tr(M_W^m), applied to an even
sequence m tending to infinity, gives the asserted spectral-radius
bound. Again this is an elementary prior-tool consequence and an upper
bound, not the lower bound required for Sidorenko.

## 2. Why the generic structural facts do not close the odd-moment gap

One cannot deduce tr(M^5)>=rho(M)^5 from positivity, pair-exchange
symmetry, the correct positive/negative inertia, symmetric-sector
entrywise domination, and (1). Here is a strictly positive rational
nine-by-nine counterexample to that logical implication.

Index rows and columns by ordered pairs (i,j), i,j in{0,1,2}. Let J be
the all-one matrix and S the pair-exchange permutation. Define

    B=J-(3/20)I+(17/20)S.                             (2)

Every entry is positive. It is symmetric and commutes with S. The
symmetric sector has dimension6; its eigenvalues are 97/10 on the
all-one vector and 7/10 with multiplicity5. The antisymmetric sector
has eigenvalue -1 with multiplicity3. Thus its inertia is precisely
6 positive and3 negative, matching the full-rank n=3 Rossman inertia.
Moreover

    tr(B)=51/5 >=97/10=rho(B),
    sum_(tail) lambda=1/2>0.

In the conventional orthonormal unordered-pair basis its symmetric block
is uu^T+(7/10)I, with u_i=1 on diagonal pairs and sqrt(2) on off-diagonal
pairs. Its antisymmetric block is -I. Consequently the corresponding
symmetric principal block entrywise dominates the absolute antisymmetric
block, including its diagonal. Nevertheless

    lambda_2(B)+lambda_min(B)=7/10-1=-3/10<0,
    tr(B^5)-rho(B)^5=5(7/10)^5-3=-43193/20000<0.        (3)

These are exact algebraic equalities, independently checked with rational
matrix powers in the accompanying script.

B is not a Rossman transfer, so it is not a counterexample to his
conjecture or to Sidorenko. Indeed the diagonal entries of any M(t)
recover Aij^2. Here A01^2=17/20 and A00^2=A11^2=17/10. The entry
M(t)_(01),(10) must then be

    (17/20)^t (17/10)^(1-t) <=17/10,

whereas B_(01),(10)=37/20>17/10. Thus the missing product-form constraint
is essential. The example rules out relying on the listed generic
structural facts alone.

## 3. Actual searches and their exact limits

The auxiliary numerical searches optimize actual Rossman transfers,
not arbitrary matrices such as B. Saved files:

- `continuation_20261002_spectral_obstruction_search.py`;
- `continuation_20261002_majorization_n5.json` (100 starts, shortest tail);
- `continuation_20261002_pseudo_1_125_n5.json` (100 starts, signed norm);
- `continuation_20261002_majorization_n8_k4.json` (120 starts, longer tail).

No reliable negative value was found. Minima approached rank-one boundary
matrices, with values of roundoff size. The analytic gradient was checked
against finite differences. These searches neither prove the conjecture
nor certify an obstruction; the exact example (2) concerns only the
insufficient generic proof assumptions.

`continuation_20261002_regular_radial_search.py` additionally searches the
sufficient radial-smoothing condition

    F(W)>=F(J+tau(W-J))

for positive symmetric regular hosts. The regular parameterization is
symmetric Sinkhorn scaling; its derivative is computed implicitly from
the row-sum constraints. The objective's gradient is checked by finite
differences before each run. This is another auxiliary route, not a known
valid implication in reverse: failure of radial monotonicity would not
by itself refute Sidorenko. Results are explicitly labeled numerical.

## 4. The remaining full spectral gap

Rossman's prior transfer identity reduces ML10 to tr(M_W^5). His prior
Rayleigh-vector bound gives rho(M_W)>=n^2(mean W)^3. A sufficient global
step would therefore be

    tr(M_W^5)>=rho(M_W)^5.

Neither (1), generic sector domination, the finite-host Schur certificate,
nor the searches establish this step. The four-state result proves the
target only on its stated family. No unrestricted solution is claimed.
