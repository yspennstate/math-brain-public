SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-22T23:33:23Z.
attacking: sharpen the integrated-Fourier stable-rank threshold continuously using an exact capped-simplex elementary-symmetric minimum and apply account02/B02's regularized-determinant theorem.

# account01/B02 — gap-stable-rank integrated Fourier theorem

**Run:** `20260922T233323Z-account01-B02-qform-r16`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control read:** revision `2026-09-22.15`  
**Assignment:** Integrated Fourier estimate / FOURIER  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction discipline

The owner target is unchanged: for independent real original-coordinate variables with one-dimensional probability densities bounded by one and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal bound on the density of `Q=X^TAX`, or give a target-valid counterexample. Continuity is tracked separately from essential boundedness.

This report uses no moment, support, Gaussian, log-concavity, or post-rotation independence assumption. It does not use the refuted law-uniform pointwise Fresnel decay, arbitrary-joint coarea bound, positive conditional projection-density moment, fiber-supremum bound, fixed-good-minor principle, or conditional-cap-as-independence shortcut.

The named designated partner actually used is **account02/B02**, run `20260922T221114Z-account02-B02-qform-r11-2ea3913a`, canonical report

`yspennstate/math-open-problems@c726a32fa4d8e1e8ab246d48560b89cf1d4c4857`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T221114Z-account02-B02-qform-r11-2ea3913a/REPORT.md`.

Its source-pinned regularized determinant input is the following. For a physical cross block `B=A[I,J]` between disjoint ORIGINAL-coordinate banks and `1<=q<2`, if the maximum coordinate diagonal of the range projection on one usable side is at most `q/2`, then

`|phi_Q(t)| <= det(I+c_q t^2 B B^T)^(-1/(4q)),`

where

`c_q=2q/(pi^2 e^2).`                                               (1.1)

For `q=2`, (1.1) holds without a leverage hypothesis. Arbitrary self-curvature in the two banks and arbitrary outside couplings are retained. I use this completed partner theorem exactly in that scope.

The preceding B02 run used the coarse implication `sr(B)>=k => e_k>=F^(2k)/k^k`, which required stable-rank thresholds 3,4,5 for the three useful choices of `q`. The new point here is an exact capped-simplex minimum that lowers those thresholds to `2+delta`, `3+delta`, and `4+delta`, for every fixed positive gap `delta`.

## 2. Exact capped-simplex compound lemma

Let `x_1,...,x_m>=0`, put

`S=sum_j x_j>0`,

and assume

`max_j x_j <= S/r_0`,                                              (2.1)

where

`r_0=k-1+delta`, `k>=2` integer, `0<delta<=1`.                    (2.2)

Then

`boxed: e_k(x_1,...,x_m) >= [delta/r_0^k] S^k.`                    (2.3)

The constant is sharp under (2.1).

### Proof

Normalize `p_j=x_j/S`, so `sum p_j=1` and `0<=p_j<=a:=1/r_0`.

Take two coordinates `u,v` that are both strictly between `0` and `a`, and hold all other coordinates fixed. At fixed sum `u+v=s`,

`e_k(u,v,p_rest)
 = uv e_(k-2)(p_rest)
   + s e_(k-1)(p_rest)
   + e_k(p_rest).`                                                (2.4)

The last two terms are fixed, while the coefficient of `uv` is nonnegative. Hence moving `(u,v)` to an endpoint of the allowed segment

`max(0,s-a) <= u <= min(a,s)`

cannot increase `e_k`; at an endpoint at least one of the two coordinates is `0` or `a`. Repeating finitely many times leaves at most one coordinate strictly between `0` and `a`.

Because `1/a=r_0=k-1+delta`, the terminal vector is, up to permutation,

- if `0<delta<1`: `k-1` entries equal to `1/r_0`, one entry equal to `delta/r_0`, all others zero;
- if `delta=1`: `k` entries equal to `1/k`, all others zero.

In both cases exactly one `k`-fold product survives and equals `delta/r_0^k`. Thus (2.3) follows. Equality holds at the displayed packed vector. QED.

### Stable-rank form

For the squared singular values `x_j=s_j(B)^2`, write

`F=||B||_F`, `sr(B)=F^2/||B||_op^2`.

If

`sr(B)>=r_0=k-1+delta`,                                            (2.5)

then `max x_j<=F^2/r_0`, so (2.3) gives

`boxed: e_k(s_1(B)^2,...) >= [delta/(k-1+delta)^k] F^(2k).`         (2.6)

This is exact at the level of stable-rank information. In particular it interpolates continuously between the integer thresholds used in the previous B02 run.

## 3. Main theorem: integrated Fourier from a gap above the critical stable rank

### Theorem `QFORM-GAP-STABLERANK-L1-FOURIER-v1`

Assume the partner determinant estimate (1.1) is valid for some `1<=q<=2`. Let `k` be an integer satisfying

`k>2q`,                                                            (3.1)

and let `0<delta<=1`. If

`sr(B)>=k-1+delta`,                                                (3.2)

then

`boxed:
 integral_R |phi_Q(t)| dt
 <= A_(q,k,delta) / ||B||_F,
`                                                                    (3.3)

where

`boxed:
 A_(q,k,delta)
 = [pi e/(k sqrt(2q))]
   B(1/(2k), 1/(4q)-1/(2k))
   sqrt(k-1+delta) delta^(-1/(2k)).
`                                                                    (3.4)

Consequently `Q` has a bounded **continuous** density, vanishing at infinity, and

`boxed:
 ||p_Q||_infinity <= A_(q,k,delta)/(2pi ||B||_F).
`                                                                    (3.5)

### Proof

Let `x_j=s_j(B)^2`. The determinant expansion and (2.6) give

`det(I+c_q t^2BB^T)
 = sum_(ell>=0) c_q^ell t^(2ell)e_ell(x)
 >= 1 + c_q^k [delta/(k-1+delta)^k] F^(2k)t^(2k).`              (3.6)

Set

`gamma=c_q^k [delta/(k-1+delta)^k]F^(2k).`

By (1.1),

`|phi_Q(t)| <= (1+gamma t^(2k))^(-1/(4q)).`                       (3.7)

The beta substitution `u=gamma t^(2k)` yields

`integral_R (1+gamma t^(2k))^(-1/(4q))dt
 = gamma^(-1/(2k))/k
   B(1/(2k),1/(4q)-1/(2k)).`                                    (3.8)

The beta integral is finite exactly under (3.1). Since

`c_q^(-1/2)=pi e/sqrt(2q)`

and

`[delta/(k-1+delta)^k]^(-1/(2k))
 =sqrt(k-1+delta) delta^(-1/(2k)),`

(3.3)--(3.4) follow. Fourier inversion for an `L^1` characteristic function supplies the continuous density and (3.5). QED.

## 4. Three direct corollaries

The partner theorem gives three especially useful choices.

### 4.1 Leverage at most one half

If one usable side of `B` has range-projection leverage at most `1/2`, choose `q=1`, `k=3`. For every fixed `delta in (0,1]`,

`sr(B)>=2+delta`

implies (3.3)--(3.5), with

`A_(1,3,delta)
 =[pi e/(3sqrt2)] B(1/6,1/12)
  sqrt(2+delta) delta^(-1/6).`                                   (4.1)

Thus the previous direct-L1 threshold `sr>=3` drops to **any fixed positive stable-rank gap above 2**.

### 4.2 Leverage at most three quarters

If one usable side has range-projection leverage at most `3/4`, choose `q=3/2`, `k=4`. For every fixed `delta>0`,

`sr(B)>=3+delta`

implies (3.3)--(3.5). The previous direct-L1 threshold `sr>=4` drops to **any fixed positive gap above 3**.

### 4.3 No leverage assumption

Use the unconditional `q=2` partner estimate and `k=5`. For every fixed `delta>0`,

`sr(B)>=4+delta`

implies (3.3)--(3.5), with no leverage condition. The previous no-leverage direct-L1 threshold `sr>=5` drops to **any fixed positive gap above 4**.

The blow-up `delta^(-1/(2k))` is explicit. It is not an artifact of the proof of Lemma 2: the capped-simplex lower bound is attained by the packed singular-value profile, so a separate structural mechanism is needed to cross the critical integer stable-rank surfaces uniformly.

## 5. Quantitative half-gap version and actual partner application

Taking `delta=1/2` gives clean uniform thresholds and constants:

`q=1,   k=3: A=63.0685433407`,
`q=3/2, k=4: A=79.8573615039`,
`q=2,   k=5: A=96.7131567758`.                                  (5.1)

Therefore

- leverage `<=1/2` and `sr(B)>=5/2` imply
  `integral|phi_Q|<=63.069/F` and `||p_Q||_infinity<=10.038/F`;
- leverage `<=3/4` and `sr(B)>=7/2` imply
  `integral|phi_Q|<=79.858/F` and `||p_Q||_infinity<=12.710/F`;
- with no leverage assumption, `sr(B)>=9/2` implies
  `integral|phi_Q|<=96.714/F` and `||p_Q||_infinity<=15.393/F`.

This is an equation-level application of the named account02/B02 result: (1.1) is precisely its completed regularized-determinant estimate, and the new Lemma 2 supplies the missing determinant compound at the lower stable-rank threshold.

The same partner handoff records the live matching currency

`F=||B||_F >=768^(-1/4)=0.1899589214...`                         (5.2)

for the selected aggregate packet in account01/B19's matching branch. Substitution into (5.1) yields continuous-density bounds

`boxed: <52.842` on the `(leverage<=1/2, sr>=5/2)` branch,

`boxed: <66.908` on the `(leverage<=3/4, sr>=7/2)` branch,

`boxed: <81.031` on the `(sr>=9/2)` no-leverage branch.              (5.3)

The first line is a genuine enlargement of the previous B02 direct-L1 branch: stable ranks in `[5/2,3)` are now paid with continuity, whereas the previous direct-L1 statement started at `3`.

## 6. More flexible leverage/stable-rank frontier

The discrete examples above are only convenient fixed points. For `q<2`, the partner theorem requires leverage `h<=q/2`; Theorem 3 then only requires an integer `k>2q` and a fixed stable-rank gap above `k-1`.

For example, with `k=3`, any fixed `q<3/2` pays every packet having

`h<=q/2`, `sr(B)>=2+delta`.

Thus for every fixed `epsilon,delta>0` with `epsilon<1/4`, the region

`h<=3/4-epsilon`, `sr(B)>=2+delta`

has an unweighted `L^1_t` Fourier bound with a finite constant depending only on `epsilon,delta` and `F`; no dimension or input-law parameter enters. This pushes the low-stable-rank direct-Fourier frontier substantially beyond the earlier `h<=1/2, sr>=3` certificate.

Likewise `k=4` permits any fixed `q<2`, hence any leverage bounded by `1-epsilon`, once `sr(B)>=3+delta`.

## 7. What remains and why this is not full closure

The owner target supplies three large eigenvalues of `A`, not a priori a physical cross block whose Frobenius mass, stable-rank gap and range leverage satisfy the hypotheses above. The current aggregate reductions do supply `O(1)` Frobenius currency in important branches, but fixed-good-minor and universal rank-three-cut reductions are known false.

The precise remaining determinant-Fourier obstruction is now concentrated near the **critical integer stable-rank surfaces**:

- rank-two / stable-rank `2+o(1)` packets when the available leverage is below `3/4`;
- stable-rank `3+o(1)` packets when leverage is close to one;
- stable-rank `4+o(1)` packets for the unconditional `q=2` estimate.

The `delta^(-1/(2k))` divergence in (3.4) shows that the determinant-compound argument alone cannot provide a universal constant across these surfaces from stable rank alone. These are exactly the regimes where pair/rank-two, ridge, one-sided-square, grouped-bank, and near-coloop mechanisms should be coupled to the Fourier estimate rather than replaced by another fixed-minor argument.

I found no target-valid counterexample to the global stronger criterion

`integral_R |E exp(it X^TAX)| dt <= C`

under the bare three-large-eigenvalue hypothesis. Therefore that criterion remains OPEN, not refuted.

## 8. Status

`ESSENTIAL_STEP_APPLIED`.

Proved: a strict quantitative extension of the completed direct integrated-Fourier branch from integer stable-rank thresholds to every fixed positive gap above the critical thresholds, with exact capped-simplex constants and continuous output density in its scope.

Not proved: the unrestricted QFORM conjecture; a global unweighted `L^1_t` characteristic-function bound; continuity in branches controlled only by non-Fourier essential-density estimates.

No publication-priority or novelty claim is made.
