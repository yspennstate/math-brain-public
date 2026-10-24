Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 progress-first run — the global rank-k sketch entropy route is false, and an adaptive ridge skeleton replaces it

**Status: PROVED PARTIAL.** This report does **not** solve Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The full-source worst-case exponent remains

```text
gamma = 1/2 - 1/(2r)
```

instead of the conjectured

```text
alpha = 1/2 - 1/p.
```

The mathematical progress in this run is a decisive method correction plus a stronger deterministic replacement.

1. The critical **global Haar-sketch image entropy hypothesis** proposed in the preceding report is false, already for `p=2` and every fixed tensor order `r>=3`. I give an explicit symmetric tensor family with `S=(sum_i ||T_i||_I_2^2)^(1/2) asy_r 1` for which the true process image has Euclidean diameter `O(d^(-1/2))`, but with probability strictly greater than `1/4` a single unbiased Haar rank-one tangent sketch has an `exp(c d)` packing at a fixed positive scale. Thus the noisy sketch image can be exponentially more complicated than the process it was meant to approximate. The conditional implication in the predecessor remains logically correct, but its proposed entropy hypothesis cannot hold uniformly.

2. The failure is not a failure of low-rank approximation itself; it is a failure of using one **global, x-independent random sketch** and then trying to bound the entire noisy image. I prove an anchored-subspace version of the Haar tangent-sketch lemma whose error depends only on the Euclidean residual outside the anchor.

3. More importantly, I replace the random sketch by a **deterministic adaptive spectral/ridge skeleton**. At every `x`, the tangent map has Hilbert--Schmidt mass `O_r(S)`. A ridge leverage operator of effective dimension at most `k` therefore approximates the actual process point `F(x)` at the exact source-critical scale

```text
C_r d^(1/2-1/p) S / sqrt(k)
```

for every `p>=2`, with no random-sketch noise and no global unbiasedness requirement. The full conjectured exponent is reduced to the entropy of this adaptive effective-rank skeleton.

This is a materially different route from the failed one-scale PAC-Bayes and global rank-`k` sketch approaches. The next bottleneck is no longer pointwise variance; it is the complexity of the **data-dependent high-singular-value tangent directions**.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Installed title: `Gaussian Tensor Bounds`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac, A. Rodder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.
- Primary general comparison: A. S. Bandeira, S. Gopi, H. Jiang, K. Lucca, T. Rothvoss, *A Geometric Perspective on the Injective Norm of Sums of Random Tensors*, arXiv:2411.10633 / STOC 2025.
- Stronger present general variance-parameter comparison recovered: I. Aden-Ali, *On the Injective Norm of Sums of Random Tensors and the Moments of Gaussian Chaoses*, arXiv:2503.10580.
- Source norm:

```text
||T||_I_p = sup_{||x_1||_p,...,||x_r||_p <= 1}
            |T[x_1,...,x_r]|.
```

For symmetric tensors this is equivalent, up to an `r`-dependent factor (and exactly for `p=2`), to the diagonal/symmetric norm used below.

- Source target:

```text
E ||sum_i g_i T_i||_I_p
 <= polylog(d,n) C(r,p) d^(1/2-1/p)
    (sum_i ||T_i||_I_p^2)^(1/2).
```

- Regime: `2 <= p < 2r`, beyond established matrix, rank-one, independent/sparse-entry, and `p>=2r` cases.
- Pre-write master inspected: `509710122c6162b1fe37985cdb555176a5962012`.
- Immediate P09 predecessor: `2026-09-20T055900Z__all-p-rank-k-sketch-and-minimax-barrier.md`, creation commit `7f7bc786ee1bcb34b1c3d35a3f3b0f9565c51a5b`, blob `cec68e1c3f96619680cda040cad4af849d57e041`.
- Historical C0035/successor-gate material and all earlier P09 reports remain preserved. No peer or historical file is edited.

## 1. Source-current baseline and inherited theorem

A bounded fresh source check on 20 September 2026 found the Randomstrasse101 source still stating Conjecture 16 in the above form. BGJLR's type-2 theorem gives polynomial exponent

```text
1/2 - 1/max{p,2r},
```

up to logarithms, hence `gamma=1/2-1/(2r)` in the unresolved range `p<2r`. Their geometric argument is explicitly volumetric. Aden-Ali's PAC-Bayes bound improves the variance-parameter estimate, notably removing one logarithm from the first contraction term, but still retains higher-contraction/Frobenius-type losses in the arbitrary low-`p` regime and does not establish the conjectured type-2 exponent there.

Accordingly the fixed source metric is unchanged:

```text
old arbitrary-tensor exponent: gamma = 1/2 - 1/(2r),
new arbitrary-tensor exponent: gamma = 1/2 - 1/(2r),
target exponent:               alpha = 1/2 - 1/p.
```

The predecessor proved the following useful pointwise fact. Write `B_i` for the symmetric multilinear form associated to `T_i`, put

```text
S^2 := sum_i ||T_i||_I_p^2,
F(x) := (B_i(x,...,x))_i,
(A_x u)_i := B_i(x,...,x,u),
```

with `r-1` copies of `x` in the tangent map. Real polarization gives, with `c_r=r^r/r!`,

```text
||A_x||_HS <= c_r S                                      (1.1)
```

for every `x in B_p^d` and every `p>=2`. A Haar rank-`k` unbiased map `R_k=(d/k)P_E` then satisfies

```text
E ||A_x R_k x - F(x)||_2^2
 <= C_r d^(1-2/p) S^2/k.                                 (1.2)
```

The predecessor proposed the sufficient hypothesis

```text
log M(Y_k(B_p^d), c d^alpha S/sqrt(k))
 <= C_r k polylog(d,n),                                  (1.3)

Y_k(x):=A_x R_k x,
```

with probability at least `3/4`, and proved that (1.3) would imply the conjectured polynomial exponent.

The first job of the present run was to attack (1.3), rather than build more machinery on top of it.

## 2. Counterexample: the global critical-sketch entropy hypothesis is false

The next theorem is an obstruction to the **method**, not to Conjecture 16.

### Theorem 2.1 (rank-one global sketch creates spurious exponential entropy)

Fix an integer `r>=2`. For every sufficiently large `d` there exist symmetric order-`r` tensors

```text
T_1,...,T_d in (R^d)^(tensor r)
```

such that

```text
S^2 := sum_(j=1)^d ||T_j||_I_2^2 asy_r 1,                (2.1)
```

and the true process image satisfies

```text
F(B_2^d) subset d^(-1/2) B_2^d.                          (2.2)
```

Nevertheless, if `E` is a Haar-uniform one-dimensional subspace, `P_E` its orthogonal projection, and

```text
R_1 := d P_E,
Y_E(x) := A_x R_1 x,                                      (2.3)
```

then there are constants `eta_r,c>0`, depending only on `r`, such that

```text
P_E[ log M(Y_E(B_2^d), eta_r) >= c d ] > 1/4              (2.4)
```

for all sufficiently large `d`.

Consequently, for this family there is **no** fixed polylogarithmic `L(d,d)` for which the predecessor's global-image estimate

```text
log M(Y_E(B_2^d), c_r' S) <= C_r L(d,d)                   (2.5)
```

can hold with probability at least `3/4` at every sufficiently small fixed critical-scale constant `c_r'>0`.

The theorem applies in particular to every `r>=3`, where `p=2<2r` lies in the genuinely unresolved tensor regime.

### Proof

Fix a unit vector `b in R^d`; for concreteness take `b=e_1`. For `j=1,...,d` define the homogeneous polynomial

```text
P_j(z) := d^(-1/2) z_j (b^T z)^(r-1).                    (2.6)
```

Let `T_j` be the unique symmetric order-`r` tensor associated to `P_j`.

#### Step 1: source normalization is constant

For `p=2`, Banach's theorem for symmetric multilinear forms identifies the Euclidean injective norm with the diagonal polynomial norm. Hence

```text
||T_j||_I_2
 = sup_{||z||_2<=1} |P_j(z)|
 <= d^(-1/2).                                              (2.7)
```

For `j>=2`, because `b=e_1` is orthogonal to `e_j`, the exact two-coordinate maximization gives

```text
sup_{a^2+t^2<=1} t a^(r-1)
 = m_r,

m_r := r^(-1/2) ((r-1)/r)^((r-1)/2).                     (2.8)
```

Therefore

```text
S^2
 = d^(-1) [1 + (d-1)m_r^2],                              (2.9)
```

so for `d>=2`,

```text
m_r/sqrt(2) <= S <= 1.                                    (2.10)
```

Thus the source normalization is genuinely of constant order; no hidden vanishing `S` is being used.

#### Step 2: the true image is tiny

The process feature map is explicit:

```text
F(x)
 = (P_j(x))_(j=1)^d
 = d^(-1/2) (b^T x)^(r-1) x.                              (2.11)
```

Hence for `||x||_2<=1`,

```text
||F(x)||_2 <= d^(-1/2),                                   (2.12)
```

which proves (2.2). In particular, the actual process image has diameter at most `2/sqrt(d)`.

#### Step 3: exact tangent formula

The symmetric multilinear form associated to (2.6) is

```text
B_j(z_1,...,z_r)
 = [1/(r sqrt(d))]
   sum_(m=1)^r (z_m)_j prod_(ell != m) (b^T z_ell).       (2.13)
```

Therefore, if

```text
beta := b^T x,
tau  := b^T R_1 x,                                        (2.14)
```

then

```text
Y_E(x)
 = [1/(r sqrt(d))]
   [ beta^(r-1) R_1 x
     + (r-1) tau beta^(r-2) x ].                          (2.15)
```

The second term is the source of the artificial entropy: one random scalar `tau` multiplies a full `(d-1)`-dimensional family of `x`'s.

#### Step 4: choose a high-dimensional affine sphere on which beta and tau are fixed

Choose a unit vector `e` spanning `E`, oriented so that

```text
a := b^T e >= 0.                                          (2.16)
```

Put

```text
c := sqrt(1-a^2),
f := (b-ae)/c in E^perp                                   (2.17)
```

whenever `c>0`. Thus

```text
b = a e + c f.                                             (2.18)
```

Set

```text
x_0 := (e+f)/4,                                            (2.19)
W   := E^perp intersect f^perp.                            (2.20)
```

Then `dim W=d-2`, and because `b in span{e,f}`, every `y in W` is orthogonal to `b`. For any

```text
y in W,  ||y||_2=1/2,
x := x_0+y,                                                (2.21)
```

we have

```text
||x||_2^2 = 1/8 + 1/4 = 3/8 < 1,                         (2.22)
```

so `x in B_2^d`, while

```text
beta = b^T x = (a+c)/4,                                   (2.23)
R_1 x = (d/4)e,
tau = b^T R_1 x = (d/4)a.                                (2.24)
```

Both `beta` and `tau` are constant as `y` varies on the sphere in `W`.

Let `Q_W` denote orthogonal projection onto `W`. Since `Q_W R_1 x=0` and `Q_W x=y`, (2.15) gives the exact identity

```text
Q_W Y_E(x)
 = lambda_E y,                                             (2.25)

lambda_E
 := [(r-1)/(r sqrt(d))] tau beta^(r-2).                   (2.26)
```

Thus a high-dimensional Euclidean sphere is copied linearly into the sketch image whenever `lambda_E` is bounded below.

#### Step 5: this happens with probability > 1/4

For a Haar random line, the random variable

```text
X := a^2 = ||P_E b||_2^2                                  (2.27)
```

satisfies the exact moments

```text
E X   = 1/d,
E X^2 = 3/[d(d+2)].                                       (2.28)
```

Take `theta=1/100`. Paley--Zygmund gives

```text
P(X >= theta/d)
 >= (1-theta)^2 (E X)^2 / E X^2
 = (1-theta)^2 (d+2)/(3d).                               (2.29)
```

Markov gives

```text
P(X > 1/2) <= 2/d.                                        (2.30)
```

Therefore, for `d>=18`,

```text
P(theta/d <= X <= 1/2)
 >= (0.99)^2 (d+2)/(3d) - 2/d
 > 1/4.                                                    (2.31)
```

On this event,

```text
a >= 1/(10 sqrt(d)),
c >= 1/sqrt(2),
beta >= 1/(4 sqrt(2)),
tau >= sqrt(d)/40.                                        (2.32)
```

Hence

```text
lambda_E
 >= [(r-1)/(40 r)] (1/(4 sqrt(2)))^(r-2)
 =: lambda_r > 0.                                         (2.33)
```

The lower bound depends only on the fixed tensor order `r`.

#### Step 6: exponential packing

Let `m=d-2` and choose an orthonormal basis `w_1,...,w_m` of `W`. A standard binary coding argument supplies a set

```text
C subset {+-1}^m,
|C| >= exp(c m),                                           (2.34)
```

with pairwise Hamming distance at least `m/4`. Define

```text
y_eps := (1/(2 sqrt(m))) sum_(j=1)^m eps_j w_j.           (2.35)
```

Then `||y_eps||_2=1/2` and for distinct codewords

```text
||y_eps-y_eps'||_2 >= 1/2.                                (2.36)
```

By (2.25) and (2.33), on the event in (2.31),

```text
||Y_E(x_0+y_eps)-Y_E(x_0+y_eps')||_2
 >= ||Q_W(Y_E(x_0+y_eps)-Y_E(x_0+y_eps'))||_2
 >= lambda_r/2.                                            (2.37)
```

Therefore

```text
log M(Y_E(B_2^d), lambda_r/4)
 >= c(d-2).                                                (2.38)
```

with probability greater than `1/4`. This proves (2.4).

Finally, in the predecessor's notation `A=c_r d^alpha S`, and here `alpha=0` and `S<=1`. Thus for every sufficiently small fixed constant `c_r'` the radius `c_r' A` is below `lambda_r/4`. Since a fixed-degree polylogarithm is `o(d)`, (2.38) contradicts the proposed `O(polylog(d))` entropy bound for `k=1` on an event of probability greater than `1/4`. Therefore such a low-entropy event cannot have probability at least `3/4` for all large `d`. QED.

### What this counterexample means

The true process image in this example is microscopic: radius `d^(-1/2)`. The global rank-one sketch image, however, contains an exponentially large packing at **constant** scale with positive probability. The sketch has created complexity that is not present in `F(B_2^d)`.

This explains why the predecessor's pointwise mean-square estimate, despite being sharp, was the wrong object on which to impose a uniform entropy bound. A single sketch is selected first; the supremum over `x` can then align with its noise. The fixed-`x` variance estimate does not control that adaptive overfitting.

This also clarifies why the matrix calibration from the predecessor was insufficient as a counterexample test: one scalar matrix example had large diameter but low entropy. The family (2.6) instead has **large entropy generated entirely by sketch noise**, while the original process remains tiny.

## 3. Anchored Haar sketches localize the noise to the unexplained residual

The global route fails because it sketches the entire vector `x`, including directions that should have been treated as already understood. The following exact lemma shows how anchoring removes that defect.

### Lemma 3.1 (anchored-subspace tangent sketch)

Let `V <= R^d` be any fixed subspace of dimension `m<d`. Put

```text
D := d-m.
```

Choose `1<=q<=D`, draw a Haar-uniform `q`-dimensional subspace `H <= V^perp`, and define

```text
R_(V,q)
 := P_V + (D/q) P_H.                                      (3.1)
```

Then

```text
rank(R_(V,q)) <= m+q,
E R_(V,q) = I_d.                                           (3.2)
```

For every `p>=2`, every `x in B_p^d`, and every P09 tensor family,

```text
E || A_x R_(V,q) x - F(x) ||_2^2
 <= 2 c_r^2 S^2 ||P_(V^perp)x||_2^2 / q.                 (3.3)
```

In particular, if a cell of the parameter space is known to satisfy

```text
||P_(V^perp)x||_2 <= delta,                                (3.4)
```

then its tangent-sketch RMS error is only

```text
C_r S delta / sqrt(q),                                    (3.5)
```

not the global `C_r d^alpha S/sqrt(q)` scale.

#### Proof

Because a Haar `q`-plane in the `D`-dimensional space `V^perp` has mean projection `(q/D)P_(V^perp)`, (3.2) is immediate.

Write

```text
z := P_(V^perp)x.                                          (3.6)
```

The anchored map fixes the `V` component exactly, so

```text
(R_(V,q)-I)x
 = [(D/q)P_H - P_(V^perp)] z.                             (3.7)
```

The rank-`q` Haar covariance calculation from the predecessor, now performed in dimension `D`, gives

```text
|| E[(R_(V,q)-I)x ((R_(V,q)-I)x)^T] ||_op
 <= 2 ||z||_2^2/q.                                        (3.8)
```

Therefore, using `||A_x||_HS<=c_r S`,

```text
E ||A_x(R_(V,q)-I)x||_2^2
 <= [2||z||_2^2/q] ||A_x||_HS^2
 <= 2 c_r^2 S^2 ||z||_2^2/q.                             (3.9)
```

QED.

### Calibration on the counterexample

The obstruction family (2.6) has one distinguished direction `b`. Anchor it:

```text
V := span{b},
q := 1.                                                    (3.10)
```

Then `R_(V,1)` fixes `b`, hence

```text
b^T R_(V,1) x = b^T x = beta.                             (3.11)
```

Equation (2.15) becomes

```text
Y_V(x)
 = beta^(r-1)/(r sqrt(d))
   [ R_(V,1)x + (r-1)x ].                                 (3.12)
```

Let `U=V+H`, which has dimension at most two. On `U^perp`,

```text
P_(U^perp)Y_V(x)
 = [(r-1)/(r sqrt(d))] beta^(r-1) P_(U^perp)x,            (3.13)
```

so the entire high-dimensional component now has radius `O_r(d^(-1/2))`. The remaining component lies in the fixed two-dimensional space `U`; even though its radius can be `O(sqrt(d))`, its constant-scale covering entropy is only `O_r(log d)`.

Thus the same family that destroys the **global** Haar-sketch entropy hypothesis is benign after anchoring its dangerous direction. This is not a proof for arbitrary tensors, but it identifies the correct qualitative repair: dangerous high-gain directions must be absorbed into a local/adaptive anchor before random compression is applied to the residual.

## 4. Deterministic adaptive spectral truncation reaches the critical scale

The anchored lemma still leaves the problem of choosing `V`. There is, however, a canonical pointwise choice that needs no randomness.

### Lemma 4.1 (adaptive top-k tangent skeleton)

For `x in B_p^d`, let

```text
s_1(x) >= s_2(x) >= ... >= 0                              (4.1)
```

be the singular values of the tangent map `A_x`. Let `V_x(k)` be the span of its top `k` right singular vectors and `P_x(k)` the corresponding orthogonal projection. Define

```text
Z_k^hard(x) := A_x P_x(k) x.                              (4.2)
```

Then for every `1<=k<d`,

```text
||F(x)-Z_k^hard(x)||_2
 <= c_r S ||x||_2/sqrt(k+1)
 <= c_r d^alpha S/sqrt(k+1).                              (4.3)
```

#### Proof

By (1.1),

```text
sum_j s_j(x)^2 = ||A_x||_HS^2 <= c_r^2 S^2.              (4.4)
```

Hence

```text
s_(k+1)(x) <= c_r S/sqrt(k+1).                            (4.5)
```

On `V_x(k)^perp`, the operator norm of `A_x` is exactly `s_(k+1)(x)`. Therefore

```text
||A_x(I-P_x(k))x||_2
 <= s_(k+1)(x)||x||_2,                                    (4.6)
```

which gives (4.3). QED.

### Interpretation

The global random sketch achieved the correct approximation scale only **in mean square for each fixed x**, and the supremum could overfit the sketch noise. Lemma 4.1 achieves the same polynomial scale **deterministically and simultaneously pointwise**, because the compression subspace is allowed to depend on the local tangent geometry.

The remaining issue is now clean: how complicated can the family of top-`k` tangent directions be as `x` moves through `B_p^d`?

Hard spectral cutoffs can jump when singular values cross. The next lemma replaces them by a smooth ridge filter while retaining effective dimension `k`.

## 5. A smooth ridge-leverage skeleton with effective dimension at most k

### Theorem 5.1 (adaptive ridge skeleton)

For `x in B_p^d`, set

```text
M_x := A_x^* A_x.                                         (5.1)
```

Fix `1<=k<=d` and define

```text
tau := c_r S/sqrt(k),                                      (5.2)
G_(x,k)
 := M_x (M_x + tau^2 I)^(-1),                             (5.3)
Z_k(x)
 := A_x G_(x,k) x.                                        (5.4)
```

If `S=0`, the result is trivial and we set `G_(x,k)=0`. Otherwise:

1. `G_(x,k)` is positive semidefinite and `0 <= G_(x,k) <= I`.
2. Its effective dimension satisfies

```text
Tr G_(x,k) <= k.                                           (5.5)
```

3. The deterministic approximation error obeys

```text
||F(x)-Z_k(x)||_2
 <= (tau/2)||x||_2
 <= [c_r/2] d^alpha S/sqrt(k).                            (5.6)
```

Thus every process point admits a **smooth, process-adaptive effective-rank-k approximation at the exact conjectured polynomial scale**.

#### Proof

Diagonalize `A_x` by singular values `s_j`. On the corresponding right singular vector, `G_(x,k)` has eigenvalue

```text
g_j = s_j^2/(s_j^2+tau^2),                                (5.7)
```

which lies in `[0,1]`. This proves the first claim.

Moreover,

```text
Tr G_(x,k)
 = sum_j s_j^2/(s_j^2+tau^2)
 <= tau^(-2) sum_j s_j^2
 = tau^(-2)||A_x||_HS^2
 <= k,                                                     (5.8)
```

using (1.1) and the definition of `tau`.

For the residual,

```text
F(x)-Z_k(x)
 = A_x(I-G_(x,k))x.                                       (5.9)
```

On a singular direction with singular value `s`, the scalar multiplier of the operator `A_x(I-G)` is

```text
s * tau^2/(s^2+tau^2).                                    (5.10)
```

Writing `t=s/tau`,

```text
s tau^2/(s^2+tau^2)
 = tau * t/(1+t^2)
 <= tau/2.                                                 (5.11)
```

Hence

```text
||A_x(I-G_(x,k))||_op <= tau/2.                           (5.12)
```

Multiplying by `||x||_2<=d^alpha` proves (5.6). QED.

### Why this is better aligned with the conjecture

The operator `G_(x,k)` automatically retains precisely the tangent directions whose singular values are large enough to matter at scale `S/sqrt(k)`. Directions below that threshold are suppressed because their total contribution to `F(x)` is already below the desired chaining scale.

Unlike the global Haar sketch:

- there is no random realization for the supremum to overfit;
- no unbiasedness constraint forces rare/large amplification;
- the minimax obstruction from the predecessor does not apply, because the compression is allowed to depend on `x` and on `A_x`;
- the counterexample in Section 2 is passed automatically: its tangent is an `O(d^(-1/2))` multiple of the identity plus a rank-one perturbation, so at constant critical scale the identity bulk is below threshold and only the structured rank-one part can survive.

The price is that `G_(x,k)` varies with `x`. Controlling that variation is the new geometric problem.

## 6. A deterministic entropy criterion for the adaptive skeleton

The predecessor's random-image criterion was too strong because the approximating image contained sketch noise. The ridge skeleton yields a corrected deterministic criterion.

### Theorem 6.1 (adaptive-skeleton entropy criterion)

Let

```text
A := c_r d^alpha S.                                       (6.1)
```

Assume there is a polylogarithmic quantity `L=L(d,n)>=1` such that for every dyadic `1<=k<=d`,

```text
log N(
  Z_k(B_p^d),
  c A/sqrt(k)
) <= C_r k L,                                              (6.2)
```

for a sufficiently small fixed `r`-dependent constant `c>0`.

Then

```text
E ||sum_i g_i T_i||_I_p
 <= C_(r,p) d^alpha S
    [sqrt(L) log(2d) + sqrt(log(2d))].                    (6.3)
```

Hence (6.2) would establish the conjectured polynomial dimension exponent for arbitrary deterministic symmetric tensors throughout `2<=p<2r`.

#### Proof

By Theorem 5.1, for every `x in B_p^d`,

```text
||F(x)-Z_k(x)||_2 <= A/(2sqrt(k)).                         (6.4)
```

Thus any `cA/sqrt(k)`-cover of `Z_k(B_p^d)` induces, after changing constants, an `C_rA/sqrt(k)`-cover of `F(B_p^d)` of the same cardinality. Therefore

```text
log N(F(B_p^d), C_r A/sqrt(k))
 <= C_r k L.                                               (6.5)
```

For scales between `A/sqrt(d)` and `A`, choose dyadic `k` comparable to `(A/eps)^2`; this gives

```text
log N(F(B_p^d),eps)
 <= C_r L (A/eps)^2.                                      (6.6)
```

Integrating the square root gives the coarse Dudley contribution

```text
C_r A sqrt(L) log(2d).                                    (6.7)
```

For scales below `A/sqrt(d)=c_r S d^(-1/p)`, the deterministic Lipschitz estimate

```text
||F(x)-F(y)||_2 <= C_r S ||x-y||_p                        (6.8)
```

and the standard volumetric cover of `B_p^d` give the same fine-scale contribution as in the predecessor,

```text
C_(r,p) d^alpha S sqrt(log(2d)).                          (6.9)
```

Dudley's inequality yields (6.3). QED.

### Important distinction from the false criterion

Theorem 6.1 is still conditional; it does **not** claim (6.2). But its approximating set is deterministic and lies uniformly within the required radius of the true process image. The explicit family from Section 2 cannot create a large spurious cloud through a shared random sketch. Any failure of (6.2) must therefore reflect genuine complexity of the high-singular-value tangent geometry, not external sketch noise.

## 7. The new volumetric obstruction

The old volumetric obstruction can now be stated more sharply.

The elementary bound

```text
||A_x||_HS <= c_r S                                       (7.1)
```

says that at scale `S/sqrt(k)` there can be at most `k` tangent singular directions above threshold. Pointwise, the problem is therefore already `k`-dimensional.

What prevents immediate closure is that the identity of those directions can vary with `x`. A naive Grassmannian cover of all `k`-planes costs approximately

```text
exp(Theta(k d)),                                           (7.2)
```

which is far too large. The conjecture requires replacing that ambient Grassmannian complexity by roughly

```text
exp(k polylog(d,n)).                                       (7.3)
```

using the special fact that `A_x` is not an arbitrary matrix-valued function: it is a degree-`r-1` polynomial contraction of one fixed tensor family.

This is a more informative bottleneck than the previous global sketch question. The desired theorem is now a **polynomially generated leverage-subspace entropy bound**.

A successful proof can take one of two forms:

1. show that the ridge operators `G_(x,k)` themselves have only `exp(k polylog)` effective metric complexity at the relevant scale; or
2. prove an inverse theorem: if the family `G_(x,k)` has too many separated states, then the tensor family admits a sparse/block/norming structure already covered by earlier P09 partial theorems.

The C05 hypercube-rich-subspace handoff is potentially relevant precisely to branch (2), but now with the correct object: discretized high-leverage tangent directions, not the entire noisy Haar-sketch image.

## 8. Counterexample tests for the new route

Before building a proof around the adaptive skeleton, it passes the two obstructions that killed earlier methods.

### 8.1 The diagonal / dense-dust witness

For a diagonal tensor, the dangerous Frobenius mass can be spread over all coordinates even when the injective norm is small. The ridge filter does not sum the whole Frobenius covariance blindly. It only retains singular directions with `s_j` comparable to or larger than `S/sqrt(k)`, and (5.8) charges their **effective count**, not ambient rank.

This does not prove the entropy bound, but it avoids the one-scale PAC-Bayes failure in which every tiny coordinate was paid for simultaneously through a global covariance trace.

### 8.2 The global Haar-sketch witness from Section 2

For the family (2.6),

```text
A_x
 = [1/(r sqrt(d))]
   [ beta^(r-1) I
     + (r-1) beta^(r-2) x b^T ].                          (8.1)
```

Thus `A_x` is a scalar multiple of the identity of size `O_r(d^(-1/2))` plus a rank-one perturbation. At the `k=1`, `p=2` critical scale, the identity bulk is below the ridge threshold for large `d`. The adaptive skeleton therefore retains at most the structured low-rank part; it does not reproduce the exponential artificial packing created by the global Haar sketch.

This is exactly the behavior wanted from an intermediate lemma.

## 9. Remaining gap

No source-level closure is claimed. The arbitrary-tensor exponent remains `gamma`.

The main open implication is now:

```text
For tau ~ S/sqrt(k),
G_(x,k) = A_x^*A_x (A_x^*A_x + tau^2 I)^(-1),
Tr G_(x,k) <= k.

Prove that the image
  x -> A_x G_(x,k) x
has covering entropy O(k polylog(d,n))
at radius d^alpha S/sqrt(k),

or produce a source-valid obstruction and pivot again.                 (9.1)
```

A generic trace-`k` PSD family is much too large, so (9.1) must exploit the polynomial dependence

```text
x -> A_x = contraction of the fixed tensors T_i against x^(r-1).       (9.2)
```

The strongest plausible next mechanism is a **spectral-threshold inverse theorem**: if the high-leverage tangent subspaces vary through too many essentially different coordinate/sign patterns, extract either a sparse-coordinate structure (where earlier P09 norming/block theorems apply) or a sign-poor branch controlled by anti-concentration.

## 10. Next concrete attack

The next run should not return to global Haar-sketch image entropy. That route is now explicitly refuted.

1. **Soft-projector stability.** Derive a resolvent identity for

```text
G_(x,k)-G_(y,k)
```

in terms of `A_x-A_y`, but split singular values into `>>tau`, `~tau`, and `<<tau` rather than paying the naive global `1/tau^2` Lipschitz factor.

2. **Threshold crossing is cheap.** Prove that directions whose singular values cross the threshold `tau` contribute only `O(tau ||x-y||_2)` to the process increment, so spectral projector discontinuity need not be covered at full Grassmannian resolution.

3. **Inverse branch.** If many points produce genuinely different `>>tau` leverage subspaces, discretize signs/coordinates of their leading vectors and test whether the C05 hypercube-rich lemma forces sparse coordinate dependence. If yes, reduce that branch to the earlier P09 structured-class theorems.

4. **Counterexample first.** Test any proposed entropy lemma against (a) the diagonal tensor/dense-dust witness, (b) the explicit family (2.6), and (c) the matrix case. Reject the lemma immediately if it reintroduces global Frobenius mass or shared-sketch noise.

A useful concrete subtarget is to prove an entropy bound for the ridge skeleton on the class where every `A_x^*A_x` has at most `k` eigenvalues above `4tau^2` and the corresponding spectral projectors have a uniform polynomial resolvent modulus. That would be a genuine broader covariance-structure class and a controlled stepping stone toward the arbitrary case.

## 11. Obligation ledger

```text
FULL SOURCE METRIC
  arbitrary deterministic tensors, 2 <= p < 2r:
  exponent before = gamma = 1/2 - 1/(2r)
  exponent after  = gamma = 1/2 - 1/(2r)
  target          = alpha = 1/2 - 1/p
  source status   = OPEN / not solved here

INTERMEDIATE OBLIGATIONS
  [PROVED] tangent Hilbert--Schmidt mass <= c_r S for every p>=2
  [PROVED] global Haar rank-k pointwise RMS <= C_r d^alpha S/sqrt(k)
  [REFUTED AS A METHOD HYPOTHESIS]
           global Haar-sketch image entropy O(k polylog) at critical scale;
           explicit p=2, r>=3 family has exp(c d) rank-one sketch packing
           with probability >1/4 while the true image has radius d^(-1/2)
  [PROVED] anchored Haar sketch variance depends only on residual outside anchor
  [PROVED] adaptive top-k tangent truncation approximates F(x) at critical scale
  [PROVED] adaptive ridge operator has Tr <= k and deterministic critical-scale error
  [PROVED] O(k polylog) entropy for the adaptive ridge skeleton would imply
           the conjectured polynomial exponent
  [OPEN]   prove that adaptive-skeleton entropy bound using polynomial tangent structure
  [OPEN]   or refute it and pivot to a genuinely different nonlinear/multiscale route
```

The word `REFUTED` above applies only to the **intermediate global-sketch entropy hypothesis**, not to Randomstrasse101 Conjecture 16. The source problem remains OPEN.

No finite exhaustive claim requiring a checker is introduced in this report. The new claims are analytic and their proofs are given on the page.