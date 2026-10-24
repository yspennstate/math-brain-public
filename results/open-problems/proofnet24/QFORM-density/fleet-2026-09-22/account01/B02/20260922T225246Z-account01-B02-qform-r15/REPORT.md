SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B02, 2026-09-22T22:52:46Z.
attacking: convert the partner regularized-determinant bound into a genuine unweighted L1 characteristic-function theorem by paying the determinant with stable-rank compound mass.

# account01/B02 — stable-rank unweighted Fourier theorem

**Run:** `20260922T225246Z-account01-B02-qform-r15`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control read:** revision `2026-09-22.15`; fresh brain head observed at `2add339e27af7a12f5055c08a2cf42a52d687456` before the run write.  
**Assignment:** Integrated Fourier estimate / FOURIER.  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and conditional end-to-end argument

The full target remains: independent real original coordinates with densities bounded by one, arbitrary real symmetric A having at least three eigenvalues of modulus at least one, and a universal bound for the density of Q=X^TAX. No Gaussian, moment, log-concavity, compact-support, connected-support, post-rotation independence, or pointwise scalar Fresnel-decay hypothesis is used here.

A sufficient full-target route would be:

1. extract from the three-large-eigenvalue hypothesis a physical cross block B having dimension-free Frobenius mass and either enough stable rank or a separately paid high-leverage/low-rank structure;
2. on the enough-stable-rank branch, prove `int_R |phi_Q(t)| dt <= C` directly;
3. apply Fourier inversion to obtain a continuous density with sup norm at most `C/(2pi)`;
4. route the complementary low-stable-rank/high-leverage collar into the already completed pair/ridge/hyperbolic mechanisms.

This run proves step 2 in a quantitatively stronger form than the preceding half-Riesz result. Step 1/complementary routing remains unpaid globally.

## 2. Named partner result consumed exactly

I use the completed account02/B02 theorem from

`yspennstate/math-open-problems@c726a32fa4d8e1e8ab246d48560b89cf1d4c4857`
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B02/20260922T221114Z-account02-B02-qform-r11-2ea3913a/REPORT.md`.

Its underlying independently checked regularized-determinant estimate states that for any quadratic-affine form R in cap-one independent ORIGINAL coordinates and any physical cross block B, with arbitrary self blocks and outside couplings,

`|phi_R(t)| <= det(I+c_q t^2 B B^T)^(-1/(4q)),`                 (2.1)

where

`c_q = 2q/(pi^2 e^2).`                                           (2.2)

For `1<=q<2`, (2.1) holds when on one physical side

`max_i (P_range(B))_ii <= q/2`;                                 (2.3)

for `q=2` the source supplies (2.1) with no leverage condition.

The previous partner run integrated (2.1) against `|t|^(-1/2)` to get a half-Riesz estimate. Here I integrate (2.1) with no weight.

## 3. Stable-rank compound lemma

Let the squared singular values of B be

`x_j=s_j(B)^2`, `S=sum_j x_j=||B||_F^2`, `m=max_j x_j=||B||_op^2`,

and `r=S/m=sr(B)`. For an integer k with `r>=k`,

`boxed(e_k(x_1,...,x_rk) >= S^k/k^k).`                           (3.1)

Here the notation `r_k` only denotes the number of nonzero singular values; the stable rank r need not be an integer.

Proof. Put `p_j=x_j/S`, so `max_j p_j=1/r`. Draw k iid indices with law p. The probability that all k draws are distinct is

`P_distinct = k! e_k(p_1,p_2,...).`                              (3.2)

Conditioned on the first l draws being distinct, their total p-mass is at most `l/r`; hence the next draw is new with conditional probability at least `1-l/r`. Therefore

`P_distinct >= prod_{l=0}^{k-1}(1-l/r)
             >= prod_{l=0}^{k-1}(1-l/k)=k!/k^k`,                 (3.3)

because r>=k. Combining (3.2)--(3.3) and rescaling by S^k proves (3.1). No dimension or rank upper bound is used.

## 4. Main theorem: genuine unweighted L1 Fourier control

### Theorem `QFORM-STABLERANK-L1-FOURIER-v1`

Assume the partner estimate (2.1) is available for parameters q and B. Let k be an integer satisfying

`k>2q` and `sr(B)>=k`.                                            (4.1)

Then

`boxed(
 int_R |phi_R(t)| dt
 <= C_(k,q) ||B||_F^(-1),
)`                                                               (4.2)

where

`C_(k,q)
 = [pi e/sqrt(2qk)]
   Beta(1/(2k), 1/(4q)-1/(2k)).`                                 (4.3)

Consequently R has a bounded continuous density and

`boxed(
 ||p_R||_infinity <= C_(k,q)/(2pi ||B||_F).
)`                                                               (4.4)

Proof. Expanding the determinant into elementary symmetric functions gives

`det(I+c_q t^2 BB^T)
 >= 1+c_q^k e_k(x)t^(2k).`                                       (4.5)

Hence by (2.1),

`|phi_R(t)|
 <= (1+c_q^k e_k(x)t^(2k))^(-1/(4q)).`                           (4.6)

Because k>2q, the beta integral converges and yields

`int_R (1+gamma t^(2k))^(-1/(4q)) dt
 = gamma^(-1/(2k))/k
   Beta(1/(2k),1/(4q)-1/(2k)).`                                  (4.7)

With `gamma=c_q^k e_k(x)`, (3.1) gives

`gamma^(-1/(2k))
 <= c_q^(-1/2) k^(1/2) ||B||_F^(-1).`                            (4.8)

Since `c_q^(-1/2)=pi e/sqrt(2q)`, substitution into (4.7) proves (4.2)--(4.3). Standard Fourier inversion for an integrable characteristic function gives a bounded continuous density and (4.4).

This theorem is genuinely unweighted L1 in time. It does not derive L1 from a density bound and does not assume pointwise one-dimensional quadratic-phase decay.

## 5. Three useful universal branches

Three convenient parameter choices are:

### (A) no leverage assumption
Take `q=2`, `k=5`. If

`sr(B)>=5`,                                                       (5.1)

then

`int |phi_R| <= 95.117693 ||B||_F^(-1),`                         (5.2)

and

`boxed(||p_R||_infinity <=15.138451 ||B||_F^(-1)).`              (5.3)

Continuity is proved.

### (B) moderate one-side leverage
Take `q=3/2`, `k=4`. If

`sr(B)>=4`, `max diag P_range(B)<=3/4`,                           (5.4)

then

`int |phi_R| <=78.285654 ||B||_F^(-1),`                          (5.5)

and

`boxed(||p_R||_infinity <=12.459549 ||B||_F^(-1)).`              (5.6)

Continuity is proved.

### (C) diffuse one-side range
Take `q=1`, `k=3`. If

`sr(B)>=3`, `max diag P_range(B)<=1/2`,                           (5.7)

then

`int |phi_R| <=61.550525 ||B||_F^(-1),`                          (5.8)

and

`boxed(||p_R||_infinity <=9.796071 ||B||_F^(-1)).`               (5.9)

Continuity is proved.

The general formula (4.3) also gives intermediate leverage thresholds by choosing q between 1 and 2; the constant diverges as k approaches `2q` from above, so a uniform proof still needs a quantitative gap.

## 6. Actual application to the live aggregate matching currency

The same partner report records the completed account01/B19 matching branch with two physical residual banks satisfying

`||B_1||_F^2 ||B_2||_F^2 >=1/768`,                              (6.1)

hence for a maximizing bank

`F=max_r ||B_r||_F >=768^(-1/4).`                                (6.2)

Applying the new theorem to that exact F gives the following **continuous-density** conclusions on the corresponding bank:

- if `sr(B)>=5`, no leverage assumption is needed and
  `||p_R||_infinity <79.694`;
- if `sr(B)>=4` and one-side leverage is at most `3/4`,
  `||p_R||_infinity <65.591`;
- if `sr(B)>=3` and one-side leverage is at most `1/2`,
  `||p_R||_infinity <51.570`.

These are direct unweighted-Fourier closures of the stated aggregate branches. They retain arbitrary self-curvature and outside couplings exactly as allowed by the partner determinant theorem. I do not infer that the global spectral hypothesis always forces the B19 matching branch or any one of these stable-rank/leverage alternatives.

## 7. Sharpened remaining collar

Relative to an O(1)-Frobenius cross packet, the unweighted Fourier problem is now confined to a quantitative collar:

1. `sr(B)<3`; or
2. `3<=sr(B)<4` with one-side range leverage exceeding `1/2` on every side to which (2.1) could be applied; or
3. `4<=sr(B)<5` with the relevant one-side range leverage exceeding `3/4`.

At `sr(B)>=5` there is no leverage obstruction at all.

This is strictly sharper for the integrated-Fourier assignment than the previous half-Riesz branch, which needed only `sr>=5/2` but did not yield unweighted L1. The two estimates are complementary: the half-Riesz theorem handles lower stable rank for density transducers; the present theorem gives direct continuity whenever sufficient compound rank is available.

## 8. First essential missing implication

`QFORM-L1-LOW-STABLERANK-HIGH-LEVERAGE-CLOSURE-v1`:

Starting from the actual full-target aggregate/matching reductions, prove that every dimension-free-Frobenius packet in the remaining collar of Section 7 is routed into one of the already completed physical-pair, ridge, one-sided-square, grouped-bank, or hyperbolic mechanisms, without replacing small self-curvature by zero and without selecting a vanishing local minor.

Equivalently, for a direct integrated-Fourier proof, one needs a second mechanism that pays the near-rank-two/near-coloop packets for which the determinant in (2.1) has too few uniformly macroscopic factors to be L1 by itself.

No source-valid counterexample to the full-target unweighted criterion `int |phi_Q(t)|dt <= C` was found. The global integrated-Fourier criterion therefore remains OPEN rather than refuted.

## 9. Status discipline

This report proves a new supporting theorem and its exact branchwise consequences. It does **not** prove the full quadratic-form conjecture, does not prove the global three-large-eigenvalue hypothesis forces a qualifying B, and does not claim novelty or publication priority. The branches above prove continuous densities; the full target's continuity remains open until all structural branches are closed.
