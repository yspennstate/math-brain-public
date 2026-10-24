# account02/B04 independent fixed-multiplicity audit r24

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`.

- source SHA-256 advertised by the owner/package: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`
- git blob independently read from the pinned commit: `183ccd294763214e6a707e8d4749ff9a8cf7006d`
- manuscript length: 790 source lines
- current manuscript blob on master during this run: unchanged at `183ccd294763214e6a707e8d4749ff9a8cf7006d`

## Verdict

**Baseline 17-eigenvalue manuscript: PASS in this independent B04 review.** I read the complete 790-line source during this invocation and independently re-derived the sensitive analytic and algebraic steps. I found no FALSE statement and no mathematical GAP in the written theorem

` s_17(A)>=s>0  =>  ||p_(X^TAX+b^TX+c)||_infinity <= 10000 K^2/s.`

This is one independent review, not a self-awarded independent-validation certificate. The unrestricted three-eigenvalue QFORM conjecture is not solved here.

**Repository package: GAP (reproducibility metadata/checker missing).** Fresh master contains `README.md`, `AUDIT.md`, `manuscript.tex`, `audits/`, and `improvements/`, but not the `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, or `checks.json` named by the README/current objective. `SOURCE_MANIFEST.json` was also fetched directly and returned not found. Those four items are therefore **UNCHECKED because absent**, not silently treated as passing. This package gap does not alter the mathematical verdict because the proof is self-contained in `manuscript.tex`.

## End-to-end source audit

| Source lines | Statement / dependency | Status | Independent reasoning, impact, next obligation |
|---|---|---|---|
| 1--74 | Definitions, theorem quantifiers, normalization, architecture | PASS | Singular values are correctly identified with absolute eigenvalues for symmetric `A`; all dimensions, signs, affine terms, remaining spectrum and arbitrary rough product laws are retained. Final `Y=KX` and `Q=(s/K^2)Qtilde` scaling gives `K^2/s`. |
| 75--129 | Fourier normalization, Plancherel, Gaussian inversion, power envelope | PASS | `g_epsilon` has transform `e^{-epsilon t^2}` under the stated convention. Gaussian regularization plus the `L^2` approximate identity proves Plancherel; `phi in L^1` gives a bounded continuous density. The envelope integrates to `2ap/(p-1)`. |
| 130--169 | Riesz/negative-half-moment formula | PASS | Tonelli is applied to nonnegative gamma/Gaussian representations. The inner integral is `sqrt(2) Gamma(1/4)|t|^{-1/2}` and the `3/4` envelope contributes exactly `12 sqrt(u)`. |
| 170--218 | Singular-value perturbation, Schur spectral count, diagonal dominance | PASS | Approximation numbers justify both nonsymmetric singular-value inequalities. The Schur count follows from the complementary compression of `A^{-1}` and survives singular `A` by `A+epsilon I` with the threshold relaxed before the limit. Strict row dominance is valid without symmetry. |
| 219--255 | Geometric Brascamp--Lieb heat flow | PASS | Rebuilt in detail below; no missing boundary term, nonintegrable majorant, or unjustified endpoint exchange found. |
| 257--309 | Product-projection density and scalar Fourier powers | PASS | Orthogonal maps occur only in deterministic integrals. The physical product density is never rotated and then declared independent. `-b log b<=1-b` gives `e^{d/2}`; the `m=floor(p/2)` argument gives the stated scalar Fourier constant. |
| 311--421 | Decoupling, graph BL, regularized determinant, volume envelopes | PASS | Copying only an original product bank is legitimate; difference densities stay cap one. Graph weights form an exact frame. The `d_i` powers cancel and `alpha=(2 pi e)^2` cancels the entropy tax, yielding determinant exponent `-1/8`. `k=5` is directly integrable; `k=3` is used only with the half-potential weight. |
| 422--519 | Scalar/definite/hyperbolic pivots and quarter-power concentration | PASS | All changes of variables retain original-coordinate conditioning. Hyperbolic tails use one physical density cap and the Jacobian `1/(2 sqrt D)`; the logarithmic critical level is handled in measure-domination form. The quarter-power route proves non-atomicity before layer cake is used. |
| 520--679 | Ordered disjoint minors, sampled interpolation, completion, spectral-to-volume, random cut | PASS | Singular deleted seeds can have nonsingular extensions, so the sampling multiplicity is correctly an inequality. `P=A[:,T]B^{-1}A[S,:]` may be nonsymmetric; the proof uses singular values. Global `rank R<=3r`, restricted `rank R[L,L]<=r`, and `D=0` on the seed are all used in their correct places. The diagonal-dominance contradiction has positive slack. Random-cut factor is exactly `4^{-k}`. |
| 680--790 | Singular kernels, pivot half potential, nine-direction half potential, main theorem and scaling | PASS | The manuscript keeps truncated and full half potentials distinct. Scalar pivot loses at most one Schur direction and invokes the nine-direction full half-potential only after that hypothesis is verified. Pair pivots lose at most two. The final maximum branch is finite and the general `K,s` scaling is correct. |

No baseline mathematical section is left UNCHECKED in this review.

## B04 primary lens: heat-flow reconstruction and endpoint audit

For bounded compactly supported `h_i` of positive mass, put `f_i(t,s)=g_t*h_i(s)`, `v_i=partial_s log f_i`, and

`F(t,x)=prod_i f_i(t,u_i.x)^{c_i}`.

Because the chosen heat kernel satisfies `partial_t f_i=partial_s^2 f_i`, direct differentiation gives

`(partial_t-Delta_x)F = F[sum_i c_i v_i^2 - |sum_i c_i u_i v_i|^2]`.

Let `W` have columns `sqrt(c_i)u_i`. The frame identity is `WW^T=I`, hence `||W||=1`; applying it to `(sqrt(c_i)v_i)_i` makes the bracket nonnegative.

The integration-by-parts passage is justified without hidden smoothness of the original `h_i`. For any `0<tau<=t<=T`, heat convolution makes each factor smooth and positive. If the original support lies in `[-R,R]`, then `f_i(t,s)` has a Gaussian tail uniformly on `[tau,T]`, while

`|partial_s log f_i(t,s)| <= (|s|+R)/(2 tau)`

by writing the logarithmic derivative as the heat-kernel weighted average of `-(s-y)/(2t)`. Higher derivatives needed in the displayed calculation have the same Gaussian-times-polynomial domination. Since

`sum_i c_i (u_i.x)^2=|x|^2`,

the product and the boundary terms are integrably Gaussian. Thus differentiation under the integral and integration by parts are legitimate, and `int F(t)` is nondecreasing.

Taking traces gives `sum c_i=d`. With `x=sqrt(t)z`,

`sqrt(t) f_i(t,sqrt(t)u_i.z) -> (4 pi)^(-1/2) M_i exp(-(u_i.z)^2/4)`.

For `t>=1`, compact support and `(s-a)^2 >= s^2/2-a^2` give a uniform majorant `C exp(-(u_i.z)^2/8)`; the frame identity turns the product into `C' exp(-|z|^2/8)`. Dominated convergence therefore yields the exact large-time limit `prod M_i^{c_i}`.

At `t downarrow0`, the non-Lebesgue-point set of each one-dimensional `h_i` is null. Its inverse image under the nonzero functional `x -> u_i.x` is null by rotation plus Fubini. There are only finitely many factors, so almost every `x` is simultaneously good and Fatou gives the desired inequality. Zero-mass factors are zero almost everywhere. Finally `h_i^{(m)}=min(h_i,m) 1_{[-m,m]}` increases pointwise to arbitrary nonnegative integrable `h_i`, and monotone convergence closes both sides. **No endpoint exchange in this proof needs an unproved uniform-integrability claim.**

## Lower-threshold audit: account03/B04 nine-eigenvalue candidate

I also independently audited the new immutable account03/B04 candidate `improvements/account03/B04/20260924T121940Z-account03-B04-fixedmult-audit-r1/REPORT.md`, including its grouped product-Fourier compiler, marginal-free `E_3` density compiler, marginal-free `E_2` half-potential compiler, pivot assembly and scaling.

### Grouped compiler — PASS WITH ONE EXPLICIT LIMIT REPAIR

The report's only materially compressed passage is the sentence that smooths the complex pushforward `mu_t`, expands its `L^2` norm with an independent copy of the `J` bank, and then passes back to the unsmoothed measure. The claimed formula is correct, but a self-contained paper should spell out the limit. I supplied that repair in this run's improvement note.

The key points I checked are:

1. Push `e^{itF}dP_H` through the physical `k`-dimensional projection `W`; its complex density `a_t` satisfies `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`. Plancherel after `xi=2t(y+beta)` gives exactly `M_H(pi/|t|)^k`.
2. Condition on the original `I` coordinates before treating the pushforward through the full-row-rank physical map `M_J`. Translation by `M_I X_I` is unitary in `L^2`. Jensen bounds the mixture `L^2` norm by the averaged conditional one without discarding the `I`-phase: after expanding the conditional square and then averaging `X_I`, that phase becomes the product of the physical one-dimensional characteristic functions.
3. For a compact approximate identity `rho_epsilon`, expansion is absolutely legitimate and gives the probability kernel `kappa_epsilon(M_JD)` with `D=X_J-X'_J`. Pure `J` phases have modulus one. The uniform bound obtained later is independent of `epsilon`.
4. Fourier Fatou (`hat rho_epsilon ->1`, `|hat rho_epsilon|<=1`) gives `||nu_x||_2^2 <= liminf ||nu_x*rho_epsilon||_2^2`; Fatou in `x` then closes the unsmoothed `L^2` estimate. Thus no unjustified exchange with a possibly non-`L^2` rough density is needed.
5. Weighted Holder is exact because `sum_{T contains i} w_T/alpha_i=1`. The map `D -> (M_JD,(c_i.D)_{i in T})` has Gram determinant `S^2 det(C_T C_T^T)`, so the baseline product-projection lemma applies after deterministic SVD scaling.
6. The entropy inequality is self-contained: order a random `ell`-subset uniformly. Then `H(sequence)=H(w)+log(ell!)`, while entropy subadditivity and coordinate marginals `alpha_i/ell` give `H(sequence)<=-sum alpha_i log alpha_i+ell log ell`. This is exactly the required bound.

With this limit passage made explicit, I found no mathematical gap in the grouped compiler.

### Marginal-free `E_3` and `E_2` promotions — PASS

For third crossing volume `Z`, the incident masses satisfy `sum_i J_i=3Z`. Promotion identities are exact Gram--Schmidt identities:

`J_i=||w_i||^2 e_2(CC^T)`,

and, after a second promoted physical row,

`H_ij=det(PP^T)||C_2||_F^2`.

A residual row carrying more than half the one-volume mass produces a literal three-row Gram determinant `>H_ij/2`. These alternatives exhaust the heavy-marginal chain and preserve original-coordinate product provenance. The dominant diffuse constant is

`C_3=3 sqrt(2) e (9/2)^(1/6)=14.818337662843...`.

For second crossing volume, the analogous heavy-row promotion is exact, and the Riesz integral

`int_R |t|^(-1/2) min(1,L/|t|) dt = 8 sqrt(L)`

gives

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`.

### Nine-eigenvalue assembly — PASS after the explicit compiler-limit repair

In the no-pivot branch, the baseline order-three volume theorem at `s_9>=1` and the random cut give `E_3^{-1/6}<=160`, hence density

`<=160 C_3 = 2370.93402605488... <2400`.

At an outer scalar pivot, the Schur complement retains at least eight unit-scale eigenvalues. If it has a pivot, the baseline pivot half-potential theorem applies. If it has no pivot, `s_5>=1` is enough for the baseline order-two volume theorem and the new marginal-free `E_2` compiler, giving full half potential below `153`. Thus the scalar-pivot branch is controlled. Definite and indefinite pair pivots retain more than the hypotheses used by their baseline receivers. Scaling then gives a complete candidate theorem under `s_9(A)>=s`.

I found no source-valid counterexample to this nine-direction candidate. This review is **one** independent review of that improvement; it does not by itself satisfy the owner's two-review release gate.

## Constant sharpening discovered during this review

The nine-direction candidate can use the exact baseline scalar-pivot arithmetic instead of the rounded `600/601` constants. The manuscript proves

`H <= eta^(-1/2)(8+3L0) = 200+120 log 16`,

with `L0=4+4 log16` and `eta=1/100`. Therefore the full Schur half potential is at most

`201+120 log16`,

because the tail outside distance one costs at most one. The no-pivot Schur alternative is below `153`, so this exact pivot value still dominates. Multiplying by the outer scalar-pivot factor `eta^(-1/2)=10` gives the candidate normalized constant

`2010+1200 log16 = 5337.106466687737... <5338`.

All other nine-direction branches are below `2400`. Thus, conditional only on the now-reviewed grouped compiler, the complete nine-eigenvalue replacement proof has constant `<5338 K^2/s`, not merely `6010 K^2/s`. The separate improvement note records the full dependency map and limit repair.

## Counterexample/barrier status

The earlier B04 adaptive-leverage theorem showed that target-scale order-four volume on a selected physical crossing does **not** force a leverage gap below one: a no-pivot `s_13>=1` construction can have an order-four carrier crossing with leverage exactly one. Thus a leverage-only order-four shortcut is not a valid unconditional threshold proof. The new marginal-free order-three compiler avoids that obstruction entirely.

I did not obtain a complete proof below nine directions. The current interpolation/rank route to order-three volume needs the worst sampled seed `r=2`, where its existing global/restricted rank bookkeeping asks for `4r+1=9` large singular values. This is a limitation of this proof route, not a counterexample to an eight-eigenvalue theorem.

## Status summary

- Pinned 17-eigenvalue manuscript: **PASS** in this independent complete B04 audit.
- Geometric Brascamp--Lieb heat flow and all rough limiting passages: **PASS**.
- Missing package files `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`: **GAP / UNCHECKED because absent**.
- account03/B04 nine-eigenvalue replacement: **PASS in this review after an explicit local smoothing/Fatou repair**; still requires another genuinely separate full review before any independent-validation label.
- Sharpened nine-direction candidate constant: **`2010+1200 log16 <5338`**, with all original hypotheses retained.
- Full three-eigenvalue conjecture: **OPEN**.
