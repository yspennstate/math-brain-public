# FOREST B02 — deletion-boundary reconnection identity and CLC Schur gate

Run: `20260922T050844Z-b02-forest-r12`

Outcome: **ESSENTIAL_STEP_APPLIED**. The team's existing `FOREST-KN-COCKS-RECONCILED-v3` remains an internal `FULL_PROOF_CANDIDATE`; this report does not promote the Grimmett-Winkler forest conjecture to an established/public result, novelty, or priority claim. Context: `WITHOUT_VERIFIED_BRAIN`.

## Exact inputs consumed

Lead: fleet01/B01 `FOREST-KN-COCKS-RECONCILED-v3`, commit `0509904b9b699563a2b6fe60b6226948886a6b86`, handoff blob `e02a4281a67d992d06d7c2c70586efa656353cab`. Its complete conditional chain is

`unit theorem on every K_n -> Cocks fixed-graph weighted upgrade -> Semple-Welsh minor closure -> arbitrary simple G by deletion -> unit target`.

Latest named OTHER-account partner consumed: fleet03/B03 `FOREST-KN-TO-ALL-SOURCE-CLOSURE-v1`, handoff blob `199bba1b1e1e0d11fa721d12d90d5defc1a5bf20`. It independently source-validates the same globalization chain and supplies a 5-vertex weighted witness whose Rayleigh polynomial has a negative mixed coefficient while remaining positive for every positive weight. I apply that witness below to the new reconnection identity. I also use the partner's immediately preceding `FOREST-STARK-THETA-EXACT-v1`, blob `8afc6858af7d5deedc916c663d78158d87534eda`, which shows that explicit simple theta families force arbitrarily large positive virtual boundary weights; a bounded-weight separator proof cannot cover all graphs.

Primary source anchors:

* Anari--Liu--Oveis Gharan--Vinzant, *Log-Concave Polynomials III: Mason's Ultra-Log-Concavity Conjecture for Independent Sets of Matroids*, arXiv:1811.01600, pp. 1--2: for an n-element matroid, `g_M(y,z)=sum_{I independent} y^(n-|I|) z^I` is completely log-concave. The exponent is the ground-set size `n`, not the matroid rank. The same source explicitly distinguishes spectral negative dependence from entrywise negative correlation.
* Semple--Welsh, *Negative correlation in graphs and matroids*, Combinatorics, Probability and Computing 17 (2008): Section 2 defines independence correlation for every positive real edge weighting; Proposition 3.5 proves minor closure; the Section 5 Note explicitly records Cocks's fixed-graph theorem that if Conjecture 1.1 holds for a graph G, then M(G) is independence correlated.

## 1. Exact deletion-boundary reconnection identity

Fix distinct edges `e,f` of a finite simple graph `G`, and put `H=G-{e,f}`. Give the edges of H arbitrary positive weights `w`. Let `mu_H` be the weighted forest law

`mu_H(S)=w^S/A`,  `A=sum_{S forest in H} w^S`.

For a forest `S` in H define

`A_e(S)=1{S+e is acyclic}`,  `A_f(S)=1{S+f is acyclic}`,

`J_ef(S)=1{S+e+f is acyclic}`,

and the reconnection indicator

`Q_ef(S)=A_e(S)A_f(S)-J_ef(S)`.

Graphically, `Q_ef=1` exactly when e and f are individually addable but together create a cycle. Equivalently, after contracting every component of S, the images of e and f are distinct nonloops forming a parallel pair in the quotient multigraph.

Set

`B=sum A_e(S)w^S`, `C=sum A_f(S)w^S`, `D=sum J_ef(S)w^S`.

With activities `x,y` on e,f, the full forest polynomial is exactly

`Z_G(x,y;w)=A+xB+yC+xyD`.

Hence its Rayleigh difference is independent of x,y:

`Delta_ef=(partial_e Z)(partial_f Z)-Z partial_ef Z=BC-AD`.

Writing

`a=P_H(A_e=1)`, `b=P_H(A_f=1)`, `j=P_H(J_ef=1)`, `q=P_H(Q_ef=1)`,

we have `j=P_H(A_eA_f)-q`, so

`Delta_ef/A^2 = ab-j = q-Cov_H(A_e,A_f)`.

Therefore the desired sign is **equivalent** to the concrete probabilistic comparison

`Cov_H(A_e,A_f) <= P_H(Q_ef=1)`.

This is not a reformulation using rooted forests, fixed size, or a surrogate measure: at unit H weights it is exactly the source uniform law on all unrooted forests of H.

## 2. Complete log-concavity at the deletion boundary

Let `m=|E(G)|`. For the graphic matroid, the ALOV homogenization is exactly

`g(y,z)=sum_{F forest in G} y^(m-|F|) z^F`.

At `y=1` and positive edge activities this is the partition function of all unrooted forests; setting all activities to one gives the requested uniform law, including the empty forest, disconnected forests, and every size. ALOV proves complete log-concavity of this exact polynomial.

Evaluate at `y=1`, `z_h=w_h` for `h in H`, and take `z_e,z_f -> 0+`. By log-concavity on the positive orthant and continuity,

`R := grad(g)grad(g)^T-g Hess(g) = -g^2 Hess(log g) >= 0`

at the deletion boundary.

Under `mu_H`, write `K=|S|`, `mu=E K`, `v=Var K`, and define

`u_e=a+Cov(A_e,K)`, `u_f=b+Cov(A_f,K)`,

`r=m-mu-v`, `t=ab-j=q-Cov(A_e,A_f)`.

Direct differentiation gives the exact principal block

```
R[{y,e,f}]/A^2 =
[ r    u_e  u_f ]
[ u_e  a^2  t   ]
[ u_f  t    b^2 ]  >= 0.
```

Indeed, `g_y/A=E(m-K)`, `g_yy/A=E[(m-K)(m-K-1)]`, `g_e/A=a`, and `g_ye/A=E[A_e(m-K-1)]`, with the analogous f identities.

Consequently, for every finite simple graph and every positive H-weighting,

`r>=0`, `u_e^2<=r a^2`, `u_f^2<=r b^2`, and `|t|<=ab`.

The last inequality is the source-valid factor-two statement `0<=j<=2ab`; it is spectral and does **not** assert the Rayleigh sign.

When `r>0`, the Schur complement gives the sharper interval

`|t-u_eu_f/r| <= sqrt[(a^2-u_e^2/r)(b^2-u_f^2/r)]`.

Equivalently,

`Cov(A_e,A_f)-q <= -u_eu_f/r + sqrt[(a^2-u_e^2/r)(b^2-u_f^2/r)]`.

A concrete sufficient sign certificate is

`u_eu_f>=0` and `(u_e/a)^2+(u_f/b)^2>=r`

for `a,b>0`, `r>0`; then the lower endpoint of the Schur interval is nonnegative. This certificate is not claimed universal. If `r=0`, PSD forces `u_e=u_f=0`, so the unsimplified block is used rather than dividing by r.

### First essential missing implication for a log-concavity-only proof

The exact unpaid statement is now

`Cov_H(A_e,A_f) <= P_H(Q_ef=1)`.

Complete log-concavity supplies the displayed PSD/Schur interval but does not force its lower endpoint nonnegative. Any independent proof that avoids the Cocks transfer must inject genuinely graphic structure into this reconnection-domination step; citing log-concavity as though it implied entrywise Rayleigh would be invalid.

## 3. Named partner witness applied to the reconnection identity

The latest fleet03/B03 handoff gives the simple graph

`E={02,03,04,12,13,14,23}`

with `e=02`, `f=13`, and variable activity `w` on `g=23`, whose exact Rayleigh polynomial is

`Delta(w)=36-2w+4w^2`.

I independently re-expanded this witness through the boundary variables above. For `H=G-{e,f}` the coefficient pairs (g absent, g present) are

`A=(16,15)`, `B=(14,7)`, `C=(14,7)`, `D=(10,3)`, `Q=(3,1)`.

Therefore

`Delta(w)=(14+7w)^2-(16+15w)(10+3w)=36-2w+4w^2`,

`q(w)=(3+w)/(16+15w)`,

`Cov(A_e,A_f)=(12+63w+11w^2)/(16+15w)^2`,

and exactly

`q(w)-Cov(A_e,A_f)=Delta(w)/(16+15w)^2`.

The mixed coefficient of Delta is negative, yet its discriminant is `-572`, so Delta is positive for every real w. This **refutes coefficientwise positivity of the weighted Rayleigh polynomial as a universal proof mechanism** while simultaneously showing, in the new language, that reconnection domination can be true only after cancellation between coefficients. The partner result is therefore directly applied rather than merely cited.

## 4. Exact homogenization normalization negative control

The ALOV homogenizing degree is the number of ground-set elements. Replacing `m=|E(G)|` by the graphic rank is not source-valid and is not an innocuous reparameterization. On `K_3` with two marked edges, the resulting putative `(y,e,f)` matrix has determinant exactly `-1/16`. Thus the rank-homogenized shortcut fails PSD already on a triangle.

This is a source-valid counterexample to that tempting normalization shortcut and is why all formulas above retain the ground-set degree exactly as stated in ALOV.

## 5. Exact regression

`forest_boundary_reconnection_check.py` exhaustively enumerates every labelled simple graph on 2--5 vertices: 1,098 graphs and 11,766 present edge pairs. It checks the reconnection identity, every principal minor of the CLC block, the factor-two consequence, and the target sign, both at unit H-weights and at a deterministic positive 1/2/3 weight pattern. Both regimes have zero identity, PSD, factor-two, and target failures. Positive addability covariance occurs in 5,973 pair instances. The largest exact observed `Cov(A_e,A_f)/q` is `119/134` at unit weights and `21325/21984` in the weighted regression. The Schur sufficient certificate alone closes 63 instances, so it is useful but far from universal. The checker also verifies the `K_3` rank-degree determinant `-1/16` and ends `STATUS=ALL_EXACT_CHECKS_PASS`.

Checker SHA-256: `6cf8c08d0d0e76a26eb505dedffdf31cbf645ea20bc2f9983752f76232761ec4`.
Output SHA-256: `dbf82f65977a8794cc4da36b14d8556408bdeeefb4eea1e40712b841b0e93654`.

The separate partner-witness checker ends `STATUS=PARTNER_WITNESS_RECONNECTION_IDENTITY_PASS`.
Checker SHA-256: `43085485e8e30d6e952b62c85386f2c6458bd3ad74b063559ef0142be63799cd`.
Output SHA-256: `0f2735509cc09c0bef2de34a67f2397280be9b9cb8ca871e8fdb0e4236a7a7d1`.

Finite enumeration is regression evidence only and is not used to extrapolate the all-graphs theorem.

## 6. Relation to the team's current proof candidate

This report does not create a new unpaid step in the lead's existing internal full candidate. The lead route remains the complete-graph Hermite theorem followed by the fixed-graph Cocks weighted upgrade and Semple--Welsh minor closure, and its v3 handoff records two internal end-to-end reviews. The present contribution is a materially different deletion-boundary mechanism that clarifies exactly what complete log-concavity can and cannot supply and gives an equivalent reconnection-domination target for any proof avoiding Cocks.

Public/external closure still requires ordinary expert/source scrutiny of the assembled proof, especially the original Cocks result and the complete-graph Hermite/Stark argument, before any claim that a longstanding open problem is solved.
