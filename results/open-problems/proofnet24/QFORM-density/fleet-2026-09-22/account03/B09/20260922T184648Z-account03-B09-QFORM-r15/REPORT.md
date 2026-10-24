SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B09, 2026-09-22T18:46:48Z.
attacking: translation-uniform half-Riesz smoothing for the first unpaid Schur residual, using a second physical square pivot or a genuine two-direction original-coordinate cross bank.

# account03/B09 QFORM r15 — second-pivot logarithmic smoothing and two-cross half-Riesz routing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Logical worker: `account03/B09`  
Run: `20260922T184648Z-account03-B09-QFORM-r15`  
Control observed before publication: `yspennstate/math-research-brain@3b492b0cd6eba9c9474d3fdcfb7b20a98a82cd54`, OWNER CONTROL revision `2026-09-22.11`  
Outcome: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The full target remains open: for independent real coordinates with densities bounded by one and every real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound `P{X^TAX in I}<=C|I|` for every interval `I`, or produce a valid target counterexample. Continuity remains a separate stronger conclusion.

## 1. Corrections and completed inputs actually used

This run does **not** use the refuted arbitrary-joint rank-three coarea `2/3` estimate, the refuted conditional projection-density moment, law-uniform pointwise quadratic-phase decay, post-rotation independence, or a one-small-minor reduction.

Completed inputs used in equations below:

1. **Arbitrary-rank quarter small-ball theorem.** `QFORM-ARBITRARY-RANK-QUARTER-SMALLBALL-v1`, source `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`, path `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`. For every nonzero symmetric `T`, arbitrary affine terms, and independent cap-one coordinates `Z`,

   `sup_w P{|Z^T T Z+b^TZ+d-w|<rho} <= min(1,5(rho/||T||)^(1/4)).`       (1.1)

2. **Scalar Schur singular-value inheritance.** account01/B09 `QFORM-SCHUR-SINGULAR-INHERITANCE-v1`, source present at `yspennstate/math-open-problems@d511859edaa636cdc00fcd64155ab07506875c3d`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/B09-20260922T174813Z-r15/REPORT.md`. If a nonzero physical scalar pivot is completed, then `s_{j+1}(S)<=s_j(T)` for the Schur remainder `T`; in particular `s_2(S)>=1` implies `||T||>=1` after any nonzero second scalar pivot.

3. **Rank-two original-coordinate cross Fourier endpoint.** The completed cross-block theorem used in account03/B09 r12 gives, for a physical cut with cross block `C` and two singular values `sigma_1,sigma_2>0`, while allowing arbitrary within-bank quadratic and affine terms,

   `|phi(t)| <= min(1, 2pi (sigma_1 sigma_2)^(-1/2)|t|^(-1)).`           (1.2)

4. **Nested-cut structural reduction.** account03/B20 `QFORM-NESTED-CUT-THREE-RESOURCE-v1`, canonical source `yspennstate/math-open-problems@06ef7346c08f41c3fac240e1acdeb1b42dc2995d`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260922T165009Z-account03-B20-QFORM-r13/REPORT.md`. Its unresolved heavy-pivot alternative supplies a genuine original coordinate with `|A_ii|>=157/320`.

5. **Fresh cross-account same-role result.** account02/B09 `QFORM-RANK3-BILINEAR-SCHUR-BANK-v1`, canonical source `yspennstate/math-open-problems@caa2cef304844e9d6f841acaf2e003f0bc1c24b5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260922T183809Z-account02-B09-QFORM-r7/REPORT.md`. It pays an exact-rank-three indefinite physical pair by aggregating its entire rank-one Schur bank before reciprocal minor inversion. In particular, whenever

   `R_ij:=|A_ij|^2 sum_{k!=i,j}|A_ik A_jk| >= r>0`,

   its zero-diagonal exact-rank-three theorem gives the actual inequality

   `||p_Q||_infinity <= 2^(5/4)sqrt(15) r^(-1/4).`                        (1.3)

   I therefore do not duplicate that exact-rank-three bank problem here; the new work below targets the higher-rank Schur residual left after a physical pivot.

The designated partner `account04/B09` still had no completed current-QFORM handoff or canonical current-QFORM research directory at the fresh checks, so no result is fabricated or awaited. Work continues asynchronously as directed.

## 2. New one-dimensional lemma: a physical square has only a logarithmic half-Riesz singularity after averaging its cap-one input

### Lemma 2.1 — `QFORM-SHIFTED-SQUARE-HALFRIESZ-LOG-v1`

Let `X` have a probability density `f<=1`. For every `a!=0`, every translation `m`, and every `c!=0`,

`E |a(X-m)^2+c|^(-1/2)
 <= |a|^(-1/2) [8+log_+(|a|/|c|)].`                                  (2.1)

Here `log_+(u)=max(log u,0)`.

### Proof

By changing signs inside the absolute value take `a>0`, and by translation take `m=0`.

**Case `c>=0`.** The kernel `(a x^2+c)^(-1/2)` is even and decreasing in `|x|`. Among all probability densities bounded by one, the bathtub/rearrangement principle maximizes its integral by the indicator of `[-1/2,1/2]`. Hence

`E(...) <= (2/sqrt(a)) asinh(sqrt(a)/(2sqrt(c))).`                      (2.2)

If `c>=a`, this is `<2/sqrt(a)`. If `0<c<a`, use

`asinh z <= log(1+2z)`

and `1+sqrt(a/c)<=2sqrt(a/c)` to obtain

`E(...) <= a^(-1/2)[2log2+log(a/c)]`,                                  (2.3)

which is stronger than (2.1).

**Case `c<0`.** Put `r=sqrt(|c|/a)`, so the kernel is

`a^(-1/2)|x^2-r^2|^(-1/2)`.

If `0<r<1`, use `f<=1` on `[-2,2]` and only total mass one outside it. Since for `|x|>2`, `|x^2-r^2|>=3`,

`E(...) <= a^(-1/2)[1 + integral_{-2}^2 |x^2-r^2|^(-1/2) dx]`
`       = a^(-1/2)[1+pi+2 arcosh(2/r)]`
`       <= a^(-1/2)[1+pi+2log4+2log(1/r)]`
`       = a^(-1/2)[1+pi+2log4+log(a/|c|)]`
`       < a^(-1/2)[8+log(a/|c|)].`                                     (2.4)

If `r>=1`, let `U` be the union of the two length-two intervals centered at `+r` and `-r`. On one such interval, writing distance from the root as `u in[0,1]`, the left and right contributions are bounded respectively by

`integral_0^1 [u(2r-u)]^(-1/2) du <=2/sqrt(r)<=2`,
`integral_0^1 [u(2r+u)]^(-1/2) du <=sqrt(2/r)<=sqrt2.`                  (2.5)

Both root neighborhoods therefore contribute `<4+2sqrt2`. Outside `U`, both factors `|x-r|` and `|x+r|` are at least one, so the kernel is at most `a^(-1/2)` and total remaining probability mass is at most one. Thus the whole expectation is `<8a^(-1/2)`, again (2.1). QED.

The divergence at `c=0` is only logarithmic after the physical cap-one average. The next lemma pays it using a genuine small-ball estimate for the remaining quadratic form, without square-root decoupling.

## 3. New theorem: a second physical scalar pivot pays the Schur half-Riesz problem

### Theorem 3.1 — `QFORM-HALFRIESZ-SECOND-PIVOT-v1`

Let `Y` have independent cap-one coordinates and let

`F(Y)=Y^T S Y+b^TY+d`

with real symmetric `S` satisfying

`s_2(S)>=1.`                                                               (3.1)

If some original coordinate satisfies

`|S_kk|>=1/2,`                                                             (3.2)

then, uniformly in `w`,

`boxed: E|F-w|^(-1/2) <= sqrt(2)[12+log(625/2)] <25.095.`                 (3.3)

### Proof

Write `a=S_kk` and complete the **original physical** variable `Y_k`:

`F = a(Y_k+m(Z))^2 + R(Z)`,                                               (3.4)

where `Z` consists of the remaining original coordinates, and the quadratic matrix `T` of `R` is the scalar Schur complement.

By `QFORM-SCHUR-SINGULAR-INHERITANCE-v1`,

`L:=||T|| >= s_2(S) >=1.`                                                 (3.5)

The affine terms induced in `R` are arbitrary, but (1.1) allows them. Thus for every center `u` and every `rho>0`,

`P{|R-u|<rho} <= min(1,5(rho/L)^(1/4)).`                                 (3.6)

In particular `R` has no atoms. Apply Lemma 2.1 conditionally on `Z` with `c=R-w` and average:

`E|F-w|^(-1/2)
 <= |a|^(-1/2)[8+E log_+(|a|/|R-w|)].`                                  (3.7)

Layer cake and (3.6) give

`E log_+(|a|/|R-w|)
 = integral_0^infinity P{|R-w|<|a|e^(-u)} du`
` <= integral_0^infinity min(1,5(|a|/L)^(1/4)e^(-u/4)) du`
` <= 4 + log_+(625|a|/L).`                                               (3.8)

Therefore

`E|F-w|^(-1/2)
 <= |a|^(-1/2)[12+log_+(625|a|/L)].`                                    (3.9)

Since `L>=1`, the right side is at most

`g(|a|)=|a|^(-1/2)[12+log(625|a|)]`

for `|a|>=1/2`. Its derivative has the sign of

`1-(1/2)[12+log(625|a|)]`,                                               (3.10)

which is already negative at `|a|=1/2` and decreases thereafter. Hence the maximum is attained at `|a|=1/2`, proving (3.3). QED.

This theorem is translation-uniform and allows every remaining spectral direction. It proves a fractional potential, not by itself a density statement.

## 4. New theorem: two genuine cross directions also pay the half-Riesz problem

### Theorem 4.1 — `QFORM-HALFRIESZ-TWO-CROSS-v1`

Let the same general quadratic-affine `F` have a disjoint original-coordinate cut `I,J` whose cross block `C=S[I,J]` has

`sigma_1(C)>=sigma_2(C)>=beta>0.`                                       (4.1)

Then

`boxed: sup_w E|F-w|^(-1/2) <= 8 beta^(-1/2).`                          (4.2)

### Proof

Put `Delta=sigma_1 sigma_2>=beta^2`. The original-coordinate cross-block Fourier theorem gives (1.2):

`|phi_F(t)|<=min(1,K/|t|)`, `K=2pi Delta^(-1/2)`.                       (4.3)

The Fourier transform of `|x|^(-1/2)` gives the standard half-Riesz representation

`E|F-w|^(-1/2)
 <=(2pi)^(-1/2) integral_R |t|^(-1/2)|phi_F(t)| dt.`                    (4.4)

The majorant in (4.3) makes this integral finite, and

`integral_R |t|^(-1/2)min(1,K/|t|)dt =8sqrt(K).`                        (4.5)

Substitution yields

`E|F-w|^(-1/2) <=8 Delta^(-1/4) <=8 beta^(-1/2).`                       (4.6)

No self block, sign, affine term, or extra eigenvalue was discarded. QED.

## 5. Exact routing when only `s_2(S)>=1` is known

This pays two of the three branches in the current Schur residual.

Let

`D=diag(S)`, `H=S-D`, `d=||D||_op=max_i|S_ii|.`                         (5.1)

If `d>=1/2`, Theorem 3.1 gives the universal half-Riesz bound `<25.095`.

Assume now `d<1/2`. By singular-value perturbation,

`s_2(H)>=s_2(S)-||D|| >=1-d.`                                           (5.2)

For a random Rademacher diagonal `R_eps`, put

`K_eps=(H-R_eps H R_eps)/2.`                                            (5.3)

After permuting the sign classes, `K_eps=[[0,C],[C^T,0]]` for an original-coordinate cut. Convexity of the Ky-Fan four-norm gives some cut with

`s_1(C)+s_2(C) >= s_2(H)/2 >=(1-d)/2.`                                 (5.4)

Hence either

`(A)  s_2(C)>=(1-d)/8`,                                                 (5.5)

or

`(B)  s_1(C)>3(1-d)/8` and `s_2(C)<(1-d)/8`.                           (5.6)

In branch (A), Theorem 4.1 yields

`sup_w E|F-w|^(-1/2)
 <=8 sqrt(8/(1-d)) <=32`,                                                (5.7)

because `d<1/2`.

Therefore the entire translation-uniform Schur half-Riesz problem under `s_2(S)>=1` is now reduced to one sharply stated geometry:

`QFORM-ONE-STRONG-CROSS-HALFRIESZ-v1`: all physical diagonals satisfy `|S_ii|<1/2`, while an original-coordinate cut has one strong cross singular value `>3/16` but its second cross singular value is below the two-direction threshold. The arbitrary same-bank curvature must still be retained; the known `(U+V)^2` control shows that one strong bilinear direction alone cannot simply be declared smoothing.

There is a further already-paid subcase of this residual. If the hollow part `H` itself has rank two and is in the one-bank-diffuse regime, account01/B09 `QFORM-HOLLOW-RANK2-ONEBANK-DIFFUSE-HALFRIESZ-v1` gives

`sup_w E|F-w|^(-1/2) <= C_RD gamma^(-1/2),`
`C_RD=32sqrt(10)2^(1/4),`                                               (5.8)

where its two nonzero hollow eigenvalues are `+/-gamma`. Here `gamma=s_2(H)>=1-d>1/2`, so that subcase is also uniformly paid. Thus the genuinely new remaining branch is a higher-rank or two-heavy-bank version of the one-strong-cross configuration.

## 6. Target-level consequence after one outer physical pivot

Let `A` satisfy the target spectral hypothesis `s_3(A)>=1` and suppose an original coordinate pivot obeys

`|A_ii|>=alpha>0.`                                                       (6.1)

Completing that physical square gives

`Q=A_ii(X_i+m(Y))^2+F(Y)`,                                              (6.2)

and scalar Schur singular-value inheritance gives `s_2(S)>=1` for the quadratic matrix `S` of `F`. The cap-one square pushforward yields for almost every `t`

`p_Q(t) <= |A_ii|^(-1/2) E|F-t|^(-1/2).`                               (6.3)

Consequently:

- if the Schur residual has a physical diagonal `>=1/2` in modulus,

  `||p_Q||_infinity <25.095/sqrt(alpha)`;                               (6.4)

- if the low-diagonal Schur residual falls in the two-cross branch (5.5),

  `||p_Q||_infinity <=32/sqrt(alpha)`.                                  (6.5)

Apply this to the actual heavy pivot `alpha=157/320` supplied by `QFORM-NESTED-CUT-THREE-RESOURCE-v1`. The two paid branches become

`boxed: ||p_Q||_infinity <35.827`                                      (6.6)

and

`boxed: ||p_Q||_infinity <45.686`,                                     (6.7)

respectively, hence the same constants multiply `|I|` in the interval inequality `P{Q in I}`.

Thus the B20 physical-pivot alternative is no longer generically unpaid. After the outer pivot, only the explicit one-strong-cross Schur configuration (plus its already-paid rank-two diffuse subcase) remains.

## 7. Why this is a real mechanism change

The preceding B09 runs emphasized local indefinite pairs, rank-two Schur products, ridge smoothing, and conditional spectral counterexamples. This run instead proves a **fractional-potential bridge**: a second physical square has a logarithmic singularity, and a completely general quarter-power small-ball estimate on the remaining Schur form integrates that logarithm. No selected third coordinate is inverted and no conditional fiber supremum is taken.

The mechanism is complementary to account02/B09 r7: that result aggregates a rank-one Schur bank in exact rank three; the present argument tolerates an arbitrary-rank Schur remainder whenever a second physical pivot exists, because only its operator-scale small-ball estimate is used.

## 8. Scope and next exact implication

Proved this run:

- `QFORM-SHIFTED-SQUARE-HALFRIESZ-LOG-v1`;
- `QFORM-HALFRIESZ-SECOND-PIVOT-v1`;
- `QFORM-HALFRIESZ-TWO-CROSS-v1`;
- the routing (5.1)-(5.7), reducing the `s_2(S)>=1` half-Riesz problem to the one-strong-cross geometry;
- explicit target-level constants (6.6)-(6.7) on two large pieces of the current B20 heavy-pivot branch.

Not proved:

- `QFORM-ONE-STRONG-CROSS-HALFRIESZ-v1` in arbitrary same-bank curvature/higher-rank scope;
- the zero/near-zero outer-pivot global branch;
- the full QFORM conjecture;
- continuity of the new density branches. The arguments above establish essential boundedness through interval/density domination only.

The next B09 step should attack the one-strong-cross branch by keeping the full same-bank quadratic forms inside a two-bank operator inequality, rather than conditioning to a rotated singular coordinate. A successful bound there would complete `QFORM-SCHUR-HALFRIESZ-TWO-LARGE-v1` and would close every target matrix possessing the B20-sized physical pivot; the remaining global problem would then be the zero/near-zero physical-pivot branch.

## 9. Finite constant check

`verify_constants.py` and `CHECKS.txt` in this run directory evaluate only the displayed constants and the monotonicity sign in (3.10):

- second-pivot half-Riesz constant `25.094660299255583`;
- after `alpha=157/320`, `35.826673350780275`;
- two-cross half-Riesz constant `32`;
- after `alpha=157/320`, `45.68515905588798`;
- derivative numerator at `a=1/2`: `-7.872302234588229`.

Those computations are diagnostics, not substitutes for the analytic proofs above.
