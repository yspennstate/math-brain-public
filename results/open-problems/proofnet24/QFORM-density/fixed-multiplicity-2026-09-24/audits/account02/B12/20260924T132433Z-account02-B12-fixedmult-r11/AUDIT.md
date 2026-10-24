# account02/B12 — complete fixed-multiplicity audit, scalar-pivot / logarithmic-kernel lens

Run: `QFORM-FM-AUDIT-B12-20260924T132433Z-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Reviewer role: account02/B12 (counterexample emphasis; scalar pivots, completing-square shifts, square/log kernels)  

## Source pin and verdict

Mathematical baseline audited: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, file `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`. The source git blob is `183ccd294763214e6a707e8d4749ff9a8cf7006d`, package SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes, 790 lines. At the final pre-write refresh, master was `8c893780233ba299a0fa3954b07409f462d744fe` and `manuscript.tex` still returned the same source blob.

**Mathematical verdict on the pinned 17-eigenvalue theorem: PASS in this review.** I found no theorem-breaking FALSE statement and no fatal mathematical GAP. I found one harmless presentation GAP in the projection-density proof (described below), plus UNCHECKED package/build and historical-test claims that are not mathematical dependencies. This is one worker review, not formal verification or an independent-validation certificate. The unrestricted three-eigenvalue QFORM conjecture remains open.

I read the complete package requested by the owner: `README.md`, `SOURCE_MANIFEST.json`, all 790 lines of `manuscript.tex`, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`, plus the package `DELIVERY_STATUS.md` required by the README. The table below covers every manuscript source line 1–790; no source range is intentionally omitted.

## End-to-end source audit

| Lines | Statement / equations | Verdict | Independent reasoning, counterexample/repair, impact and next obligation |
|---|---|---|---|
| 1–46 | Preamble, abstract, conventions | PASS | Mathematical scope matches the theorem actually proved: arbitrary dimension/signature/remaining spectrum/affine terms and rough product densities. No continuity of all branches is promised. |
| 47–61 | `thm:main`, `cor:33`, equation `eq:main` | PASS | Quantifiers are closed and scale correctly. `s_17(A)>=s>0` is the only spectral hypothesis. The 33 statement is genuinely a stronger-hypothesis corollary. |
| 62–90 | proof architecture, `eta=1/100`, `kappa=1/80^2` | PASS | The two spectral counts are correctly separated: order 3 is used only for a half-potential, order 5 for direct Fourier inversion. No rotated-coordinate independence is asserted. |
| 91–120 | `lem:fourier`, Plancherel, inversion, Gaussian inversion | PASS | The regularized Plancherel argument, approximate identity, weak convergence, and Gaussian Fourier normalization all have the stated `2pi` constants. Fubini is protected by Gaussian integrability. |
| 122–130 | `lem:envelope` | PASS | Direct integration gives `2ap/(p-1)` and inversion gives `ap/[pi(p-1)]`; hypothesis `p>1` is exactly the endpoint needed. |
| 132–160 | `lem:riesz`, negative half moments | PASS | The Gamma representation and `v -> t^2/(4v)` substitution give the coefficient `1/sqrt(2pi)`. The weighted envelope integral is exactly `12 sqrt(u)`. Extended values and Tonelli are handled correctly. |
| 161–181 | singular-value notation and `lem:rank` | PASS | Both inequalities follow from the best-rank approximation formula and do not need symmetry; this is important later because `R,E` are nonsymmetric. |
| 183–207 | `lem:schur` | PASS | In the invertible case inverse-compression/interlacing gives the absolute-eigenvalue count after separately treating signs. The singular case can be approached by a sequence `A+eps I` avoiding singular pivots; the moving threshold `t-|eps|` tends to `t`, so the claimed non-strict threshold survives. |
| 209–217 | strict diagonal dominance | PASS | Standard maximal-coordinate proof works without symmetry. |
| 218–255 | geometric rank-one Brascamp–Lieb | PASS | Heat-flow differentiation has the correct sign because the frame map is a contraction; the large-time Gaussian normalization uses `sum c_i=d`; small-time Fatou plus truncation/monotone convergence covers rough nonnegative integrable functions. |
| 256–282 | `lem:projection` | **GAP (presentation only)** | The proof is mathematically valid. After dropping factors with `b_i=0`, the entropy sum is over `b_i>0`; the text then writes the all-index identity `sum_i(1-b_i)=d/2` as if no terms were added. The repair is simply `log p <= (1/2) sum_{b_i>0}(1-b_i) <= (1/2) sum_i(1-b_i)=d/2`. This changes no constant or downstream claim. |
| 283–301 | `lem:scalar-fourier` | PASS | For `m=floor(p/2)`, `m>=p/4`; inversion at zero for the sum of `m` differences plus the scalar projection bound gives `2pi sqrt(2e)/sqrt(p)`. Difference densities are indeed capped by one. |
| 302–324 | cross-form and `lem:decoupling` | PASS | Cauchy–Schwarz, an independent copy in the J-bank, and integration over original independent I-coordinates yield the product. Jensen gives the fourth power. No moments or rotated independence are used. |
| 325–373 | `thm:determinant`, `eq:graph-bl` | PASS | The whitened frame sums to identity. The one-dimensional Jacobian powers in BL are correct. `||g_j||_{1/c_j}<=1` uses both cap and mass; scalar-Fourier with `p=2/d_i` cancels the `d_i` factors. With `alpha=(2pi e)^2`, all residual scalar factors cancel, and the fourth root gives determinant exponent `-1/8`. |
| 374–400 | crossing volumes and `cor:vol-fourier` | PASS | Cauchy–Binet identities are correct. Retaining the kth coefficient gives exponent `k/4`; `k=5` yields `5e Z_5^{-1/10}` and `k=3` yields the stated half-moment bound, not a density bound. |
| 401–414 | `lem:square` | PASS | Change of variables on two monotone inverse branches gives the exact square-root profile. The interval-preimage length estimate is sharp in order. Rough densities need no pointwise regularity beyond choosing bounded versions. |
| 415–421 | conditional scalar profile `eq:profile` | PASS | Completing the square is conditional on original coordinates. The random shift may be unbounded and depend arbitrarily on the complement; this causes no issue because for each conditioning value it is a deterministic translation. The residual quadratic matrix is exactly the scalar Schur complement. The domination/test-function formulation avoids exceptional-slice assumptions. |
| 423–434 | `lem:definite` | PASS | Completion of the square plus deterministic orthogonal coordinates in the two-dimensional integral does not assert independence after rotation. The joint density cap is enough and the `(delta,theta)` Jacobian is `1/(2 sqrt(det B))`, giving `pi M/sqrt(|det B|)`. |
| 435–482 | `lem:hyperbola`, `eq:hyperbola`, `eq:hyper-coarea` | PASS | The hyperbolic level-set Jacobian is `1/(2 sqrt D)`. Crucially, the eigenvectors only parametrize points in the original plane; the integrand remains `f_1(w_1)f_2(w_2)`, so no rotated-law independence is used. Tail integrals use only density cap 1 and mass 1. The middle interval produces the correct logarithm and the critical level is handled measure-theoretically. See stress counterexample below: the logarithm is genuinely necessary. |
| 483–525 | `lem:quarter`, `eq:quarter`, `eq:log-bound` | PASS | Large diagonal gives square-root concentration. Otherwise random signs isolate a cross block with norm at least `L/4`; one determinant singular factor plus Gaussian smoothing yields quarter power. Layer cake then gives `L_0=4+4 log 16`; shrinking rho excludes atoms. No support/moment assumption is hidden. |
| 526–544 | pivot and volume definition; no-pivot entry bound | PASS | A symmetric invertible 2x2 principal block is definite when determinant is positive and indefinite when negative, so the later pivot split is exhaustive. No-pivot implies `|a_ii|<eta` and `|a_ij|<1/7` from the 2x2 determinant bound. |
| 545–564 | `lem:sampling` | PASS | Bordered determinant identity is valid for the nonsymmetric interpolant. Squaring removes sorting signs. Each ordered `(r+1)` extension is charged at most `(r+1)^2` times; singular seeds can have nonsingular extensions, so the proof correctly uses an inequality rather than equality. |
| 565–580 | `lem:completion` | PASS | With `E` only the off-diagonal LxL error and `D=A_ii-P_ii` on L, one gets `R_LL=P_LL`, hence restricted rank `<=r`. Interpolation makes `R-P` vanish on rows S, columns T and the whole LxL block; the remaining support splits into rows T plus columns S, giving global rank `<=3r`. `D` vanishes on the seed exactly. |
| 581–619 | `prop:volume` | PASS | Telescoping finds a bad ratio. At `r=0`, the off-diagonal Frobenius norm plus small diagonal makes `||A||<1`. At `1<=r<=4`, `eps<=(r+1)/80<=1/16`; rank spending produces at least `r+1` large diagonal entries because `m=4k-3>=4r+1`. Those entries lie in L. The explicit row-sum bound `23/28 < 371/400` makes an `(r+1)x(r+1)` subblock of `R_LL` invertible, contradicting restricted rank `<=r`. The use of singular values for nonsymmetric `A-E` is correct. |
| 620–645 | random cut and no-pivot consequences | PASS | Each ordered disjoint `(S,T)` lands across a fair cut with probability `4^{-k}`. Hence `Z_k^{-1/(2k)}<=160`. Constants are correct: order 3 gives `12 sqrt(80e)<200`; order 5 gives `800e<2400`. |
| 646–674 | truncated half potential and `lem:kernels` | PASS | Both kernels are locally integrable exactly at the needed endpoint. The two-square-root kernel is logarithmically divergent as `d->0` but bounded by `8+3 log_+(1/|d|)` for nonzero d. The log-kernel overlap/layer-cake argument gives the uniform value 8. Stress tests below show neither logarithm can simply be deleted. |
| 675–714 | `prop:pivot-H` | PASS | Scalar pivot: Schur count leaves one spectral direction for quarter-power anti-concentration of the residual; profile plus Tonelli gives `E J(R-a)`, and the logarithmic moment closes it. Definite pair: uniform conditional density closes immediately. Indefinite pair: hyperbolic logarithm is integrated against the half kernel and `sup D^{-1/2} log_+D=2/e`. The constants are safely below 600. |
| 715–724 | `prop:nine` | PASS | Pivot and no-pivot cases cover all matrices. The no-pivot estimate is a full half-potential; outside the truncated unit window the kernel is at most 1, so `<=601` is valid. |
| 725–749 | proof of main theorem | PASS | No-pivot branch uses the order-five density estimate. Scalar pivot removes one coordinate and Schur leaves at least 16 large modes, enough for Proposition 9; `10*601=6010`. A principal definite pair has density `<=10pi`. An indefinite pair leaves at least 15 Schur modes, hence residual operator norm at least 1; averaging its log envelope using `L_0` gives `<251`. Test-function/Tonelli language handles conditioning-dependent critical values. Scaling `Y=KX`, `Q=(s/K^2) Qtilde` produces exactly `10^4 K^2/s`. |
| 750–780 | threshold accounting and limitations | PASS | The manuscript accurately identifies why 17 appears and explicitly does not claim three eigenvalues or optimality. Continuity is separated from essential boundedness. |
| 781–790 | acknowledgments and classical attributions | UNCHECKED | Bibliographic priority/attribution was not independently re-researched in this B12 run and is not used as a proof dependency because the needed inequalities are reproved in the manuscript. No mathematical impact on the theorem. |

## B12 adversarial endpoint tests

### 1. The indefinite-pair logarithm is real, not proof slack

Take independent `X,Y ~ Unif[-1/2,1/2]`, so each density is exactly one, and let

`Z = 2XY = (X,Y) [[0,1],[1,0]] (X,Y)^T`.

For `0<|z|<1/2`, direct product change of variables gives

`p_Z(z) = log(1/(2|z|))`.

Thus an indefinite two-coordinate pivot can have an unbounded conditional density at its critical level even for compactly supported cap-one inputs. Any attempted repair replacing Lemma `hyperbola` by a uniform L-infinity conditional bound is FALSE. The manuscript correctly retains a logarithmic singularity.

The singularity is nevertheless integrable against the later half kernel:

`int_{-1/2}^{1/2} |z|^{-1/2} log(1/(2|z|)) dz = 4 sqrt(2) < 8`.

This is a concrete rough-law stress test of the endpoint mechanism in `lem:kernels` / `prop:pivot-H`.

### 2. The scalar square-root singularity is also sharp

For `X ~ Unif[-1/2,1/2]`, the density of `X^2` is exactly

`p_{X^2}(z)=z^{-1/2} 1_{(0,1/4)}(z)`.

So a scalar pivot does not itself give a bounded conditional density. Worse, composing two coincident square-root kernels is logarithmically divergent. Correspondingly, for `0<d<1/4`,

`J(d) >= int_{2d}^1 dx/x = log(1/(2d))`.

Hence a uniform-in-d bound for `J(d)` is impossible. The quarter-power/logarithmic anti-concentration of the Schur residual is a genuine obligation, not cosmetic slack.

### 3. Completing-square shifts do not need moments or bounded support

At a scalar pivot, the conditional shift `m(X_{-i})` can be arbitrary and unbounded. At a two-coordinate pivot, the conditional vector shift can likewise be arbitrary. The proof never integrates a bound depending on these shifts: it translates each conditional original-coordinate density, preserving its cap and (for the pair) product structure. This checks the manuscript's stated rough-law scope and shows why no hidden moment/support assumption enters through completion of the square.

## Constants independently checked in the pivot chain

With `eta=1/100` and `L_0=4+4 log16`:

- scalar-pivot truncated half potential: `10(20+12 log16) = 532.710646... <560<600`;
- definite-pair truncated half potential: `40 pi =125.663706... <160`;
- indefinite-pair truncated half potential after the scalar maximum: `10(32+4 log16)+4/e =432.375... <444<600`;
- no-pivot order-three full half potential: `12 sqrt(80e)=176.959... <200`;
- no-pivot order-five density: `800e=2174.625... <2400`;
- final scalar-pivot density: `6010`;
- final indefinite-pair density bound: `10(10+5 log16)+1/e=238.997... <251`.

These are arithmetic checks only; the proof audit above supplies the analytic justifications.

## Package/support-file audit

- **README.md — PASS.** It states the correct 17-eigenvalue candidate, explicitly labels it a candidate under independent review, and does not claim the unrestricted theorem.
- **SOURCE_MANIFEST.json — PASS for source pin / GAP only as unverified build metadata.** The baseline commit, git blob, SHA-256, byte count and line count agree with the package and fetched source identity. The compiled-PDF hash, three-pass build and visual-render claims were not independently reproduced here, so those delivery facts are **UNCHECKED** in this review and have no proof impact.
- **AUDIT.md — PASS as a clearly labeled historical self-report; its old finite-test counts are UNCHECKED here.** The current package itself correctly warns that the later checker does not reproduce those older counts. I do not promote those historical diagnostics to proof evidence.
- **proof_map.csv — PASS.** The labels and statement/proof line ranges agree with the manuscript and were used to structure this complete review.
- **verify.py — PASS as a scoped finite checker.** Its exact tests exercise interpolation identities/ranks and the diagonal-dominance slack; its floating tests probe Schur counts and graph weights. The script explicitly says it is not a proof certificate.
- **checks.json — PASS for internal consistency with the current checker schema; execution provenance UNCHECKED.** It reports 534 exact interpolation seeds, 18 exact volume cases, 9 strict cases, slack `297/2800`, 240 Schur diagnostics and 30 graph cases. I did not rerun external processes in this audit, and none of these finite counts is used to infer universal correctness.

## Attempt to reduce 17: exact obstruction to the current rank-count route

No lower-threshold theorem is claimed. I did not create an improvement artifact because the owner requires a complete replacement proof before lowering 17.

The present proof would also work from 16 large singular values for every bad sampling ratio occurring at `r<=3`; the only unpaid endpoint is `r=4`. There, with `m=16`, global rank spending gives only

`m-3r = 16-12 = 4`

large entries of the diagonal part, whereas the contradiction to `rank(R[L,L])<=4` requires **five** large diagonal coordinates.

This is not just an arithmetic oversight in the written argument. The three abstract conclusions used at that step are insufficient by themselves. On 16 formal coordinates split into an eight-coordinate seed and an eight-coordinate complement L, let `D` vanish on the seed and equal one on four L-coordinates. Let `R` be diagonal, equal one on all eight seed coordinates and on the other four L-coordinates. Then

- `rank R = 12 = 3r`,
- `rank R[L,L] = 4 = r`,
- `D` vanishes on the seed,
- `D+R = I_16`, so `s_16(D+R)=1`,
- but D has only four large diagonal entries in L.

Therefore no proof using only these rank-count facts can force the five-coordinate diagonal-dominance contradiction at 16. This synthetic example is **not** a counterexample to the 16-eigenvalue density theorem or to a strengthened no-pivot volume proposition; it is a counterexample to the tempting shortcut “replace 17 by 16 in the same rank-count proof.” A valid 16 theorem must exploit additional interpolation/symmetry/no-pivot structure or a different analytic receiver at the `r=4` endpoint, and must provide a full replacement dependency chain and constants.

## Final status and next obligations

- `thm:main` at multiplicity 17: **PASS in this independent worker review**.
- Fatal mathematical FALSE findings: **none**.
- Mathematical GAP findings: **none**.
- Presentation GAP: projection proof's dropped-`b_i=0` entropy sum; one-line inequality repair above, no downstream effect.
- UNCHECKED: bibliographic priority, compiled-PDF/build/render claims, historical/self-audit test counts, and actual execution provenance of the supplied finite checker; none is a theorem dependency.
- Threshold 16: **OPEN**. The exact local obligation is the `r=4` endpoint; the existing rank budget alone cannot close it.
- Unrestricted three-eigenvalue QFORM: **OPEN and not claimed solved**.
