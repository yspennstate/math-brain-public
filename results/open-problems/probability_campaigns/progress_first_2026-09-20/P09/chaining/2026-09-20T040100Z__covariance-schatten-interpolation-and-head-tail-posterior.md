Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 progress-first run — covariance Schatten interpolation and a head/tail posterior obstruction

**Status: PROVED PARTIAL.** This report does **not** prove Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The full-source worst-case polynomial exponent remains

```text
gamma = 1/2 - 1/(2r)
```

rather than the conjectured

```text
alpha = 1/2 - 1/p.
```

The useful progress is an unconditional covariance-structure inequality for arbitrary symmetric tensors. It interpolates a weighted `q`-slot contraction against *lower-order* variance parameters through Schatten moments of the posterior covariance. This identifies a concrete route around the volumetric obstruction: one needs posterior increments whose covariance is spectrally flat/low-effective-rank at entropy cost comparable to that effective rank. A new head/tail posterior makes that target explicit, and an exact entropy-versus-variance identity shows why the most obvious product-tail realization still fails on dense coordinate dust.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Installed title: `Gaussian Tensor Bounds`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac, A. Rodder, *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.
- Source norm: `||T||_sym(I_p) = sup_{||x||_p<=1} |T[x,...,x]|`.
- Source target:

```text
E ||sum_i g_i T_i||_sym(I_p)
 <= polylog(d,n) C(r,p) d^(1/2-1/p)
    (sum_i ||T_i||_sym(I_p)^2)^(1/2).
```

- Regime: `2 <= p < 2r`.
- Pre-write master inspected: `56703929ea96a6170c9e72208d3b35c4f936d02f`.
- Immediate P09 predecessor: `2026-09-20T024819Z__posterior-packing-and-variance-localized-chaining.md`, creation commit `e6b8ed46fec54055fb18b65735492ebf03d5b619`, blob `00904e4de0aca301cd6ff3ab1bf8dd519f3d08f2`, together with immutable erratum `2026-09-20T024819Z__posterior-packing-erratum.md`, commit `aacded50720589a4cdc0cd3559e077d5c99dcc74`, blob `504f474d2bc9abbc21967698b402d3713a3a3c34`.
- Historical C0035/successor-gate material is preserved; no peer or historical file is edited.

## 1. Source-current baseline

A bounded fresh check on 20 September 2026 recovered the August 24, 2026 arXiv rendering of Randomstrasse101. Entry 8 still states Conjecture 16, records the `p>=2r` result of Bandeira--Gopi--Jiang--Lucca--Rothvoss, explicitly attributes the `p<2r` failure to a volumetric barrier, and notes Aden-Ali's PAC-Bayes improvement. It also separates the matrix, independent-entry, rank-one and other structured cases from the general deterministic-tensor problem. No later primary full solution was found in this bounded check; that is a search result, not a worldwide nonexistence claim.

The fixed metric therefore remains

```text
old arbitrary-tensor exponent: gamma = 1/2 - 1/(2r),
new arbitrary-tensor exponent: gamma = 1/2 - 1/(2r),
target exponent:               alpha = 1/2 - 1/p.
```

So the headline exponent does not move in this run. The advance is a new structural inequality that changes what must be controlled in a multiscale posterior/chaining proof.

## 2. Variance parameters and the object to interpolate

For clarity I use the multilinear injective version inside the proof. For symmetric order-`r` tensors, polarization changes the symmetric source norm by a factor depending only on `r`, which is harmless in `C(r,p)`.

For `0 <= q <= r`, define the `q`-free-slot variance parameter

```text
sigma_q^2
 := sup_{u_1,...,u_{r-q} in B_p^d}
    sum_i ||T_i[u_1,...,u_{r-q}, dot,...,dot]||_F^2.       (2.1)
```

There are `q` free slots in the Frobenius norm. In particular, up to the polarization constant,

```text
sigma_0 <= C_r S,
S := (sum_i ||T_i||_sym(I_p)^2)^(1/2).                    (2.2)
```

The existing general contraction estimates imply, again up to `C_r`,

```text
sigma_q <= C_r d^max(q/p - 1/2, 0) S.                     (2.3)
```

Fix `x in B_p^d`, an integer `1<=q<=r`, and a positive semidefinite matrix `C`. Define the covariance-weighted contraction energy

```text
V_q(x,C)
 := sum_i ||(C^(1/2))^(tensor q)
              T_i[x,...,x,dot,...,dot]||_F^2,             (2.4)
```

with `r-q` copies of `x`.

The preceding P09 posterior arguments naturally produce sums of these quantities. The difficulty was that a crude estimate

```text
V_q(x,C) <= ||C||_op^q sigma_q^2                           (2.5)
```

keeps the *highest* variance parameter `sigma_q`, which is exactly where the bad power `d^(q/p-1/2)` enters when `q>p/2`.

The next theorem trades covariance Schatten moments for a reduction in the order of the variance parameter.

## 3. New covariance Schatten interpolation theorem

### Theorem 3.1

Let `p>=2`. For arbitrary deterministic symmetric order-`r` tensors, every `x in B_p^d`, every PSD matrix `C`, every `1<=q<=r`, and every integer `1<=s<=q`,

```text
V_q(x,C)
 <= sigma_(q-s)^2 [ Tr(C^(q/s)) ]^s.                      (3.1)
```

Together with the trivial operator-norm branch (2.5),

```text
V_q(x,C)
 <= min {
      ||C||_op^q sigma_q^2,
      min_(1<=s<=q) sigma_(q-s)^2 [Tr(C^(q/s))]^s
    }.                                                     (3.2)
```

This is an arbitrary-tensor statement: no coefficient support, block decomposition, independence, rank assumption, or interaction-degree assumption is imposed on the `T_i`.

### Proof

Diagonalize

```text
C = sum_j c_j u_j u_j^T,
```

where `c_j>=0` and the `u_j` are Euclidean orthonormal. Because `p>=2`,

```text
||u_j||_p <= ||u_j||_2 = 1,                               (3.3)
```

so every eigenvector is admissible in the supremum defining the variance parameters.

Write

```text
B_i(j_1,...,j_q)
 := T_i[x,...,x,u_(j_1),...,u_(j_q)].                      (3.4)
```

Expanding the weighted Frobenius norm in the eigenbasis gives the exact identity

```text
V_q(x,C)
 = sum_i sum_(j_1,...,j_q)
      (prod_(t=1)^q c_(j_t)) B_i(j_1,...,j_q)^2.           (3.5)
```

Fix `1<=s<=q`. For nonnegative numbers `a_1,...,a_q`, generalized AM--GM applied to the `binom(q,s)` products indexed by `s`-subsets gives

```text
prod_(t=1)^q a_t
 <= (1/binom(q,s))
    sum_(J subset [q], |J|=s) prod_(t in J) a_t^(q/s).    (3.6)
```

Indeed, the geometric mean of those `binom(q,s)` terms is exactly `prod_t a_t`, since each `a_t^(q/s)` occurs in `binom(q-1,s-1)` of them and

```text
(q/s) binom(q-1,s-1) / binom(q,s) = 1.
```

Apply (3.6) with `a_t=c_(j_t)` inside (3.5). By symmetry of each `T_i`, all `s`-subset contributions agree after summation, so it is enough to keep the first `s` indices. For fixed `j_1,...,j_s`, summing over the remaining `q-s` indices gives

```text
sum_i sum_(j_(s+1),...,j_q)
 B_i(j_1,...,j_q)^2
 = sum_i ||T_i[x^(r-q),u_(j_1),...,u_(j_s),dot^(q-s)]||_F^2
 <= sigma_(q-s)^2,                                        (3.7)
```

because `x` and all `u_(j_t)` lie in `B_p^d`.

Therefore

```text
V_q(x,C)
 <= sigma_(q-s)^2
    sum_(j_1,...,j_s) prod_(t=1)^s c_(j_t)^(q/s)
 = sigma_(q-s)^2 [sum_j c_j^(q/s)]^s
 = sigma_(q-s)^2 [Tr(C^(q/s))]^s,                         (3.8)
```

which is (3.1). The operator-norm branch follows directly from (2.4), and taking the minimum proves (3.2). QED.

### Immediate special branches

The first and last interpolation branches are

```text
V_q(x,C) <= sigma_(q-1)^2 Tr(C^q),                         (3.9)
V_q(x,C) <= sigma_0^2 (Tr C)^q.                           (3.10)
```

More importantly for `q>=2`, taking `s=q-1` yields

```text
V_q(x,C)
 <= sigma_1^2 [Tr(C^(q/(q-1)))]^(q-1).                   (3.11)
```

Thus high tensor order can be reduced all the way to the one-free-slot variance if the covariance has controlled Schatten moments.

## 4. A precise p=2 spectral-flatness route

The case `p=2` is the cleanest test because (2.3) gives

```text
sigma_1 <= C_r S.                                         (4.1)
```

Suppose a posterior increment has covariance `C` obeying

```text
||C||_op <= A/k,
Tr C <= A                                                   (4.2)
```

for some scale parameter `1<=k<=d`. For `q=1`, the operator branch gives

```text
V_1(x,C) <= (A/k) sigma_1^2.                              (4.3)
```

For `q>=2`, use (3.11) and the elementary PSD inequality

```text
Tr(C^t) <= ||C||_op^(t-1) Tr C,   t>=1.                  (4.4)
```

With `t=q/(q-1)`,

```text
[Tr(C^(q/(q-1)))]^(q-1)
 <= ||C||_op (Tr C)^(q-1)
 <= A^q/k.                                                 (4.5)
```

Hence every contraction order satisfies

```text
V_q(x,C) <= C_(r,A) S^2/k.                                (4.6)
```

This is the exact covariance profile one would want in the barycentric posterior-packing lemma from the preceding run.

### Proposition 4.1 (conditional geometric criterion for p=2)

Assume that for every dyadic `1<=k<=d` there is one common prior `P_k` and, for every `x in B_2^d`, a posterior whose process-space barycenter is `a(x)=(T_i[x^r])_i`, whose KL cost is at most

```text
K_k <= A k L                                                (4.7)
```

and whose one-slot covariance satisfies (4.2), with `L` polylogarithmic in `d,n`. Then the posterior-packing lemma gives

```text
log N(B_2^d,d_T, C_(r,A) S/sqrt(k)) <= C_(r,A) k L.       (4.8)
```

Combining these scales with the elementary Lipschitz bound

```text
d_T(x,y) <= C_r sigma_1 ||x-y||_2 <= C_r S ||x-y||_2     (4.9)
```

for the terminal range below `S/sqrt(d)`, Dudley's integral is bounded by

```text
C_(r,A) S sqrt(L) log(2d)                                 (4.10)
```

up to another harmless `sqrt(log d)` contribution from the terminal Euclidean cover. In particular, when `L=O(log d + log n)`, this has the conjectured **dimension exponent zero** for `p=2`, with only polylogarithmic loss.

### Proof of the conditional criterion

The central variance of the `r`-slot pushforward posterior is a binomial sum of `V_q(x,C)`, `q>=1`; the `q=0` term cancels exactly as in the predecessor report. Equation (4.6) therefore gives radius `C_(r,A)S/sqrt(k)`. The barycentric posterior-packing lemma turns KL `A kL` into (4.8).

For `epsilon` between `C S/sqrt(d)` and `CS`, select `k` comparable to `(S/epsilon)^2`; then

```text
log N(epsilon) <= C_(r,A) (S^2/epsilon^2) L.              (4.11)
```

Integrating `sqrt(log N)` on this interval costs at most

```text
C S sqrt(L) log(2d).                                       (4.12)
```

Below `CS/sqrt(d)`, (4.9) and the standard Euclidean covering of `B_2^d` give

```text
log N(epsilon) <= d log(1 + C_r S/epsilon),               (4.13)
```

whose entropy integral over `[0,CS/sqrt(d)]` is `O_r(S sqrt(log(2d)))`. This proves (4.10). QED.

This proposition is **conditional**. It is not a solution. Its value is that it converts the low-`p` tensor problem into a specific entropy/covariance construction problem with no hidden polynomial dimension loss.

## 5. Implement the promised head/tail posterior

The preceding report showed that the coordinate-adaptive one-scale posterior is poisoned by dense tiny coordinates. I therefore tried to encode the large coordinates and leave the tail in a bounded alphabet.

Fix `1<=k<=d` and put

```text
a := k^(-1/p).                                             (5.1)
```

For `x in B_p^d`, let `H=H_k(x)` be a set of the `k` largest coordinates in absolute value, write

```text
h := P_H x,
z := x-h.                                                   (5.2)
```

Then every tail coordinate obeys

```text
|z_j| <= a.                                                (5.3)
```

### Common prior P_k

First choose `H` uniformly among all `k`-subsets of `[d]`. Conditional on `H`:

- for `j in H`, draw independent `N(0,a^2)` coordinates;
- for `j notin H`, draw independent Rademacher coordinates `+a` or `-a`.

### Posterior Q_(x,k)

Choose `H=H_k(x)` deterministically. Conditional on that set:

- for `j in H`, draw `N(h_j,a^2)`;
- for `j notin H`, choose the sign so that

```text
P(theta_j=+a) = (1+z_j/a)/2,
P(theta_j=-a) = (1-z_j/a)/2.                              (5.4)
```

Then

```text
E_Q theta = x.                                             (5.5)
```

The covariance is diagonal and exact:

```text
C_(x,k)
 = a^2 P_H
   + sum_(j notin H) (a^2-z_j^2) e_j e_j^T.              (5.6)
```

In particular,

```text
||C_(x,k)||_op <= a^2 = k^(-2/p).                         (5.7)
```

## 6. Exact KL cost and the entropy-versus-tail-variance dichotomy

The KL cost decomposes as

```text
KL(Q_(x,k)||P_k)
 = log binom(d,k)
   + ||h||_2^2/(2a^2)
   + sum_(j notin H) phi(z_j/a),                          (6.1)
```

where

```text
phi(t)
 := KL(Bern((1+t)/2) || Bern(1/2))
  = ((1+t)/2) log(1+t) + ((1-t)/2) log(1-t).              (6.2)
```

Since `h` has at most `k` coordinates and `||h||_p<=1`,

```text
||h||_2^2 <= k^(1-2/p),
||h||_2^2/(2a^2) <= k/2.                                  (6.3)
```

Also, for `|t|<=1`, Pinsker and the chi-square upper bound give

```text
t^2/2 <= phi(t) <= t^2.                                   (6.4)
```

Therefore

```text
KL(Q_(x,k)||P_k)
 <= log binom(d,k) + k/2 + k^(2/p)||z||_2^2               (6.5)
 <= log binom(d,k) + k/2
    + k^(2/p)(d-k)^(1-2/p).                               (6.6)
```

The more important fact is not the upper bound. Let

```text
t_j := z_j/a,
e_j := phi(t_j),
v_j := (a^2-z_j^2)/a^2 = 1-t_j^2.                        (6.7)
```

From (6.4),

```text
1/2 <= e_j + v_j <= 1                                     (6.8)
```

for every tail coordinate. Summing gives the exact coarse dichotomy

```text
(d-k)/2
 <= KL_tail + a^(-2) Tr(C_tail)
 <= d-k.                                                   (6.9)
```

Thus every tail coordinate must pay in one of only two currencies: coding entropy or posterior variance.

### Countercheck: the product tail cannot realize the spectral-flatness criterion

At `p=2`, `a^2=1/k`. If `KL_tail <= B k log(2d)` and `k` is substantially smaller than `d/log d`, then (6.9) forces

```text
Tr(C_tail)
 >= (1/k)[(d-k)/2 - Bk log(2d)],                          (6.10)
```

which is of order `d/k`, not order one. Therefore the posterior has the good operator norm `O(1/k)` but the wrong trace/effective rank. By Theorem 3.1, the high-order contractions can still be large.

This formally reproduces the dense-coordinate-dust obstruction in a stronger way: for this whole product-tail family, low KL and spectrally flat covariance are incompatible at coarse scales. One cannot repair the previous argument merely by choosing a better coordinate threshold.

## 7. Tensor pushforward and the resulting covering statement

Take `r` independent slots from `Q_(x,k)` and push them through

```text
Phi(theta_1,...,theta_r)
 := (T_i[theta_1,...,theta_r])_i.                          (7.1)
```

By multilinearity and slot independence,

```text
E Phi = a_T(x) := (T_i[x^r])_i.                            (7.2)
```

The product posterior KL is `r` times (6.1). Its central second moment is exactly

```text
Delta_k(x)^2
 = sum_(q=1)^r binom(r,q) V_q(x,C_(x,k)).                 (7.3)
```

Combining (7.3) with Theorem 3.1 gives the new arbitrary-tensor bound

```text
Delta_k(x)^2
 <= sum_(q=1)^r binom(r,q)
    min {
      ||C_(x,k)||_op^q sigma_q^2,
      min_(1<=s<=q)
        sigma_(q-s)^2 [Tr(C_(x,k)^(q/s))]^s
    }.                                                     (7.4)
```

Hence, on any stratum `X subset B_p^d` on which

```text
KL(Q_(x,k)||P_k) <= K,
Delta_k(x) <= R,
```

for all `x in X`, the barycentric posterior-packing lemma from the predecessor gives

```text
N(a_T(X), ||.||_2, 2 sqrt(2) R)
 <= 4 exp(2rK).                                            (7.5)
```

Equation (7.4), not the crude Frobenius contraction, is the useful new input.

## 8. Why this is not secretly the full conjecture

If one discards all spectral information and uses only (5.7), then

```text
Delta_k(x)^2
 <= sum_(q=1)^r binom(r,q) k^(-2q/p) sigma_q^2.           (8.1)
```

Inserting the known worst-case bound (2.3) simply regenerates the old polynomial balance. In particular the `q=r` branch reproduces the same low-`p` obstruction that leads to exponent `gamma`.

If instead one tries to exploit Theorem 3.1 through trace moments, (6.9) shows why the present product-tail posterior cannot supply them at low entropy. Thus neither half of the argument is being hidden behind a new notation: the remaining gap is real and explicit.

## 9. What changed this run

**Inherited theorem.** The preceding run had an arbitrary-tensor barycentric posterior-packing lemma and variance-localized covering theorem with exact cancellation of the `q=0` process variance, but dense coordinate dust could still inflate the highest contraction.

**New theorem.** Theorem 3.1 shows that a high-order covariance-weighted contraction can be paid for with a *lower-order* tensor variance parameter and a Schatten moment of the posterior covariance. For `p=2`, Proposition 4.1 proves that a spectrally flat posterior with KL proportional to effective rank would yield the conjectured dimension exponent, up to polylogarithms.

**New failed route with exact reason.** The head/tail product posterior has the desired operator norm, but (6.9) proves an entropy-versus-trace obstruction: dense tail coordinates force either order-`d` coding cost or order-`d/k` covariance trace. This route therefore cannot provide Proposition 4.1 at coarse scales.

The full-source metric remains `gamma -> gamma`; the structural obligation ledger advances from

```text
"remove dense-dust inflation from the central variance"
```

to the sharper target

```text
"construct correlated/low-rank multiscale posterior increments with
 KL = O(k polylog(d,n)), ||C||op = O(1/k), Tr C = O(1)
 (or the corresponding Schatten-moment substitute), without product-tail dust."
```

## 10. Remaining gap and next attack

The next attack should **not** add another independent noisy coordinate to every tail location. Equation (6.9) proves that strategy structurally wrong.

The most promising next move is an **approximate-barycenter multiscale packing lemma**. At a coarse scale, encode only a `k`-complexity approximation `y` to `x` using a correlated support/subspace posterior whose covariance is rank-`O(k)` and spectrally flat; leave the residual `z=x-y` deterministic at that scale and introduce it only through the process increment at the next scale. This changes the requirement from

```text
E Theta = x at every scale
```

to

```text
||E Phi - a_T(x)||_2 <= current covering radius,
```

which should permit a posterior supported on a low-dimensional random subspace without paying for every dust coordinate.

The concrete next lemma to prove is:

> If a common prior admits posteriors with process-space barycenter error at most `eta`, KL at most `K`, and central variance at most `R^2`, then the target set has a cover at radius `eta + C R` with log-cardinality `O(K)`.

That approximate version of posterior packing is straightforward at the abstract level; the real work is then to build a correlated head/subspace posterior for tensor increments and use Theorem 3.1 to show its radius is `O(S/sqrt(k))` in the `p=2` test case before attempting general `p`.

A successful `p=2` construction would have to pass two tests simultaneously:

1. diagonal/direct-sum tensors must remain polylogarithmic rather than incur `d^(1/(2r))`;
2. flat dense vectors must avoid the product-tail identity (6.9) by correlating the residual coordinates, rather than hiding their variance in a full-rank covariance.

No closure, publication, or source-level resolution is claimed in this report.