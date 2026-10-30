SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-22T22:11:14Z.
attacking: integrated Fourier estimate — convert aggregate physical cross energy into a translation-uniform half-Riesz bound with arbitrary self-curvature, and identify the exact low-effective-rank obstruction.

# fleet02/B02 — arbitrary-self stable-rank half-Riesz Fourier estimate

**Run:** `20260922T221114Z-fleet02-B02-qform-r11-2ea3913a`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Live owner revision:** `2026-09-22.15`  
**Assignment:** Integrated Fourier estimate / FOURIER  
**Classification:** `ESSENTIAL_STEP_APPLIED + CANDIDATE_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction discipline

The target remains the full arbitrary-product-law statement: independent real coordinates with one-dimensional probability densities bounded by one, and a real symmetric matrix with at least three eigenvalues of modulus at least one; prove a universal essential density bound for `Q=X^T A X`, or give a valid target counterexample.

This run uses no moment hypothesis, no diagonal-basis independence, no law-uniform pointwise Fresnel decay, no arbitrary-joint coarea bound, no positive conditional projection-density moment, no fixed-good-minor principle, and no conditional density cap created by rotation. All coordinate banks below are ORIGINAL coordinate banks. The new estimate retains arbitrary quadratic self-blocks on both sides and arbitrary outside curvature.

The principal analytic input is the completed regularized determinant theorem

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`
`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`,

whose Sections 4--6 were independently checked by this slot in an earlier run. For a physical cross block `B=A[I,J]`, it gives, for `1<=q<2`, under the one-side range-leverage condition

`max_i (P_range(B))_ii <= q/2`,

and with no leverage condition for `q=2`,

`|phi_R(t)| <= det(I + c_q t^2 B B^T)^(-1/(4q)),`
`c_q=2q/(pi^2 e^2).`                                                (1.1)

The source allows arbitrary self phases and outside couplings.

## 2. Weighted determinant lemma

For a real random variable `R`, write

`H_1/2(R)=sup_a E |R-a|^(-1/2).`

Let the squared singular values of `B` be `x_j=s_j(B)^2`, and let

`E_k(B)=e_k(x_1,...,x_r)`.

If `k>q`, (1.1) implies

`boxed(
 H_1/2(R) <= H_(k,q) E_k(B)^(-1/(4k)),
)`                                                                    (2.1)

where

`H_(k,q)= [sqrt(e)/(k 2^(3/4) q^(1/4))]
           Beta(1/(4k), 1/(4q)-1/(4k)).`                             (2.2)

Proof. The nonnegative determinant expansion gives

`det(I+c_q t^2 BB^T) >= 1+c_q^k E_k(B)t^(2k).`                       (2.3)

The Gaussian-regularized half-Riesz Fourier identity, already justified in the earlier B02 square-assisted theorem, gives

`H_1/2(R)
 <= (1/sqrt(2pi)) int_R |t|^(-1/2)|phi_R(t)|dt.`                    (2.4)

The exact beta substitution yields

`int_R |t|^(-1/2)(1+gamma t^(2k))^(-1/(4q))dt
 = gamma^(-1/(4k))/k
   Beta(1/(4k),1/(4q)-1/(4k)),`                                    (2.5)

which is finite exactly when `k>q`; inserting `gamma=c_q^kE_k(B)` gives (2.1)--(2.2). No pointwise scalar oscillatory estimate is used.

This weighted estimate was implicit inside the earlier square-assisted theorem. The new step is to convert it to dimension-free **Frobenius currency with arbitrary self-curvature** by stable-rank inequalities, and to identify the sharp mechanism obstruction at low effective rank.

## 3. Stable-rank conversion

Put

`F=||B||_F`, `S=F^2=sum_j x_j`,
`r_s=sr(B)=S/max_j x_j`.

### Lemma 3.1: second compound

For every nonzero `B`,

`E_2(B) >= (1-1/r_s) S^2/2.`                                       (3.1)

Indeed `E_2=(S^2-sum x_j^2)/2`, while

`sum x_j^2 <= (max x_j)S=S^2/r_s`.

Hence, if `r_s>=3/2`,

`E_2(B)>=S^2/6.`                                                    (3.2)

### Lemma 3.2: third compound under stable rank at least 5/2

If `r_s>=5/2`, then

`boxed(E_3(B)>=S^3/32.)`                                           (3.3)

Proof. Write `m=max x_j=S/r_s`. First suppose `5/2<=r_s<=4`. Under the constraints `0<=x_j<=m` and fixed sum `S`, concentrating two coordinates until they equal `m` can only decrease `e_3`: for two coordinates `a,b`, with the others fixed, the dependence on the pair at fixed `a+b` is `ab * (sum of the remaining coordinates)` plus terms depending only on `a+b`; making the pair more unequal decreases `ab`. Repeating gives the packed minimizer. In particular its contribution from triples containing the first two packed masses is

`m^2(S-2m)=S^3 (r_s-2)/r_s^3.`                                    (3.4)

The function `(r-2)/r^3` on `[5/2,4]` has minimum `1/32` at the right endpoint (the other endpoint is `0.032>1/32`), proving (3.3) in this range.

For `r_s>=4`, Newton's identity gives

`E_3=(S^3-3S sum x_j^2+2 sum x_j^3)/6
    >= S^3(1-3/r_s)/6
    >= S^3/24`,                                                     (3.5)

which is stronger than (3.3). QED.

## 4. Main theorem — arbitrary self-blocks paid by aggregate stable rank

### Theorem `QFORM-ARBITRARY-SELF-STABLERANK-HALFRIESZ-v1`

Let `R` be any quadratic-affine form in independent cap-one original coordinates, and let `B` be any physical cross block between two disjoint original-coordinate banks. All same-bank quadratic terms and all outside couplings may be arbitrary.

**High-effective-rank branch.** If

`sr(B)>=5/2`,                                                        (4.1)

then without any leverage hypothesis,

`boxed(
 H_1/2(R) <= C_hi ||B||_F^(-1/2),
 C_hi=H_(3,2) 32^(1/12)=13.13569963967... .
)`                                                                    (4.2)

This is (2.1) at `q=2,k=3` plus (3.3).

**Intermediate-effective-rank diffuse-range branch.** If

`sr(B)>=3/2`                                                         (4.3)

and on at least one side the coordinate leverage of `range(B)` is at most `3/4`, then

`boxed(
 H_1/2(R) <= C_mid ||B||_F^(-1/2),
 C_mid=H_(2,3/2) 6^(1/8)=17.59621620368... .
)`                                                                    (4.4)

This is (2.1) at `q=3/2,k=2` plus (3.2).

Thus an arbitrary-self Frobenius packet is now analytically paid except for a quantitatively low-effective-rank/high-leverage collar. In particular, a cross bank failing both fixed branches must satisfy

`sr(B)<5/2`, and if `sr(B)>=3/2` then some physical coordinate has range leverage `>3/4`.                                          (4.5)

This is a source-valid reduction to a near-rank-one / near-coloop geometry, not a claim that such a bank is globally forced by `s_3(A)>=1`.

## 5. A genuine counterexample to the unrestricted Frobenius half-Riesz upgrade

The stable-rank qualification cannot simply be deleted.

Let `X,Y` be independent `Uniform[-1/2,1/2]`, and set

`R=(X+Y)^2=X^2+2XY+Y^2.`                                            (5.1)

Across the one-coordinate cut the physical cross block is `B=[1]`, so `||B||_F=1`. But `S=X+Y` has triangular density

`p_S(s)=1-|s|`, `|s|<=1`.

Therefore

`H_1/2(R)>=E R^(-1/2)=E |S|^(-1)
 =2 int_0^1 (1-s) ds/s = infinity.`                                (5.2)

So there is **no** universal theorem of the form

`H_1/2(R)<=C ||B||_F^(-1/2)`                                       (5.3)

for arbitrary self-curvature and merely nonzero cross Frobenius mass. This refutes that tempting strengthening of the completed zero-self Frobenius theorem. It is a mechanism counterexample, not a counterexample to the owner QFORM target.

## 6. Application to the live arbitrary-self matching gap

The completed fleet01/B19 S0 matching theorem is source-pinned at

`yspennstate/math-open-problems@39451a4c1065252ae9485eb99bdb5bb2c40f97f0`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B19/20260922T201657Z-fleet01-B19-QFORM-r11/REPORT.md`.

Inside its already-established matching branch it supplies two physical residual cross banks with

`||B_1||_F^2 ||B_2||_F^2 >=1/768`,                                (6.1)

hence one bank has

`F=max_r ||B_r||_F >=768^(-1/4).`                                  (6.2)

It also uses the genuine scalar-square transducer

`||p_Q||_infinity <= |a|^(-1/2) H_1/2(R).`                         (6.3)

Consequently, **without any zero-self assumption on the selected source bank**:

- if the maximizing bank has `sr>=5/2`, then

  `H_1/2(R)<30.139`, and on the existing subbranch `|a|>=1/4`,

  `boxed(||p_Q||_infinity<60.278);`                                (6.4)

- if instead it has `sr>=3/2` and one-side range leverage `<=3/4`, then

  `H_1/2(R)<40.373`, and on `|a|>=1/4`,

  `boxed(||p_Q||_infinity<80.746).`                                (6.5)

Therefore the arbitrary-self Frobenius-matching debt is narrowed to the explicit low-stable-rank/high-leverage collar (4.5). This is the first unpaid implication left by this theorem, not a relabeling of the full target.

## 7. Named partner fleet03/B02 applied to an actual inequality

The latest completed designated-partner result is fleet03/B02 r15,

`QFORM-ONE-SIDED-SQUARE-RANK2-FOURIER-v1`,
`yspennstate/math-open-problems@328f301cc05ac55f7dd9e3f2534890e63495470e`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T210429Z-fleet03-B02-qform-r15/REPORT.md`.

In its exact rank-two one-sided-isolation setting it proves, for arbitrary product cap-one banks,

`||p_Q||_infinity <7.019062 |d|^(-1/4) Delta^(-3/8),`             (7.1)

where `Delta=s_1(B)s_2(B)`.

For an exact-rank-two block with `sr(B)>=3/2`, Lemma 3.1 gives

`Delta^2=E_2(B)>=||B||_F^4/6.`                                    (7.2)

Substitution into the **partner theorem** yields the new Frobenius-form inequality

`boxed(
 ||p_Q||_infinity
 < 7.019062 * 6^(3/16)
   |d|^(-1/4)||B||_F^(-3/4)
 < 9.822 |d|^(-1/4)||B||_F^(-3/4).
)`                                                                    (7.3)

For comparison with the matching currency, if additionally `||B||_F>=768^(-1/4)` and `|d|>=1/4`, then (7.3) gives

`boxed(||p_Q||_infinity<48.273).`                                  (7.4)

This is an equation-level use of the named partner's completed integrated-Fourier theorem. The one-sided isolation required by that theorem is retained exactly; it is not inferred from stable rank or from the global spectral hypothesis.

## 8. First unpaid implication and full-target status

The new analytic frontier is now concrete:

`QFORM-LOW-STABLERANK-HIGH-LEVERAGE-ARBITRARY-SELF-v1` — in the live matching/Schur reduction, handle the case where every O(1)-Frobenius residual cross bank either has stable rank `<3/2`, or has stable rank below `5/2` and contains a physical range leverage `>3/4`. Route this near-rank-one / near-coloop geometry into the completed pair-log, rank-two, ridge, one-sided-square, or aggregate hyperbolic mechanisms without replacing merely small self-curvature by zero and without selecting a vanishing local minor.

The rank-one construction (5.1) shows why some extra structure is genuinely necessary for a half-Riesz argument with arbitrary self blocks. The partner r15 theorem pays one important exact-rank-two isolated subcase, but no source-valid argument currently forces that isolation from `s_3(A)>=1`.

No target-valid counterexample to the unweighted full-target criterion `int |phi_Q(t)|dt<infinity` was found here. The stronger Fourier criterion therefore remains open, not refuted. The owner QFORM conjecture remains **OPEN**.

## 9. Deterministic checks

`CHECK.py` and `CHECKS.txt` record the beta constants, matching-branch numerical substitutions, the exact truncated divergence formula in (5.2), and deterministic random regression checks of (3.2)--(3.3). These computations are checks only; Sections 2--8 are analytic.

No novelty or publication-priority claim is made.
