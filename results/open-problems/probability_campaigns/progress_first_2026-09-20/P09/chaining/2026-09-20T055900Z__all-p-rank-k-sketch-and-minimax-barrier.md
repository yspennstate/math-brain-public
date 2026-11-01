Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 maximum was requested, but this runtime does not provide authenticated GPT-6/maximum attestation.

# P09 progress-first run — all-p rank-k tangent sketch reduction and a minimax barrier

**Status: PROVED PARTIAL.** This report does **not** prove Randomstrasse101 Conjecture 16 for arbitrary deterministic tensors. The fixed full-source worst-case polynomial exponent remains

```text
gamma = 1/2 - 1/(2r)
```

rather than the conjectured

```text
alpha = 1/2 - 1/p.
```

The mathematical progress is twofold.

1. The rank-`k` tangent-sketch mechanism from the preceding run is extended from `p=2` to the entire source regime `p>=2`. At the correct source normalization, every point of `B_p^d` admits an unbiased rank-`k` tangent approximation with RMS error

```text
C_r d^(1/2-1/p) S / sqrt(k),
S^2 = sum_i ||T_i||_I_p^2.
```

A scale-by-scale entropy estimate for the corresponding random sketch images would therefore imply Conjecture 16 throughout the unresolved `2 <= p < 2r` range.

2. That error scale is **minimax-sharp for the whole class of unbiased rank-`k` linear tangent sketches**. For every distribution of rank-`k` linear maps with mean identity, there is an explicit symmetric order-`r` tensor family and a point `x in B_p^d` for which the mean-square tangent-sketch error is at least

```text
c_r d^(1-2/p) S^2 / k.
```

Thus there is no hidden polynomial slack to recover by improving the pointwise sketch variance. The remaining problem is genuinely the entropy of the random low-rank image at this critical approximation scale.

- Native role: `P09`
- Native slot: `6aa7b454b5808191bb00d87697d89388`
- Installed title: `Gaussian Tensor Bounds`
- Repository / branch: private `yspennstate/math-open-problems`, `master`
- Source: A. S. Bandeira, D. Dmitriev, K. Lucca, P. Nizic-Nikolac, A. Rodder et al., *Randomstrasse101: Open Problems of 2025*, arXiv:2603.29571, Entry 8, Conjecture 16.
- Source norm:

```text
||T||_I_p = sup_{||x||_p <= 1} |T[x,...,x]|.
```

- Source target:

```text
E ||sum_i g_i T_i||_I_p
 <= polylog(d,n) C(r,p) d^(1/2-1/p)
    (sum_i ||T_i||_I_p^2)^(1/2).
```

- Regime: `2 <= p < 2r`, beyond the already established matrix, rank-one, independent-entry/sparse-entry, and `p>=2r` cases.
- Pre-write master inspected: `400c0350c9031d5570c237a13b005f1be1432a5e`.
- Immediate P09 predecessor: `2026-09-20T050000Z__approximate-packing-and-rank-k-sketch-reduction.md`, blob `d4f789d95b3e9b31027e3a93c7ebb640e2b2c0c4`.
- Historical C0035/successor-gate material and every earlier P09 report remain preserved. No peer or historical file is edited.

## 1. Source-current baseline and fixed metric

A fresh bounded source check on 20 September 2026 re-read Entry 8 of arXiv:2603.29571. The source still states Conjecture 16 as

```text
E ||sum_i g_i T_i||_I_p
  <= \tilde O_(r,p)( d^(1/2-1/p) S ),
```

for symmetric deterministic order-`r` tensors and `p>=2`. The same source explicitly says that the geometric covering argument reaches the conjectured dimension dependence for `p>=2r` and encounters the volumetric barrier for `p<2r`. It also separates the matrix, rank-one and independent-entry worlds from the arbitrary correlated deterministic-summand problem. The strongest general primary improvement recovered remains Aden-Ali, arXiv:2503.10580, whose PAC-Bayes/contraction estimate sharpens the earlier BGJLR bound but does not remove all higher-contraction losses in the general low-`p` regime.

Accordingly the full-source metric is unchanged:

```text
old arbitrary-tensor exponent: gamma = 1/2 - 1/(2r),
new arbitrary-tensor exponent: gamma = 1/2 - 1/(2r),
target exponent:               alpha = 1/2 - 1/p.
```

This run changes the intermediate obligation substantially: the previous `p=2` random-sketch reduction is now source-normalized for every `p>=2`, and its approximation scale is proved optimal among unbiased rank-`k` linear tangent sketches.

## 2. A dimension-free Hilbert--Schmidt tangent bound for every p >= 2

Let `q=p/(p-1)`, so `1 <= q <= 2`. Write `B_i` for the symmetric `r`-linear form associated to `T_i`, and put

```text
S^2 := sum_i ||T_i||_I_p^2.                               (2.1)
```

Let

```text
c_r := r^r / r!.                                           (2.2)
```

The real polarization identity gives

```text
|B_i(x_1,...,x_r)|
 <= c_r ||T_i||_I_p prod_j ||x_j||_p.                     (2.3)
```

Indeed, after scaling to `||x_j||_p<=1`, the signed polarization formula expresses `B_i(x_1,...,x_r)` as an average of diagonal values at vectors of `p`-norm at most `r`; homogeneity contributes `r^r`, and the `r!` in the polarization denominator gives (2.3).

For `x in B_p^d`, define the tangent map

```text
A_x : R^d -> R^n,
(A_x u)_i := B_i(x,...,x,u),                               (2.4)
```

with `r-1` copies of `x`. For each `i`, the row functional

```text
u -> B_i(x,...,x,u)
```

has dual `ell_q` norm at most `c_r ||T_i||_I_p`. Since `q<=2`,

```text
||a||_2 <= ||a||_q.                                        (2.5)
```

Therefore

```text
||A_x||_HS^2
 = sum_i || row_i(A_x) ||_2^2
 <= c_r^2 sum_i ||T_i||_I_p^2
 = c_r^2 S^2.                                              (2.6)
```

This is the key source-normalized fact. No dimension factor appears in the Hilbert--Schmidt mass of a one-slot tangent, for any `p>=2`.

Also, for `x in B_p^d`,

```text
||x||_2 <= d^alpha,
alpha := 1/2 - 1/p.                                        (2.7)
```

The entire source dimension factor is therefore already visible in the elementary embedding `ell_p^d -> ell_2^d`; it does not enter through the tangent Hilbert--Schmidt norm.

## 3. A Haar rank-k tangent sketch with the source-critical error scale

Let `1 <= k < d`. Draw a Haar-uniform `k`-dimensional subspace `E <= R^d`, let `P_E` be its orthogonal projection, and define

```text
R_k := (d/k) P_E.                                          (3.1)
```

Then

```text
rank(R_k)=k,
E R_k = I_d.                                               (3.2)
```

For `x in B_p^d`, define

```text
F(x) := ( B_i(x,...,x) )_i,                               (3.3)
Y_k(x) := A_x R_k x
        = ( B_i(x,...,x,R_k x) )_i.                       (3.4)
```

There are `r-1` unsketched copies of `x` in (3.4).

### Lemma 3.1 (exact covariance scale of the Haar sketch)

For every `x in R^d`,

```text
E (R_k-I)x = 0                                             (3.5)
```

and

```text
|| E[(R_k-I)x ((R_k-I)x)^T] ||_op
 <= 2 ||x||_2^2 / k.                                      (3.6)
```

#### Proof

By rotation invariance it is enough to take `x=||x||_2 e_1`. Put

```text
X := e_1^T P_E e_1.
```

For a Haar `k`-plane,

```text
E X   = k/d,
E X^2 = k(k+2)/(d(d+2)).                                  (3.7)
```

The covariance is invariant under rotations fixing `e_1`, hence it has one eigenvalue in the `e_1` direction and one on `e_1^perp`. The parallel variance is

```text
lambda_parallel
 = ||x||_2^2 E[(dX/k - 1)^2]
 = ||x||_2^2 * 2(d-k)/(k(d+2))
 <= 2 ||x||_2^2/k.                                        (3.8)
```

Moreover

```text
E ||R_k x||_2^2
 = (d/k)||x||_2^2,                                        (3.9)
```

so the total covariance trace is

```text
(d/k - 1)||x||_2^2 = (d-k)||x||_2^2/k.                   (3.10)
```

Dividing the remaining trace among the `d-1` orthogonal directions gives

```text
lambda_perp
 = d(d-k) ||x||_2^2 /
   [k(d+2)(d-1)]
 < ||x||_2^2/k.                                           (3.11)
```

This proves (3.6). QED.

### Theorem 3.2 (all-p pointwise tangent-sketch approximation)

For every `p>=2`, every `x in B_p^d`, and every symmetric deterministic tensor family,

```text
E Y_k(x) = F(x),                                           (3.12)
```

and

```text
E ||Y_k(x)-F(x)||_2^2
 <= 2 c_r^2 d^(2alpha) S^2 / k.                           (3.13)
```

Equivalently, the RMS approximation scale is

```text
rho_k <= sqrt(2)c_r d^alpha S / sqrt(k).                  (3.14)
```

#### Proof

Unbiasedness follows from `E R_k=I`. Let

```text
C_x := E[(R_k-I)x ((R_k-I)x)^T].                          (3.15)
```

Then

```text
E ||Y_k(x)-F(x)||_2^2
 = Tr(A_x^* A_x C_x)
 <= ||C_x||_op ||A_x||_HS^2.                              (3.16)
```

By Lemma 3.1, (2.6) and (2.7),

```text
Tr(A_x^* A_x C_x)
 <= (2||x||_2^2/k) c_r^2 S^2
 <= 2 c_r^2 d^(2alpha) S^2/k.                             (3.17)
```

QED.

### What changed relative to the preceding report

The previous rank-`k` theorem was only formulated and proved at `p=2`. Equation (2.6) shows that its Hilbert--Schmidt mechanism survives unchanged for every `p>=2`; only the inevitable embedding factor `||x||_2<=d^alpha||x||_p` appears. This is exactly the dimension factor conjectured by the source.

## 4. A critical-sketch entropy criterion implies the full source exponent

The predecessor report proved the following random-approximation packing transfer: if a random map `Y_omega` approximates `F` pointwise in mean square at radius `rho`, then a deterministic packing of `F(X)` transfers, up to constants, to the image of some realization of `Y_omega`. The event-restricted form permits us to insist simultaneously that the realization satisfy a typical-sketch entropy estimate.

Theorem 3.2 turns that abstract transfer into an all-`p` reduction.

### Theorem 4.1 (critical rank-k entropy criterion)

Fix `p>=2` and put

```text
A := c_r d^alpha S.                                       (4.1)
```

Suppose that there is a polylogarithmic quantity `L=L(d,n)>=1` such that for every dyadic `k` with `1<=k<=d`, with probability at least `3/4` over the Haar `k`-plane,

```text
log M(
  Y_k(B_p^d),
  c A/sqrt(k)
) <= C_r k L.                                              (4.2)
```

Here `M(K,eps)` is the Euclidean packing number of the process image and `c>0` is a sufficiently small numerical constant.

Then

```text
E ||sum_i g_i T_i||_I_p
 <= C_(r,p) d^alpha S
    [ sqrt(L) log(2d) + sqrt(log(2d)) ].                  (4.3)
```

In particular, if `L` is polylogarithmic in `(d,n)`, then (4.3) has exactly the polynomial dimension exponent requested by Conjecture 16.

#### Proof

From Theorem 3.2, for every fixed `x`,

```text
E ||Y_k(x)-F(x)||_2^2 <= C_r A^2/k.                       (4.4)
```

Apply the event-restricted packing-transfer lemma from the preceding P09 report with a fixed Markov factor, say `a=2`, and with the event in (4.2). Since the event has probability at least `3/4` and the pointwise good-approximation event has probability at least `3/4`, their intersection retains a positive numerical fraction. Therefore (after changing constants)

```text
log N(
  F(B_p^d),
  C_r A/sqrt(k)
) <= C_r k L                                               (4.5)
```

for every dyadic `k<=d`. Here we used the standard relation that a maximal packing is a cover at a comparable radius.

For scales

```text
C_r A/sqrt(d) <= eps <= C_r A,                             (4.6)
```

choose dyadic `k` comparable to `(A/eps)^2`. Monotonicity of covering numbers and (4.5) give

```text
log N(F(B_p^d),eps)
 <= C_r L (A/eps)^2.                                      (4.7)
```

Hence the coarse part of Dudley's integral is

```text
int_[C_r A/sqrt(d)]^[C_r A]
 sqrt(log N(F(B_p^d),eps)) d eps
 <= C_r A sqrt(L) log(2d).                                (4.8)
```

It remains to control the scales below `A/sqrt(d)`. The process map itself is Lipschitz in the `ell_p` norm. Indeed, telescoping the multilinear form and using (2.3), for `x,y in B_p^d`,

```text
||F(x)-F(y)||_2
 <= r c_r S ||x-y||_p.                                   (4.9)
```

The unit ball of any `d`-dimensional normed space satisfies

```text
N(B_p^d, delta B_p^d) <= (1+2/delta)^d.                  (4.10)
```

Since

```text
A/sqrt(d)
 = c_r S d^(alpha-1/2)
 = c_r S d^(-1/p),                                        (4.11)
```

the fine-scale integral obtained from (4.9)-(4.10) is

```text
int_0^[C_r S d^(-1/p)]
 sqrt{ d log(1+C_r S/eps) } d eps
 <= C_(r,p) S d^(1/2-1/p) sqrt(log(2d))
 = C_(r,p) d^alpha S sqrt(log(2d)).                       (4.12)
```

Combining (4.8) and (4.12) with Dudley's entropy integral proves (4.3). QED.

### Consequence

The unresolved source problem has now been reduced, by an elementary and source-normalized argument, to one concrete geometric statement:

> prove that a **typical rank-`k` tangent-sketch image** has only `exp(polylog(d,n)*k)` points at separation `d^alpha S/sqrt(k)`.

No better pointwise approximation scale is needed. The next section shows that, within the entire unbiased linear rank-`k` sketch class, no better polynomial scale is even available.

## 5. New minimax obstruction — the d^alpha/sqrt(k) error is sharp

The following theorem attacks the intermediate lemma before building the rest of the proof around it.

### Theorem 5.1 (minimax sharpness for unbiased rank-k linear tangent sketches)

Fix `r>=2`, `p>=2`, `d>=2`, and `1<=k<=d/2`. Let `R` be **any** random real `d x d` linear map such that

```text
rank(R) <= k   almost surely,
E R = I_d.                                                  (5.1)
```

Then there exist symmetric deterministic order-`r` tensors

```text
T_1,...,T_d
```

and a point `x in B_p^d` such that, with

```text
S^2 = sum_j ||T_j||_I_p^2 <= 1,                           (5.2)
```

the associated tangent sketch

```text
Y_R(x) := ( B_j(x,...,x,Rx) )_(j=1)^d                    (5.3)
```

satisfies

```text
E Y_R(x) = F(x),                                           (5.4)
```

but

```text
E ||Y_R(x)-F(x)||_2^2
 >= [1/(2r^2)] d^(2alpha) S^2/k.                          (5.5)
```

Thus the `d^alpha/sqrt(k)` RMS scale in Theorem 3.2 is minimax-optimal up to an `r`-dependent constant for unbiased linear rank-`k` tangent sketches.

#### Proof, step 1: every unbiased rank-k sketch has large average Frobenius error

Since `rank(R)<=k`,

```text
|Tr R| <= sqrt(k) ||R||_F.                                (5.6)
```

Therefore

```text
E ||R||_F^2
 >= (1/k) E (Tr R)^2
 >= (1/k) (E Tr R)^2
 = d^2/k.                                                  (5.7)
```

Using `E R=I`,

```text
E ||R-I||_F^2
 = E||R||_F^2 - 2 Tr(E R) + d
 >= d^2/k - d
 = d(d-k)/k.                                               (5.8)
```

Let `eps` be uniform on `{+-1}^d` and define

```text
x_eps := d^(-1/p) eps.                                    (5.9)
```

Then `||x_eps||_p=1`, and for every deterministic matrix `M`,

```text
E_eps ||M x_eps||_2^2
 = d^(-2/p) ||M||_F^2.                                   (5.10)
```

Averaging (5.10) with `M=R-I` and then over `R`, (5.8) implies that there is at least one sign vector `eps_*` such that, for

```text
x := d^(-1/p) eps_*,                                      (5.11)
```

we have

```text
E ||(R-I)x||_2^2
 >= d^(-2/p) d(d-k)/k
 = d^(2alpha) (d-k)/k.                                    (5.12)
```

#### Proof, step 2: construct a tensor family whose tangent sees that full Euclidean error

Let `q=p/(p-1)` and put

```text
b := d^(-1/q) eps_*.                                      (5.13)
```

Then

```text
||b||_q=1,
b^T x=1.                                                   (5.14)
```

Let

```text
u := eps_*/sqrt(d).                                        (5.15)
```

Because

```text
x = d^alpha u,
b = d^(-alpha) u,                                         (5.16)
```

we have

```text
x b^T = u u^T.                                             (5.17)
```

For `j=1,...,d`, define the homogeneous polynomial

```text
P_j(z)
 := d^(-1/2) z_j (b^T z)^(r-1).                           (5.18)
```

Let `T_j` be its associated symmetric order-`r` tensor. Since `||b||_q=1`, for every `||z||_p<=1`,

```text
|P_j(z)|
 <= d^(-1/2) |z_j| |b^T z|^(r-1)
 <= d^(-1/2).                                              (5.19)
```

Hence

```text
||T_j||_I_p <= d^(-1/2)
```

and therefore (5.2) holds.

The symmetric multilinear form associated to (5.18) is

```text
B_j(z_1,...,z_r)
 = [1/(r sqrt(d))]
   sum_(m=1)^r
   (z_m)_j prod_(ell != m) (b^T z_ell).                   (5.20)
```

At the chosen point `x`, because `b^T x=1`, the tangent map is

```text
(A_x w)_j
 = B_j(x,...,x,w)
 = [1/(r sqrt(d))]
   [ w_j + (r-1) x_j (b^T w) ].                           (5.21)
```

In matrix form,

```text
A_x
 = [1/(r sqrt(d))]
   [ I + (r-1) x b^T ]
 = [1/(r sqrt(d))]
   [ I + (r-1) u u^T ].                                   (5.22)
```

The matrix in the last brackets has eigenvalue `r` along `u` and eigenvalue `1` on `u^perp`. Consequently

```text
||A_x w||_2
 >= ||w||_2/(r sqrt(d))                                   (5.23)
```

for every `w`.

Take `w=(R-I)x`. Equations (5.12) and (5.23) yield

```text
E ||Y_R(x)-F(x)||_2^2
 = E ||A_x(R-I)x||_2^2
 >= [1/(r^2 d)] E||(R-I)x||_2^2
 >= [(d-k)/(r^2 d k)] d^(2alpha).                         (5.24)
```

Since `k<=d/2`, `(d-k)/d>=1/2`, and since `S^2<=1`,

```text
E ||Y_R(x)-F(x)||_2^2
 >= d^(2alpha)/(2r^2 k)
 >= d^(2alpha) S^2/(2r^2 k).                              (5.25)
```

Unbiasedness (5.4) is immediate from `E R=I`. QED.

### Interpretation

Theorem 5.1 rules out a large family of tempting improvements. One cannot hope to beat the source-critical factor by replacing the Gaussian sample-covariance sketch with a cleverer unbiased rank-`k` **linear** sketch and proving a uniformly smaller pointwise variance. The obstruction is not a defect of the Gaussian sketch: it follows from rank, unbiasedness and a concrete symmetric tensor family.

So the only useful place left for the rank-`k` route to win is **entropy/cancellation at the critical error scale**.

## 6. A second calibration: small entropy can coexist with enormous sketch diameter

The previous report showed that `E||R||_op >= d/k` for any unbiased rank-`k` sketch. The Haar model makes the phenomenon exact: `||R_k||_op=d/k`.

It is important not to respond by demanding a small diameter for `Y_k(B_p^d)`. That condition already fails in the known matrix world.

At `p=2`, `r=2`, take a single tensor `T=I_d`. Then

```text
||T||_I_2 = 1,
Y_k(x) = x^T R_k x,
```

and because the spectrum of `R_k` is `{d/k,0}`,

```text
Y_k(B_2^d) = [0,d/k].                                     (6.1)
```

Thus the sketched image diameter is `d/k`, polynomially larger than the critical error scale `1/sqrt(k)`. Nevertheless this image is one-dimensional, so its packing entropy at that critical scale is only logarithmic.

This example sharply distinguishes the quantity that matters from one that does not:

```text
BAD target:   uniformly small ||R_k||_op or image diameter;
GOOD target:  log packing <= O(k polylog) at scale A/sqrt(k).
```

Any next proof must tolerate very large leverage directions if they occupy low-complexity pieces of the image.

## 7. Remaining gap

The full conjecture is now concentrated into the critical-sketch entropy statement (4.2). The obstruction has two faces:

1. `R_k` has a `k`-dimensional high-leverage range with eigenvalue `d/k`, so radius/Lipschitz arguments lose a polynomial factor even in matrix examples.
2. outside that range, the first `r-1` tensor slots still depend on all `d` coordinates, so rank alone does not make the entire polynomial image `k`-dimensional.

Theorem 5.1 says there is no pointwise-variance shortcut around this. A proof has to exploit **how the high-leverage part is organized**, not try to make it disappear.

The C05 handoff `operations/progress_first_2026-09-20/handoffs/2026-09-20T051200Z__C05_hypercube_rich_subspace_to_P06_P09.md` supplies a potentially useful inverse branch: a low-dimensional coefficient subspace containing unusually many sign points must have sparse coordinate dependence. This is relevant because a discretized failure of (4.2) would produce many separated witnesses; if those witnesses create a sign-rich tangent subspace, the handoff lemma forces a sparse-coordinate structure, precisely the kind of branch already handled well by the earlier P09 block/norming-cover theorems.

That observation is not yet a proof of (4.2): the missing step is to turn a large Euclidean packing of the nonlinear sketch image into either (a) a sign-rich low-dimensional tangent configuration to which the C05 inverse lemma applies, or (b) a sign-poor branch with enough anti-concentration to bound the packing directly.

## 8. Next concrete attack

The next run should attack (4.2) directly, not revisit the pointwise sketch variance.

1. **Leverage stratification.** For the Haar sketch `R_k=(d/k)P_E`, write `x=u+v` with `u in E`, `v in E^perp`, and stratify by `||u||_2`. Points with `||R_k x||` below the critical scale are automatically negligible because `||A_x||_op<=||A_x||_HS<=c_rS`.
2. **Critical high-leverage branch.** For each non-negligible stratum, discretize only the `k`-dimensional `u` coordinate first, then analyze the residual `v -> B_i[(u+v)^(r-1),u]` process. Do not replace it by the worst-case operator norm `d/k`.
3. **Inverse/anti-concentration dichotomy.** If a stratum has more than `exp(C k polylog)` separated residual witnesses, extract a discrete sign configuration from the tangent coefficient subspace. Apply the C05 hypercube-rich lemma as the structured inverse branch; otherwise prove the required packing bound from sign-poor anti-concentration.
4. **Counterexample test first.** Before claiming such a dichotomy, test it against both exact calibrations in this report: the scalar identity-matrix example, where diameter is huge but entropy is tiny, and the sharpness family (5.18), where the pointwise `d^alpha/sqrt(k)` error cannot be improved.

If the inverse/anti-concentration statement fails on either calibration, reject it immediately and move to a nonlinear or multiscale sketch rather than adding another lemma to the same route.

## 9. Obligation ledger

```text
FULL SOURCE METRIC
  arbitrary deterministic tensors, 2 <= p < 2r:
  exponent before = gamma = 1/2 - 1/(2r)
  exponent after  = gamma = 1/2 - 1/(2r)
  target          = alpha = 1/2 - 1/p
  source status   = OPEN / not solved here

INTERMEDIATE OBLIGATIONS
  [PROVED] one-slot tangent Hilbert--Schmidt mass <= c_r S for every p>=2
  [PROVED] Haar rank-k unbiased tangent sketch RMS <= C_r d^alpha S/sqrt(k)
  [PROVED] critical sketch-entropy hypothesis => full conjectured polynomial exponent
  [PROVED] d^alpha S/sqrt(k) is minimax-sharp for unbiased rank-k linear tangent sketches
  [PROVED] small image diameter is unnecessary and generally false even in the matrix calibration
  [OPEN]   prove O(k polylog(d,n)) packing entropy of typical sketch image at the critical scale
  [OPEN]   or refute that entropy statement and replace the linear sketch route
```

No closure claim is made. No finite exhaustive claim requiring a checker is introduced in this report. The new results are analytic lemmas with proofs on the page.
