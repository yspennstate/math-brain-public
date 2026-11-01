Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 progress-first run — posterior packing, exact cancellation of base variance, and variance-localized chaining

**Status: PROVED PARTIAL.** This report does **not** prove Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The fixed worst-case polynomial exponent remains `gamma = 1/2-1/(2r)` rather than the conjectured `alpha = 1/2-1/p`. The new progress is an arbitrary-tensor covering/chaining reduction which is non-volumetric and which cancels the entire zeroth-order process variance before the entropy estimate is formed. It replaces a global Frobenius penalty by a scale-dependent family of posterior *central* variances, and then localizes those central variances to points whose natural Gaussian variance is still visible at that scale. A counterexample at the end shows that variance localization alone is still insufficient: dense coordinate dust can inflate the highest contraction while leaving the process value macroscopic. That identifies the next required move as a genuinely multiscale head/tail barycentric decomposition rather than another one-shot covariance optimization.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Installed title: `Gaussian Tensor Bounds`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac, A. Rodder, *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.
- Source norm:

```text
||T||_sym(I_p) := sup_{||x||_p<=1} |T[x,...,x]|.
```

- Source target for symmetric deterministic order-`r` tensors `T_i` and iid standard Gaussian `g_i`:

```text
E ||sum_i g_i T_i||_sym(I_p)
 <= polylog(d,n) C(r,p) d^(1/2-1/p)
    (sum_i ||T_i||_sym(I_p)^2)^(1/2).
```

- Regime: `2 <= p < 2r`.
- Pre-run master inspected: `bf35e0dea9b649c3f5f2b267f31e16278446e592`.
- Immediate P09 predecessor: `2026-09-20T015600Z__adaptive-maurey-pacbayes-and-norming-cover.md`, creation commit `679080f15ff9cace286a0d3dbbba014a151c753d`, blob `ac34c9b551bd30cdee92d14f4d9a5a43e89df4c8`.
- Historical C0035/successor-gate material is preserved; no historical or peer file is edited.

## 1. Source-current baseline

Put

```text
alpha := 1/2 - 1/p,
gamma := 1/2 - 1/(2r),
S := (sum_i ||T_i||_sym(I_p)^2)^(1/2).
```

The strongest primary general results recovered for this run remain the same ones used in the predecessor report:

1. Bandeira--Gopi--Jiang--Lucca--Rothvoss, arXiv:2411.10633, obtain the geometric covering/contraction bound and the worst-case polynomial exponent

```text
d^(1/2 - 1/max(p,2r)),
```

up to logarithms. Hence the conjectured exponent is reached for `p>=2r`, while `p<2r` leaves exponent `gamma`.

2. Aden-Ali, arXiv:2503.10580, proves the sharper PAC-Bayes contraction inequality and removes an unnecessary logarithmic loss from the worst-case polynomial estimate, but the low-`p` exponent remains `gamma` after insertion of the general contraction bounds.

3. Randomstrasse101, arXiv:2603.29571, still states Conjecture 16 in the low-`p` regime and explicitly identifies the volumetric obstruction. A bounded fresh search on 20 September 2026 located no later primary theorem claiming the arbitrary-deterministic-tensor low-`p` conjecture. This is a status check, not a claim that no such work exists anywhere.

Known matrix, rank-one, independent-entry and `p>=2r` cases are not being claimed as new.

Thus the fixed full-source metric remains

```text
old arbitrary-tensor exponent: gamma,
new arbitrary-tensor exponent: gamma,
target exponent:               alpha.
```

## 2. The inherited obstruction and what must change

The predecessor report constructed a coordinate-adaptive empirical posterior. For a test vector `x`, a probability vector `q=q(x)`, and an integer `s>=1`, it produced an empirical vector `Theta` with

```text
E Theta = x,
M_s(x) := E Theta Theta^T
        = (1-1/s) xx^T + (1/s) D_{x,q},
D_{x,q} := diag(q_j + x_j^2/q_j).
```

For `r` independent slots, the posterior quadratic quantity was

```text
V_s(x)
 := sum_i <T_i, M_s(x)^(tensor r) T_i>_F.
```

A one-shot PAC-Bayes argument pays the point-selection entropy against `V_s(x)` itself. At a flat vector this retains the `ell=0` term

```text
sum_i T_i[x^r]^2,
```

and recreates the Aden-Ali polynomial balance. The promised attack was therefore to make entropy interact with *incremental* covariance rather than total variance.

The main observation below is that passing from a PAC-Bayes expectation inequality to a packing argument automatically performs exactly this subtraction:

```text
posterior second moment - squared posterior mean
= posterior central variance.
```

That removes the entire zeroth-order term before any covering number is estimated.

## 3. General posterior-to-packing lemma

The following statement is independent of tensors.

### Lemma 3.1 (barycentric posterior packing)

Let `T` be a subset of a Hilbert space `H`, with metric `d(u,v)=||u-v||_H`. Let `P` be one fixed probability measure on `H`. Suppose that for every `t in T` there is `Q_t << P` satisfying

```text
E_{Q_t} Z = t,
KL(Q_t || P) <= K,
E_{Q_t} ||Z-t||_H^2 <= R^2.
```

Then

```text
N(T,d,2 sqrt(2) R) <= 4 exp(2K).                           (3.1)
```

Here the covering centers may be chosen in `T` itself.

### Proof

For each `t`, let

```text
B_t := { z : ||z-t||_H < sqrt(2) R }.
```

Markov gives

```text
Q_t(B_t) >= 1/2.                                           (3.2)
```

Write `q=Q_t(B_t)` and `a=P(B_t)`. Data processing of relative entropy under the indicator of `B_t` gives

```text
K >= KL(Bern(q) || Bern(a)).                               (3.3)
```

For `q>=1/2`,

```text
KL(Bern(q)||Bern(a))
 = -h(q) - q log a - (1-q) log(1-a)
 >= -log 2 + (1/2) log(1/a),                              (3.4)
```

because `h(q)<=log 2` and the last Bernoulli term is nonnegative. Hence

```text
a >= (1/4) exp(-2K).                                       (3.5)
```

Now take any `2 sqrt(2)R`-separated subset `{t_1,...,t_M}` of `T`. The balls `B_{t_j}` are pairwise disjoint, so (3.5) implies

```text
1 >= sum_j P(B_{t_j})
  >= M (1/4) exp(-2K).
```

Therefore `M<=4 exp(2K)`. A maximal separated subset is a `2 sqrt(2)R`-net, proving (3.1). QED.

### Why this is the right operation

The lemma does not estimate volume in the ambient coordinate space and does not use a Euclidean covering of `B_p^d`. It counts distinguishable process points by asking how many posterior clouds, each carrying a fixed amount of **one common prior mass**, can be disjoint. Most importantly, the radius is a central second moment around the barycenter, not the raw posterior second moment.

## 4. Apply the lemma to the tensor Gaussian metric

Define the coefficient map

```text
a(x) := ( T_1[x,...,x], ..., T_n[x,...,x] ) in R^n,
```

and its natural Gaussian metric

```text
d_T(x,y) := ||a(x)-a(y)||_2.                               (4.1)
```

For `x != 0`, write

```text
L_2 := ||x||_2,
q_x(j) := x_j^2 / L_2^2       on supp(x),                  (4.2)
q_x(j) := 0                   off supp(x).
```

Use the same latent prior as the predecessor report: a coordinate `J` uniform on `[d]` and a standard Cauchy amplitude. Under the posterior, take

```text
J ~ q_x,
Z | J=j ~ N(x_j/q_x(j), 1),
Y := Z e_J.
```

Then `E Y=x`. Its second moment is

```text
D_x := E YY^T
     = diag(q_x(j) + x_j^2/q_x(j))                         (4.3)
```

with zero entries off `supp(x)`. On the support, the special choice (4.2) gives the exact simplification

```text
(D_x)_{jj} = x_j^2/L_2^2 + L_2^2.                         (4.4)
```

Take `s` iid copies and average them. For each of the `r` tensor slots do this independently, obtaining `Theta_1,...,Theta_r`. Let the latent prior be the corresponding fixed product prior and push it forward by

```text
Phi(theta)
 := ( T_i[Theta_1,...,Theta_r] )_{i=1}^n in R^n.           (4.5)
```

Call the pushforward prior `P_s` and the pushforward posterior at `x` by `Q_{x,s}`. Multilinearity and independence give the exact barycentric identity

```text
E_{Q_{x,s}} Phi = a(x).                                    (4.6)
```

Data processing gives

```text
KL(Q_{x,s} || P_s)
 <= r s kappa(x,q_x),                                      (4.7)
```

where `kappa` is the one-atom KL from the predecessor report.

### 4.1 The KL cost is still only logarithmic

The prior calculation proved

```text
kappa(x,q)
 <= log d - H(q) + c_0 + log(2 + sum_j x_j^2/q_j).         (4.8)
```

For (4.2), if `k=|supp(x)|`, then

```text
sum_j x_j^2/q_x(j) = k L_2^2 <= d L_2^2.                  (4.9)
```

Since `||x||_p<=1` and `p>=2`,

```text
L_2 <= d^(1/2-1/p) = d^alpha.                              (4.10)
```

Consequently

```text
kappa(x,q_x) <= C log(2d)                                  (4.11)
```

uniformly on `B_p^d` (the numerical constant can be taken independent of the tensors; `p` is fixed throughout the source problem). Thus

```text
KL(Q_{x,s}||P_s) <= C r s log(2d).                         (4.12)
```

## 5. Exact cancellation of the zeroth-order variance

Define

```text
b(x) := ||a(x)||_2
      = (sum_i T_i[x^r]^2)^(1/2).                          (5.1)
```

The predecessor report computed the raw posterior second moment

```text
V_s(x)
 := E_{Q_{x,s}} ||Phi||_2^2
 = sum_{ell=0}^r binom(r,ell)
     (1-1/s)^(r-ell) s^(-ell) W_ell(x)^2,                 (5.2)
```

where

```text
W_ell(x)^2
 := sum_i ||
      (D_x^(1/2))^(tensor ell)
      T_i[x,...,x, dot,...,dot]
    ||_F^2,                                                (5.3)
```

with `r-ell` copies of `x` and `ell` free slots. In particular

```text
W_0(x)^2 = b(x)^2.                                         (5.4)
```

The quantity needed in Lemma 3.1 is not `V_s(x)`. It is the posterior central variance

```text
Delta_s(x)^2
 := E_{Q_{x,s}} ||Phi-a(x)||_2^2
  = V_s(x) - b(x)^2.                                       (5.5)
```

Substituting (5.2),

```text
Delta_s(x)^2
 = [(1-1/s)^r - 1] b(x)^2
   + sum_{ell=1}^r binom(r,ell)
       (1-1/s)^(r-ell) s^(-ell) W_ell(x)^2.               (5.6)
```

The bracketed coefficient is nonpositive. Since the left side is nonnegative, dropping that negative term yields the key inequality

```text
boxed:
Delta_s(x)^2
 <= sum_{ell=1}^r binom(r,ell) s^(-ell) W_ell(x)^2.        (5.7)
```

**There is no `ell=0` term.**

This is the substantive cancellation missing from the one-shot PAC-Bayes estimate. The process value itself is no longer multiplied by the entropy cost. Only posterior fluctuations around that value determine the covering radius.

## 6. New arbitrary-tensor covering theorem

The next refinement is to avoid taking a global supremum over contractions that occur only at process points already invisible at the current metric scale.

For `u>=0`, define the active set

```text
A_u := { x in B_p^d : b(x) > u },                          (6.1)
```

and, for `1<=ell<=r`, the variance-truncated weighted contraction

```text
H_ell(u) := sup_{x in A_u} W_ell(x),                       (6.2)
```

with the convention `H_ell(u)=0` if `A_u` is empty.

Also put

```text
R_s(u)^2
 := C_r sum_{ell=1}^r s^(-ell) H_ell(u)^2.                (6.3)
```

### Theorem 6.1 (variance-localized posterior covering)

For every `u>=0` and integer `s>=1`,

```text
N(B_p^d, d_T, max{u, C_r R_s(u)})
 <= 1 + 4 exp(C_r s log(2d)).                              (6.4)
```

All tensors are arbitrary deterministic symmetric order-`r` tensors. There is no block, rank, independence, coefficient-support, or interaction-degree assumption.

### Proof

If `x notin A_u`, then by definition

```text
d_T(x,0)=b(x)<=u,
```

so the entire inactive set is covered by the one center `0` at radius `u`.

On `A_u`, equations (4.6), (4.12), and (5.7) show that the pushforward posteriors `Q_{x,s}` satisfy Lemma 3.1 with one common prior `P_s`, KL at most `C_r s log(2d)`, and central variance at most `R_s(u)^2`. Lemma 3.1 therefore covers `a(A_u)` by at most

```text
4 exp(C_r s log(2d))
```

balls of radius `C_r R_s(u)`. Add the origin for the inactive set. QED.

### Corollary 6.2 (pointwise entropy profile)

There are constants depending only on `r,p` such that, for every `0<epsilon<=2H_0`, where

```text
H_0 := sup_{x in B_p^d} b(x),                              (6.5)
```

we have

```text
sqrt(log N(B_p^d,d_T,C_r epsilon))
 <= C_{r,p} sqrt(log(2d))
    [ 1 + max_{1<=ell<=r}
        { H_ell(epsilon) / epsilon }^(1/ell) ].            (6.6)
```

Changing the argument `epsilon` in `H_ell` by an `r`-dependent constant only changes the displayed constants.

### Proof

Apply Theorem 6.1 with `u` a fixed small multiple of `epsilon` and choose

```text
s := ceil( C_r [1 + max_ell
                 {H_ell(u)/epsilon}^{2/ell}] ).            (6.7)
```

Then each summand in (6.3) is `O_r(epsilon^2)`, so `R_s(u)=O_r(epsilon)`. Insert (6.7) into (6.4) and take square roots of logarithms. QED.

## 7. A new chaining reduction for Conjecture 16

Because `a(B_p^d)` lies in the Euclidean ball `H_0 B_2^n`, the elementary ambient covering estimate also gives

```text
sqrt(log N(B_p^d,d_T,epsilon))
 <= sqrt( n log(1 + C H_0/epsilon) ).                      (7.1)
```

Combining (6.6), (7.1), and Dudley's entropy integral gives the following arbitrary-tensor reduction.

### Theorem 7.1 (variance-localized contraction integral)

Let

```text
Psi(epsilon)
 := min {
      sqrt( n log(1+C H_0/epsilon) ),
      C_{r,p} sqrt(log(2d))
      [1 + max_{1<=ell<=r}
          {H_ell(c_r epsilon)/epsilon}^{1/ell}]
    }.                                                     (7.2)
```

Then

```text
E ||sum_i g_i T_i||_sym(I_p)
 <= C_r integral_0^(2H_0) Psi(epsilon) d epsilon.          (7.3)
```

In particular, Conjecture 16 follows for any tensor family for which

```text
integral_0^(2H_0) Psi(epsilon) d epsilon
 <= polylog(d,n) C(r,p) d^alpha S.                         (7.4)
```

### Proof

The centered Gaussian process

```text
X_x := sum_i g_i T_i[x^r]
```

has canonical metric (4.1) and contains the base point `x=0`, where `X_0=0`. Dudley's theorem bounds `E sup_x X_x` by a universal constant times the entropy integral of its canonical metric. Apply the smaller of the two entropy bounds (6.6) and (7.1) at each scale. Applying the same estimate to `-X_x` and using

```text
sup_x |X_x| <= sup_x X_x + sup_x (-X_x)
```

gives (7.3). Equation (7.4) is then immediate. QED.

### Why this is stronger information than the global contraction bound

The current primary global geometry takes contractions such as

```text
sigma_ell
 := sup_{x_1,...,x_{r-ell} in B_p}
    (sum_i ||T_i[x_1,...,x_{r-ell},dot^ell]||_F^2)^(1/2)
```

without remembering whether the maximizing vectors correspond to process points with large or tiny `b(x)`. Theorem 7.1 keeps that correlation. A bad contraction is charged at scale `epsilon` only if it occurs at an `x` with

```text
b(x) > c_r epsilon.
```

This is precisely the information a volumetric estimate discards.

## 8. Sanity check: recovering the known worst-case exponent, not falsely claiming more

From (4.4), on `supp(x)`,

```text
D_x <= (1+||x||_2^2) I
    <= 2 d^(2 alpha) I.                                   (8.1)
```

Therefore the weighted contractions obey

```text
H_ell(0)
 <= C_r d^(alpha ell) sigma_ell.                           (8.2)
```

If we throw away the new `u`-dependence and insert (8.2) into (6.6), then, up to logarithms,

```text
sqrt(log N(epsilon))
 <= d^alpha
    max_ell (sigma_ell/epsilon)^(1/ell).                   (8.3)
```

This is the same polynomial-scale entropy structure as the current geometric theory, not a miraculous full proof.

The general contraction comparison gives

```text
sigma_ell <= C_r d^max(ell/p-1/2,0) S.                    (8.4)
```

For the worst term `ell=r` in the unresolved regime `p<2r`, the exponent becomes

```text
alpha + (1/r)(r/p - 1/2)
 = 1/2 - 1/(2r)
 = gamma.                                                   (8.5)
```

Thus a proof which immediately replaces every `H_ell(epsilon)` by its global supremum throws away all the new information and returns exactly to the known `gamma` obstruction. The full-source exponent has therefore honestly not moved.

What *has* moved is the reduction: the obstruction is no longer forced to be described as ambient volume. It is now enough to control high contractions **conditioned on the process point still having variance at the scale being chained**.

## 9. Counterexample to the tempting next lemma: variance truncation alone still does not beat dense dust

Before building the full proof around (7.3), test the strongest tempting simplification:

> Perhaps `b(x)>u` by itself forces the adaptive high-order contraction `W_r(x)` to be small enough to remove the `gamma` loss.

This is false, even for the simplest diagonal tensor.

Take `p=2`, `r>=3`, `n=1`, and

```text
T := sum_{j=1}^d e_j^(tensor r).                           (9.1)
```

Its symmetric injective `I_2` norm is `1`, so `S=1`. Fix any constant `c in (0,1)`, and define the positive unit vector

```text
x_1 = c,
x_j = sqrt((1-c^2)/(d-1)),   j=2,...,d.                   (9.2)
```

Then

```text
||x||_2=1,
```

and the process coefficient is

```text
b(x)
 = T[x^r]
 = c^r + (d-1)^((2-r)/2) (1-c^2)^(r/2)
 >= c^r.                                                    (9.3)
```

So this point lies in the active set `A_u` for every fixed `u<c^r`, uniformly in `d`.

For the posterior choice (4.2), `q_j=x_j^2` and, because every coordinate in (9.2) is nonzero and `L_2=1`,

```text
(D_x)_{jj} = 1 + x_j^2 >= 1.                              (9.4)
```

At `ell=r`, no copies of `x` remain, and therefore

```text
W_r(x)^2
 = || (D_x^(1/2))^(tensor r) T ||_F^2
 = sum_{j=1}^d (D_x)_{jj}^r
 >= d.                                                      (9.5)
```

Hence

```text
H_r(u) >= sqrt(d)   for every fixed u<c^r.                 (9.6)
```

This refutes the proposed intermediate lemma. A macroscopic process value can coexist with an enormous adaptive highest contraction because an arbitrarily diffuse low-amplitude tail keeps all coordinates inside the exact barycentric posterior. The tail contributes little to `T[x^r]` but heavily to the posterior fluctuation because exact one-scale mean preservation insists on representing it immediately.

This is a sharper description of the remaining volumetric obstruction than the flat-vector calculation in the previous run: **the problem is not only flat points; it is dense dust attached to an otherwise important point.**

## 10. Consequence: what a successful multiscale posterior must do

The counterexample dictates the next design rather than merely saying “try chaining.” At a coarse scale, the posterior must not represent every tiny coordinate of `x` exactly. Instead write a nested decomposition

```text
x = x^(0) + z^(1) + z^(2) + ...                            (10.1)
```

where `x^(0)` contains the large coordinates and `z^(k)` introduces one smaller magnitude layer at a time. Entropy at level `k` should be charged only against the Gaussian metric increment

```text
a(x^(0)+...+z^(k)) - a(x^(0)+...+z^(k-1)),                (10.2)
```

not against `a(x)` itself.

For symmetric tensors, multilinearity gives the exact algebraic expansion

```text
T[(y+z)^r]-T[y^r]
 = sum_{m=1}^r binom(r,m) T[y^(r-m), z^m].                 (10.3)
```

Thus every increment contains at least one copy of the newly introduced layer `z`. This is the mechanism missing from every one-shot posterior so far: tiny coordinate dust can only enter a covariance factor at the scale where that dust itself is being added.

A viable next lemma should therefore have the form

```text
sqrt(log N_k)
 * [ central variance of the mixed terms in (10.3) ]^(1/2),
```

with the parent `y` chosen from the previous finite net and the child posterior randomizing only the new layer. The discrete choice of parent costs `log N_{k-1}`; the sparse coordinate posterior for `z` pays the new support/amplitude entropy. This is a true chaining recursion, not a repetition of the one-scale PAC-Bayes bound.

The first mandatory counter-test for that lemma is exactly (9.1)--(9.2): the constant-sized head should be resolved at a coarse level while the `(d-1)`-coordinate dust is postponed to finer levels, where its contribution to (10.3) is small. The second test is the genuinely flat vector, where no head exists and the method must recover its gain through many balanced layers rather than hide a polynomial loss in the first level.

## 11. Relation to the new C05 entropy handoff

The fresh C05 handoff at commit `4425a137c14eeb0d7f05bda458b686f46117067f` proves exact entropy deficits for signed matrix fibers from Gram covariance defects. It may become useful **after** a mixed increment in (10.3) is discretized into a signed-permutation-symmetric coefficient family. That Gaussian-to-sign / tensor-increment bridge has not been proved here, so the C05 lemma is not used as if its hypotheses already held. Ownership remains unchanged.

## 12. What changed this run

### New proved statements

1. **Lemma 3.1:** a barycentric posterior-to-packing theorem converting KL plus posterior *central* variance into a covering number without ambient volume.

2. **Exact tensor cancellation (5.7):** for the empirical tensor posterior, the `ell=0` process variance cancels completely. The covering radius starts at `ell=1`.

3. **Theorem 6.1 / Corollary 6.2:** a variance-localized covering bound for arbitrary deterministic symmetric tensors. High contractions are charged at a scale only on process points still visible at that scale.

4. **Theorem 7.1:** an arbitrary-tensor Dudley reduction to the scale-dependent high-variance contraction profile `H_ell(epsilon)`.

### New negative result / method boundary

The diagonal “head plus dense dust” construction (9.1)--(9.6) proves that process-variance truncation by itself cannot control `H_r(u)`. Exact one-scale barycentricity still allows tiny coordinates to poison high-order posterior covariance.

### Full-source metric

```text
arbitrary deterministic tensors:
    gamma -> gamma   (no headline exponent movement)

target:
    alpha = 1/2 - 1/p
```

The mathematical progress is a stronger non-volumetric arbitrary-tensor covering reduction and an exact identification of the next obstruction.

## 13. Obligation ledger

| obligation | before | after |
|---|---|---|
| Full arbitrary-tensor exponent `gamma -> alpha` | OPEN | OPEN |
| Remove `ell=0` entropy/variance coupling | OPEN | **PROVED: exact central-variance cancellation (5.7)** |
| Obtain an arbitrary-tensor non-volumetric covering inequality | partial / one-shot | **PROVED: Theorem 6.1** |
| Preserve scale information instead of global contraction maxima | OPEN | **PROVED: variance-localized `H_ell(u)` reduction** |
| Determine whether variance localization alone beats dense dust | unknown | **NO: counterexample (9.1)--(9.6)** |
| True multiscale head/tail barycentric chaining | OPEN | next attack |

## 14. Next concrete attack

Construct the first **two-level head/tail posterior chaining lemma** based on (10.3):

1. choose a deterministic magnitude threshold and a parent net for the head `y`;
2. represent only the new layer `z` with a sparse barycentric posterior;
3. push that posterior through the mixed tensor increment in (10.3);
4. prove that its central variance contains at least one tail-weighted slot in every term;
5. optimize the threshold and sample count;
6. test first on the diagonal head+dust vector (9.2), then on the completely flat vector;
7. reject the method immediately if summing the two levels reconstructs the old global `ell=r` loss.

Only after this two-level calculation survives both witnesses should it be iterated into a full dyadic chain or combined with the C05 signed-fiber entropy mechanism.

No finite checker is added: the claims here are analytic Hilbert-space/KL/covering arguments, and the useful verification is the explicit proof plus the two exact obstruction calculations rather than another certificate rerun.
