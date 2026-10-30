# fleet03/B02 r53 — independent end-to-end audit of the nine-eigenvalue manuscript

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Verdict: **MATHEMATICAL PASS AFTER ONE LOCAL NOTATION REPAIR.** No fatal gap was found in the written nine-eigenvalue theorem. This report is one genuinely separate worker audit; programme-level two-review/release status is not self-assigned here.

The unrestricted three-eigenvalue conjecture remains OPEN. Multiplicity eight remains OPEN. Full-target continuity remains OPEN.

## Pinned source actually read

Repository `yspennstate/math-open-problems`, source commit

`eeb752c8943536541b34b42b8bf48e924f4d3d2f`

at

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`.

Git blob `19fb119877426b640b2c0dae19ec2f78a399fe11`; SHA-256 `bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3`; 955 lines / 60,749 bytes. The companion README, proof map, author self-audit, MANIFEST and checks were also read from package commit `af592913ccfc4a87dfbf7c3a49bf2c5d4bbae359`.

I read all 955 lines rather than sampling theorem statements only.

## End-to-end audit map

### Lines 1–85: statement, normalization and architecture — PASS

The theorem quantifiers are preserved: arbitrary dimension, independent coordinate densities bounded by `K`, arbitrary real symmetric `A`, arbitrary affine terms, and only `s_9(A)>=s`. The rescaling `Y=KX`, `A/s`, followed by one-dimensional output scaling, correctly produces the factor `K^2/s`. No post-rotation independence is asserted.

### Lines 87–160: Fourier identities, envelopes, Riesz half potential — PASS

The Fourier normalization is internally consistent. Gaussian regularization justifies Plancherel and inversion. The power-envelope integral gives `ap/[pi(p-1)]`. The half-Riesz representation and the `|t|^{-1/2}` weight have the correct constants; the `3/4` envelope integrates to the displayed `12 sqrt(u/(2pi))` bound.

### Lines 165–203: perturbation/rank and Schur spectral count — PASS

The singular-value approximation formula yields both perturbation inequalities. The principal-pivot Schur count is valid; the singular case is obtained by fixed-threshold regularization without interchanging an unstable eigenvalue count at the boundary.

### Lines 204–278: diagonal dominance, geometric Brascamp–Lieb and product projections — PASS

The heat-flow proof uses exactly the geometric frame identity. The product-projection density estimate keeps the original product density and performs only deterministic integration; it does not declare projected coordinates independent. Zero projection weights can be omitted because the associated density factors are bounded by one. The scalar consequence has the correct `sqrt(e)/|a|` scaling.

### Lines 279–320: integrated scalar Fourier powers and decoupling — PASS

For `p>=2`, putting `m=floor(p/2)` gives

`int |fhat|^p <= int |fhat|^(2m)`.

The latter is the characteristic function of a sum of `m` independent differences. Fourier inversion at zero plus the one-dimensional product-projection bound yields

`int |fhat(t)|^p dt <= 2*pi*sqrt(2e)/sqrt(p)`.

This is the exact integrated-Fourier input B02 was asked to scrutinize. The decoupling step integrates original independent coordinates before discarding the remaining modulus-one phase; no false conditional-independence interface appears.

### Lines 321–396: regularized determinant and crossing-volume envelopes — PASS

The vectors weighted by `c_j,d_i` form a geometric frame. In the Brascamp–Lieb application, the scale factors and the scalar Fourier `L^(2/d_i)` norms cancel the powers of `d_i`. With `alpha=(2*pi*e)^2` and `a=2t`, fourth-rooting gives exactly

`|phi_Z(t)| <= det(I+t^2 M^T M/(pi^2 e^2))^(-1/8)`.

Cauchy–Binet gives the stated elementary-symmetric crossing volumes. Retaining one volume order gives the `k/4` characteristic-function exponent. The order-five density and order-three half-potential corollaries have the correct reciprocal-volume exponents.

### Lines 397–527: grouped product-Fourier receiver and physical-row promotion — PASS

This is the main new mechanism. The complex projected measure `mu_t` is legitimately in `L^2`: its variation is dominated by an ordinary convolution having a bounded density. The proof correctly mollifies before Jensen. Expanding the conditional mollified `L^2` norm gives a nonnegative kernel `K_delta(M_JD)`; the pure `J` phase is discarded only after the original `I` variables have been integrated into scalar Fourier factors.

Weighted Holder is applied to a finite measure, not incorrectly to a probability measure. The selected linear map has row-Gram determinant `S^2 det(C_T C_T^T)`. Its product-projection density cap and the integrated scalar Fourier estimate give the correct subset factor. Entropy subadditivity yields

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

After the uniform mollifier bound, approximate-identity convergence gives the unmollified `L^2` estimate.

The heavy-row promotion is physical: every promoted hub is a literal original coordinate, Gram–Schmidt gives the exact incident-volume factorization, and all residual couplings are retained. Hence order three gives a genuine `|t|^{-3/2}` receiver and a density bound; order two gives only a half-potential, as stated.

### Lines 528–662: scalar/pair kernels and quarter-power concentration — PASS after a local notation repair

The scalar square profile, definite pair Jacobian and pair half-potential scaling are correct. The hyperbolic pair coarea computation has the correct Jacobian `1/(2 sqrt(D))`, and the tail estimate uses only an original-coordinate density cap.

**Local presentation repair.** On the positive tail, the source chooses an original coordinate `i` with `|u_i|>=|u|/sqrt2`. On the negative tail it says to use `w` instead of `u` but then reuses the symbol `i` in a bound controlled by `|u_i|`. The correct proof chooses a separate coordinate `i_-` with `|w_{i_-}|>=|w|/sqrt2`. Since `|u|=|w|`, the same cutoff bound and every displayed constant are unchanged. This is notation/presentation, not a mathematical obstruction.

The quarter-power concentration argument is also valid: either a large physical diagonal gives square-root small-ball control, or a signed physical cut has operator norm at least `L/4`, after which the regularized determinant estimate and Gaussian smoothing give exponent `1/4`. Layer cake then gives the uniform logarithmic potential.

### Lines 663–766: disjoint-minor interpolation and spectral-to-volume proposition — PASS

The determinant-squared seed sampling is over nonsingular disjoint seeds only. The bordered determinant identity gives the expected Frobenius off-diagonal residual. Completion satisfies global `rank R<=3r` while its exterior `LxL` block has rank at most `r`; the proof correctly uses the latter at the diagonal-dominance contradiction.

Under no pivots, `|A_ij|^2<p+d^2`. If `V_k<kappa^k`, telescoping produces `r<=k-1` with a small volume ratio. Rank subtraction forces `r+1` large diagonal entries of `D` outside the seed, and the stated margins make the corresponding compression of `R` strictly diagonally dominant, contradicting restricted rank. This yields `V_k>=kappa^k` for `k<=3`. The random coordinate cut has exact expectation `4^{-k}V_k`.

### Lines 767–860: pair half potential, five-eigenvalue receiver and proof of the nine theorem — PASS

The full pair half-potential scales as `D^{-1/4}`. In the indefinite case the logarithmic density envelope is integrated against the half-kernel without assuming symmetry of the input laws; interval-superlevel rearrangement justifies centering the majorant.

At a scalar pivot, the Schur complement retains at least eight unit-scale spectral directions, hence the five-direction full-half-potential proposition applies. Definite and indefinite two-coordinate pivots are handled separately. The source's six normalized branch bounds are all below 400. General `K,s` scaling is correct.

The theorem therefore establishes essential boundedness at multiplicity nine. It does not prove a continuous representative in every branch, and it does not claim one.

### Lines 861–935: spectral-tail/overlap theorem — PASS

For every sampled seed the decomposition satisfies `A-R=D+E`, with `D` diagonal and `E` zero diagonal, hence exact Frobenius orthogonality. Best rank-`3r` approximation gives the spectral tail, while same-index bordering gives exactly the sampled diagonal energy. Averaging yields

`W^cross_(r,1)+(r+1)^2 V_(r+1) >= V_r sum_(j>3r)s_j(A)^2`.

For `s_8(A)>=1`, the `r=2` corollary `W>=2V_2-9V_3` follows. This is supporting algebra only; the manuscript correctly does not promote it to an eight-eigenvalue density theorem.

### Lines 936–955: threshold accounting and references — PASS / scope correctly stated

The text accurately identifies the multiplicity-eight missing step as an analytic receiver for the shared physical coordinate. The two cited bibliography entries match the primary arXiv records: Bennett–Carbery–Christ–Tao, arXiv `math/0505065`, and Rudelson–Vershynin, arXiv `1402.4492`.

## Independent quantitative improvement obtained in this audit

Using the same proved analytic architecture, I retuned the structural parameters and tightened only elementary rational bookkeeping. The complete proof and exact certificates are in

`proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/fleet03/B02/20260924T150953Z-fleet03-B02-fixedmult-audit-r53/CONSTANT_360_25.md`.

It proves the candidate sharpening

\[
 \boxed{\|p_Q\|_\infty<360.25\,K^2/s\quad\text{when }s_9(A)\ge s.}
\]

Parameters are

`d=3757/50000`, `p=28503/10000000`, `h=8227/100000`.

The critical no-pivot interpolation margin is exactly `39/500000>0`. The two largest branch bounds are

- no pivot: `360.2399257329...`, exact slack to `360.25` equal to `20720248807/2056750000000`;
- indefinite pair: `360.234972`, exact slack `3757/250000`.

The exact rational checker is `VERIFY_360_25.py`, with recorded certificates in `CHECKS_360_25.json`. Finite arithmetic checking is not substituted for the analytic proof; all analytic dependencies are the source lemmas audited above.

## Designated partner application

The completed fleet04/B02 theorem at `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7` gives, whenever a nonsingular physical `3x3` principal block `B` has a zero diagonal entry,

`int |phi_Q(t)|^2 dt <= 6*pi*2^(2/3)|det B|^(-1/3)`

and a continuous density. Plancherel therefore gives

`||p_Q||_2^2 <= 3*2^(2/3)|det B|^(-1/3)`.

Combining with the new multiplicity-nine bound gives the actual overlap inequality

`||p_Q||_4 < 28.05 |det B|^(-1/12)`.

This is an equation-level use of the designated partner result. Continuity in this overlap is supplied by the partner theorem, not inferred from the global nine-direction essential bound.

## Final status

- Nine eigenvalues, constant 400 source: **fleet03/B02 mathematical PASS after the local negative-tail notation repair**.
- Nine eigenvalues, constant `<360.25`: **new proved candidate retuning in this run; requires an independent review before release status**.
- Eight eigenvalues: **OPEN**. The remaining gap is the dependence-safe shared-anchor analytic receiver beyond the critical `|t|^{-1}` endpoint.
- Three eigenvalues: **OPEN**.
- Full-target continuity: **OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, diagonal-basis, or post-rotation-independence assumption was introduced.
