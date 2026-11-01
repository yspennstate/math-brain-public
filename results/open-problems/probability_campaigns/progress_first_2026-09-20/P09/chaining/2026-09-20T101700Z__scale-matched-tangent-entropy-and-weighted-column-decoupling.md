Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 progress-first run — scale-matched tangent entropy and weighted one-slot decoupling

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The full-source arbitrary-tensor polynomial exponent recovered from the primary literature remains

```text
gamma = 1/2 - 1/(2r)
```

in the unresolved range `2 <= p < 2r`, versus the conjectured

```text
alpha = 1/2 - 1/p.
```

This run changes method from the preceding active-Grassmannian/commutator route. The main new point is that one does not actually need to count active subspaces directly. A scale-matched operator-norm cover of the **tangent field itself** already transfers to a process cover at the conjectured dimension scale, with only `O(k log k)` additional entropy. I then prove an exact balanced one-slot Maurey decomposition of every process point into normalized tangent columns, identify a new weighted-column route to the tangent entropy bound, and prove a sparse common-witness certificate for every active range using spectral sparsification. Finally I give an order-`r` counterexample showing why unweighted normalized-column entropy is the wrong object: normalized tangent directions may sweep an entire high-dimensional sphere while carrying zero process mass.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Registered role: `chaining / geometric-probabilistic proof`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Immediate P09 predecessor: `probability_campaigns/progress_first_2026-09-20/P09/chaining/2026-09-20T085800Z__active-frame-truncation-and-commutator-counterexample.md`, creation commit `fc1c4e334ab4a663a36728424f393c71ab9ec8aa`, blob `f81831035b3e38c5da44b7ec6b331d5c0b00310e`.
- Historical C0035 material, earlier P09 reports, and peer files are preserved. This file is additive and immutable.

## 1. Source statement and current primary baseline

Source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac, A. Rodder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.

The source norm is the **symmetric diagonal injective norm**

```text
||T||_I_p := sup_{||x||_p <= 1} |T[x,...,x]|.
```

For symmetric `r`-linear forms, real polarization gives

```text
||T||_(full p-injective)
 <= P_r ||T||_I_p,
P_r := r^r/r!.
```

The precise value of `P_r` is irrelevant to the dimension exponent, but it matters that it depends only on `r`. I therefore keep a fixed symbol `C_r` whenever a mixed evaluation such as `T[x^(r-1),v]` is used.

The source asks for

```text
E ||sum_i g_i T_i||_I_p
 <= C(r,p) polylog(d,n) d^(1/2-1/p)
    (sum_i ||T_i||_I_p^2)^(1/2).
```

A bounded fresh primary-source check on 20 September 2026 recovered the same general baseline as the preceding runs:

1. Bandeira--Gopi--Jiang--Lucca--Rothvoss, arXiv:2411.10633 / STOC 2025, gives the general geometric correlated-tensor estimate and settles the target polynomial exponent when `p >= 2r`; in the low-`p` regime its general polynomial exponent is the volumetric one `1/2 - 1/(2r)`.
2. Ishaq Aden-Ali, arXiv:2503.10580, gives a sharper PAC-Bayesian variance-parameter inequality and improves the BGJLR bound, but does not remove the arbitrary correlated `p<2r` polynomial obstruction.
3. Dartois--McKenna, arXiv:2603.01342 (March 2026), gives a deterministic moment inequality and sharp bounds for several random-tensor ensembles, but the stated models do not resolve the universal Gaussian sum of arbitrary deterministic correlated summands in Conjecture 16.
4. The Randomstrasse101 source itself still records Conjecture 16 and separately lists the matrix, rank-one, independent-entry, Hankel/structured, and `p>=2r` situations.

No later primary source resolving the exact arbitrary deterministic `2<=p<2r` statement was recovered in this bounded check. This is not a claim about unpublished or unindexed work.

Hence the headline metric for this report is

```text
old arbitrary exponent = gamma = 1/2 - 1/(2r)
new arbitrary exponent = gamma = 1/2 - 1/(2r)
target exponent        = alpha = 1/2 - 1/p
source status           = OPEN / not solved here
```

The advances below are reductions and restricted theorems, not a source-level resolution.

---

## 2. Tangent setup in the exact source normalization

Put

```text
S^2 := sum_i ||T_i||_I_p^2,
alpha := 1/2 - 1/p.
```

For `x in B_p^d`, define the process embedding and its one-slot tangent map

```text
F(x) := (T_i[x,...,x])_(i=1)^n in R^n,
(A_x v)_i := T_i[x,...,x,v],
```

where `A_x v` contains `r-1` copies of `x` and one copy of `v`. Then

```text
F(x) = A_x x.                                             (2.1)
```

Real polarization and `p>=2` imply

```text
||A_x||_HS <= C_r S,                                      (2.2)
```

because each row functional `v -> T_i[x^(r-1),v]` has `ell_q` norm at most `C_r ||T_i||_I_p`, where `q=p/(p-1)<=2`, and therefore Euclidean norm at most the same quantity.

Likewise, telescoping the first `r-1` slots gives

```text
||A_x-A_y||_op <= C_r S ||x-y||_p,                        (2.3)
```

and telescoping all `r` slots gives

```text
||F(x)-F(y)||_2 <= C_r S ||x-y||_p.                        (2.4)
```

Also

```text
||x||_2 <= d^alpha ||x||_p <= d^alpha.                    (2.5)
```

For convenience set

```text
R := C_r S.                                                (2.6)
```

All constants below may absorb a different fixed factor depending only on `r` (and, in final chaining statements, on `p`).

The Gaussian process in Conjecture 16 is exactly

```text
X_x := <g,F(x)>,
```

with canonical metric

```text
d_T(x,y)=||F(x)-F(y)||_2.                                  (2.7)
```

Thus Euclidean covering of `F(B_p^d)` is the relevant covering problem.

---

## 3. New theorem: scale-matched tangent entropy transfers to process entropy

Let

```text
Acal := { A_x : x in B_p^d } subset R^(n x d).             (3.1)
```

For an integer `k>=1`, define the critical tangent and process scales

```text
tau_k := R/sqrt(k),
rho_k := d^alpha R/sqrt(k) = d^alpha tau_k.                (3.2)
```

The predecessor controlled process points by active spectral subspaces. The following theorem bypasses explicit Grassmannian counting.

### Theorem 3.1 (scale-matched tangent-to-process entropy reduction)

For every integer `k>=1`,

```text
log N(F(B_p^d), ||.||_2, 2 rho_k)
 <= log N(Acal, ||.||_op, tau_k)
    + C k log(2k),                                        (3.3)
```

where `C` is universal after the fixed `r`-dependent normalization has been placed in `R`.

Equivalently, if the degree-`(r-1)` tangent field admits an operator-norm `R/sqrt(k)` net of size `exp(H_k)`, then the original degree-`r` process admits a `d^alpha R/sqrt(k)` net of size at most

```text
exp( H_k + C k log(2k) ).                                 (3.4)
```

The `d^alpha` factor appears **once**, exactly at the conjectured source scale, from the deterministic embedding `B_p^d subset d^alpha B_2^d`.

### Proof

Take an internal `tau_k`-net

```text
B_1,...,B_M in Acal,
M=N(Acal,||.||_op,tau_k),                                  (3.5)
```

so for every `x in B_p^d` there is `a` with

```text
||A_x-B_a||_op <= tau_k.                                  (3.6)
```

Because every center is itself `A_y` for some `y`, (2.2) gives

```text
||B_a||_HS <= R.                                          (3.7)
```

For such a center,

```text
||F(x)-B_a x||_2
 =||(A_x-B_a)x||_2
 <=tau_k ||x||_2
 <=rho_k.                                                  (3.8)
```

It remains to cover each fixed linear image `B_a(B_p^d)` at radius `rho_k` with `exp(O(k log k))` points.

Since

```text
B_p^d subset d^alpha B_2^d,                               (3.9)
```

it suffices to cover the ellipsoid

```text
E_a := d^alpha B_a(B_2^d).                                (3.10)
```

Let the singular values of `B_a` be

```text
s_1 >= s_2 >= ... >= 0.
```

By (3.7),

```text
sum_j s_j^2 <= R^2.                                       (3.11)
```

Let `J` be the set of singular directions satisfying

```text
s_j > R/(2 sqrt(k)).                                      (3.12)
```

Then

```text
|J| * R^2/(4k)
 < sum_(j in J) s_j^2
 <= R^2,
```

so

```text
|J| <= 4k.                                                (3.13)
```

The tail of the ellipsoid orthogonal to `J` has Euclidean radius at most

```text
d^alpha * R/(2 sqrt(k)) = rho_k/2.                        (3.14)
```

The head lies in a Euclidean ball of dimension at most `4k` and radius at most

```text
d^alpha ||B_a||_op <= d^alpha R.                          (3.15)
```

A standard volumetric net of that head at radius `rho_k/2` has cardinality at most

```text
(1 + 4 d^alpha R/rho_k)^(4k)
 = (1+4 sqrt(k))^(4k).                                    (3.16)
```

Appending zero in the tail gives a `rho_k`-net of the whole ellipsoid, because the head and tail errors are each at most `rho_k/2`. Hence

```text
log N(B_a(B_p^d),||.||_2,rho_k)
 <= 4k log(1+4 sqrt(k))
 <= C k log(2k).                                          (3.17)
```

Combining (3.8) and (3.17) over the `M` tangent centers gives (3.3). QED.

### What changed relative to the predecessor

The predecessor asked for a dictionary of active left singular subspaces. Theorem 3.1 shows that a scale-matched operator cover of the **whole tangent map** is enough and automatically ignores subcritical singular directions. No spectral gap, commutator estimate, or explicit frame matching is required in the transfer step.

This is also robust to the previous commutator counterexample: if all rotating singular directions have size below `R/sqrt(k)`, then the tangent field is already one-ball coverable at that scale regardless of how wildly their normalized directions rotate.

---

## 4. Conditional full-exponent corollary

Theorem 3.1 isolates a concrete order-reduction target.

### Corollary 4.1 (critical tangent entropy would imply Conjecture 16 up to logs)

Assume there is a quantity `L(d,n)` such that for every dyadic `k` with `1<=k<=d`,

```text
log N(Acal,||.||_op,R/sqrt(k))
 <= C_r k L(d,n).                                         (4.1)
```

Then

```text
E sup_(x in B_p^d) |<g,F(x)>|
 <= C_(r,p) d^alpha S
    [ sqrt(L(d,n)+log(2d)) log(2d)
      + sqrt(log(2d)) ].                                  (4.2)
```

In particular, if `L(d,n)` is polylogarithmic, the desired source polynomial exponent `d^alpha` follows.

### Proof sketch with the endpoint included

By Theorem 3.1, at dyadic `k`,

```text
log N(F(B_p^d),||.||_2,C rho_k)
 <= C_r k [L(d,n)+log(2k)].                               (4.3)
```

Let

```text
A := d^alpha R.                                           (4.4)
```

Then `rho_k=A/sqrt(k)`. On each dyadic interval between `A/sqrt(k)` and `A/sqrt(2k)`, the Dudley integrand is bounded by

```text
C sqrt(k[L+log(2d)]),                                     (4.5)
```

while the interval length is `O(A/sqrt(k))`. Hence each dyadic scale contributes

```text
O(A sqrt(L+log(2d))).                                     (4.6)
```

and summing over `O(log d)` scales gives the first term in (4.2).

For the terminal interval below `rho_d`, use (2.4):

```text
N(F(B_p^d),||.||_2,eps)
 <= N(B_p^d,||.||_p,eps/(C_r S))
 <= (1 + C_r S/eps)^d.                                   (4.7)
```

Since

```text
rho_d = d^alpha R/sqrt(d) = R d^(-1/p),                  (4.8)
```

the terminal entropy integral is at most

```text
C_(r,p) d^alpha S sqrt(log(2d)).                          (4.9)
```

The large-scale endpoint is harmless because `||F(x)||_2<=S`. This proves (4.2). QED.

### Interpretation

The arbitrary low-`p` conjecture is reduced to the concrete mesoscopic statement

```text
log N({A_x:x in B_p^d}, ||.||_op, C_r S/sqrt(k))
 <= k polylog(d,n).                                       (4.10)
```

This is a degree-`(r-1)` matrix-valued entropy problem. Crucially, the target radius is exactly the spectral activity threshold already identified in the predecessor.

---

## 5. New exact one-slot decomposition: balanced tangent-column Maurey

The tangent entropy problem still needs a mechanism. The following identity decouples one tensor slot without paying any higher-contraction/Frobenius term.

For fixed `x`, write the tangent columns

```text
c_j(x) := A_x e_j in R^n,
a_j(x) := ||c_j(x)||_2.                                   (5.1)
```

Define

```text
L(x) := sum_(j=1)^d |x_j| a_j(x).                         (5.2)
```

By Cauchy--Schwarz and (2.2),

```text
L(x)
 <= ||x||_2 (sum_j a_j(x)^2)^(1/2)
 = ||x||_2 ||A_x||_HS
 <= d^alpha R.                                            (5.3)
```

If `L(x)>0`, put

```text
q_x(j) := |x_j| a_j(x)/L(x)                               (5.4)
```

on those coordinates with `a_j(x)>0`, and define the unit tangent direction

```text
u_(x,j) := sign(x_j) c_j(x)/a_j(x).                       (5.5)
```

Then `||u_(x,j)||_2=1` and

```text
F(x)
 = A_x x
 = sum_j x_j c_j(x)
 = L(x) sum_j q_x(j) u_(x,j).                             (5.6)
```

Thus `F(x)/L(x)` is exactly a barycenter of **unit** one-slot tangent directions.

### Theorem 5.1 (balanced one-slot empirical approximation)

For every `x in B_p^d` and every integer `k>=1`, there exist indices

```text
j_1,...,j_k in [d]
```

(repetitions allowed) such that

```text
|| F(x)
   - (L(x)/k) sum_(a=1)^k u_(x,j_a) ||_2
 <= L(x)/sqrt(k)
 <= d^alpha R/sqrt(k).                                    (5.7)
```

Moreover the random empirical approximation obtained by drawing `J_a iid~q_x` satisfies

```text
E || F(x)
      - (L(x)/k) sum_(a=1)^k u_(x,J_a) ||_2^2
 <= L(x)^2/k.                                             (5.8)
```

### Proof

Let `U` be the random vector taking value `u_(x,j)` with probability `q_x(j)`. Equation (5.6) gives

```text
E U = F(x)/L(x).                                          (5.9)
```

Since `||U||_2=1`, for iid copies `U_1,...,U_k`,

```text
E || (1/k)sum_a U_a - E U ||_2^2
 = (1/k) E ||U-EU||_2^2
 <= 1/k.                                                  (5.10)
```

Multiply by `L(x)^2` and use (5.3). Some realization is no worse than the mean-square bound. QED.

### Why this is better than the earlier coordinate posterior

The earlier coordinate-sampling posterior used probabilities proportional to `x_j^2`. Its coefficient vectors could have huge norm when `x_j` was tiny. The balanced choice (5.4) absorbs the tangent-column magnitude as well. Every sampled **output atom has exactly the same norm `L(x)`**, so there are no heavy output atoms at all.

The only discrete choice per sample is an index `j`, whose raw combinatorial cost is at most `log d`. The unsolved part is that the unit direction `u_(x,j)` itself still depends on the full shared witness `x^(r-1)`.

---

## 6. A covariance-structure inequality and a concrete broader class

Define the symmetric union of all nonzero normalized tangent columns

```text
Ucal := { +- c_j(x)/||c_j(x)||_2 :
          x in B_p^d, j in [d], c_j(x) != 0 }.             (6.1)
```

Equation (5.6) and (5.3) imply the deterministic inclusion

```text
F(B_p^d) subset d^alpha R conv(Ucal).                      (6.2)
```

Therefore, for `g~N(0,I_n)`,

```text
E sup_(x in B_p^d) |<g,F(x)>|
 <= d^alpha R
    E sup_(u in Ucal) <g,u>.                              (6.3)
```

This is an unconditional one-slot covariance/directional-structure inequality.

### Corollary 6.1 (low tangent-direction Gaussian width class)

If

```text
w(Ucal) := E sup_(u in Ucal) <g,u>
 <= polylog(d,n),                                         (6.4)
```

then

```text
E ||sum_i g_i T_i||_I_p
 <= C_(r,p) d^alpha S polylog(d,n).                        (6.5)
```

In particular, if all normalized tangent columns lie in a fixed symmetric set of cardinality `M`, then

```text
E ||sum_i g_i T_i||_I_p
 <= C_r d^alpha S sqrt(log(2M)).                           (6.6)
```

This gives the target source exponent for a concrete correlated tensor class in which the one-slot tangent directions have low Gaussian complexity. The scalar amplitudes of the tangent columns may depend arbitrarily on `x`, and the output directions may be correlated across coordinates; no independence of the summands is assumed.

No external novelty claim is made for this structured class. Its purpose is to identify exactly which covariance geometry the one-slot decoupling can exploit.

---

## 7. Counterexample: unweighted normalized-column entropy is false as a universal route

A tempting conclusion from Theorem 5.1 would be to try to cover the union `Ucal` itself by `poly(d,n)` directions. That is false, even for actual symmetric tensors of every fixed order `r>=3`.

Let `m>=2` and work in coordinates

```text
z_0,z_1,z_2,...,z_(m+1).
```

For `ell=2,...,m+1`, let `T_ell` be the symmetric order-`r` tensor whose diagonal polynomial is

```text
P_ell(z)
 := c_r z_0^(r-2) z_1 z_ell,                              (7.1)
```

where `c_r` is a fixed nonzero normalization depending only on `r`. Rescale once, if desired, so `||T_ell||_I_2` is a fixed constant of order one. Consequently

```text
S = Theta_r(sqrt(m)).                                     (7.2)
```

For any `theta in S^(m-1)`, set

```text
x(theta)
 := 2^(-1/2) e_0
    + 2^(-1/2) sum_(ell=2)^(m+1) theta_ell e_ell.          (7.3)
```

Then `||x(theta)||_2=1` and its `z_1` coordinate is zero. Therefore

```text
F(x(theta))=0                                             (7.4)
```

for every `theta`.

On the other hand, differentiating the diagonal polynomial in the `e_1` direction and using

```text
D P_ell(x)[e_1] = r T_ell[x^(r-1),e_1]                   (7.5)
```

gives

```text
A_(x(theta)) e_1
 = c'_r (theta_2,...,theta_(m+1)),                        (7.6)
```

for a fixed nonzero `c'_r`. Hence the normalized tangent column

```text
A_(x(theta))e_1 / ||A_(x(theta))e_1||_2                   (7.7)
```

sweeps the entire sphere `S^(m-1)`.

Thus

```text
w(Ucal) >= c sqrt(m),                                     (7.8)
```

and `Ucal` has exponentially large constant-scale covering number, despite the fact that **every process point on this whole slice is exactly zero**.

This kills the intermediate lemma

```text
"normalized tangent-column directions always have polylogarithmic
complexity"
```

and shows that Corollary 6.1 is a useful sufficient class, not the arbitrary theorem.

### Why the balanced weights diagnose the example correctly

For the wild column `j=1`, every point in (7.3) has

```text
x_1=0.                                                    (7.9)
```

Therefore its balanced barycentric mass is

```text
q_x(1) proportional to |x_1| ||A_xe_1||_2 = 0.           (7.10)
```

The direction may rotate through the full sphere, but it carries **zero process mass**. The bad geometry is therefore an artefact of forgetting the weight `|x_j|a_j(x)`.

The scale-matched tangent formulation also diagnoses the example correctly. The wild column has magnitude `Theta_r(1)`, while

```text
tau_k = R/sqrt(k) = Theta_r(sqrt(m/k)).                   (7.11)
```

For `k << m`, it is spectrally inactive and disappears inside one tangent ball. It becomes visible only for `k` comparable to `m`, exactly where `O(k log d)` entropy is affordable.

This is the strongest evidence from this run that the right next object is **weighted and scale matched**, not an unweighted Grassmannian or normalized-direction set.

---

## 8. Sparse common-witness certificate for every active range

The predecessor showed that at scale `k`, the output directions with singular value at least `c R/sqrt(k)` are the only ones that can matter at critical resolution. There is a further one-slot sparsification of those directions.

Fix `x`, a threshold `tau>0`, and let `L` be the left singular subspace of `A_x` associated with singular values at least `tau`. Let

```text
m := dim L,
U : R^m -> R^n
```

be an isometric embedding onto `L`. Put

```text
B := U^* A_x in R^(m x d),
b_j := B e_j.                                             (8.1)
```

Because all singular values represented on `L` are at least `tau`,

```text
B B^* >= tau^2 I_m.                                      (8.2)
```

Also

```text
Tr(BB^*) <= ||A_x||_HS^2 <= R^2,                          (8.3)
```

so automatically

```text
m <= R^2/tau^2.                                           (8.4)
```

At the critical threshold `tau=cR/sqrt(k)`, this is `m<=k/c^2`.

### Proposition 8.1 (weighted sparse coordinate norming of an active output range)

For every `0<eta<1`, there is a set `J subset[d]` with

```text
|J| <= C m/eta^2                                         (8.5)
```

and weights `w_j>0`, `j in J`, such that

```text
(1-eta) BB^*
 <= sum_(j in J) w_j b_j b_j^*
 <= (1+eta) BB^*.                                        (8.6)
```

Consequently, for every `u in L`,

```text
sum_(j in J) w_j |<u,A_xe_j>|^2
 >= (1-eta) tau^2 ||u||_2^2.                              (8.7)
```

At `tau=cR/sqrt(k)`, the entire active output sphere therefore has a common certificate using only `O_r(k/eta^2)` input coordinates.

### Proof

Normalize the column decomposition of `BB^*` by setting

```text
v_j := (BB^*)^(-1/2)b_j.                                  (8.8)
```

On `L`, (8.2) makes the inverse well defined, and

```text
sum_j v_j v_j^* = I_m.                                   (8.9)
```

Apply the standard Batson--Spielman--Srivastava spectral sparsification theorem to this rank-one decomposition of the identity. It gives nonnegative weights supported on `O(m/eta^2)` vectors with

```text
(1-eta)I_m
 <= sum_(j in J) w_j v_jv_j^*
 <= (1+eta)I_m.                                           (8.10)
```

Conjugating by `(BB^*)^(1/2)` gives (8.6). The lower bound (8.7) follows from (8.2). QED.

### What this buys

The active-frame problem is no longer a completely arbitrary `m`-plane problem. Every active plane has a common **one-slot coordinate certificate of size `O(k)`**. The support itself costs only

```text
log binom(d,O(k)) = O(k log(ed/k)),                        (8.11)
```

which is compatible with the conjectured entropy budget.

The remaining difficulty is the weights and the actual contracted vectors `A_xe_j` on that support.

---

## 9. The weights are not a technical nuisance: they encode the volumetric obstruction

It would be convenient to delete the BSS weights in Proposition 8.1 and claim that `O(k)` raw columns already norm the active range with the correct scale. This is false in general.

Already in dimension `m=1`, let

```text
b_1=...=b_d=d^(-1/2) in R.                               (9.1)
```

Then

```text
sum_j b_j^2=1.                                           (9.2)
```

Any single unweighted column contributes only `1/d`; any unweighted set of `s` columns contributes only `s/d`. To approximate the identity within a fixed factor without weights requires `s=Theta(d)`. BSS instead selects one column and assigns it weight `Theta(d)`.

Thus the sparse support theorem by itself does **not** remove volume. It converts the old volumetric obstruction into a much sharper one:

```text
Can the large spectral weights needed to norm the active tangent range
be reconciled with the process-specific barycentric weights
|x_j| ||A_xe_j||_2?
```

The balanced Maurey decomposition from Section 5 is precisely adapted to those process weights. This is the bridge to attack next.

---

## 10. Relation between the two new reductions

There are now two independent ways to exploit the one-slot tangent geometry.

### Route A: tangent-field entropy

Prove directly

```text
log N(Acal,||.||_op,R/sqrt(k))
 <= C_r k polylog(d,n).                                   (10.1)
```

Theorem 3.1 then yields the conjectured process exponent.

This route automatically ignores all singular directions below the critical threshold.

### Route B: weighted one-slot empirical chaining

Use the exact barycentric representation

```text
F(x)=L(x) E_(J~q_x) u_(x,J),                              (10.2)
```

where

```text
q_x(j)=|x_j| ||A_xe_j||_2/L(x),
L(x)<=d^alpha R.                                          (10.3)
```

The raw index entropy of `k` samples is only `k log d`, exactly within budget. The only missing information is how much of the shared witness `x^(r-1)` must be encoded to recover the **weighted** atom directions that actually receive mass.

Proposition 8.1 says that the active range can be certified by only `O(k)` final-slot coordinates; the counterexample in Section 7 says one must not encode directions that receive negligible process weight.

The desired new lemma should therefore be a weighted alternative of the form:

```text
Either the q_x-mass is carried by O(k polylog) tangent-column
configurations whose directions have low entropy,

or the active range admits a sparse/lower-order contraction certificate
that reduces to an already controlled structured tensor class.          (10.4)
```

This would attack the source volumetric obstruction at the place where it is now genuinely located, rather than paying for all coordinates or all normalized directions uniformly.

---

## 11. A useful restricted theorem from the tangent-field reduction

Theorem 3.1 immediately yields a concrete family beyond the earlier common-active-frame formulation.

### Proposition 11.1 (low tangent-operator entropy class)

Suppose that for each dyadic `k<=d`, the tangent field has an operator-norm net

```text
Acal_k subset Acal
```

such that

```text
|Acal_k| <= exp(C k L),
max_(x in B_p^d) min_(B in Acal_k)
    ||A_x-B||_op <= R/sqrt(k),                             (11.1)
```

where `L=polylog(d,n)`. Then

```text
E ||sum_i g_iT_i||_I_p
 <= C_(r,p) d^alpha S polylog(d,n).                        (11.2)
```

No common singular frame, commutation, block support, independence, or bounded interaction degree is required. The tangent operators may rotate arbitrarily provided they do not produce more than `exp(O(k polylog))` distinguishable matrices at their own active spectral scale.

This is a genuine enlargement of the **campaign's proved structured envelope** relative to the predecessor's common-active-frame condition, because two nearby tangent operators may have very different individual singular vectors around a repeated/clustered singular value while still being close in operator norm. No external novelty claim is made.

### Simple sufficient subcase

If the tangent field lies in a fixed `m`-dimensional linear subspace of the operator space and has operator diameter `O(R)`, then a volumetric cover inside that `m`-dimensional normed space gives

```text
log N(Acal,||.||_op,R/sqrt(k))
 <= m log(C sqrt(k)).                                     (11.3)
```

Hence (11.2) follows whenever, throughout the mesoscopic range, this quantity is `O(k polylog(d,n))`; in particular any `m=polylog(d,n)` tangent-operator family is covered. This allows arbitrary correlated tensor coefficients inside that low-complexity tangent family.

Again this is a restricted theorem, not the full conjecture.

---

## 12. What has and has not been proved

### PROVED in this run

1. **Scale-matched tangent entropy reduction**

```text
log N(F(B_p),2 d^alpha R/sqrt(k))
 <= log N({A_x},R/sqrt(k)) + C k log(2k).
```

2. **Conditional full-exponent implication:** `O(k polylog)` tangent operator entropy at every dyadic critical scale implies the Randomstrasse101 target polynomial exponent.

3. **Balanced one-slot Maurey decomposition:** every process point is a barycenter of unit normalized tangent columns with total mass at most `d^alpha R`, and `k` empirical atoms approximate it at RMS error at most `d^alpha R/sqrt(k)`.

4. **Directional-width inequality:** low Gaussian width of the normalized tangent-column union is sufficient for the target source exponent.

5. **Counterexample to unweighted normalized-column entropy:** an actual symmetric order-`r` tensor family has a zero process slice whose normalized tangent column sweeps an entire high-dimensional sphere.

6. **Sparse common-witness certificate:** every active output range at threshold `R/sqrt(k)` is spectrally normed by `O(k)` final-slot coordinates with positive weights, by BSS sparsification.

7. **Weight obstruction:** the BSS weights cannot in general be deleted; doing so can require `Theta(d)` columns even in rank one.

### NOT proved

1. No `O(k polylog)` operator-norm entropy bound for the arbitrary tangent field has been proved.
2. No universal low-width bound for the unweighted normalized tangent-column union is true.
3. No argument yet reconciles arbitrary BSS spectral weights with the process-specific balanced masses `|x_j| ||A_xe_j||`.
4. The arbitrary-tensor source exponent remains `gamma=1/2-1/(2r)` rather than `alpha=1/2-1/p` in the unresolved regime.
5. Conjecture 16 is not claimed solved.

---

## 13. Remaining gap and next attack

The remaining problem is now more concrete than the predecessor's active-Grassmannian formulation.

For a critical dyadic `k`, one needs to show that the degree-`(r-1)` tangent field cannot realize too many operator-separated configurations at separation `R/sqrt(k)` **unless** those configurations carry a sparse/lower-order certificate.

The next attack will be the following weighted dichotomy.

### Target lemma to prove or refute next

For each `x`, define

```text
a_j(x)=||A_xe_j||_2,
q_x(j)=|x_j|a_j(x)/L(x).
```

At scale `k`, split the final-slot coordinates according to their balanced mass and active leverage. Try to prove:

```text
HIGH-MASS / REGULAR branch:
  after discarding total q_x-mass O(1/sqrt(k)),
  the relevant normalized tangent columns admit a common
  exp(polylog(d,n))-complexity local dictionary;

or

SPARSE / IRREGULAR branch:
  a BSS active certificate contains a coordinate with anomalously
  large required spectral weight, and that large weight forces a
  lower-order contraction, sparse norming set, or block/direct-sum
  structure already covered by previous P09 theorems.                (13.1)
```

The Section 7 tensor family is the mandatory first counterexample test: any formulation that charges its zero-mass rotating column must be rejected. The diagonal/dense-dust tensor is the second test: a valid lemma must not reintroduce the old Frobenius penalty through many tiny coordinates.

A second line, if (13.1) fails, is to attack (10.1) directly by a scale-sensitive polynomial entropy argument for `x -> A_x` in operator norm. Theorem 3.1 ensures that success there immediately transfers to the original process with the correct `d^alpha` factor.

This is substantive progress rather than an admission/audit loop, so the P09 schedule should remain enabled subject only to actual user/platform holds.

---

## 14. Continuity / ownership

This report is additive. It does not alter canonical ownership, does not overwrite the C0035 history, does not overwrite any earlier P09 report, and does not claim a peer result as this role's theorem. The registered `P09 / chaining / geometric-probabilistic proof` role remains distinct from the P09 owner slot and from other probability campaigns.

Later independent review is welcome but does not freeze the ongoing proof search.
