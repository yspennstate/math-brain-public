Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 progress-first run — approximate barycentric packing and a rank-k sketch reduction

**Status: PROVED PARTIAL.** This report does **not** prove Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The full-source worst-case polynomial exponent remains

```text
gamma = 1/2 - 1/(2r)
```

rather than the conjectured

```text
alpha = 1/2 - 1/p.
```

The mathematical progress is a method pivot away from the one-shot posterior-covariance program of the preceding runs. Two new tools are proved here:

1. an **approximate-barycenter posterior-packing lemma**, which allows controlled deterministic bias and therefore permits genuinely multiscale/biased posterior constructions rather than exact barycenters at every scale;
2. at `p=2`, an **unbiased rank-k tangent-sketch packing reduction**. It converts a packing of the original tensor process into a packing of a randomly sketched process in which one tensor slot has rank at most `k`, while paying only `O(S/sqrt(k))` pointwise error. A precise sufficient condition on the *typical sketch image* would imply the conjectured dimension exponent zero at `p=2`.

The same calculation also identifies a hard obstruction: any unbiased rank-`k` linear sketch has operator norm at least `d/k` on average, so a proof that controls the sketched process only through `||R||op` necessarily reintroduces a polynomial loss. Thus the next step has to exploit typical orientation/cancellation of the sketched tensor rather than worst-case operator inflation.

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

- Regime: `2 <= p < 2r`; the new sketch theorem below is proved first at `p=2`.
- Pre-write master inspected: `802dc8a21e72520d1e0fb7343a9be46be3d3fa95`.
- Immediate P09 predecessor: `2026-09-20T040100Z__covariance-schatten-interpolation-and-head-tail-posterior.md`, blob `36d6f0af2c0a70fb6f4b71fd727a36268ca2b99f`.
- Historical C0035/successor-gate and all earlier P09 reports are preserved; no peer or historical file is edited.

## 1. Source-current baseline and the fixed metric

A bounded fresh source check on 20 September 2026 recovered the current Randomstrasse101 statement of Conjecture 16. It still asks for

```text
d^(1/2-1/p) * S,
S := (sum_i ||T_i||_sym(I_p)^2)^(1/2),
```

up to `C(r,p)` and polylogarithms, and still describes the general `p<2r` regime as blocked by the volumetric covering argument. The strongest general primary result recovered remains Aden-Ali's PAC-Bayes/contraction bound (arXiv:2503.10580), which improves the earlier geometric estimate but still depends on the higher contraction parameters. The July 2026 Lucca--Pesenti paper (arXiv:2607.07308) and the 17 September 2026 Zhou--Zhu paper (arXiv:2609.20520) sharpen sparse/independent-entry tensor norm estimates; they do not settle the arbitrary deterministic correlated-summand inequality in Conjecture 16.

Accordingly the fixed full-source metric is unchanged:

```text
old arbitrary-tensor exponent: gamma = 1/2 - 1/(2r),
new arbitrary-tensor exponent: gamma = 1/2 - 1/(2r),
target exponent:               alpha = 1/2 - 1/p.
```

This run changes the intermediate obligation: instead of trying to manufacture a single posterior covariance with simultaneously small entropy, trace and operator norm, it reduces the `p=2` covering problem to the entropy of a **typical random rank-k tangent sketch**.

## 2. Notation for the process image

For this run work first at `p=2`. Let

```text
F(x) := ( T_i[x,...,x] )_(i=1)^n in R^n,   x in B_2^d.    (2.1)
```

Then the canonical Gaussian metric is simply

```text
d_T(x,y) = ||F(x)-F(y)||_2.                               (2.2)
```

It is convenient to use the multilinear extension of each symmetric tensor. Define the one-free-slot variance

```text
sigma_1^2
 := sup_(x_1,...,x_(r-1) in B_2^d)
    sum_i ||T_i[x_1,...,x_(r-1),dot]||_2^2.               (2.3)
```

Polarization gives, for a constant depending only on `r`,

```text
sigma_1 <= C_r S,                                          (2.4)
```

because for each `i` the full multilinear injective norm is at most `C_r` times the symmetric injective norm.

For fixed `x`, define the linear tangent/slice map

```text
A_x : R^d -> R^n,
(A_x u)_i := T_i[x,...,x,u],                               (2.5)
```

with `r-1` copies of `x`. Then

```text
F(x) = A_x x,
||A_x||_HS^2 <= sigma_1^2.                                (2.6)
```

The second identity is the key point: although the tensor process is nonlinear in `x`, each one-slot tangent slice is a Hilbert--Schmidt operator with dimension-free squared mass after normalization by `S`.

## 3. New lemma I — approximate-barycenter posterior packing

The predecessor report used an exact-barycenter version. The following biased form is what is actually needed for a multiscale construction.

### Lemma 3.1 (approximate-barycenter packing)

Let `H` be a real Hilbert space and `T subset H`. Let `P` be a probability measure on `H`. Suppose that for every `t in T` there is a probability measure `Q_t << P` with

```text
KL(Q_t || P) <= K,                                         (3.1)
```

mean

```text
m_t := E_(Y~Q_t) Y                                         (3.2)
```

satisfying

```text
||m_t - t|| <= delta,                                      (3.3)
```

and central second moment

```text
E_(Y~Q_t) ||Y-m_t||^2 <= R^2.                             (3.4)
```

Then the packing number satisfies

```text
M(T, 2 delta + 2 sqrt(2) R) <= 4 exp(2K).                 (3.5)
```

Consequently the same bound, up to the usual factor-two conversion, holds for covering numbers.

### Proof

Take a finite subset `{t_1,...,t_M}` whose pairwise distances are strictly larger than

```text
2 delta + 2 sqrt(2) R.                                    (3.6)
```

Write `m_j=m_(t_j)` and let

```text
B_j := { y : ||y-m_j|| <= sqrt(2)R }.                     (3.7)
```

By (3.3),

```text
||m_j-m_l||
 >= ||t_j-t_l|| - ||m_j-t_j|| - ||m_l-t_l||
 > 2 sqrt(2) R,                                            (3.8)
```

so the balls `B_j` are pairwise disjoint.

By Markov's inequality and (3.4),

```text
Q_(t_j)(B_j) >= 1/2.                                      (3.9)
```

Let `p_j=P(B_j)` and `q_j=Q_(t_j)(B_j)`. Data processing of relative entropy under the map `1_(B_j)` gives

```text
K >= KL(Q_(t_j)||P)
  >= q_j log(q_j/p_j) + (1-q_j)log((1-q_j)/(1-p_j)).      (3.10)
```

Using `q_j>=1/2`, the binary entropy bound `h(q_j)<=log 2`, and `-log(1-p_j)>=0`,

```text
K >= (1/2) log(1/p_j) - log 2.                            (3.11)
```

Hence

```text
p_j >= (1/4) exp(-2K).                                    (3.12)
```

The `B_j` are disjoint, so `sum_j p_j<=1`; therefore

```text
M <= 4 exp(2K).                                            (3.13)
```

This proves (3.5). QED.

### Why this is a real change from the predecessor lemma

Exact barycenters forced the posterior to reproduce `F(x)` at every scale and made low-rank/support truncation difficult: a coarse posterior had to encode every tiny coordinate immediately. Lemma 3.1 allows a scale-dependent deterministic bias `delta`. A future chain can therefore encode only a coarse approximation to the process point and postpone the residual until the scale at which it matters.

The lemma alone does not solve the construction problem, but it removes an unnecessary exactness requirement from it.

## 4. New lemma II — a random-approximation packing transfer

The next lemma is independent of KL and is useful when one has an unbiased random sketch of each process point.

### Lemma 4.1 (random approximation transfers packings)

Let `F:X->H` and let `Y_omega:X->H` be a random family. Suppose

```text
E_omega ||Y_omega(x)-F(x)||^2 <= rho^2                  (4.1)
```

for every `x in X`. Then for every `a>1` and every `Delta>2a rho`,

```text
M(F(X), Delta)
 <= [1/(1-a^(-2))]
    sup_omega M(Y_omega(X), Delta-2a rho).                (4.2)
```

A version with an additional high-probability event `E` is also valid: if `P(E^c)<=eta`, replace the prefactor denominator by `1-a^(-2)-eta`, provided it is positive, and take the supremum only over `omega in E`.

### Proof

Let `x_1,...,x_M` realize a `Delta`-packing of `F(X)`. For each `j`, Markov gives

```text
P( ||Y_omega(x_j)-F(x_j)|| <= a rho ) >= 1-a^(-2).       (4.3)
```

Thus the expected number of good indices is at least `(1-a^(-2))M`, so for some realization `omega` at least that many are good. For two good indices,

```text
||Y_omega(x_j)-Y_omega(x_l)||
 >= ||F(x_j)-F(x_l)|| - 2a rho
 > Delta-2a rho.                                          (4.4)
```

Hence those good points form a `(Delta-2a rho)`-packing of `Y_omega(X)`. This gives (4.2). The event-restricted version follows from

```text
P(good_j and E) >= 1-a^(-2)-eta.                         (4.5)
```

QED.

This elementary lemma is the bridge that lets us use a random low-rank sketch without requiring a single sketch to approximate **all** points uniformly.

## 5. New theorem — unbiased rank-k tangent sketch at p=2

Let `1<=k<=d`. Draw independent standard Gaussian vectors

```text
z_1,...,z_k ~ N(0,I_d)                                   (5.1)
```

and define the sample-covariance sketch

```text
R_k := (1/k) sum_(a=1)^k z_a z_a^T.                       (5.2)
```

Then `R_k` is positive semidefinite, `rank(R_k)<=k`, and

```text
E R_k = I_d.                                               (5.3)
```

Define the sketched tensor-process map

```text
Y_R(x)
 := ( T_i[x,...,x,Rx] )_(i=1)^n
  = A_x R x.                                               (5.4)
```

There are `r-1` unsketched copies of `x` and one sketched slot.

### Theorem 5.1 (pointwise dimension-free tangent-sketch error)

For every `x in B_2^d`,

```text
E_R Y_R(x) = F(x),                                        (5.5)
```

and

```text
E_R ||Y_R(x)-F(x)||_2^2
 <= (2/k) sigma_1^2
 <= C_r S^2/k.                                             (5.6)
```

### Proof

Unbiasedness is immediate from `E R=I` and linearity of the last tensor slot.

For the second moment, put

```text
w_a := z_a (z_a^T x).                                     (5.7)
```

Then `R_k x = k^(-1) sum_a w_a` and `E w_a=x`. Wick's formula gives

```text
E[w_a w_a^T]
 = ||x||_2^2 I + 2xx^T,                                   (5.8)
```

so

```text
Cov((R_k-I)x)
 = (1/k)( ||x||_2^2 I + xx^T )
 =: C_x.                                                   (5.9)
```

For `||x||_2<=1`,

```text
||C_x||_op <= 2/k.                                        (5.10)
```

Using `Y_R(x)-F(x)=A_x(R-I)x`,

```text
E ||Y_R(x)-F(x)||_2^2
 = Tr(A_x^* A_x C_x)
 <= ||C_x||_op ||A_x||_HS^2
 <= (2/k) sigma_1^2.                                      (5.11)
```

Equation (2.4) gives the final source-normalized estimate. QED.

### Interpretation

The important point is what **does not** appear in (5.6): no Frobenius norm of the order-`r` coefficient tensors and no factor `d^(r-1)`. The sketch only perturbs one tensor slot, so the error is governed by the one-free-slot variance `sigma_1`, which at `p=2` is bounded by `C_r S`.

This is the first calculation in this line that gets the desired `S/sqrt(k)` scale from an actual rank-`k` object for arbitrary deterministic tensors.

## 6. A packing reduction to a typical rank-k sketch image

Apply Lemma 4.1 with

```text
rho = sqrt(2) sigma_1/sqrt(k).                            (6.1)
```

Taking a fixed numerical threshold (constants are inessential), Theorem 5.1 gives the following.

### Corollary 6.1 (typical-sketch entropy suffices)

Suppose that for some `L>=1`, with probability at least `7/8` over `R_k`,

```text
log M(
  Y_(R_k)(B_2^d),
  8 sigma_1/sqrt(k)
) <= C k L.                                                (6.2)
```

Then

```text
log M(
  F(B_2^d),
  16 sigma_1/sqrt(k)
) <= C' k L.                                               (6.3)
```

for a universal change of constants.

### Proof

For each packing point, (5.6) and Markov show that

```text
P( ||Y_R(x)-F(x)|| <= 4 sigma_1/sqrt(k) ) >= 7/8.         (6.4)
```

Intersecting with the event (6.2) leaves probability at least `3/4` for each fixed packing point. Averaging over the packing points, some realization satisfying (6.2) is simultaneously good for at least `3/4` of them. A `16 sigma_1/sqrt(k)` separation in `F` then becomes an `8 sigma_1/sqrt(k)` separation in the sketch image. Thus

```text
(3/4) M_F <= exp(CkL),                                    (6.5)
```

which is (6.3) after changing constants. QED.

### Corollary 6.2 (conditional closure criterion for p=2)

If there is a polylogarithmic `L=L(d,n)` such that (6.2) holds for every dyadic `1<=k<=d`, then

```text
E ||sum_i g_i T_i||_sym(I_2)
 <= C_r S [ sqrt(L) log(2d) + sqrt(log(2d)) ].             (6.6)
```

In particular this has the Conjecture-16 **dimension exponent zero** at `p=2`.

### Proof

By (2.4), (6.3) gives, at radii `epsilon` comparable to `S/sqrt(k)`,

```text
log N(F(B_2^d), epsilon)
 <= C_r L S^2/epsilon^2                                   (6.7)
```

for the range `C_r S/sqrt(d) <= epsilon <= C_r S`.

For the terminal range below `S/sqrt(d)`, polarization gives the deterministic Euclidean Lipschitz bound

```text
d_T(x,y) <= C_r S ||x-y||_2,                              (6.8)
```

and hence

```text
log N(F(B_2^d),epsilon)
 <= d log(1 + C_r S/epsilon).                             (6.9)
```

Dudley's integral of (6.7) over `[S/sqrt(d),S]` is

```text
O_r( S sqrt(L) log(2d) ),                                 (6.10)
```

while the integral of (6.9) over `[0,S/sqrt(d)]` is

```text
O_r( S sqrt(log(2d)) ).                                   (6.11)
```

This proves (6.6). QED.

This is **conditional**, because the typical-sketch image estimate (6.2) is not yet proved for arbitrary tensors. But it is a materially different reduction from the earlier posterior covariance criterion: the missing object is now a concrete random rank-`k` polynomial image.

## 7. Counterexample to the naive way of proving the sketch criterion

A tempting next step would be to say that `R_k` has rank `k`, bound its operator norm, and then estimate

```text
||T[x^(r-1),R_k x]||
 <= ||R_k||_op * ||T||_inj.                               (7.1)
```

That route cannot close the conjecture.

### Proposition 7.1 (unbiased low-rank sketches must inflate in operator norm)

Let `R` be a random symmetric matrix such that

```text
rank(R) <= k almost surely,
E R = I_d.                                                 (7.2)
```

Then

```text
E ||R||_op >= d/k.                                        (7.3)
```

If `R` is positive semidefinite, the proof is immediate from `Tr R <= k||R||op`; for a general symmetric rank-`k` matrix use `|Tr R|<=k||R||op` and Jensen:

```text
d = Tr(E R) = E Tr R
  <= E |Tr R|
  <= k E ||R||op.                                         (7.4)
```

For the Gaussian sample covariance (5.2), this scale is also typical: when `k<<d`, its largest eigenvalue is of order `d/k`.

Thus a proof of (6.2) that first replaces `R_k` by the worst-case scalar `||R_k||op` pays at least `d/k` and destroys the desired `S/sqrt(k)` scale. The sketch reduction therefore isolates a sharper version of the volumetric obstruction:

> **Pointwise, random orientation gives error `S/sqrt(k)`; uniformly, the same rank-k sketch has operator inflation `d/k`. The missing theorem has to preserve the former without collapsing to the latter.**

This also explains why the previous covariance approach repeatedly encountered trace/operator tradeoffs: they are different manifestations of the same average-versus-uniform geometry.

## 8. Relation to the preceding covariance-Schatten theorem

The prior report proved that weighted `q`-slot contraction energies can be interpolated against lower-order variance parameters through Schatten moments of the covariance. The present one-slot sketch uses the strongest possible instance of that philosophy: there is only one perturbed slot, so **no `q>=2` covariance term is created at all** in the pointwise error. The error is exactly

```text
Tr(A_x^* A_x C_x),                                        (8.1)
```

and the operator bound on `C_x` immediately lands on `sigma_1`.

The price is transferred from variance to **image entropy** of `x -> A_x R_k x`. This is preferable because the entropy question retains the random orientation of `R_k`; replacing it by deterministic covariance moments too early is exactly what the counterexample in Section 7 warns against.

The approximate-barycenter Lemma 3.1 remains relevant if the next sketch is biased (for example, a Haar projection of operator norm one rather than an unbiased rescaling). It allows a future multiscale chain to tolerate that bias at the radius at which it is introduced.

## 9. What is proved, what failed, and what remains

### Proved in this run

1. **Approximate-barycenter posterior packing**: exact barycenters are unnecessary; deterministic bias and posterior variance add linearly at the packing radius.
2. **Random-approximation packing transfer**: pointwise mean-square approximation suffices to transfer a constant fraction of any packing to one realization of the random approximation.
3. **Unbiased rank-k tangent sketch** for arbitrary deterministic symmetric tensors at `p=2`, with pointwise mean-square error `O_r(S^2/k)`.
4. **Typical-sketch entropy criterion**: an `exp(O(k polylog))` packing bound for the random sketch image at scale `S/sqrt(k)` would imply the full conjectured `p=2` dimension exponent.
5. **Low-rank operator-inflation obstruction**: every unbiased rank-`k` linear sketch has expected operator norm at least `d/k`, so the sketch criterion cannot be proved by a crude operator-norm reduction.

### Failed route ruled out

The natural proof

```text
rank k -> ||R||op control -> injective norm control
```

is quantitatively incompatible with the target because unbiasedness forces `||R||op` to carry a `d/k` scale. This is now a theorem, not a heuristic warning.

### Full-source gap

The arbitrary-tensor exponent has **not** moved. The missing statement is now the following concrete entropy problem.

> For `R_k=(1/k)ZZ^T`, prove with constant probability that the homogeneous image
>
> ```text
> { (T_i[x^(r-1),R_k x])_i : ||x||_2<=1 }
> ```
>
> has packing entropy `O_r(k polylog(d,n))` at radius `C_r S/sqrt(k)`, **without replacing `R_k` by `||R_k||op`**.

A proof may use cancellation in the random orientation of `range(R_k)`, a light/heavy decomposition of the `R_k`-slice, or a conditional chaining argument over `x` after the sketch is fixed.

## 10. Next attack

The next run should attack the typical-sketch entropy statement directly, not return to the discarded global-covariance construction.

The first three tests are:

1. **Rank-one witness.** Derive the sketch-image entropy exactly for `T_i=a_i v_i^(tensor r)` and confirm that no `d/k` loss is intrinsic there. This calibrates the correct dependence on the random overlaps `v_i^T R_k x`.
2. **Light/heavy decomposition of `R_k x`.** Inspired by the recent sparse-tensor work, split the sketch image according to leverage of `x` onto the `k` random directions and prove an entropy bound for the light part using the pointwise `sigma_1` energy rather than `||R_k||op`.
3. **Counterexample search for (6.2).** Before relying on the criterion, test whether a tensor family can force the typical sketch image to have entropy `exp(omega(k polylog d))` at radius `S/sqrt(k)`. A counterexample to (6.2) would not refute Conjecture 16; it would show that the one-slot sketch reduction still needs an additional multiscale decomposition.

If the typical-sketch criterion survives these tests, the next proof target is a conditional chaining inequality on `range(R_k)` that uses random orientation and the one-slot Hilbert-Schmidt energy before any operator-norm bound is taken.

## 11. Claim discipline

- `PROVED PARTIAL`, not a full solution.
- No known matrix, independent-entry, rank-one, sparse-entry, or `p>=2r` result is relabeled as new.
- The July and September 2026 independent/sparse-entry papers are treated as stronger structured primary results, not as resolution of arbitrary deterministic correlated summands.
- The full arbitrary-tensor dimension exponent remains unchanged.
- No publication-level independent audit is claimed or required before continuing research.
