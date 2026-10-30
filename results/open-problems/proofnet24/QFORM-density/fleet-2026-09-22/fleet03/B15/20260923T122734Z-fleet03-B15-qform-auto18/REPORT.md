# Uniform small-ball trace closure for rough quadratic-form limits

**Run:** `20260923T122734Z-fleet03-B15-qform-auto18`  
**Account/slot:** fleet03/B15  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / UNIFORM_INTERVAL_PROFILE_TRACE / MOVING_SHEET_TRACE`  
**Full universal QFORM theorem:** OPEN  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and exact scope

The target is: for independent real coordinates with probability densities `0<=f_i<=1`, and real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound on the density of `Q=X^T A X`, or give a valid counterexample. The present run does **not** prove the missing universal estimate. It supplies a precise rough-law/trace compiler for direct small-ball estimates and moving critical-sheet submeasures.

The newest owner delivery plan assigns B15 to supply exactly such a rough-law trace justification for new density estimates. The principal source applied below is the volume-stability theorem at

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

The designated fleet04/B15 partner result applied below is the exact Gaussian heat-height theorem at

`yspennstate/math-open-problems@ad7e5daa036cc8330b1432285ad40fec611d37dd`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T211430Z-fleet04-B15-heat-regularity-r4/REPORT.md`.

No pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea estimate, fiber supremum, moment condition, compact support, or small-random-perturbation premise is used.

## 2. Absolute continuity is automatic for every nonconstant quadratic polynomial

This is qualitative only and contains no uniform height information.

### Lemma 2.1

Let `nu << dx` be any absolutely continuous probability law on `R^n`, and let

`q(x)=x^T A x+b^T x+c`

be nonconstant. Then `q_# nu << dt`.

### Proof

Let `N subset R` have Lebesgue measure zero. The critical set

`C={x: grad q(x)=2Ax+b=0}`

is either empty or a proper affine subspace because `q` is nonconstant; hence `|C|=0`.

For integers `R,k>=1`, put

`E_(R,k)=q^{-1}(N) cap B(0,R) cap {|grad q|>=1/k}`.

The locally Lipschitz coarea formula gives

`int_(E_(R,k)) |grad q(x)| dx
 = int_N H^(n-1)(E_(R,k) cap q^{-1}(t)) dt =0`.

Since `|grad q|>=1/k` on `E_(R,k)`, this implies `|E_(R,k)|=0`. The complement of `C` is the union of the `B(0,R) cap {|grad q|>=1/k}`, so `|q^{-1}(N)|=0`. Because `nu<<dx`, `nu(q^{-1}(N))=0`. Thus `q_#nu<<dt`. QED.

For the target `A` has rank at least three, so `q(x)=x^T A x` is nonconstant. Hence absolute continuity is already unconditional under the target hypotheses. This says nothing about a universal `L^infinity` norm or continuity of a representative.

## 3. Uniform interval-profile convergence at atomless weak limits

### Theorem 3.1 (all centers and all widths)

Let probability measures `mu_m => mu` weakly on `R`, and suppose `mu` is atomless. Then, writing `F_m,F` for their distribution functions,

`d_K(mu_m,mu):=sup_t |F_m(t)-F(t)| ->0`,                         (3.1)

and consequently

`sup_(a<=b) |mu_m((a,b])-mu((a,b])| <=2 d_K(mu_m,mu) ->0`.     (3.2)

Thus weak convergence to an atomless law gives uniform convergence of the **entire unnormalized small-ball profile**, simultaneously in the center and interval width.

### Proof

Weak convergence gives `F_m(t)->F(t)` at every continuity point of `F`. Atomlessness makes `F` continuous everywhere. We recall the elementary uniformity argument.

Fix `eta>0`. Choose `L<R` such that `F(L)<eta` and `1-F(R)<eta`. By uniform continuity of the monotone continuous function `F` on `[L,R]`, choose a finite partition

`L=t_0<t_1<...<t_N=R`

such that every increment `F(t_j)-F(t_(j-1))<eta`. For all sufficiently large `m`,

`max_j |F_m(t_j)-F(t_j)|<eta`.

If `t_(j-1)<=t<=t_j`, monotonicity gives

`F_m(t_(j-1))<=F_m(t)<=F_m(t_j)`

and similarly for `F`, hence `|F_m(t)-F(t)|<=2eta`. The tails are bounded by at most `2eta` in the same way using `F(L)<eta` and `1-F(R)<eta`. Therefore `sup_t|F_m-F|->0`, proving (3.1).

For every `a<=b`,

`mu_m((a,b])-mu((a,b])=[F_m(b)-F(b)]-[F_m(a)-F(a)]`,

which proves (3.2). QED.

### Remark 3.2

The normalization by interval length is deliberately absent. Equation (3.2) does **not** imply

`sup_I |mu_m(I)-mu(I)|/|I| ->0`.

That stronger statement would be false without additional regularity. The theorem is nevertheless exactly sufficient to pass a **common** linear small-ball estimate to a limit.

## 4. Simultaneous rough-input and coefficient trace

### Theorem 4.1

Fix `n`. For each `m`, let

`nu_m=mu_(1,m) tensor ... tensor mu_(n,m)`

where every `mu_(i,m)` is a probability law with density bounded by one. Suppose

`mu_(i,m) => mu_i` for every `i`,

and let

`q_m(x)=x^T A_m x+b_m^T x+c_m`,
`q(x)=x^T A x+b^T x+c`,

with `(A_m,b_m,c_m)->(A,b,c)`. If `q` is nonconstant, then:

1. every limiting marginal `mu_i` again has a density bounded by one;
2. `nu_m=>nu:=tensor_i mu_i`;
3. `q_m#nu_m => q#nu`;
4. the complete interval-mass profiles converge uniformly:

`sup_(a<=b) |P(q_m(X_m) in (a,b])-P(q(X) in (a,b])| ->0`.     (4.1)

### Proof

For every nonnegative `phi in C_c(R)`,

`int phi dmu_i = lim_m int phi dmu_(i,m) <= int phi(x) dx`.

Hence `mu_i<=dx` as measures, so `mu_i=f_i dx` with `0<=f_i<=1`. Finite products preserve weak convergence, giving `nu_m=>nu`.

Coefficient convergence gives `q_m->q` uniformly on every compact subset of `R^n`. The sequence `nu_m` is tight. Therefore, for every bounded continuous `g` on `R`, choose a compact `K` carrying all but `eta` mass of `nu_m` and `nu` for large `m`; on `K`, `g(q_m)-g(q)->0` uniformly after restricting `g` to the compact range generated by `q_m(K),q(K)`. Combining this with weak convergence of `nu_m` against the fixed bounded continuous function `g o q` yields

`int g(q_m) dnu_m -> int g(q) dnu`.

Thus `q_m#nu_m=>q#nu`.

The limiting product `nu` is absolutely continuous. Since `q` is a nonconstant polynomial, each level set `{q=t}` has Lebesgue measure zero; hence `q#nu` is atomless. Apply Theorem 3.1 to obtain (4.1). QED.

### Corollary 4.2 (zero-loss density trace)

Under the hypotheses of Theorem 4.1, assume one constant `C<infinity` satisfies

`P(q_m(X_m) in I) <= C |I|`                                     (4.2)

for every interval `I` and every `m`. Then

`P(q(X) in I)<=C|I|` for every interval `I`,                     (4.3)

and therefore `q(X)` has a density `p` with `||p||_infinity<=C`.

Proof: fix `I`, use (4.1), and let `m->infinity`. The interval estimate (4.3) implies domination of the output measure by `C dt` first on intervals and then on Borel sets by regular approximation. QED.

This is the direct-small-ball analogue of lower semicontinuity of density height, but is stronger at the level of unnormalized profiles because the center and width may both vary with `m` in (4.1).

## 5. Quantitative coupling variant

If `Y_m,Y` are coupled, `Y` has a density bounded by `B`, and

`P(|Y_m-Y|>r)<=eta`,

then for every `t`,

`F_Y(t-r)-eta <= F_(Y_m)(t) <= F_Y(t+r)+eta`.

Hence

`d_K(L(Y_m),L(Y)) <= eta+B r`,                                  (5.1)

and Theorem 3.1 gives

`sup_I |P(Y_m in I)-P(Y in I)| <=2(eta+B r)`.                  (5.2)

This is useful when an actual probabilistic coupling supplies `(r,eta)`. It does **not** authorize a law-uniform rate from a small operator-norm matrix perturbation: arbitrary cap-one inputs can live arbitrarily far away, and previous target-valid examples refute such a uniform matrix modulus.

## 6. Moving critical-sheet trace

The previous theorem treats full pushforwards. Conditional geometric proofs often produce a moving one-sheet/minority decomposition, so a separate trace statement is needed.

### Theorem 6.1

Let `nu_m=>nu` be probability measures on `R^n`. Let continuous functions

`q_m,r_m:R^n->R`

converge locally uniformly to continuous `q,r`. Assume

`nu({r=0})=0`.                                                  (6.1)

Define finite subprobability measures on `R` by

`sigma_m(B)=nu_m({x:r_m(x)>=0, q_m(x) in B})`,
`sigma(B)=nu({x:r(x)>=0, q(x) in B})`.

Then `sigma_m=>sigma` weakly. In particular, if

`sigma_m <= C dt`                                               (6.2)

for every `m` with one constant `C`, then

`sigma <= C dt`.                                                (6.3)

### Proof

Set `T_m=(q_m,r_m)` and `T=(q,r)`. Tightness of `nu_m`, together with local uniform convergence `T_m->T`, gives

`(T_m)#nu_m => T#nu`.

Indeed, for a bounded continuous test function on `R^2`, work on a common high-mass compact set and use uniform convergence there, then use weak convergence for the fixed composition with `T`.

For `psi in C_c(R)`, the bounded function

`G(u,v)=psi(u) 1_{v>=0}`

is discontinuous only on `{v=0}`. Assumption (6.1) says `(T#nu)({v=0})=0`; therefore the portmanteau theorem for bounded functions continuous almost everywhere under the limiting law yields

`int psi d sigma_m -> int psi d sigma`.

This is weak convergence. If (6.2) holds, then for every nonnegative `psi in C_c(R)`,

`int psi d sigma = lim_m int psi d sigma_m <= C int psi(t)dt`,

which is exactly (6.3). QED.

For quadratic-form applications, if `r` is a nonzero polynomial and `nu` is an absolutely continuous product law, then (6.1) is automatic because a nonzero polynomial zero set has Lebesgue measure zero. Thus a density estimate proved on a moving one-sheet or moving Schur-critical-value submeasure survives simultaneous rough-law and coefficient limits with no loss in the constant, provided the limiting sheet polynomial is nontrivial.

## 7. Actual application of the newest volume theorem and fleet04/B15 partner theorem

The owner-pinned volume-stability result proves that if an original-coordinate cross block satisfies

`M=M0+E`, `s3(M0)>=a>0`, `max_i (P_range(M0))_ii<=1/2`, `||E||op<=a/16`,

then the full quadratic-plus-affine output, retaining arbitrary within-bank quadratic terms, outside couplings and affine terms, has a continuous density with

`||p_Q||_infinity <= B_a := 24 sqrt(3) e/(5a) <23/a`.          (7.1)

Now take **any** fixed-dimensional sequence of such certified instances with the same `a`, while allowing their cap-one input marginals to vary weakly and all coefficients to converge. Assume only that the limiting quadratic polynomial is nonconstant. Corollary 4.2 gives directly

`P(Q in I) <= B_a |I|` for every interval `I`,                  (7.2)

so

`||p_Q||_infinity <= B_a`.                                     (7.3)

This is a zero-loss rough-law/coefficient closure of the certified estimate. No continuity of the limiting density is required for (7.3).

Now apply the completed designated partner fleet04/B15 theorem to an actual inequality. Its exact heat-height identity says for every probability law `rho`, with value `+infinity` when no bounded density exists,

`sup_(epsilon>0,y) (rho*gamma_epsilon)(y)=||p_rho||_infinity`.

Combining it with (7.3) gives the target-level positive-kernel estimate

`sup_(epsilon>0,y) E gamma_epsilon(Q-y)
 <= 24 sqrt(3) e/(5a) <23/a`.                                  (7.4)

Conversely, for each approximating certified instance (7.1) implies by the same partner identity

`E gamma_epsilon(Q_m-y)<=B_a` for every `epsilon,y`.

Weak convergence of `Q_m` to `Q` passes this fixed bounded-continuous Gaussian test to the limit, giving the same inequality for every `epsilon,y`; taking the supremum and using the partner theorem again recovers (7.3). Thus the direct interval trace and the Gaussian heat trace agree on the exact constant.

The new content relative to fixed-heat convergence is (4.1): the direct interval masses converge uniformly over **all** centers and widths, which is the natural interface for future small-ball/coarea proofs.

## 8. Continuity is separate

This run proves:

- unconditional absolute continuity for every target quadratic output (Lemma 2.1);
- zero-loss preservation of common `L^infinity` estimates under simultaneous rough-input/coefficient limits (Corollary 4.2);
- zero-loss preservation for moving critical-sheet submeasures (Theorem 6.1).

It does **not** infer continuity of the limiting density from these trace principles. Such an inference is invalid in general: smooth uniformly bounded densities can converge in total variation to a discontinuous bounded density (for example Gaussian mollifications of `1_[0,1]`). Uniform height plus weak/TV convergence therefore does not preserve `C_0` regularity.

The live shared `CLAIMS.json` still lists `QFORM-CONTINUOUS-REPRESENTATIVE` as OPEN. The completed fleet04/B15 report source-reports a separate completed chain proving a matrix-dependent `C_0` density for every fixed rank-at-least-three instance; this run does not independently re-review that full chain and therefore does not alter the shared claim status. In any case, continuity is not used in (4.2)-(7.4).

## 9. Why this helps the remaining full proof

A future proof may now work on a dense or regularized family where the geometric/Fourier estimate is easiest and pass its **direct interval estimate** to arbitrary cap-one rough marginals and coefficient-boundary instances with exactly the same constant, provided the estimate was genuinely uniform before taking the limit. Likewise, a one-sheet estimate with a coefficient-dependent critical polynomial can be traced through the limit without freezing the sheet.

What this theorem cannot do is manufacture uniformity. If the available constants diverge as a minor, leverage parameter, or tail scale degenerates, trace closure does not repair that divergence. The first unpaid target-level step remains a uniform estimate on the near-null/high-leverage or low-cross-rank survivors of the current volume/ridge exits.

## 10. Provenance and integrity


The explicit changed-file allowlist in `math-open-problems` for this run is only this run directory (`CHECKPOINT.md`, `REPORT.md`, and later receipt/readback files if created). Manual fallback privacy review found only mathematical statements, public bibliographic/source pins, logical account/slot labels, and repository commit/path metadata; no credentials, signed URLs, unrelated personal data, client data, or private nonmathematical material are included.

Repository retrieval/writes are not native learned-memory ingestion. No authenticated native mathematical receiver was used, so status remains `WITHOUT_VERIFIED_BRAIN`.
