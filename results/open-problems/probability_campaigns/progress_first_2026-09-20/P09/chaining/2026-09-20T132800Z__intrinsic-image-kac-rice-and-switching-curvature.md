Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime does not expose authenticated GPT-6/maximum-effort attestation.

# P09 progress-first run — intrinsic image Kac–Rice, exact switching curvature, and a sharp matrix log obstruction

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The full arbitrary-tensor polynomial exponent in the unresolved regime `2 <= p < 2r` remains

```text
gamma = 1/2 - 1/(2r),
```

versus the conjectured

```text
alpha = 1/2 - 1/p.
```

The main purpose of this run is to complete one missing geometric step from the preceding support-curvature/Kac–Rice report and to falsify an overstrong version of that route before more work is built on it.

The predecessor derived an exact smooth-sheet support Hessian containing `Tr(G^{-1}Q)` and observed the algebraic cancellation

```text
det(G) Tr(G^{-1}Q) = Tr(adj(G)Q).
```

The remaining concern was that a rank-stratified Kac–Rice formula still appeared to carry the singular density factor `det(Q)^(-1/2)` when the image differential becomes small. This run proves that this factor is a **parameterization artifact** on every regular image sheet: after passing to the induced image metric, all singular values of the differential cancel exactly. The resulting integrand depends only on the intrinsic shape operator of the output image.

However, a second and more important obstruction appears. An explicit diagonal matrix family with the exact source normalization has

```text
S^2 = sum_i ||T_i||_(I_2)^2 = 1
```

but

```text
E ||sum_i g_i T_i||_(I_2) = Theta(sqrt(log d)).
```

For this family every exposed sheet is flat, so the smooth Kac–Rice curvature is zero. The entire `Theta(log d)` excess in the second moment is carried by the **singular switching curvature** where two exposed linear branches exchange dominance. Thus smooth critical-point Kac–Rice alone cannot prove even the matrix case. The branch-switch term is not a technical remainder; it can be the leading term.

The new geometric architecture is therefore two-part:

1. regular exposed image sheets are handled intrinsically by a normal-cycle/Kac–Rice formula in which differential singular values and preimage multiplicity disappear;
2. switching strata are handled by an exact jump formula whose density is the **output chord length** between the competing exposed points.

This isolates a new concrete arbitrary-case target: control the Gaussian weighted switching-chord measure at each critical scale, with the unavoidable matrix calibration showing that a logarithmic budget is necessary and sufficient in the simplest polyhedral case.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Registered role: `chaining / geometric-probabilistic proof`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Pre-write master observed: `969154c075f7d1b832cb00320f7a77c6390aa323`
- Immediate predecessor: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T124000Z__gaussian-support-curvature-and-kac-rice-adjugate-cancellation.md`
- Historical C0035 material, all prior P09 reports, and peer files are preserved. This report is additive and immutable.

---

## 1. Exact source normalization and current baseline

Primary source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizić-Nikolac, A. Rödder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.

For symmetric deterministic order-`r` tensors `T_1,...,T_n` on `R^d`, iid standard Gaussian `g_i`, and

```text
||T||_(I_p) := sup_(||x||_p<=1) |T[x,...,x]|,
```

the source asks for

```text
E ||sum_i g_i T_i||_(I_p)
 <= C(r,p) polylog(d,n) d^(1/2-1/p)
    (sum_i ||T_i||_(I_p)^2)^(1/2).                       (1.1)
```

A fresh bounded primary-source check on 20 September 2026 confirms that the source still states Conjecture 16 in this form. The BGJLR theorem (arXiv:2411.10633, Theorem 1.2) gives the general type-2 upper exponent

```text
1/2 - 1/max{p,2r},                                      (1.2)
```

up to its logarithmic factor. Hence in the unresolved regime `p<2r` the polynomial exponent is

```text
1/2 - 1/(2r).                                           (1.3)
```

The same source records Aden-Ali, arXiv:2503.10580, as improving the general variance-parameter/logarithmic estimate but not removing the arbitrary-correlated `p<2r` polynomial obstruction. The source also distinguishes the already established matrix, rank-one, independent-entry and `p>=2r` regimes.

No full resolution of the exact arbitrary deterministic low-`p` statement was found in this bounded check. This is not a claim about unpublished or unindexed work.

The fixed source metric remains

```text
old arbitrary exponent = 1/2 - 1/(2r)
new arbitrary exponent = 1/2 - 1/(2r)
target exponent        = 1/2 - 1/p
source status           = OPEN / not solved here.
```

---

## 2. Inherited support-curvature identity

Set

```text
S^2 := sum_i ||T_i||_(I_p)^2,
F(x) := (T_i[x^r])_(i=1)^n,
K := conv(F(B_p^d) union -F(B_p^d)).                    (2.1)
```

The Gaussian tensor norm is the support function

```text
h(g)
 := sup_(y in K) <g,y>
  = ||sum_i g_iT_i||_(I_p).                              (2.2)
```

Since `||F(x)||_2<=S`, the support function is `S`-Lipschitz.

The preceding run proved the exact distributional identity

```text
E h(g)^2
 = E ||grad h(g)||_2^2
   + integral h(g) phi_n(g) d(Delta h)(g),               (2.3)
```

where `Delta h` is the nonnegative distributional Laplacian measure. Thus

```text
E ||grad h||_2^2 <= S^2                                 (2.4)
```

and all remaining growth is contained in the Gaussian-weighted support-curvature measure

```text
I_curv := integral h phi_n d(Delta h).                   (2.5)
```

The predecessor identified the absolutely continuous density on a smooth exposed parameter branch. This report rewrites that density **intrinsically on the output image** and then treats the singular switching part.

---

## 3. Regular image sheets: quotient the parameterization before Kac–Rice

The following theorem is stated for an arbitrary smooth output sheet. It is therefore independent of the particular tensor parameterization used to generate that sheet.

Let `M subset R^n` be a `C^2` immersed `j`-dimensional submanifold. For fixed `g in R^n`, write

```text
ell_g(y) := <g,y>, y in M.                               (3.1)
```

At a critical point `y` of `ell_g|_M`, `g` is normal to `M`. Let

```text
S_(y,g) := - Hess_M ell_g(y)                             (3.2)
```

be the negative Riemannian Hessian, viewed in an orthonormal tangent frame. At a nondegenerate local maximum, `S_(y,g)` is positive definite.

### Theorem 3.1 — intrinsic regular-sheet support Hessian

Suppose `y=y(g)` is a locally unique nondegenerate maximizing point of `ell_g` on a smooth image sheet `M`. Then

```text
Hess_g h_M(g)
 = J_y S_(y,g)^(-1) J_y^*,                               (3.3)
```

where `J_y : T_yM -> R^n` is the isometric inclusion. Consequently

```text
boxed:
Delta h_M(g) = Tr(S_(y,g)^(-1)).                         (3.4)
```

#### Proof

Choose geodesic normal coordinates `u in R^j` on `M` centered at `y`, so the coordinate derivative matrix `J=Dy(0)` has orthonormal columns. The critical equation is

```text
J(u)^* g = 0.                                            (3.5)
```

Differentiate (3.5) in a coefficient direction `z`. At `u=0`, the derivative in the parameter direction `dot u` is the Hessian of the height function:

```text
D_u(J(u)^*g)[dot u]
 = Hess_M ell_g(y) dot u
 = -S_(y,g) dot u.                                       (3.6)
```

The derivative with respect to `g` is `J^*z`. Hence

```text
-S_(y,g) dot u + J^*z = 0,

dot u = S_(y,g)^(-1) J^*z.                              (3.7)
```

By the envelope theorem,

```text
grad_g h_M(g)=y(g).                                      (3.8)
```

Therefore

```text
D_g(grad h_M)[z]
 = J dot u
 = J S_(y,g)^(-1)J^* z,                                 (3.9)
```

which proves (3.3). Since `J^*J=I_j`, taking the ambient trace gives (3.4). QED.

### Relation to the predecessor's `G^{-1}Q`

Suppose a local tensor parameterization `u -> F(x(u))` has full image rank `j`. Put

```text
J := D_uF,
Q_im := J^*J,
H := - Hess_u <g,F(x(u))>                                (3.10)
```

at a nondegenerate critical point. Then the induced-metric shape operator is

```text
S = Q_im^(-1/2) H Q_im^(-1/2).                          (3.11)
```

In the original redundant parameter coordinates the smooth support curvature is

```text
Tr(H^(-1)Q_im).                                          (3.12)
```

In orthonormal image coordinates it is simply `Tr(S^{-1})`. Thus the object entering the support Hessian is intrinsic to the image sheet, not to the choice of tensor parameterization.

---

## 4. Kac–Rice on the image sheet: exact cancellation of differential singular values

For each fixed `y in M`, the tangential critical field is

```text
Psi_g(y) := P_(T_yM) g.                                  (4.1)
```

In an orthonormal tangent frame, `Psi_g(y)` is a standard `j`-dimensional Gaussian. Therefore

```text
p_(Psi_g(y))(0) = (2pi)^(-j/2),                          (4.2)
```

independently of every singular value of the original map `DF`.

At a critical point, differentiation along the image manifold gives

```text
D_y Psi_g = -S_(y,g),                                    (4.3)
```

up to the harmless orientation convention. Hence the Kac–Rice Jacobian at a local maximum is

```text
det S_(y,g).                                             (4.4)
```

### Theorem 4.1 — intrinsic adjugate formula for regular exposed sheets

Under the usual local nondegeneracy hypotheses for Kac–Rice, the Gaussian-weighted smooth support-curvature contribution of a regular `j`-dimensional image sheet has local intensity

```text
boxed:
(2pi)^(-j/2)
 h_y(g) Tr(adj(S_(y,g)))
 1_(S_(y,g) positive definite),                          (4.5)
```

where

```text
h_y(g):=<g,y>.                                           (4.6)
```

More precisely, summing (4.5) over all local maxima on the sheet upper-bounds the exposed-global-max smooth curvature contribution, while inserting the exposed-global-max indicator gives equality on that sheet.

#### Proof

By Theorem 3.1, the support-curvature weight at a nondegenerate local maximum is

```text
h_y(g) Tr(S^(-1)).                                       (4.7)
```

Kac–Rice multiplies this by the critical-field density `(2pi)^(-j/2)` and by the Jacobian `det S`. Since `S` is positive definite at a local maximum,

```text
det(S) Tr(S^(-1))
 = Tr(adj(S)).                                           (4.8)
```

This yields (4.5). QED.

### Coordinate-level cancellation identity

The same result can be verified directly from a nonorthonormal parameterization. With `Q_im` and `H` from (3.10), the Kac–Rice density of the parameter critical field is

```text
(2pi)^(-j/2) det(Q_im)^(-1/2).                           (4.9)
```

Its Jacobian is `det H`, and the support-curvature weight is `Tr(H^(-1)Q_im)`. Thus, before changing variables, the relevant measure is

```text
(2pi)^(-j/2)
 det(Q_im)^(-1/2)
 det(H)
 Tr(H^(-1)Q_im) du.                                     (4.10)
```

The induced image-volume element is

```text
dH^j(y)=det(Q_im)^(1/2) du.                              (4.11)
```

Using `S=Q_im^(-1/2) H Q_im^(-1/2)`, one obtains the exact identity

```text
boxed:
det(Q_im)^(-1/2) det(H) Tr(H^(-1)Q_im) du
 = Tr(adj(S)) dH^j(y).                                   (4.12)
```

Thus **all powers of the differential singular values cancel** on every regular image sheet.

This resolves the apparent `det(Q)^(-1/2)` blow-up left in the predecessor's rank-stratified formulation. Small image Jacobian is not, by itself, a regular-sheet obstruction. Rank-change and branch-switch strata still require separate treatment.

---

## 5. Exact singular curvature when exposed branches switch

The smooth formula above is not the whole support-curvature measure. The missing part can be written exactly.

Let `h_1,h_2` be `C^2` functions on an open set `U subset R^n`, and define

```text
h := max{h_1,h_2}.                                       (5.1)
```

Assume the switching interface

```text
Sigma := {g in U : h_1(g)=h_2(g)}                        (5.2)
```

is smooth and

```text
grad(h_1-h_2) != 0 on Sigma.                            (5.3)
```

### Theorem 5.1 — switching-Hessian jump formula

The singular part of the distributional Hessian of `h` on `Sigma` is

```text
boxed:
D^2 h|_sing
 = [(a tensor a)/||a||_2]
   H^(n-1)|_Sigma,

a := grad h_1 - grad h_2.                               (5.4)
```

Consequently the singular Laplacian measure is

```text
boxed:
Delta h|_sing
 = ||grad h_1-grad h_2||_2
   H^(n-1)|_Sigma.                                       (5.5)
```

#### Proof

On the two sides of `Sigma`, the distributional gradient is

```text
grad h
 = grad h_1 1_(h_1>h_2)
   + grad h_2 1_(h_2>h_1).                               (5.6)
```

The unit normal pointing from the `h_2` side to the `h_1` side is

```text
nu = grad(h_1-h_2)/||grad(h_1-h_2)||_2
    = a/||a||_2.                                         (5.7)
```

Differentiating (5.6) distributionally gives the ordinary Hessians in the two open regions plus the jump tensor

```text
(grad h_1-grad h_2) tensor nu
 = (a tensor a)/||a||_2                                  (5.8)
```

on the interface. Taking the trace gives (5.5). QED.

### Corollary 5.2 — switching curvature is output chord length

Suppose the two branches are smooth support branches, so

```text
grad h_a(g)=y_a(g) in K, a=1,2.                         (5.9)
```

Then

```text
boxed:
Delta h|_sing
 = ||y_1(g)-y_2(g)||_2 H^(n-1)|_Sigma.                  (5.10)
```

Therefore their contribution to the Gaussian support-curvature budget is exactly

```text
boxed:
integral_Sigma
 h(g) phi_n(g)
 ||y_1(g)-y_2(g)||_2
 dH^(n-1)(g).                                            (5.11)
```

The singular measure charges **output displacement**, not parameter distance, not preimage multiplicity, and not the number of critical points.

For a generic finite collection of branches, codimension-two multiple intersections do not carry `(n-1)`-dimensional Hessian mass, so the singular Laplacian is the sum of (5.10) over adjacent pairwise switching interfaces.

---

## 6. A sharp matrix calibration: sqrt(log d) is genuinely necessary in the source normalization

The next example is a mandatory countertest for any attempt to bound the support-curvature budget by `O(S^2)` independently of switching complexity.

Fix an integer `m>=1` and set

```text
d := 2^m,
n := m.                                                  (6.1)
```

Index the coordinates of `R^d` by sign vectors

```text
s=(s_1,...,s_m) in {+1,-1}^m.                           (6.2)
```

For `i=1,...,m`, define the diagonal symmetric matrix

```text
T_i := (1/sqrt(m)) diag( s_i )_(s in {+1,-1}^m).         (6.3)
```

### Theorem 6.1 — exact source-normalized logarithmic lower bound

The matrices (6.3) satisfy

```text
||T_i||_(I_2)=1/sqrt(m),
S^2=sum_i ||T_i||_(I_2)^2=1.                             (6.4)
```

For `g_1,...,g_m` iid standard Gaussian,

```text
boxed:
||sum_i g_iT_i||_(I_2)
 = (1/sqrt(m)) sum_i |g_i|.                              (6.5)
```

Hence

```text
boxed:
E ||sum_i g_iT_i||_(I_2)
 = sqrt(2/pi) sqrt(m)
 = sqrt(2/(pi log 2)) sqrt(log d).                       (6.6)
```

Moreover

```text
boxed:
E h(g)^2
 = 1 + (2/pi)(m-1).                                      (6.7)
```

Thus a `sqrt(log d)` factor is unavoidable in Conjecture 16's exact `S` normalization already for the matrix case.

#### Proof

Each `T_i` is diagonal with entries `+/-1/sqrt(m)`, so (6.4) is immediate. The random sum is diagonal with `s`-th diagonal entry

```text
(1/sqrt(m)) sum_i g_i s_i.                               (6.8)
```

Maximizing over all sign vectors `s` chooses `s_i=sign(g_i)`, giving (6.5). Taking expectation and using

```text
E|g_i|=sqrt(2/pi)                                        (6.9)
```

gives (6.6). For the second moment,

```text
E h^2
 = (1/m) E (sum_i |g_i|)^2
 = (1/m)[m + m(m-1)(2/pi)]
 = 1+(2/pi)(m-1).                                        (6.10)
```

QED.

### Relation to the support body

The exposed output points are the sign vectors

```text
y_s=s/sqrt(m) in R^m.                                   (6.11)
```

Their convex hull is the cube

```text
K=[-1/sqrt(m),1/sqrt(m)]^m,                              (6.12)
```

and therefore

```text
h(g)=||g||_1/sqrt(m).                                    (6.13)
```

Every individual exposed branch is linear and has zero smooth Hessian. Consequently the whole growth beyond the gradient term in (2.3) must be singular switching curvature.

---

## 7. Exact switching-curvature computation for the matrix example

Away from the coordinate hyperplanes `g_i=0`,

```text
grad h(g)
 = (1/sqrt(m))(sign g_1,...,sign g_m),                   (7.1)
```

so

```text
||grad h(g)||_2^2=1=S^2                                 (7.2)
```

almost everywhere.

Distributionally,

```text
Delta h
 = (2/sqrt(m)) sum_(i=1)^m delta_{g_i=0} dg_{-i}.       (7.3)
```

### Theorem 7.1 — the entire logarithmic excess is switching curvature

For the family (6.3),

```text
boxed:
integral h(g) phi_m(g) d(Delta h)(g)
 = (2/pi)(m-1).                                          (7.4)
```

Therefore the identity (2.3) is exact term-by-term:

```text
E h^2
 = 1 + (2/pi)(m-1),                                      (7.5)
```

with the first `1` equal to `E||grad h||^2` and the whole `Theta(log d)` remainder equal to the singular switching measure.

#### Proof

From (7.3),

```text
I_curv
 = sum_i (2/sqrt(m))
   integral_(R^(m-1))
   h(0,g_-i) phi_m(0,g_-i) dg_-i.                       (7.6)
```

Now

```text
h(0,g_-i)
 = (1/sqrt(m)) sum_(j!=i)|g_j|.                          (7.7)
```

Using

```text
phi_1(0)=1/sqrt(2pi),
E|g|=sqrt(2/pi),                                         (7.8)
```

each `i` contributes

```text
(2/sqrt(m)) phi_1(0)
 ((m-1)/sqrt(m)) sqrt(2/pi)
 = 2(m-1)/(pi m).                                        (7.9)
```

Summing over `m` coordinates gives (7.4). QED.

### Consequence

This refutes the tempting intermediate lemma

```text
I_curv <= C_r S^2                                       (7.10)
```

even for `r=p=2`.

More importantly, it proves that a proof strategy which controls only the absolutely continuous/smooth Kac–Rice curvature and treats branch switching as negligible cannot establish the source conjecture. The switching part can be the dominant term and must be budgeted at least logarithmically.

This does **not** refute Conjecture 16: the conjecture explicitly allows polylogarithmic losses, and the example exactly fits that allowance.

---

## 8. Finite-branch aggregation: a clean sufficient switching bound

The matrix example suggests the right scale of the switching penalty. The following elementary lemma makes that precise for a finite image decomposition and will be used as the comparison target for a continuous-sheet argument.

Let `K_1,...,K_M subset R^n` satisfy

```text
sup_(y in K_a)||y||_2 <= S                               (8.1)
```

for every `a`, and write

```text
h_a(g):=sup_(y in K_a)<g,y>,
h(g):=max_(1<=a<=M) h_a(g).                              (8.2)
```

### Theorem 8.1 — Gaussian finite-branch aggregation

If

```text
E h_a(g) <= A                                             (8.3)
```

for every branch, then

```text
boxed:
E h(g)
 <= A + S sqrt(2 log M).                                 (8.4)
```

The same conclusion holds if `(E h_a^2)^(1/2)<=A`.

#### Proof

Each `h_a` is `S`-Lipschitz as a function of the Gaussian coefficient vector. Gaussian concentration gives the centered moment-generating bound

```text
E exp(lambda(h_a-Eh_a))
 <= exp(lambda^2 S^2/2)                                  (8.5)
```

for every `lambda>0`. Therefore

```text
E max_a(h_a-Eh_a)
 <= (log M)/lambda + lambda S^2/2.                       (8.6)
```

Optimizing at

```text
lambda=sqrt(2 log M)/S                                   (8.7)
```

gives

```text
E max_a(h_a-Eh_a)
 <= S sqrt(2 log M).                                     (8.8)
```

Adding `max_a Eh_a<=A` yields (8.4). If `(Eh_a^2)^(1/2)<=A`, Jensen gives `Eh_a<=A`. QED.

### Corollary 8.2 — piecewise regular image class

Suppose the symmetrized tensor image can be decomposed as

```text
F(B_p^d) union -F(B_p^d)
 subset K_1 union ... union K_M                           (8.9)
```

and each branch has a source-normalized Gaussian width bound

```text
E h_a(g)
 <= C_(r,p) d^alpha S L                                  (8.10)
```

for some factor `L`. Then

```text
E h(g)
 <= C_(r,p) d^alpha S L
    + S sqrt(2 log M).                                   (8.11)
```

Thus if

```text
log M <= C d^(2alpha) polylog(d,n)^2                     (8.12)
```

and `L` is polylogarithmic, the conjectured polynomial exponent follows for this class.

This class permits arbitrary tensor ranks and coefficient correlations inside each image piece. The restriction is geometric: the exposed image must admit a controlled global piece decomposition. No novelty priority is claimed for the Gaussian max lemma itself; its role here is to quantify exactly how much switching complexity the support-curvature route is allowed to spend.

---

## 9. What has actually been removed from the obstruction

The previous report left three possible singular mechanisms mixed together:

1. small singular values of `D_TF`;
2. preimage/fiber multiplicity;
3. branch switching between distinct exposed output points.

Theorems 3.1–4.1 remove the first two on every regular image sheet:

- `det(Q)^(-1/2)` disappears after passing to induced image volume;
- the regular-sheet formula is written once per output sheet, so redundant preimages are not counted.

Theorem 5.1 shows that the third mechanism is different. It survives quotienting and has an exact geometric density

```text
output chord length = ||y_1-y_2||_2.                    (9.1)
```

The matrix cube then proves that this switching term can be `Theta(S^2 log d)` even when every smooth sheet has zero curvature.

Therefore the current bottleneck is no longer a vague rank-stratified Kac–Rice determinant estimate. It is a **Gaussian switching-chord problem on the exposed output image**.

---

## 10. Mandatory countertests

### 10.1 Matrix case `r=p=2`

Passed. The diagonal hypercube family gives the necessary `sqrt(log d)` loss and shows that switching curvature must be retained.

### 10.2 Scalar level-set rotation

For scalar output there is no positive-dimensional regular image sheet at a selected value. The intrinsic formula does not pay for rotating parameter tangents. Any nonsmoothness is handled on the one-dimensional output support body, not in the parameter space.

### 10.3 Exponential regular fiber multiplicity

A regular image sheet is counted by its induced output volume, not by the number of parameter preimages. Formula (4.12) explicitly removes the parameter Jacobian singularities that would otherwise duplicate the same sheet.

### 10.4 Flat-sign quartic from the predecessor

Its tiny formal curvature gap was paired with zero visible image differential. The intrinsic image dimension at the selected scalar output is zero, so the false `sqrt(d)` penalty does not appear.

### 10.5 `3^d-1` quartic critical points

Raw critical-point multiplicity is again irrelevant after passing to the output sheet. Distinct critical points mapping to the same local image do not create independent intrinsic curvature mass.

### 10.6 Dense coordinate dust

The current switching density is the actual output chord `||y_1-y_2||`, so two parameter states separated by dense coordinate dust but producing almost identical tensor outputs create a proportionally small switching charge.

These checks do not prove the full conjecture; they show that the new quotient/switching decomposition survives the specific false invariants already found in this campaign.

---

## 11. Old theorem, new theorem, remaining gap

| Item | Before this run | After this run |
|---|---|---|
| Full arbitrary `2<=p<2r` exponent | `1/2-1/(2r)` | unchanged; full conjecture still open |
| Smooth exposed curvature | `Tr(G^-1 Q)` in parameter tangent coordinates | intrinsic `Tr(S^-1)` on output image sheet |
| Rank-`j` Kac–Rice density | appeared to contain `det(Q)^(-1/2)` | differential singular values cancel exactly against induced image volume |
| Fiber multiplicity | expected to be quotiented | removed explicitly on regular sheets by image-level formula |
| Adjugate cancellation | `det(G)Tr(G^-1Q)` | intrinsic `Tr(adj S)` normal-cycle density |
| Switching strata | unresolved remainder | exact chord-length Hessian measure proved |
| Need for logarithms | allowed by source, not calibrated here | explicit `S=1` matrix family requires `sqrt(log d)` |
| Smooth-only Kac–Rice route | plausible partial route | refuted as sufficient even for matrices |
| New restricted class | uniform smooth curvature | finite/piecewise regular image decomposition with quantified switching penalty |
| Next arbitrary bottleneck | rank-stratified Kac–Rice moments | scale-sensitive switching-chord measure on exposed output image |

The headline exponent is intentionally unchanged. The mathematical progress is the exact quotient of the regular Kac–Rice density, the exact switching measure, and a sharp source-normalized matrix obstruction showing where the unavoidable logarithm can live.

---

## 12. Remaining gap and next concrete attack

The full problem is now split geometrically as

```text
I_curv
 = I_regular-image
   + I_switch/rank-change.                               (12.1)
```

On every regular image sheet, Theorem 4.1 gives an intrinsic normal-cycle density with no differential determinant singularity. The next attack should therefore focus on the switching term, not return to whole-tangent covering.

### Target 12.1 — scale-sensitive switching-chord inequality

For `p=2`, at the critical chaining scale

```text
eps_k := C_r S/sqrt(k),                                  (12.2)
```

seek a decomposition of the exposed output image into regular pieces for which

```text
regular-sheet curvature budget
 + switching-chord budget
 <= C_r S^2 polylog(d,n)^2                               (12.3)
```

after summing dyadic scales.

The exact switching contribution between two competing branches is

```text
integral_(h_1=h_2)
 h(g) phi(g)
 ||grad h_1-grad h_2||_2
 dH^(n-1)(g).                                            (12.4)
```

For fixed output points `y,z`, the gap is the one-dimensional Gaussian

```text
<g,y-z>,                                                  (12.5)
```

whose density at zero is proportional to `1/||y-z||`. Thus one factor of the chord in (12.4) cancels automatically in the linear two-point model. The matrix hypercube shows that summing these interfaces costs `Theta(log d)`, not `Theta(d)`.

The concrete next proof attempt is therefore:

1. **Linear-pair calibration.** Write the exact Gaussian interface integral for two fixed outputs `y,z` and identify the self-normalized chord cancellation.
2. **Moving-sheet localization.** On a regular pair of exposed image sheets, freeze each sheet at the switching scale `eps_k` and bound the error in (12.4) by the intrinsic shape-operator budget from Theorem 4.1.
3. **Adjacency rather than all pairs.** Count only interfaces that are actually adjacent in the normal fan at scale `eps_k`; all-pairs counting is forbidden by the hypercube calibration and earlier fiber counterexamples.
4. **Entropy target.** Prove that the number/effective Gaussian perimeter of `eps_k`-distinguishable adjacent output switches is at most `exp(O(k polylog(d,n)))`, or else extract a lower-order contraction/sparse norming certificate.
5. **Mandatory falsification tests.** Recheck the diagonal hypercube matrices, scalar level-set rotation, exponential regular fiber map, flat-sign quartic, `3^d-1` quartic, and dense-dust tensor before accepting any adjacency lemma.

A successful switching-chord estimate of order `S^2 polylog(d,n)^2`, combined with the intrinsic regular-sheet formula, would prove the `p=2` polynomial exponent without ever paying the volumetric parameter-space factor. The extension to `p>2` would then reinsert the natural `d^(2alpha)` support-curvature scale while keeping the image-level quotient unchanged.

If this switching route fails after the required second genuine pivot, preserve this report and hand the bottleneck to another registered probability role rather than returning to admission/audit waiting.

---

## 13. Claim discipline

- **PROVED PARTIAL:** Theorems 3.1, 4.1, 5.1, 6.1, 7.1 and 8.1 are proved under their stated assumptions.
- **PROVED PARTIAL:** The regular-image Kac–Rice density is intrinsic and contains no residual differential singular-value factor after conversion to induced image volume.
- **PROVED PARTIAL:** The explicit diagonal matrix family has exact source normalization `S=1` and expected norm `Theta(sqrt(log d))`; its `Theta(log d)` second-moment excess is entirely singular switching curvature.
- **CONDITIONAL/NEXT TARGET:** The scale-sensitive switching-chord estimate (12.3) is not proved.
- **NOT CLAIMED:** No arbitrary deterministic `2<=p<2r` solution is claimed.
- **NOT CLAIMED:** No literature novelty priority is claimed for generic Kac–Rice, normal-cycle, Gaussian concentration, or distributional max formulas. The campaign contribution is the exact tensor/source-normalized specialization, the quotient identity (4.12), and the resulting obstruction split.
- **PRESERVATION:** This is a new immutable report. It does not overwrite C0035 history, prior P09 reports, or peer-owned material.
