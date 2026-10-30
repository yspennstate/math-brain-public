SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B11, 2026-09-23T13:14:00Z.

# B11 — exact extension-mass identity and heavy-triple/diffuse-star dichotomy

Status: PROVED NEW DETERMINISTIC IDENTITY / APPLIED FLEET01-B11 / FULL QFORM OPEN / CONTINUITY SEPARATE.

## Scope

Let
[
A=RMR^T,qquad R^TR=I_3,
]
where (M) is real symmetric, invertible, and has signature ((2,1)) or ((1,2)). The random coordinates remain the original independent cap-one variables. No rotation of the product law is used.

Fix a physical pair (S={i,j}). Put
[
n_S=r_i	imes r_j,qquad g_S=|n_S|^2.
]
For (k
otin S), define the nonnegative principal-triple extension mass
[
d_{S,k}:=left|det A[Scup{k},Scup{k}]ight|.
]
Define the ordered overlap-two star
[
W_2(S):=sum_{substack{k,l
otin S\k
e l}}
left|det A[Scup{k},Scup{l}]ight|^2.
]

## Theorem — exact extension-mass second moment

For every physical pair (S),
[
d_{S,k}=|det M|,(n_Scdot r_k)^2,
]
[
sum_{k
otin S}d_{S,k}=|det M|,g_S,
]
and
[
oxed{
W_2(S)=
left(sum_{k
otin S}d_{S,k}ight)^2
-sum_{k
otin S}d_{S,k}^2.
}
]

### Proof

Cauchy--Binet for the rank-three factorization gives
[
det A[Scup{k},Scup{l}]
=det M,det R_{Scup{k}},det R_{Scup{l}}.
]
Since
[
det R_{Scup{k}}=(r_i	imes r_j)cdot r_k=n_Scdot r_k,
]
the first identity follows on taking (k=l). Parseval gives
[
sum_k(n_Scdot r_k)^2
=n_S^T(R^TR)n_S
=|n_S|^2=g_S.
]
The terms (k=i,j) vanish. Finally,
[
W_2(S)=|det M|^2
sum_{k
e l}(n_Scdot r_k)^2(n_Scdot r_l)^2,
]
which is exactly the square of the sum minus the sum of squares. QED.

## Quantitative dichotomy

Let
[
T_S:=|det M|g_S=sum_k d_{S,k}.
]
For every (0<arepsilon<1), at least one of the following holds:

1. heavy extension:
[
max_k d_{S,k}>(1-arepsilon)T_S;
]

2. diffuse overlap-two star:
[
oxed{W_2(S)ge arepsilon T_S^2
=arepsilon|det M|^2g_S^2.}
]

Indeed, if every (d_{S,k}le(1-arepsilon)T_S), then
[
sum_kd_{S,k}^2
le(max_k d_{S,k})sum_kd_{S,k}
le(1-arepsilon)T_S^2.
]

Thus a small overlap-two star is not an independent analytic degeneration: it forces nearly all extension volume of the pair through one actual original coordinate.

## Completed fleet01/B11 input applied

The completed fleet01/B11 area compiler gives, for spectral scale
[
s=min_a|lambda_a(M)|,
]
the actual full-line inequality
[
oxed{
|p_{X^TAX}|_infty
le rac{128sqrt2}{ssqrt{g_S}}.
}
]
This pays every pair with nonnegligible exterior area, including the heavy-extension alternative above. In the complementary diffuse-star alternative, the B01 averaged-frequency theorem applies whenever the physical pair is invertible indefinite:
[
|p_{X^TAX}|_infty
le22.385,
igl(|det A[S,S]|,s_{min}(A[S,S])igr)^{-1/6}
W_2(S)^{-1/12}.
]
Substitution of the new deterministic lower bound gives
[
oxed{
|p_{X^TAX}|_infty
le22.385,arepsilon^{-1/12}
igl(|det A[S,S]|,s_{min}(A[S,S])igr)^{-1/6}
|det M|^{-1/6}g_S^{-1/6}.
}
]
This is a genuine full-line bound; the ruled theorem remains restricted to its one-sheet half-line.

## What remains

Globally, the triple-volume weights
[
v_T=det(R_TR_T^T),qquad sum_{|T|=3}v_T=1,
]
can still cluster so that every individual pair area is small. The new identity reduces the unpaid geometry to a hypergraph routing question:

- a pair whose extension masses are diffuse supplies overlap-two star energy;
- a pair whose star energy is small supplies one heavy physical triple;
- two disjoint heavy triples are already paid by the disjoint-volume compiler;
- the residual is intersecting heavy-triple clustering, which must be routed into a common-coordinate hub or another paid bank receiver.

No full solution or counterexample is claimed. Arbitrary extra spectrum remains a separate interface. Small operator norm is not used as a small random quadratic error under unbounded input laws.
