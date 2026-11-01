Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime does not expose authenticated GPT-6/maximum-effort attestation.

# P09 progress-first run — self-normalized normal cones, nearcritical polynomial entropy, and a fiber-multiplicity counterexample

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The fixed source-level arbitrary-tensor polynomial exponent recovered in the unresolved regime remains

```text
gamma = 1/2 - 1/(2r),
```

versus the conjectured

```text
alpha = 1/2 - 1/p.
```

The headline exponent therefore does not change in this run. The mathematical progress is instead a sharper reduction that removes a major overcount from the preceding output-covariance argument, plus a materially different algebraic-geometric covering attack in the hardest `p=2, r>=3` subregime.

The main new facts are:

1. At an actual maximizing point, the output-covariance reduction is **exact after a self-normalizing effective-support factor**. For every `p>=2`, if `x_g` maximizes the Gaussian tensor polynomial, then

   ```text
   ||sum_i g_i T_i||_{I_p}^2
     = eta_p(x_g) g^T C_{x_g} g,
   eta_p(x)=|| |x|^(p-2) x ||_2^(-2),
   1 <= eta_p(x) <= d^(1-2/p).
   ```

   Thus only the covariance selected by its own normal direction matters. At `p=2`, `eta_2=1` identically and the earlier inequality becomes an exact self-consistent covariance identity.

2. This yields a **normal-cone directional covariance-envelope theorem** strictly weaker than the preceding Loewner-envelope hypothesis: one needs to dominate the covariance only in directions for which the point is an optimizer, not in every direction and not at every point.

3. For `p=2`, the tensor evaluation map is a fixed-degree polynomial map whose derivative has bounded Hilbert--Schmidt norm. Applying Yomdin--Comte's quantitative Morse--Sard theorem with the actual singular-value profile gives

   ```text
   N(F(B_2^d), eps)
      <= C_Y(r,d,n) sum_{j=0}^{min(d,n)}
            (R/eps)^j / sqrt(j!).
   ```

   Hence at the critical scale `eps=R/sqrt(k)`, all scale-dependent geometry already costs only `exp(O(k))`; the only uncontrolled loss is the algebraic/tame constant `C_Y(r,d,n)`.

4. A new explicit order-4, three-output tensor map has **at least `2^(d+1)` connected components in a regular fiber while its source normalization is O(1)**. Therefore raw preimage/fiber multiplicity cannot be the invariant used to sharpen `C_Y`: it can be exponentially bad even when the Gaussian tensor norm is trivially O(1).

5. The right algebraic target is consequently a **scale-sensitive image-regularity / exposed-normal version** of quantitative Morse--Sard, combining the singular-value gain above with the image-side regular-set covering framework of Zhang--Kileel (arXiv:2311.05116), rather than paying for preimage topology.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Registered role: `chaining / geometric-probabilistic proof`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Immediate predecessor: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T104700Z__tangent-entropy-counterexample-and-output-covariance-envelope.md`, predecessor blob `e95d134dee7d5295507bfb75cf453737219e48b6`.
- Historical C0035 material, all prior P09 reports, and peer files are preserved. This report is additive and immutable.

---

## 1. Exact source, normalization, and current baseline

Primary problem: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac, A. Rodder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.

For symmetric deterministic order-`r` tensors `T_1,...,T_n in (R^d)^(tensor r)`, iid standard Gaussians `g_i`, and

```text
||T||_{I_p} := sup_{||x||_p<=1} |T[x,...,x]|,
```

the conjecture asks for

```text
E ||sum_i g_i T_i||_{I_p}
 <= C(r,p) polylog(d,n) d^(1/2-1/p)
    (sum_i ||T_i||_{I_p}^2)^(1/2).                 (1.1)
```

A bounded fresh literature check on 20 September 2026 again recovers:

- Bandeira--Gopi--Jiang--Lucca--Rothvoss, arXiv:2411.10633, as the primary general geometric correlated-tensor baseline;
- Ishaq Aden-Ali, arXiv:2503.10580, as the sharper PAC-Bayesian variance-parameter inequality, including the improvement of the first logarithmic term, without removal of the arbitrary-correlated `p<2r` polynomial obstruction;
- Zhang--Kileel, arXiv:2311.05116v4, as a relevant modern primary result on covering polynomial images, substantially improving generic Yomdin--Comte covering bounds but retaining the intrinsic/domain-dimensional cost rather than the scale-dependent effective-rank cost required here;
- no later primary source in this bounded check resolving the exact arbitrary deterministic `2<=p<2r` statement.

This is a bounded search, not a claim about unindexed work.

The fixed source metric remains

```text
old arbitrary exponent = 1/2 - 1/(2r)
new arbitrary exponent = 1/2 - 1/(2r)
target exponent        = 1/2 - 1/p
source status           = OPEN / not solved here.
```

---

## 2. Inherited tensor map and covariance notation

Put

```text
S^2 := sum_i ||T_i||_{I_p}^2,
alpha := 1/2 - 1/p.
```

For `x in B_p^d`, let

```text
F(x) := (T_i[x^r])_(i=1)^n in R^n,
(A_x v)_i := T_i[x^(r-1),v],
C_x := A_x A_x^*.                                      (2.1)
```

Then

```text
F(x)=A_x x.                                             (2.2)
```

By real polarization there is a constant `P_r` depending only on `r` such that

```text
||A_x||_HS <= P_r S                                    (2.3)
```

for every `x in B_p^d`: each row is a linear functional whose Euclidean norm is at most its `l_q` norm (`q=p/(p-1)<=2`), and the mixed evaluation is controlled by `P_r ||T_i||_{I_p}`.

The predecessor used the general inequality

```text
|<g,F(x)>|^2 <= d^(2 alpha) g^T C_x g                  (2.4)
```

and hence replaced the original process by `sup_x g^T C_x g`. The next theorem shows that this replacement loses important self-consistency: at the actual optimizer one has an exact identity with a local, not ambient, dimension factor.

---

## 3. Exact self-normalized covariance identity at a maximizer

For `p>=2`, define the duality vector

```text
J_p(x) := ( |x_j|^(p-2) x_j )_(j=1)^d.                 (3.1)
```

When `||x||_p=1`,

```text
||J_p(x)||_q=1,
q=p/(p-1).                                              (3.2)
```

Define

```text
eta_p(x) := ||J_p(x)||_2^(-2).                          (3.3)
```

### Theorem 3.1 — self-normalized KKT covariance identity

Fix `g in R^n`. If the Gaussian polynomial

```text
P_g(x):=<g,F(x)>=sum_i g_i T_i[x^r]                    (3.4)
```

is not identically zero, choose `x_g in B_p^d` and a sign so that

```text
P_g(x_g)=sup_{||x||_p<=1}|P_g(x)| >0.                  (3.5)
```

Then `||x_g||_p=1` and

```text
A_(x_g)^* g = P_g(x_g) J_p(x_g).                       (3.6)
```

Consequently

```text
g^T C_(x_g) g
 = P_g(x_g)^2 ||J_p(x_g)||_2^2,                        (3.7)
```

and therefore

```text
boxed:
||sum_i g_i T_i||_{I_p}^2
 = eta_p(x_g) g^T C_(x_g) g.                           (3.8)
```

Moreover

```text
1 <= eta_p(x) <= d^(1-2/p)=d^(2 alpha).                (3.9)
```

For `p=2`, `J_2(x)=x` on the Euclidean sphere and hence

```text
boxed:
||sum_i g_i T_i||_{I_2}^2 = g^T C_(x_g) g.             (3.10)
```

#### Proof

Homogeneity forces a nonzero maximizer to lie on `||x||_p=1`. Apply Lagrange multipliers to `P_g` under

```text
Phi(x):=sum_j |x_j|^p=1.
```

The derivatives are

```text
D P_g(x)[v] = r <A_x^* g,v>,
D Phi(x)[v] = p <J_p(x),v>.                             (3.11)
```

Thus for some multiplier `lambda`,

```text
r A_x^* g = lambda p J_p(x).                            (3.12)
```

Pairing with `x` and using Euler homogeneity gives

```text
r P_g(x)=lambda p <J_p(x),x>=lambda p,                 (3.13)
```

because `<J_p(x),x>=||x||_p^p=1`. Hence `lambda p=rP_g(x)` and (3.6) follows.

Now

```text
g^T C_x g = ||A_x^* g||_2^2,
```

so (3.7)--(3.8) are immediate.

Finally, since `q<=2` and `||J_p(x)||_q=1`, norm comparison gives

```text
d^(-alpha) <= ||J_p(x)||_2 <= 1.                       (3.14)
```

Squaring and inverting gives (3.9). QED.

### Effective-support interpretation

For `p>2`, define

```text
m_eff(x):=eta_p(x)^(1/(2 alpha)).                       (3.15)
```

Then `1<=m_eff(x)<=d`. If `x` is exactly flat on `m` coordinates,

```text
x_j=m^(-1/p) on its support,
```

then

```text
eta_p(x)=m^(2 alpha),
m_eff(x)=m.                                               (3.16)
```

Thus the source factor `d^alpha` is paid **only when the actual maximizing vector is effectively dense**. Sparse or concentrated maximizers carry a strictly smaller exact factor. This is sharper than applying `||x||_2<=d^alpha` before maximization.

### Second-order condition

If `v` is tangent to the `l_p` sphere at `x_g`, i.e.

```text
<J_p(x_g),v>=0,
```

then the constrained Hessian is negative semidefinite and gives

```text
(r-1) T(g)[x_g^(r-2),v,v]
 <= (p-1) P_g(x_g)
    sum_j |x_(g,j)|^(p-2) v_j^2,                        (3.17)
```

where `T(g)=sum_i g_iT_i`. For `p=2` this becomes

```text
(r-1) T(g)[x_g^(r-2),v,v] <= P_g(x_g)||v||_2^2.        (3.18)
```

This means the covariance in (3.8) is not selected arbitrarily: it is selected by a normal direction satisfying both first- and second-order tensor criticality.

---

## 4. A strictly weaker covariance-envelope theorem

The predecessor proved a finite low-trace **Loewner** envelope theorem: all `C_x` had to be dominated, as matrices, by a small dictionary. The self-consistent identity shows this is much stronger than necessary.

### Theorem 4.1 — normal-cone directional envelope

Let `H_1,...,H_M` be PSD `n x n` matrices satisfying

```text
Tr H_a <= Lambda d^(2 alpha) (P_r S)^2                (4.1)
```

for every `a`.

Assume that for every `g`, one can choose a maximizing point `x_g` as in Theorem 3.1 such that only the **single selected direction** obeys

```text
eta_p(x_g) g^T C_(x_g) g
 <= max_(1<=a<=M) g^T H_a g.                            (4.2)
```

Then

```text
boxed:
E ||sum_i g_i T_i||_{I_p}
 <= C_r d^alpha S sqrt(Lambda log(2M)).                 (4.3)
```

#### Proof

By Theorem 3.1,

```text
||sum_i g_iT_i||_{I_p}^2
 = eta_p(x_g)g^TC_(x_g)g
 <= max_a g^TH_ag.                                      (4.4)
```

For each fixed PSD `H`, the Gaussian quadratic-form inequality gives

```text
P{g^THg >= Tr H +2 sqrt(Tr(H^2)t)+2||H||_op t}
 <= e^(-t).                                              (4.5)
```

Since `H>=0`, both `sqrt(Tr(H^2))` and `||H||_op` are bounded by `Tr H`. Union bound over `M` and integration yield

```text
E max_a g^T H_a g
 <= C Lambda d^(2 alpha)(P_rS)^2 log(2M).               (4.6)
```

Apply Jensen to the square root. QED.

### Why this is genuinely weaker than the predecessor

No matrix inequality `C_x <= H` is required. No condition is imposed on a covariance direction that never occurs as a maximizing normal. No condition is imposed on a nonmaximizing `x`. A covariance may be arbitrarily large or rotate wildly in directions transverse to its own normal cone and still satisfy (4.2).

The old Loewner-envelope theorem is recovered by using `eta_p<=d^(2alpha)` and a Loewner envelope, but Theorem 4.1 allows substantially more geometry.

At `p=2`, the exact target becomes especially clean: find a polylog-size/entropy dictionary that controls only

```text
g^T C_(x_g) g
```

for self-consistent normal pairs `(g,x_g)`, rather than `sup_x g^T C_x g`.

This is the first main change from the predecessor.

---

## 5. A different method at p=2: quantitative Morse--Sard with the exact singular profile

The covariance line has now been sharpened to the normal cone. In parallel, this section changes method and treats the tensor evaluation map as a fixed-degree polynomial map.

Set `p=2` and `r>=3`. Let

```text
F:B_2^d -> R^n,
F(x)=(T_i[x^r])_i.                                      (5.1)
```

Let `P_r` be the polarization constant above and define the derivative scale

```text
R := r P_r S.                                           (5.2)
```

Since `DF(x)=r A_x`, (2.3) gives

```text
||DF(x)||_HS <= R                                       (5.3)
```

for every `x in B_2^d`.

Write the singular values of `DF(x)` in decreasing order as

```text
s_1(x)>=s_2(x)>=...>=s_q(x),
q=min(d,n).                                              (5.4)
```

The Hilbert--Schmidt bound immediately gives

```text
s_j(x) <= R/sqrt(j)                                     (5.5)
```

for every `j` and every `x`.

Yomdin--Comte, *Tame Geometry with Application in Smooth Analysis*, LNM 1834 (2004), Chapter 7, Theorem 7.5, gives a quantitative Morse--Sard covering bound for the image of the set on which the singular values of a polynomial map are bounded by prescribed thresholds. Applying it with

```text
lambda_j=R/sqrt(j)                                      (5.6)
```

puts **every point of `B_2^d`** into that nearcritical set.

### Theorem 5.1 — factorial nearcritical entropy profile

There is a coefficient-independent constant

```text
C_Y=C_Y(r,d,n)                                           (5.7)
```

coming from the quantitative Morse--Sard theorem such that for every `eps>0`,

```text
boxed:
N(F(B_2^d), eps)
 <= C_Y sum_(j=0)^q (R/eps)^j / sqrt(j!).               (5.8)
```

No structural assumption is imposed on the deterministic tensors.

#### Proof

The coordinate polynomials of `F` all have degree `r`. The singular-value thresholds (5.6) dominate the singular values at every point by (5.5). In Theorem 7.5, the `j`th term contains the product

```text
lambda_1 ... lambda_j
 = R^j / sqrt(j!).                                       (5.9)
```

The domain is the unit Euclidean ball, so the radius factor is one. Substitution gives (5.8). QED.

### Corollary 5.2 — the critical scale already costs only O(k)

At

```text
eps_k := R/sqrt(k),                                     (5.10)
```

one has

```text
boxed:
log N(F(B_2^d),eps_k)
 <= log C_Y + (1/2)log(q+1) + k/2.                      (5.11)
```

Indeed, by Cauchy--Schwarz,

```text
sum_(j=0)^q k^(j/2)/sqrt(j!)
 <= sqrt(q+1) (sum_(j=0)^q k^j/j!)^(1/2)
 <= sqrt(q+1)e^(k/2).                                   (5.12)
```

This is an important localization of the obstruction. The **entire singular-value/volume part of the polynomial image already has the exact effective-rank scaling `exp(O(k))`**. The unresolved factor is `C_Y(r,d,n)`, the algebraic/tame complexity constant.

No novelty is claimed for the Yomdin--Comte theorem itself. The campaign-level advance is the tensor specialization (5.8)--(5.11), which shows exactly where the dimension loss sits after the Hilbert--Schmidt tangent estimate is inserted.

---

## 6. What this would give if the algebraic constant were scale-sensitive

The map `F` is `R`-Lipschitz in Euclidean norm, so the elementary domain cover gives

```text
log N(F(B_2^d),eps)
 <= d log(1+C R/eps).                                   (6.1)
```

Combining (5.11) above the scale `R/sqrt(d)` with (6.1) below it and inserting into Dudley's integral gives the unconditional parameterized bound

```text
E sup_(||x||_2<=1) |<g,F(x)>|
 <= C_r S [ log(2d) + sqrt(log(2C_Y(r,d,n))) ].         (6.2)
```

The proof is just the split

```text
[0,R/sqrt(d)] union [R/sqrt(d), CR].                    (6.3)
```

On the first interval, (6.1) integrates to `O(R sqrt(log(2d)))`. On the second interval, (5.11) in continuous form gives an integrand bounded by

```text
sqrt(log C_Y) + C R/eps + sqrt(log(q+1)),               (6.4)
```

whose integral is

```text
O(R sqrt(log C_Y) + R log(2d)).                         (6.5)
```

Since `R=C_rS`, (6.2) follows.

The standard quantitative Morse--Sard theorem does **not** supply a dimension-benign estimate for `C_Y`; therefore (6.2) is not a new source-level improvement and is not presented as one. What it proves is sharper:

> At `p=2`, after the exact tensor derivative estimate, all scale-dependent entropy is already correct. Any polynomial loss left in this algebraic route is entirely an image-complexity/multiplicity issue.

For comparison, Zhang--Kileel, arXiv:2311.05116v4, proves substantially sharper general covering theorems for polynomial images and regular sets, with logarithmic covering bounds of the form intrinsic-dimension times `log(1/eps)` plus regularity complexity. Applied globally to an arbitrary `d`-variable tensor map, however, the intrinsic/domain dimension is still `d`. The missing hybrid theorem is therefore **scale-sensitive regularity with effective dimension `k` at resolution `R/sqrt(k)`**.

---

## 7. Counterexample before building on raw multiplicity: an O(1)-norm tensor map with 2^(d+1) regular fiber components

A tempting next step would be to try to bound the Yomdin constant by counting connected components of polynomial fibers. That route is false at the required scale.

### Theorem 7.1 — exponential regular fiber multiplicity with fixed output dimension and bounded source normalization

For every `d>=2`, define a homogeneous degree-4 polynomial map on `R^(d+1)` with variables `(t,x_1,...,x_d)` by

```text
H_d(t,x)
 := ( t^4,
      t^2 ||x||_2^2,
      sum_(j=1)^d x_j^4 ) in R^3.                       (7.1)
```

Each coordinate is the diagonal polynomial of a symmetric order-4 tensor. Their exact Euclidean injective norms satisfy

```text
||T_1||_{I_2}=1,
||T_2||_{I_2}=1/4,
||T_3||_{I_2}=1,                                        (7.2)
```

so

```text
S^2=1+1/16+1=33/16,                                     (7.3)
```

independent of `d`.

Nevertheless there are regular values `y in R^3` for which

```text
H_d^(-1)(y) cap B_2^(d+1)                               (7.4)
```

has at least

```text
2^(d+1)                                                 (7.5)
```

connected components.

#### Proof

Choose fixed `t_0>0` and `rho>0` with

```text
t_0^2+rho^2<1.                                          (7.6)
```

Set

```text
y_1=t_0^4,
y_2=t_0^2 rho^2.                                        (7.7)
```

Choose

```text
rho^4/d < y_3 < rho^4/(d-1).                            (7.8)
```

The first two fiber equations force

```text
t=+t_0 or -t_0,
||x||_2=rho.                                             (7.9)
```

The third equation is

```text
sum_j x_j^4=y_3.                                        (7.10)
```

No coordinate `x_j` can vanish on this fiber. If one vanished, Cauchy--Schwarz on the remaining `d-1` coordinates would give

```text
sum_j x_j^4 >= rho^4/(d-1)>y_3,                         (7.11)
```

a contradiction.

Hence every coordinate sign is constant on a connected component. Every one of the `2^d` sign orthants contains a solution of (7.10): in the positive orthant the flat point has quartic sum `rho^4/d<y_3`, while a point sufficiently close to `(rho,0,...,0)` but still strictly positive has quartic sum greater than `y_3`; continuity gives a crossing. Coordinatewise sign symmetry supplies the other orthants. The two choices of sign of `t` cannot connect because `t` never vanishes. Thus there are at least `2^(d+1)` components.

It remains to check regularity. Critical points of

```text
x -> sum_j x_j^4
```

on the sphere `||x||_2=rho` have all nonzero coordinates of equal magnitude. If there are `m` nonzero coordinates, the critical value is

```text
rho^4/m.                                                (7.12)
```

The interval (7.8) contains no such critical value. Therefore the gradients of `||x||_2^2` and `sum_jx_j^4` are linearly independent on (7.10). Together with the nonzero `t` derivative of `t^4`, the three gradients of the coordinates of `H_d` are linearly independent throughout the fiber. Hence `y` is a regular value. QED.

### Why this matters for P09

The Gaussian tensor problem for these three tensors is trivial at the source scale:

```text
E sup_(||z||_2<=1) |<g,H_d(z)>|
 <= E||g||_2 sup_z ||H_d(z)||_2
 <= C S = O(1).                                         (7.13)
```

Thus a fixed three-dimensional output process with bounded source normalization can have exponentially complicated **preimage topology**.

This proves that a sharpened algebraic proof must not pay for raw fiber-component multiplicity. In particular, simply replacing the opaque constant in Yomdin--Comte by a Petrovskii--Oleinik--Milnor--Thom count of preimage components can reintroduce an `exp(c d)` loss even where the probability problem is elementary.

This counterexample was checked before making such a multiplicity lemma the next proof target.

---

## 8. Convex/support geometry removes the same overcount

The Gaussian process depends only on the symmetric convex hull

```text
K := conv( F(B_p^d) union -F(B_p^d) ).                   (8.1)
```

Indeed

```text
||sum_i g_i T_i||_{I_p}=h_K(g).                         (8.2)
```

Thus disconnected or highly multiple fibers carrying the same output geometry are irrelevant.

The self-normalized identity can be restated as a support-normal condition. If `x_g` exposes the support value in direction `g`, then

```text
A_(x_g)^*g = h_K(g) J_p(x_g),                           (8.3)
```

and

```text
h_K(g)^2 = eta_p(x_g) g^T C_(x_g)g.                    (8.4)
```

At `p=2`, the support value is **exactly** the square root of the tangent covariance in its own exposing normal direction.

This shows why both previous overcounts occur:

- whole-tangent entropy counts rotations invisible to the output;
- unrestricted `sup_x g^TC_xg` counts covariances not selected by `g`;
- raw algebraic fiber multiplicity counts many preimages of the same or nearby output support geometry.

All three should be quotiented before entropy is paid.

---

## 9. The new concrete bottleneck: scale-sensitive image regularity, not fiber regularity

The two new routes meet at one precise statement.

For `p=2`, normalize the derivative scale to `R=C_rS`. At critical resolution

```text
eps_k=R/sqrt(k).                                        (9.1)
```

Yomdin--Comte already contributes the factorial singular-value term corresponding to effective rank `k`. Zhang--Kileel shows that once a set is `(K,k)`-regular, its image-side covering entropy is essentially

```text
k log(1/eps) + log K + O(k log ambient_dimension).       (9.2)
```

The desired hybrid lemma is therefore:

### Target 9.1 — scale-sensitive tensor-image regularity

At scale `eps_k`, the part of the tensor image that is distinguishable at that scale should admit a regular decomposition with

```text
effective dimension <= C_r k,
log K_eff(k) <= C_r k polylog(d,n).                      (9.3)
```

Equivalently, a sufficient direct covering form is

```text
log N(F(B_2^d), C_rS/sqrt(k))
 <= C_r k polylog(d,n).                                  (9.4)
```

But (9.3) is the more structural target: it says *why* the cover should exist, and it avoids paying for the exponential regular fibers in Theorem 7.1 because those fibers correspond to one image point.

A support-function version may be weaker still: it is enough to establish (9.3) only for output sheets that can be exposed by a normal satisfying the KKT conditions (3.6), (3.17).

If (9.4) holds at dyadic scales, Dudley gives

```text
E ||sum_i g_i T_i||_{I_2}
 <= C_r S polylog(d,n),                                  (9.5)
```

which is the exact conjectured polynomial exponent at `p=2` for arbitrary deterministic tensors.

For general `p>2`, Theorem 3.1 says the corresponding scale must be stratified by the local effective support `m_eff(x_g)`, with local factor `m_eff(x_g)^alpha` instead of paying `d^alpha` everywhere.

---

## 10. Next attack

The next run should not return to a global tangent cover or a raw fiber count. The concrete attack is:

1. **p=2 first.** Work with exposed/self-consistent pairs `(g,x_g)` satisfying

   ```text
   A_x^*g=P_g(x)x
   ```

   and the second-order inequality (3.18).

2. Use the singular threshold `R/sqrt(k)` to split `DF(x)` into at most `k` active output directions plus a subcritical remainder.

3. Apply Zhang--Kileel's image-side regular-set covering theorem to the active **output image**, not to the preimage critical set. The missing proof obligation is to show that the number of output-intersection components at resolution `eps_k` is `exp(O(k polylog))`; preimage component count is forbidden by Theorem 7.1.

4. Use the normal-cone covariance identity (3.10) to identify output sheets that are not exposed at scale `eps_k` and discard them before counting.

5. Mandatory countertests before accepting any intermediate lemma:
   - the predecessor's constant-level-set rotating-tangent example;
   - the zero-process rotating-column example;
   - the diagonal dense-dust example;
   - Theorem 7.1's three-output quartic map with `2^(d+1)` regular fiber components.

If this scale-sensitive image-regularity route fails twice, preserve the handoff and pivot as directed rather than returning to whole-tangent entropy.

---

## 11. Obligation ledger

| Obligation | Before this run | After this run |
|---|---|---|
| Full arbitrary `2<=p<2r` source exponent | OPEN | OPEN |
| Avoid global `d^alpha` when optimizer is sparse | only crude global factor | exact `eta_p(x_g)` / effective-support identity proved |
| Output covariance reduction | unrestricted `sup_x g^TC_xg` | exact covariance at self-consistent maximizing pair |
| Covariance envelope assumption | Loewner domination for all `x`/directions | directional domination only on normal-cone pairs |
| p=2 critical-scale entropy | no algebraic effective-rank formula | Yomdin specialization gives `log C_Y + O(k)` |
| Algebraic obstruction | vague semialgebraic constant | explicit bounded-norm 3-output map with exponential regular fiber multiplicity |
| Next algebraic target | low-trace covariance envelope | scale-sensitive **image** regularity / exposed-sheet entropy |

The old/new full-source exponent is intentionally unchanged. The progress in this report is the exact optimizer covariance geometry and the isolation/refutation of the wrong algebraic multiplicity invariant, not a relabeling of a known special case.
