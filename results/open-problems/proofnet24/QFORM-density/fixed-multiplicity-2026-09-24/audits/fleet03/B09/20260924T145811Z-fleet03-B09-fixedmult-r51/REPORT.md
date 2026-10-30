# fleet03/B09 r51 — full fixed-multiplicity audit and `s_16` closure candidate

Run: `20260924T145811Z-fleet03-B09-fixedmult-r51`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned manuscript commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Pinned source blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Pinned SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Verdict

**Baseline `s_17` manuscript: PASS in this independent run.** I read the complete 790-line source in contiguous ranges, checked every stated lemma/proposition against its use in the main theorem, and found no fatal mathematical gap. This remains a mathematical review, not formal verification or journal peer review.

**New result from this run:** a complete candidate proof lowers the sufficient multiplicity from seventeen to **sixteen**, with

\[
\boxed{\|p_{X^TAX+b^TX+c}\|_\infty\le6010K^2/s\quad\text{if }s_{16}(A)\ge s>0.}
\]

The full proof is in the sibling improvement file `S16_MASS_TRANSPORT_CLOSURE.md`. It is pending the two independent end-to-end reviews required by the owner protocol and therefore is **not yet independently validated**.

The unrestricted three-eigenvalue conjecture remains open.

## Complete source audit

### Lines 1–168: statement, Fourier preliminaries, negative half potential — PASS

- Quantifiers and scaling target are correct and dimension/sign/law uniform.
- Fourier normalization is internally consistent: Plancherel carries `2*pi`, inversion carries `1/(2*pi)`.
- The Gaussian regularization proof uses legitimate dominated/monotone convergence.
- The Riesz half-potential constant follows from the gamma representation and the displayed weighted Fourier integral.

### Lines 169–217: perturbation, Schur spectral count, diagonal dominance — PASS

- The singular-value approximation formula proves both Lipschitz perturbation and rank shift for nonsymmetric auxiliaries.
- The Schur count is correct in the invertible case through the complementary compression of `A^{-1}`.
- In the singular limiting case, applying the invertible statement to `A+epsilon I` at threshold `t-|epsilon|` and then taking ordered-modulus limits does yield the claimed closed-threshold count. No fixed-delta repair is mathematically required, though such a rewrite could be stylistically clearer.
- Strict row diagonal dominance is used only to obtain invertibility; later quantitative inverse bounds additionally use the same argument for the transpose when needed.

### Lines 221–301: geometric BL, projection densities, scalar Fourier powers — PASS

- The heat-flow derivative has the correct sign after the frame identity; trace gives `sum c_i=d`.
- The projection-density proof does not infer independence after rotation. It integrates the original product density along orthogonal fibers and applies the proved rank-one BL inequality.
- Indices with `b_i=0` are safely discarded as pointwise factors `<=1`; including their `1-b_i` contributions only enlarges the final entropy upper bound.
- The scalar Fourier-power estimate uses `|fhat|<=1`, Plancherel, and the projection lemma at a signed coefficient vector of norm `sqrt(2m)` with the constants consistent.

### Lines 310–403: decoupling and regularized determinant — PASS

- Cauchy--Schwarz is taken before the copy expansion, so same-bank phases are removed only in modulus and no false rotated-coordinate independence is introduced.
- The graph weights form an exact rank-one frame after the `H^{-1/2}` substitution.
- `d_i<=1` makes the scalar Fourier exponent `2/d_i>=2`; the `d_i` powers cancel as stated.
- The determinant exponent `-1/8` follows from the fourth-root step.
- The order-five envelope has exponent `5/4>1` and gives a density; the order-three exponent `3/4` is used only with the Riesz weight, as required.

### Lines 404–525: scalar, definite, hyperbolic and quarter-power estimates — PASS

- The scalar square profile and interval-preimage estimate have the correct two-branch factor.
- The definite-pair Jacobian is `1/(2 sqrt(det B))`; integrating `theta` yields `pi/sqrt(det B)`.
- The hyperbolic change of variables has the correct determinant scale and treats the rough-law exceptional critical value through test-function/Tonelli domination rather than pointwise conditioning.
- The quarter-power alternative is exhaustive: either a diagonal is large, or the off-diagonal part has operator norm at least half and a physical sign split produces a large cross operator. The Gaussian smoothing integral yields the stated fourth-root small-ball bound and atom exclusion.

### Lines 528–630: ordered disjoint volumes, interpolation, rank bounds, spectral-to-volume — PASS

This is B09's primary lens and was re-derived in detail.

- The bordered-determinant identity is correct for the nonsymmetric interpolation `P=A[:,T]B^{-1}A[S,:]`; sorting signs disappear after squaring.
- The proof gives the full weighted expectation
  `sum w_ST ||F_ST||_F^2 / V_r <= (r+1)^2 V_(r+1)/V_r`, not merely the existence statement. This stronger fact is the key new input used below.
- `R-P` is supported in rows `T` or columns `S`, yielding the global `rank R<=3r`, while `R_LL=P_LL` gives the sharper restricted rank `<=r`.
- Under the baseline `4r+1` count, rank shift forces `r+1` large diagonal entries in `L`; the exact terminal dominance margin is
  \[
  371/400-23/28=297/2800>0.
  \]
- The random-cut factor `4^{-k}` is correct because an ordered disjoint `(S,T)` lands on the prescribed sides with probability `2^{-2k}`.

### Lines 632–790: no-pivot consequences, pivots, scaling and limitations — PASS

- The no-pivot `s_9` half-potential and `s_17` density estimates use the correct order-three/order-five conclusions.
- The truncated/full half-potential distinction is preserved; the outer tail contributes at most one.
- Scalar, definite-pair, and indefinite-pair pivot branches exhaust the manuscript pivot definition.
- Under the normalized `s_17` theorem, Schur counts leave more than enough directions for the respective downstream estimates.
- Scaling `Y=KX`, `A -> A/s`, and `Q=(s/K^2) Qtilde` gives the correct `K^2/s` factor.
- The manuscript correctly limits continuity to branches where an integrable characteristic-function envelope was actually proved.

## Support-file audit — PASS with stated limitations

I read the current `README.md`, `SOURCE_MANIFEST.json`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. The manifest matches the pinned manuscript blob/hash and the support checker is explicitly scoped as finite reproducibility diagnostics rather than proof. The current support files are present; the earlier r50 release-side observation that they were absent is therefore obsolete.

## New `17 -> 16` argument

The improvement is based on one new aggregation step.

For a physical four-set `T`, define

\[
W_T=\sum_{S\cap T=\varnothing, |S|=4}\det(A_{S,T})^2,
\qquad V_4=\sum_TW_T.
\]

A fixed four-column cut `T | T^c` has exactly four crossing columns and Gram determinant `W_T`. Re-running the manuscript projection-density lemma plus bilinear Plancherel therefore gives the continuous-density receiver

\[
\|p_Q\|_\infty\le2eW_T^{-1/8}.
\]

Now assume no pivot and `s_16(A)>=1`. For every nonsingular four-seed `(S,T)` whose interpolation residual has Frobenius norm at most `1/16`, global rank `<=12` forces **four** large complement diagonal entries. These do not contradict restricted rank four, but they make the corresponding `4x4` block `P_HH` quantitatively invertible. With

\[
\delta=(74-3\sqrt{101})/100=0.438503731366...,
\]

one gets

\[
\det(A_{S,H})^2\det(A_{H,T})^2
\ge\delta^8\det(A_{S,T})^2.
\]

Choosing one such `H` for every low-residual seed and summing gives the exact mass-transport inequality

\[
\sum_{\rm LOW}w_{S,T}
\le\delta^{-8}\sum_H W_H^2.
\]

Set `tau=delta^8/2`. If some `W_H>=tau`, the four-column receiver gives `||p_Q||_infty<13.521`. Otherwise the low-residual seeds carry less than half of `V_4`, so the high-residual seeds carry more than half. The manuscript's weighted sampling expectation then forces

\[
25 V_5/V_4>1/512,
\qquad V_5/V_4>1/12800=\kappa/2.
\]

Since `s_16=>s_13`, the baseline order-four proposition gives `V_4>=kappa^4`; hence `V_5>kappa^5/2`. The random-cut and order-five Fourier lemmas give

\[
\|p_Q\|_\infty<400e\,2^{11/10}=2330.706.
\]

Thus every no-pivot `s_16` state is paid. All pivot branches already close under `s_16`: scalar pivot leaves at least fifteen large Schur directions and gives `6010`; definite pair `<40`; indefinite pair `<251`. Therefore the normalized global constant is `6010` and scaling gives `6010K^2/s`.

Arithmetic was independently executed in the sibling `CHECK.py`; its saved output reports PASS. That computation checks constants only; the proof is symbolic.

## Designated partner application

For completeness, the inherited fleet04/B09 physical-cross theorem gives `||p||_infty<=3|det C|^{-1/3}` for a literal invertible `3x3` cross block. On the full target-valid block matrix with `C=diag(2,2,1)`, the spectrum is `{-2,-2,-1,1,2,2}` and the theorem gives the actual inequality

\[
\|p_Q\|_\infty\le3\,4^{-1/3}=1.889881574842...,
\]

with continuity. This check is not used in the `s_16` closure.

## Remaining obligation

The new `s_16` theorem needs **two independent existing-worker end-to-end reviews** before it can replace the pinned baseline as independently validated. The next threshold `s_15` is not obtained by the same collar: a terminal four-seed then forces only three large complement diagonal entries, so a new `3+1` aggregation or genuinely stronger order-four endpoint is required.

Full three-eigenvalue QFORM remains OPEN. Full-target continuity remains OPEN; the fixed-multiplicity `s_16` candidate establishes essential boundedness globally and continuity in the two no-pivot exits.
