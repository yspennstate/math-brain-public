Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime does not expose authenticated GPT-6/maximum-effort attestation.

# P09 progress-first run — Gaussian support curvature, visible soft modes, and Kac–Rice adjugate cancellation

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The full arbitrary-tensor polynomial exponent remains

```text
gamma = 1/2 - 1/(2r)
```

in the unresolved regime `2 <= p < 2r`, versus the conjectured

```text
alpha = 1/2 - 1/p.
```

This run changes method again. The predecessor isolated a scale-sensitive image/exposed-normal entropy problem after proving a self-normalized KKT covariance identity and showing that raw fiber multiplicity can be exponentially bad. Here I stop trying to count sheets and instead differentiate the **support function in the Gaussian normal variable**. This gives an exact Gaussian curvature identity. At a smooth exposed normal, the curvature has an explicit resolvent formula involving the constrained Hessian and the **tangential process covariance**. This automatically kills input/fiber directions that are invisible to the image.

The main new facts are:

1. For the support function

   ```text
   h(g) = ||sum_i g_i T_i||_{I_p}
   ```

   of the symmetrized tensor image, there is an exact distributional Gaussian identity

   ```text
   E h(g)^2
     = E ||grad h(g)||_2^2
       + integral h(g) phi(g) d(Delta h)(g),
   ```

   where `Delta h` is the nonnegative distributional Laplacian measure and `phi` is Gaussian density. Since `||grad h||<=S` almost everywhere, the entire remaining problem is a **Gaussian-weighted support-curvature bound**.

2. At a smooth nondegenerate exposed maximizer `x=x(g)`, define the constrained tangent curvature `G_(g,x)` and tangential covariance `Q_x` below. Then

   ```text
   Hess h(g)
      = r A_x P_T G_(g,x)^(-1) P_T A_x^*,

   Delta h(g)
      = r Tr(G_(g,x)^(-1) Q_x).
   ```

   This is an exact formula, not a covering inequality.

3. The covariance entering that formula is exactly the image-visible differential energy:

   ```text
   Q_x
     = P_T A_x^* A_x P_T
     = (1/r^2) (D_T F(x))^* D_T F(x).
   ```

   In particular, tangent/fiber rotation on which the tensor image does not move has zero weight. This directly avoids the earlier tangent-entropy and fiber-multiplicity counterexamples.

4. If `G/h` has eigenvalues `delta_j>0` and `q_j=<v_j,Q_x v_j>`, then

   ```text
   h Tr(G^(-1)Q_x) = sum_j q_j/delta_j,
   sum_j q_j <= P_r^2 S^2.
   ```

   Hence the only local obstruction is now precise: **small normalized curvature gaps carrying nontrivial image-derivative energy**. Small curvature in a direction with `q_j=0` costs nothing.

5. For a globally smooth exposed support with the scale-correct curvature lower bound

   ```text
   G_(g,x) >= kappa d^(-2 alpha) h(g) I_T,
   ```

   I prove the conjectured polynomial exponent outright:

   ```text
   E h(g)
      <= d^alpha S sqrt(1 + r P_r^2/kappa).
   ```

   This is a genuine broader deterministic tensor class: the maximizing point, singular vectors, and output covariance may rotate continuously with `g`; no common frame, block support, independent entries, rank-one assumption, or finite covariance dictionary is required. The assumption is a uniform exposed-curvature condition, so this is a **restricted theorem**, not Conjecture 16.

6. A tempting stronger shortcut — controlling only the minimum curvature gap — is false as a useful invariant. For

   ```text
   U(x)=(sum_j x_j^2)^2-sum_j x_j^4,
   ```

   every flat sign vector is a maximizer and the normalized constrained gap is `2/(d-1)`, which would suggest a spurious `sqrt(d)` loss. Yet the actual Gaussian norm is one-dimensional and `O(1)`. The new formula sees the correct answer because `Q_x=0` on the tangent space.

7. At `p=2`, the tangential critical map has derivative exactly `-G`. Therefore a Kac–Rice/coarea Jacobian contributes `det G`, and the dangerous inverse-curvature term cancels algebraically:

   ```text
   det(G) Tr(G^(-1)Q)
      = Tr(adj(G) Q).
   ```

   This is the next route to the arbitrary case: integrate exposed critical points with their Jacobian rather than count them. An additional explicit quartic example has `3^d-1` spherical critical points while its Gaussian norm is `O(1)`, proving that raw critical-point/Bezout counts are the wrong invariant.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Registered role: `chaining / geometric-probabilistic proof`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Pre-write master observed: `2238107c2708233ef67f54ea9aa6034540f51157`
- Immediate predecessor: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T115000Z__self_normalized_normal_cones_and_nearcritical_polynomial_entropy.md`, creation commit `a30bf3aa874b3ab08c28c5c30851452fe51eff0d`.
- Historical C0035 material, all prior P09 reports, and peer files are preserved. This report is additive and immutable.

---

## 1. Exact source, normalization, and bounded current baseline

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

The source itself records the BGJLR geometric result as reaching the desired polynomial dependence for `p>=2r` and identifies the volumetric obstruction for `p<2r`. A bounded fresh primary check on 20 September 2026 again recovered:

- Bandeira–Gopi–Jiang–Lucca–Rothvoss, arXiv:2411.10633, as the general geometric correlated-tensor baseline;
- Ishaq Aden-Ali, arXiv:2503.10580, as a sharper PAC-Bayesian variance-parameter bound which improves the general estimate but does not remove the arbitrary-correlated `p<2r` polynomial obstruction;
- no later primary source in this bounded check resolving the exact arbitrary deterministic `2<=p<2r` statement.

This is a bounded literature check, not a claim about unpublished or unindexed work.

The fixed source metric remains

```text
old arbitrary exponent = 1/2 - 1/(2r)
new arbitrary exponent = 1/2 - 1/(2r)
target exponent        = 1/2 - 1/p
source status           = OPEN / not solved here.
```

---

## 2. Tensor map, support body, and inherited KKT identity

Set

```text
S^2 := sum_i ||T_i||_(I_p)^2,
alpha := 1/2 - 1/p.
```

For `x in B_p^d`, define

```text
F(x) := (T_i[x^r])_(i=1)^n in R^n,                       (2.1)
(A_x v)_i := T_i[x^(r-1),v].                             (2.2)
```

Then

```text
F(x)=A_x x.                                               (2.3)
```

Let `P_r` denote a fixed real-polarization constant depending only on `r`. Since `p>=2`, every Euclidean unit vector has `l_p` norm at most one, and polarization gives

```text
||A_x||_HS <= P_r S                                      (2.4)
```

for every `x in B_p^d`.

Also

```text
||F(x)||_2 <= S.                                         (2.5)
```

Define the symmetrized image body

```text
K := conv( F(B_p^d) union -F(B_p^d) ) subset R^n.        (2.6)
```

Its support function is exactly the random tensor norm as a function of the Gaussian coefficient vector:

```text
h(g)
 := sup_(y in K) <g,y>
  = sup_(||x||_p<=1) |<g,F(x)>|
  = ||sum_i g_iT_i||_(I_p).                              (2.7)
```

Consequences used below:

```text
h is convex and positively 1-homogeneous,                (2.8)
|h(g)-h(g')| <= S ||g-g'||_2.                            (2.9)
```

Thus `h` is differentiable almost everywhere and `||grad h||_2<=S` wherever differentiable.

The predecessor proved the exact KKT identity. If `h(g)>0` and, after choosing the maximizing sign, `x=x_g` is a maximizer with

```text
h(g)=<g,F(x)>,                                            (2.10)
```

then, for

```text
J_p(x)=(|x_j|^(p-2)x_j)_j,                               (2.11)
```

one has

```text
A_x^* g = h(g) J_p(x).                                   (2.12)
```

This report differentiates (2.12) rather than replacing the process by a global covariance supremum.

---

## 3. New exact global identity: Gaussian support curvature

The support function `h` need not be smooth. Convexity nevertheless gives a canonical distributional Hessian and Laplacian.

Let `Delta h` denote the distributional Laplacian of `h`. Because `h` is convex, `Delta h` is a nonnegative locally finite Radon measure. Let

```text
phi_n(g)=(2 pi)^(-n/2) exp(-||g||_2^2/2)                (3.1)
```

be Gaussian density.

### Theorem 3.1 — Gaussian support-curvature identity

For the tensor support function (2.7),

```text
boxed:
E h(g)^2
 = E ||grad h(g)||_2^2
   + integral_(R^n) h(g) phi_n(g) d(Delta h)(g).          (3.2)
```

In particular,

```text
E h(g)^2
 <= S^2
    + integral h(g) phi_n(g) d(Delta h)(g).              (3.3)
```

Therefore Conjecture 16 would follow from

```text
integral h phi_n d(Delta h)
 <= C_(r,p) d^(2alpha) S^2 polylog(d,n)^2.               (3.4)
```

The measure in (3.4), not raw tangent entropy or raw fiber count, is the exact geometric quantity left after the elementary gradient energy is removed.

#### Proof

First assume `h` is smooth away from the origin. Put

```text
f(g)=h(g)^2/2.                                            (3.5)
```

Euler homogeneity gives

```text
g . grad h(g)=h(g),                                      (3.6)
```

hence

```text
g . grad f(g)=h(g)^2.                                    (3.7)
```

Gaussian integration by parts gives

```text
E[g . grad f(g)] = E[Delta f(g)].                        (3.8)
```

By the chain rule,

```text
Delta f = ||grad h||_2^2 + h Delta h.                    (3.9)
```

Combining (3.7)–(3.9) proves (3.2) in the smooth case.

For a general support function, mollify `h` on annuli, or equivalently use the standard distributional Hessian measure of a convex function together with a cutoff at radius `R` and then let `R->infinity`. The Lipschitz bound `h(g)<=S||g||_2` supplies Gaussian integrability. The convex chain rule gives, as measures,

```text
Delta(h^2/2)
 = ||grad h||_2^2 dg + h Delta h.                        (3.10)
```

The same Gaussian integration by parts then yields (3.2). Finally use `||grad h||<=S` almost everywhere to obtain (3.3). QED.

### Interpretation

`Delta h` has two conceptually different pieces:

1. an absolutely continuous curvature density on smooth exposed-normal regions;
2. a singular curvature measure on switching/degenerate strata where the exposed image point changes nonsmoothly.

The next sections identify the smooth density exactly. Thus the full arbitrary problem separates into a **visible soft-curvature problem** plus a **switching-stratum problem**.

---

## 4. Exact Hessian at a smooth exposed maximizer

Fix `g` at which the maximizing sign and maximizing point `x=x(g)` are locally unique and `C^1`, with `||x||_p=1` and `h(g)>0`. Work after absorbing the maximizing sign into `g` locally, so (2.10)–(2.12) hold.

Define the Euclidean tangent space to the `l_p` sphere

```text
T_x := {v in R^d : <J_p(x),v>=0},                       (4.1)
```

and let `P_x` be Euclidean orthogonal projection onto `T_x`.

Define

```text
D_x := diag(|x_j|^(p-2)).                                (4.2)
```

For the Gaussian-combined tensor

```text
T(g):=sum_i g_i T_i,                                     (4.3)
```

define the symmetric second-contraction operator `B_(g,x)` by

```text
<u,B_(g,x)v>
 := T(g)[x^(r-2),u,v].                                   (4.4)
```

Finally define the constrained tangent curvature

```text
G_(g,x)
 := P_x [ (p-1)h(g) D_x - (r-1)B_(g,x) ] P_x |_T_x.     (4.5)
```

At a nondegenerate strict constrained maximum, `G_(g,x)` is positive definite. Indeed, the constrained Hessian of `T(g)[x^r]` is `-r G_(g,x)` on `T_x`.

Define the tangential process covariance

```text
Q_x := P_x A_x^* A_x P_x |_T_x.                         (4.6)
```

### Theorem 4.1 — exposed-sheet Hessian resolvent formula

At every smooth nondegenerate exposed maximizer as above,

```text
boxed:
Hess h(g)
 = r A_x P_x G_(g,x)^(-1) P_x A_x^*.                    (4.7)
```

Consequently,

```text
boxed:
Delta h(g)
 = r Tr(G_(g,x)^(-1) Q_x).                              (4.8)
```

#### Proof

Differentiate the KKT equation (2.12) in an arbitrary coefficient direction `z in R^n`. Write `dot x` and `dot h` for the derivatives of `x(g)` and `h(g)` in direction `z`.

The derivative of the left side is

```text
A_x^* z + (r-1) B_(g,x) dot x.                           (4.9)
```

The derivative of the right side is

```text
dot h J_p(x) + h(g)(p-1)D_x dot x.                      (4.10)
```

Because `x(g)` remains on the `l_p` sphere,

```text
dot x in T_x.                                            (4.11)
```

Project (4.9)=(4.10) onto `T_x`. The `dot h J_p(x)` term disappears, giving

```text
G_(g,x) dot x = P_x A_x^* z.                             (4.12)
```

Hence

```text
dot x = G_(g,x)^(-1) P_x A_x^* z.                       (4.13)
```

The envelope theorem and `DF(x)=rA_x` give

```text
grad h(g)=F(x(g)),                                       (4.14)
D(grad h)[z]=r A_x dot x.                                (4.15)
```

Insert (4.13) into (4.15) to obtain (4.7). Taking the trace and cycling the finite-dimensional trace gives (4.8). QED.

### Sign check

The same formula holds on a branch where the maximizing tensor value originally has negative sign: absorb that sign simultaneously into `g` in the KKT equation. The two signs cancel in the second derivative, so (4.7) remains positive semidefinite, as required for a support function.

---

## 5. The covariance is exactly the image-visible differential energy

The earlier campaign encountered two recurring overcounts:

- tangent operators can rotate while `F(x)` is constant;
- a fiber may contain exponentially many components even when the output set is simple.

The covariance in (4.8) automatically quotients both effects.

### Proposition 5.1 — tangential covariance equals the differential Gram operator

Let `D_TF(x)` denote the derivative of `F` restricted to the tangent space `T_x`. Then

```text
D_TF(x)=r A_x P_x,                                       (5.1)
```

and therefore

```text
boxed:
Q_x
 = (1/r^2) (D_TF(x))^* D_TF(x).                         (5.2)
```

In particular,

```text
rank Q_x = rank D_TF(x),                                 (5.3)
Tr Q_x = (1/r^2)||D_TF(x)||_HS^2 <= P_r^2 S^2.          (5.4)
```

Moreover the selected Gaussian normal is killed tangentially:

```text
P_x A_x^* g=0,                                           (5.5)
```

which is just the projected KKT equation.

#### Proof

`DF(x)=rA_x` by homogeneity of each degree-`r` coordinate polynomial, so restriction to `T_x` gives (5.1). Taking the Gram matrix proves (5.2)–(5.3). Equation (5.4) follows from `||A_x||_HS<=P_rS`, and (5.5) follows from `A_x^*g=hJ_p(x)` because `J_p(x)` is normal to `T_x`. QED.

### `p=2` specialization

When `p=2`, `J_2(x)=x` and `P_x=I-xx^*`. Since `A_xx=F(x)`,

```text
A_x P_x A_x^*
 = A_xA_x^* - F(x)F(x)^*.                               (5.6)
```

Thus the output-side tangential covariance removes exactly the radial process direction. At a selected normal `g`, it annihilates `g`.

This is strictly more selective than the predecessor's unrestricted covariance `C_x=A_xA_x^*`.

---

## 6. Visible soft modes are the precise local obstruction

At a smooth nondegenerate exposed point let

```text
K_(g,x):=G_(g,x)/h(g).                                   (6.1)
```

Choose an orthonormal eigenbasis `v_1,...,v_m` of `K_(g,x)` on `T_x`, where `m=d-1`, with

```text
K_(g,x)v_j = delta_j v_j,
delta_j>0.                                                (6.2)
```

Define the image visibility weights

```text
q_j:=<v_j,Q_x v_j> >=0.                                  (6.3)
```

Then

```text
sum_j q_j = Tr Q_x <= P_r^2 S^2.                        (6.4)
```

### Theorem 6.1 — exact visible-soft-mode formula

At a smooth exposed point,

```text
boxed:
h(g) Tr(G_(g,x)^(-1)Q_x)
 = sum_j q_j/delta_j.                                    (6.5)
```

Consequently, for every threshold `rho>0`,

```text
sum_(delta_j>=rho) q_j/delta_j
 <= P_r^2 S^2/rho.                                       (6.6)
```

Equivalently, the ridge-regularized quantity obeys

```text
boxed:
h(g) Tr((G_(g,x)+rho h(g)I)^(-1)Q_x)
 <= P_r^2 S^2/rho.                                       (6.7)
```

#### Proof

Since `G=hK`,

```text
h Tr(G^(-1)Q)=Tr(K^(-1)Q).
```

Taking the trace in the eigenbasis of `K` gives (6.5). Equations (6.6) and (6.7) follow from (6.4). QED.

### Uniform upper edge

There is no corresponding large-eigenvalue obstruction. Since the single combined tensor `T(g)` has

```text
||T(g)||_(I_p)=h(g),                                     (6.8)
```

polarization gives

```text
||B_(g,x)||_op <= P_r h(g).                              (6.9)
```

Also `0<=D_x<=I` coordinatewise. Therefore every eigenvalue of `K=G/h` at a maximum is at most

```text
C_(r,p):=(p-1)+(r-1)P_r.                                (6.10)
```

Thus only the **lower** edge `delta_j downarrow 0` can make (6.5) large.

### Dyadic obligation

For `ell>=0`, define the visible soft energy

```text
E_ell(g)
 := sum_(2^(-ell-1)<delta_j<=2^(-ell)) q_j.             (6.11)
```

up to a fixed `O_(r,p)(1)` shift covering the upper edge. Then

```text
sum_j q_j/delta_j
 <= C_(r,p) P_r^2S^2
    + 2 sum_(ell>=0) 2^ell E_ell(g).                    (6.12)
```

A sufficient scale-by-scale target is therefore

```text
E E_ell(g)
 <= C_(r,p) d^(2alpha) S^2 2^(-ell) w_ell              (6.13)
```

with

```text
sum_ell w_ell <= polylog(d,n)^2.                        (6.14)
```

This is substantially sharper than controlling the minimum eigenvalue of `G`: a very soft direction is harmless if the tensor image barely moves in that direction.

---

## 7. A genuinely broader restricted class achieving the source exponent

The visible-soft formula immediately proves the conjectured polynomial exponent for a class that allows continuously rotating tangent and output frames.

### Theorem 7.1 — uniformly curved exposed-image class

Assume the tensor support function `h` is `C^2` on `R^n\{0}` and for every `g!=0` its exposed maximizing point can be chosen smoothly and nondegenerately so that

```text
G_(g,x(g))
 >= kappa d^(-2alpha) h(g) I_(T_x)                      (7.1)
```

for some `kappa>0` independent of `d,n`.

Then

```text
boxed:
E ||sum_i g_iT_i||_(I_p)
 <= d^alpha S sqrt(1 + r P_r^2/kappa).                  (7.2)
```

In particular the exact conjectured **polynomial** dimension exponent holds, with no logarithmic loss, on this class.

#### Proof

Condition (7.1) gives

```text
G^(-1)
 <= kappa^(-1) d^(2alpha) h(g)^(-1) I_T.                (7.3)
```

Hence, by (5.4),

```text
h(g) Tr(G^(-1)Q_x)
 <= kappa^(-1)d^(2alpha) TrQ_x
 <= kappa^(-1)d^(2alpha)P_r^2S^2.                       (7.4)
```

Because `h` is globally smooth away from zero, Theorem 3.1 has no singular switching contribution. Combine (3.2), (4.8), `||grad h||<=S`, and (7.4):

```text
E h^2
 <= S^2 + r kappa^(-1)d^(2alpha)P_r^2S^2.              (7.5)
```

Since `d^(2alpha)>=1`,

```text
E h
 <= (E h^2)^(1/2)
 <= d^alpha S sqrt(1+rP_r^2/kappa).                     (7.6)
```

QED.

### Scope

The theorem requires neither:

- common eigenvectors of `A_xA_x^*`;
- a finite frame dictionary;
- block/direct-sum support;
- rank-one summands;
- entry independence;
- a small tangent-operator cover.

The maximizer and all singular directions may rotate continuously with `g`. The assumption is instead geometric: the exposed image has enough curvature precisely in directions where the parameter can move. This makes Theorem 7.1 a genuine broader deterministic covariance/geometry class, but it remains a restricted theorem.

For `p=2`, the hypothesis is simply

```text
G_(g,x) >= kappa h(g) I_T,                               (7.7)
```

with no dimension factor.

---

## 8. Counterexample before using a gap-only theorem

A minimum-curvature-gap bound by itself would still overcount geometry invisible to the tensor image.

### Theorem 8.1 — exponentially many flat-sign maximizers with gap `Theta(1/d)` but zero visible curvature cost

Let `p=2`, `r=4`, `n=1`, and consider the scalar quartic

```text
U(x)
 := (sum_(j=1)^d x_j^2)^2 - sum_(j=1)^d x_j^4.          (8.1)
```

On the Euclidean unit sphere,

```text
U(x)=1-sum_j x_j^4,                                     (8.2)
```

so its maximum is

```text
h_0=1-1/d,                                               (8.3)
```

attained at every flat sign vector

```text
x_j in {+d^(-1/2),-d^(-1/2)}.                           (8.4)
```

Thus there are `2^d` maximizing parameter points.

At every such point, the constrained Hessian of `U` on `x^perp` is

```text
-8/d I_(x^perp).                                         (8.5)
```

Since `r=4` and the constrained Hessian is `-rG`,

```text
G = 2/d I_(x^perp).                                      (8.6)
```

Therefore the normalized curvature gap is

```text
delta_min(G/h_0)=2/(d-1).                               (8.7)
```

A theorem based only on `delta_min` would pay a factor of order `sqrt(d)`.

However `n=1`, and at a critical point the tangent KKT equation gives

```text
P_x A_x^*=0.                                             (8.8)
```

Hence

```text
Q_x=P_xA_x^*A_xP_x=0.                                   (8.9)
```

The exact visible-curvature cost is therefore

```text
h_0 Tr(G^(-1)Q_x)=0.                                    (8.10)
```

The actual Gaussian tensor norm is just

```text
|g| h_0,
```

whose expectation is `h_0 sqrt(2/pi)=O(1)`.

This example does **not** contradict Theorem 7.1; it shows that the uniform-gap hypothesis is sufficient but far from necessary. More importantly, it validates (6.5): soft curvature is dangerous only when it is visible through `Q_x`.

### Relation to earlier counterexamples

This same mechanism explains why the earlier scalar level-set-rotation example did not threaten the original conjecture. For scalar output, every tangential differential direction at a selected normal is killed by KKT, so the image-visible `Q_x` removes the spurious rotation exactly.

---

## 9. Raw critical-point counts are also the wrong invariant

The predecessor showed that a regular fiber can have exponentially many components at bounded source norm. The same pathology occurs for critical points themselves.

### Theorem 9.1 — `3^d-1` spherical critical points with `O(1)` Gaussian norm

Let `p=2`, `r=4`, `n=1`, and

```text
V(x):=sum_(j=1)^d x_j^4.                                (9.1)
```

Then

```text
||V||_(I_2)=1.                                           (9.2)
```

The critical points of `V` on `S^(d-1)` are exactly the vectors obtained by choosing a nonempty support `A subset {1,...,d}` and setting

```text
x_j = +/- |A|^(-1/2) for j in A,
x_j = 0              for j notin A.                     (9.3)
```

Hence the number of spherical critical points is

```text
sum_(m=1)^d binom(d,m) 2^m
 = 3^d-1.                                                (9.4)
```

Nevertheless, for scalar Gaussian `g`,

```text
||gV||_(I_2)=|g|,
E||gV||_(I_2)=sqrt(2/pi).                                (9.5)
```

#### Proof

The Lagrange equation for `V` on the sphere is

```text
4x_j^3 = 2lambda x_j.                                    (9.6)
```

Thus every nonzero coordinate has the same squared magnitude. The unit-sphere constraint forces that magnitude to be `|A|^(-1/2)` on a support `A`, with arbitrary signs. This gives (9.3) and the count (9.4). The norm statement is immediate from `sum x_j^4<= (sum x_j^2)^2=1`, with equality at a coordinate vector. QED.

### Consequence

Neither

- Bezout-style counts of all critical points,
- counts of maximizing parameter points,
- nor raw fiber multiplicity

can be the missing image-complexity invariant. A successful argument must retain **Jacobian/curvature weights** and quotient null image directions.

---

## 10. New p=2 bridge: the critical-map Jacobian is exactly the curvature operator

The previous two sections point directly toward Kac–Rice/coarea rather than counting.

Set `p=2`. On the sphere define

```text
P_x:=I-xx^*,                                             (10.1)
```

and for fixed `g` define the tangent critical field

```text
Psi_g(x):=P_x A_x^*g in T_x.                             (10.2)
```

The spherical critical points of `T(g)[x^r]` satisfy `Psi_g(x)=0`.

At such a critical point with value

```text
h_x:=T(g)[x^r],                                          (10.3)
```

and after choosing a local sign so `h_x>0`, define

```text
G_x:=P_x[h_x I-(r-1)B_(g,x)]P_x |_T_x.                  (10.4)
```

### Theorem 10.1 — exact critical-map Jacobian

At every spherical critical point and every `v in T_x`,

```text
boxed:
D_x Psi_g[v] = -G_x v.                                  (10.5)
```

Thus at a nondegenerate local maximum,

```text
|det D_T Psi_g(x)| = det G_x.                           (10.6)
```

#### Proof

Differentiate

```text
Psi_g(x)=P_xA_x^*g.                                     (10.7)
```

For tangent `v`,

```text
D P_x[v]=-(v x^* + x v^*).                              (10.8)
```

At a critical point, KKT gives

```text
A_x^*g=h_x x.                                            (10.9)
```

Therefore

```text
(DP_x[v])A_x^*g = -h_x v.                               (10.10)
```

The derivative of `A_x^*g` in direction `v` is

```text
(r-1)B_(g,x)v.                                          (10.11)
```

Projecting onto `T_x` gives

```text
D_xPsi_g[v]
 = -h_xv+(r-1)P_xB_(g,x)v
 = -G_xv.                                               (10.12)
```

QED.

---

## 11. Adjugate cancellation: Kac–Rice removes the inverse soft gap

At a smooth exposed normal, the support curvature contains

```text
Tr(G^(-1)Q).                                             (11.1)
```

At a nondegenerate critical point, Kac–Rice/coarea weights the point by the absolute Jacobian determinant `|det D_TPsi|`. At a local maximum this is `det G` by Theorem 10.1.

### Theorem 11.1 — inverse-curvature cancellation

For every positive definite tangent curvature matrix `G` and PSD tangential covariance `Q`,

```text
boxed:
det(G) Tr(G^(-1)Q)
 = Tr(adj(G)Q).                                          (11.2)
```

The right side is polynomial in the entries of `G`; it contains no inverse curvature singularity.

#### Proof

For invertible `G`,

```text
adj(G)=det(G)G^(-1).                                     (11.3)
```

Multiply by `Q`, take the trace, and obtain (11.2). QED.

### Why this matters

Suppose one bounds the selected global maximum by summing a nonnegative curvature functional over all local maxima and then applies Kac–Rice. The local factor has the schematic form

```text
Tr(G^(-1)Q) * det(G).                                    (11.4)
```

The dangerous reciprocal soft eigenvalue cancels against the critical-point Jacobian. In an eigenbasis of `G`,

```text
Tr(adj(G)Q)
 = sum_j q_j prod_(l!=j) lambda_l(G).                   (11.5)
```

A single soft eigenvalue does not create a divergence; it removes a factor from exactly one cofactor term and suppresses all the others.

This is the first mechanism in the campaign that directly couples the **same curvature degeneracy** appearing in the support Hessian to the Jacobian weight naturally present when critical points are integrated rather than counted.

---

## 12. Rank/effective-dimension compatibility with the predecessor

The Kac–Rice field at a fixed point has covariance

```text
Cov_g(P_xA_x^*g)=Q_x.                                   (12.1)
```

By Proposition 5.1,

```text
rank Q_x=rank D_TF(x).                                  (12.2)
```

Thus the rank that controls whether the tangent critical field is nondegenerate is exactly the differential rank that entered the predecessor's Yomdin/nearcritical polynomial-image argument.

This gives a coherent rank-stratified picture:

- on a rank-`j` image stratum, only `j` tangent directions are visible to the output;
- null tangent/fiber directions have `q=0` and should never be charged in (6.5);
- a Kac–Rice formula should be applied only on the visible rank-`j` bundle, not in all `d-1` tangent directions;
- the predecessor's factorial singular-value term `1/sqrt(j!)` is therefore compatible with the covariance rank appearing here.

This explains why both the `3^d-1` critical-point example and the earlier exponential-fiber example can coexist with a tiny image: their huge multiplicity largely lives in directions that should be quotiented before the Jacobian is paid.

---

## 13. A conditional rank-stratified Kac–Rice reduction

The following is the exact next proof target. I record it as **CONDITIONAL**, because completing the stratified coarea/Kac–Rice regularization across rank changes and branch-switch strata is still missing.

For `p=2`, let

```text
Psi_x(g)=P_xA_x^*g.                                     (13.1)
```

On a regular stratum where `rank Q_x=j`, restrict `Psi_x` to the `j`-dimensional visible tangent bundle. Standard Kac–Rice, when its nondegeneracy hypotheses hold on that stratum, converts a sum over exposed critical points into an integral containing

```text
p_(Psi_x)(0)
 * E[ det(G_vis)
      Phi(g,x,G,Q)
      1_(local maximum)
      | Psi_x=0 ].                                       (13.2)
```

For the support-curvature functional

```text
Phi= h_x Tr(G_vis^(-1)Q_vis),                            (13.3)
```

Theorem 11.1 converts the inverse-curvature factor to

```text
h_x Tr(adj(G_vis)Q_vis).                                (13.4)
```

The remaining tasks are therefore **polynomial moment/density estimates**, not inverse Hessian estimates.

A sufficient full `p=2` target is to prove, after summing regular rank strata and controlling the singular image stratum, that

```text
integral h phi_n d(Delta h)
 <= C_r S^2 polylog(d,n)^2.                             (13.5)
```

By Theorem 3.1 this would give

```text
E||sum_i g_iT_i||_(I_2)
 <= C_r S polylog(d,n),                                 (13.6)
```

which is the source exponent at `p=2`.

No claim is made here that (13.5) has been proved.

---

## 14. Why the new target survives the campaign's mandatory countertests

### 14.1 Scalar level-set rotation

The earlier scalar tensor had exponential tangent-operator entropy on a level set where `F` was constant. Here `D_TF=0` along the invisible directions, hence `Q=0`; the support-curvature formula does not pay for the rotation.

### 14.2 Exponential regular fiber multiplicity

The predecessor's bounded-norm three-output degree-4 map had exponentially many components in one regular fiber. Fiber-null directions have zero `D_TF`, hence zero `Q`; raw preimage multiplicity is absent from the local visible-curvature integrand.

### 14.3 Flat-sign quartic `U`

The normalized curvature gap is only `Theta(1/d)`, but `Q=0` at every scalar maximizing point. Thus a gap-only route fails and the new weighted route gives zero local cost.

### 14.4 `3^d-1` critical points for `V=sum x_j^4`

A raw critical-point count is exponential. Kac–Rice/coarea instead weights points by the Jacobian; Theorem 11.1 shows this same determinant cancels the inverse curvature entering the support Hessian.

### 14.5 Matrix case `r=2`

The formulas reduce to ordinary support curvature of a matrix-norm image. No ambient tensor Frobenius factor `d^(1/(2r))` is introduced; `TrQ<=P_r^2S^2` remains source-normalized.

### 14.6 Dense-dust witness

The earlier dense-dust obstruction came from charging high-order posterior covariance in coordinates making negligible process contribution. Here a parameter direction contributes only through the actual image differential Gram operator `Q=(D_TF)^*D_TF/r^2`; a tangent direction with tiny image derivative has proportionally tiny weight.

These checks do not prove the full theorem, but they remove the specific false intermediate lemmas that broke earlier routes.

---

## 15. Old theorem, new theorem, remaining gap

| Item | Before this run | After this run |
|---|---|---|
| Full arbitrary `2<=p<2r` exponent | `1/2-1/(2r)` | unchanged; full conjecture still open |
| Optimizer covariance geometry | exact KKT/self-normalized covariance | retained |
| p=2 image entropy | nearcritical Yomdin profile plus uncontrolled tame constant | retained |
| Global geometric target | scale-sensitive image/exposed-sheet entropy | exact Gaussian support-curvature measure |
| Smooth exposed local density | not identified | `r Tr(G^-1Q)` exactly |
| Invisible tangent/fiber directions | removed heuristically by output covariance | killed exactly by `Q=(D_TF)^*D_TF/r^2` |
| Curvature obstruction | not isolated | only **visible soft modes** `q_j/delta_j` |
| New unconditional restricted class | covariance/image-envelope classes | uniformly curved smooth exposed-image class, target exponent |
| Raw gap strategy | not yet countertested | refuted as necessary/useful invariant by flat-sign quartic |
| Raw critical-point count | open possibility after Morse–Sard route | refuted by `3^d-1` quartic critical points |
| Next arbitrary-case mechanism | image regularity | rank-stratified Kac–Rice/coarea with adjugate cancellation |

The headline exponent is intentionally unchanged. The progress is the exact curvature formula, a new target-exponent class, two counterexamples eliminating bad invariants, and an algebraic cancellation that removes the inverse-Hessian singularity from the next integration method.

---

## 16. Remaining gap and next concrete attack

The full problem is now concentrated on controlling the Gaussian-weighted curvature measure

```text
integral h phi_n d(Delta h).                             (16.1)
```

For `p=2`, the next attack is:

1. **Regular rank-`j` Kac–Rice.** Work on strata where `rank D_TF=j`. Write the Gaussian density of the visible critical field `Psi_x=P_xA_x^*g` at zero in the intrinsic `j`-dimensional covariance metric.

2. **Use adjugate cancellation before any norm bound.** Never estimate `G^-1` separately. Multiply by the Kac–Rice Jacobian first and replace

   ```text
   det(G)Tr(G^-1Q)
   ```

   by

   ```text
   Tr(adj(G)Q).
   ```

3. **Exploit source normalization of the remaining polynomial moments.** `G` is linear in the Gaussian tensor `T(g)` and `Q` is deterministic at fixed `x`; use polarization plus the rank-`j` covariance normalization rather than ambient coefficient Frobenius norms.

4. **Handle degenerate/switching strata on the image side.** Use the predecessor's nearcritical polynomial-image estimate or a Zhang–Kileel-style regular image cover only for the discriminant contribution. Do not count preimages or all critical points.

5. **Mandatory falsification tests before accepting any bound:** the scalar level-set rotation tensor, the exponential-fiber degree-4 map, the flat-sign quartic `U`, the `3^d-1` critical-point quartic `V`, the diagonal dense-dust family, and `r=p=2` matrices.

A successful execution of steps 1–4 with total curvature budget `O_r(S^2 polylog(d,n)^2)` would settle the `p=2` polynomial exponent. For `p>2`, the same geometry has the natural curvature scale `d^(-2alpha)h`; after the Euclidean case, the next extension is a weighted tangent Kac–Rice formula using the `l_p` second fundamental form `(p-1)D_x` and the predecessor's exact effective-support factor `eta_p(x)`.

If the rank-stratified Kac–Rice route fails after a second genuine pivot, preserve this report and hand this bottleneck to a complementary probability role, as required by the owner directive, rather than reverting to admission/audit waiting.

---

## 17. Claim discipline

- **PROVED PARTIAL:** Theorems 3.1, 4.1, 6.1, 7.1, 8.1, 9.1, 10.1, and 11.1 above are proved within their stated assumptions.
- **CONDITIONAL:** Section 13 records the Kac–Rice reduction target under standard regular-stratum nondegeneracy; the final rank-stratified integration is not yet proved.
- **NOT CLAIMED:** No arbitrary deterministic `2<=p<2r` solution is claimed.
- **NOT CLAIMED:** No literature novelty priority is claimed for generic convex support-function identities, Gaussian integration by parts, Kac–Rice, or the adjugate identity. The new campaign contribution is their source-normalized tensor specialization and the resulting obstruction/cancellation architecture.
- **PRESERVATION:** This report is a new immutable file. It does not overwrite C0035 history, prior P09 reports, or peer-owned material.
