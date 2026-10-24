# account01/B07 full audit — fixed-multiplicity manuscript

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T133059Z-account01-B07-fixedmult-audit-r12`  
Repository: `yspennstate/math-open-problems`  
Baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Audited current-head snapshot at start: `d11ccbed9e8d0f45b0f42b519564641bdfb9f1bc`; source blob there is still exactly `183ccd294763214e6a707e8d4749ff9a8cf7006d`.  
Manifested SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

## Verdict

**PASS for the complete written 17-eigenvalue theorem, modulo one nonfatal wording GAP in `lem:projection`; no fatal mathematical defect found.**

The theorem audited is exactly: independent arbitrary real coordinate densities `<=K`; arbitrary real symmetric `A`; arbitrary affine `b,c`; if `s_17(A)>=s>0`, then `X^TAX+b^TX+c` has an essentially bounded density with norm at most `10000 K^2/s`. The audit does not claim the unrestricted three-eigenvalue conjecture.

The only manuscript issue I found is a presentation-level omission in the product-projection proof: after rows with `b_i=0` are dropped, the proof jumps from a sum over retained rows to `sum_i(1-b_i)=d`. The valid chain is

`sum_{b_i>0}(-b_i log b_i) <= sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`.

Thus the stated `e^{d/2}` bound is unchanged. No downstream constant or theorem changes.

## Full source-range audit

Every source line 1--790 was read. The following table records the end-to-end verdict rather than merely the B07 starting lens.

| Source range / label | Verdict | Reasoning and downstream consequence |
|---|---|---|
| 1--46 preamble, abstract | PASS | Abstract matches the theorem actually proved; no extra continuity/optimality claim. |
| 47--85 `thm:main`, `cor:33`, architecture | PASS | Quantifiers retain arbitrary dimension, signature, remaining spectrum, affine terms and rough product laws. Normalization target `K=s=1` is later reversed correctly. |
| 86--121 `lem:fourier` | PASS | Gaussian regularization, Plancherel normalization and inversion constants are consistent with `hat f(t)=int e^{itx}f(x)dx`; weak convergence identifies the density. |
| 122--131 `lem:envelope` | PASS | Envelope has integral `2ap/(p-1)` and inversion contributes `1/(2pi)`. |
| 132--160 `lem:riesz` | PASS | Gamma representation, Gaussian inversion, Tonelli and the `sqrt(2) Gamma(1/4)|t|^{-1/2}` integral give the displayed normalization; the power-envelope integral is `12 sqrt(u)`. |
| 161--181 `lem:rank` | PASS | SVD approximation formula proves perturbation and the rank-shift inequality for nonsymmetric matrices. |
| 182--208 `lem:schur` | PASS | For invertible `A`, `S^{-1}` is the complementary principal block of `A^{-1}`; signed interlacing applied at `+-t^{-1}` gives the absolute spectral count. Singular `A` is obtained by `A+eps I` with thresholds approaching `t` from below. |
| 209--217 `lem:dd` | PASS | Standard maximal-coordinate proof works without symmetry. |
| 218--255 `thm:bl` | PASS | Heat-flow sign is correct: `partial_t F-Delta F>=0`, so the integral is nondecreasing toward the product of masses. Frame contraction, large-time Gaussian limit, small-time Fatou and monotone truncation are adequate. |
| 256--283 `lem:projection` | **GAP (nonfatal wording)** | BL setup and Jacobians are correct. After zero-`b_i` factors are dropped, one needs the extra inequality `sum_{b_i>0}(1-b_i)<=sum_i(1-b_i)=d`. The stated bound remains valid. |
| 284--301 `lem:scalar-fourier` | PASS | `m=floor(p/2)>=p/4`; `|hat f|^{2m}` is an integrable characteristic function of `m` differences. Projection density at zero yields exactly `2pi sqrt(2e)/sqrt(p)`. |
| 302--325 `lem:decoupling` | PASS | First Cauchy--Schwarz leaves an independent `J` copy; original `I` independence gives the product Fourier factors. Jensen gives the fourth-power version. Difference densities stay `<=1`. |
| 326--373 `thm:determinant` | PASS | The graph frame sums to identity. `c_j,d_i` lie in `[0,1]`; the BL Jacobians and `L^{1/c_j}`, `L^{1/d_i}` factors are correct. Scalar Fourier powers cancel the `d_i` factors, the entropy factor contributes `e^{theta/2}`, and `alpha=(2pi e)^2` cancels the remaining scalar term. Fourth roots give exponent `-1/8`. |
| 374--400 `Z_k`, `cor:vol-fourier` | PASS | Cauchy--Binet expansion is correct; retaining the order-`k` term yields exponent `k/4`. For `k=5`, inversion gives `5e Z_5^{-1/10}`; for `k=3`, the Riesz estimate gives the stated half-potential bound. |
| 401--422 `lem:square`, profile | PASS | Two inverse branches and derivative give the square-root density; interval preimage length is correct. Conditional measure domination gives the Schur-complement profile without claiming independence. |
| 423--436 `lem:definite` | PASS | Two-dimensional quadratic polar coordinates have Jacobian `1/(2 sqrt(det B))`; joint cap is used before any deterministic rotation. |
| 437--484 `lem:hyperbola` | PASS | Hyperbolic Jacobian, original-coordinate tail selection, tail cutoffs and logarithmic filling argument are valid. The branch constant `15/2 log 2<6` and `Lambda>=2/sqrt(D)` yield the displayed envelope. |
| 485--525 `lem:quarter` | PASS | Large diagonal gives a square small-ball bound. Otherwise the random-sign cut supplies a physical cross block with norm `>=L/4`; determinant decay, Gaussian smoothing and layer cake produce the quarter-power and log bounds. |
| 526--544 `def:pivot-volume`, no-pivot entry bound | PASS | Ordered disjoint pairs and increasing index conventions are explicit. No pivot implies `|a_ij|^2<eta^2+eta<1/49`, hence `|a_ij|<1/7`. |
| 545--565 `lem:sampling` | PASS | **B07 core check.** For a nonsingular ordered disjoint seed `B=A[S,T]`, row elimination gives the bordered identity `det extension = +/- det(B)(A_lm-P_lm)`. Squaring removes sorting signs. Each ordered `(r+1,r+1)` disjoint extension has at most `(r+1)^2` deleted seed pairs. Singular seeds carry zero sampling weight but may have nonsingular extensions, so only `<=` is valid; the manuscript states exactly that. |
| 566--581 `lem:completion` | PASS | **B07 core check.** `E` is precisely the off-diagonal `LxL` defect, `D` the diagonal defect on `L`, and `D=0` on `S union T`. Interpolation makes `R-P` vanish on rows `S`, columns `T` and all `LxL`; remaining support is in rows `T` or columns `S`, giving global rank `<=3r`, while `R[L,L]=P[L,L]` has rank `<=r`. |
| 582--620 `prop:volume` | PASS | Telescoping/first-zero logic finds a small adjacent volume ratio. The `r=0` case contradicts `||A||<1`. For `1<=r<=4`, perturbation plus global rank forces `r+1` large diagonal entries of `D` in `L`; no-pivot entry bounds and `||E||_F<=1/16` make `R[H,H]` strictly diagonally dominant, contradicting restricted rank `<=r`. Constants check: diagonal lower `371/400`, row upper `23/28`, slack `297/2800>0`. |
| 621--631 `lem:cut` | PASS | **B07 core check.** Each ordered disjoint pair `(S,T)` survives a fair physical cut as `S subset I, T subset J` with exact probability `2^{-2k}=4^{-k}`; linearity gives the expectation with no multiplicity loss. |
| 632--645 `cor:no-pivot` | PASS | `Z_k^{-1/(2k)}<=160`; the `k=3` half-potential is `<200`, and `k=5` density is `800e<2400`. |
| 646--675 `H`, `lem:kernels` | PASS | Near/far split in `J(d)` and layer-cake overlap argument for the logarithmic kernel are correct at the stated generous constants. |
| 676--715 `prop:pivot-H` | PASS | Scalar pivot uses one surviving Schur direction and the log potential; definite pair is direct; indefinite pair uses the uniform logarithmic envelope. These alternatives exhaust pivots. |
| 716--725 `prop:nine` | PASS | Pivot branch gives truncated half-potential; no-pivot `s_9` gives the full half-potential. The outside tail contributes at most one. |
| 726--749 proof of `thm:main` | PASS | No-pivot `s_17` closes directly. Scalar pivot loses one Schur direction and has at least nine for the half-potential; pair pivots close as written. Scaling `Y=KX` gives cap one and `Q=(s/K^2) Qtilde`, hence `10000K^2/s`. |
| 750--790 accounting, remarks, bibliography | PASS for mathematical scope; **UNCHECKED for exhaustive prior-art/priority** | Threshold accounting accurately describes this proof. The bibliography is attribution only and is not a proof dependency. I did not perform an exhaustive publication-priority review in this run. |

## Supplementary-file audit

- `README.md`: PASS. It now accurately lists the complete source and support files and distinguishes the conversation PDF from repository source.
- `DELIVERY_STATUS.md`: PASS as a status document; its native-scheduler statements are not mathematical evidence and were not used in this audit.
- `AUDIT.md`: PASS as a historical self-report, **not** independent validation. Its older finite-test counts are explicitly distinguished from the new checker.
- `proof_map.csv`: PASS. The labels and source/proof ranges match the source read in this run.
- `SOURCE_MANIFEST.json`: PASS for internal consistency: it pins baseline commit, source blob, line/byte counts and support hashes. **UNCHECKED:** I did not independently recompute the PDF binary hash or visually inspect the unavailable compiled binary.
- `verify.py` / `checks.json`: PASS for code-to-result consistency. I independently reran the mathematical body of the checker in the present local Python environment (omitting only the repository-file SHA gate) and reproduced exactly: `534` interpolation seeds, `18` volume-sampling cases, `9` strict-sampling cases, diagonal slack `297/2800`, `240` floating Schur threshold cases and `30` graph-weight cases. These diagnostics are not proof certificates.

## Downstream status

No fatal gap is present in the pinned 17-direction argument on this review. The projection wording issue can be repaired locally without changing any statement or constant.

After finishing the baseline audit, I separately reconstructed the current nine-direction improvement. That work is saved in this run's improvement artifact. The baseline manuscript itself is intentionally not overwritten.