# fleet02/B02 — full fixed-multiplicity audit, auto11

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Source snapshot actually read this invocation: `yspennstate/math-open-problems@6241df6fc911c10cc7ee925dc4ca566f8c12cff0`. Canonical manuscript: git blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`, 47,883 bytes, 790 lines. I read `README.md`, `DELIVERY_STATUS.md`, `SOURCE_MANIFEST.json`, `manuscript.tex` in full, `AUDIT.md`, `proof_map.csv`, `verify.py`, and `checks.json`. The source manifest and checker both identify the same manuscript hash. The checker reports PASS on 534 exact interpolation seeds, 18 volume-sampling cases, 9 strict-sampling cases, 240 Schur diagnostics, and 30 graph-weight diagnostics; I treat these only as finite diagnostics, not proof.

## Verdict

**PASS** for the written 17-eigenvalue theorem

\[
s_{17}(A)\ge s>0\quad\Longrightarrow\quad
\|p_{X^TAX+b^TX+c}\|_\infty\le 10^4K^2/s.
\]

I found no fatal mathematical gap and no source range left mathematically unchecked. Bibliographic attribution in the two final references is marked `UNCHECKED` because it is not a proof dependency. The product-projection line after zero-weight factors are dropped is a compressed inequality, not a gap: the surviving sum is at most the full sum `d`.

## Line-range ledger

| source lines | status | independent check / downstream impact |
|---|---|---|
| 1–46 | PASS | Definitions/typesetting/abstract agree with the theorem and later proof; no hidden mathematical dependency. |
| 47–90 | PASS | Quantifiers, singular-value convention, normalized parameters, pivot definition and `9=4*3-3`, `17=4*5-3` architecture are internally consistent. |
| 91–131 | PASS | Fourier convention gives Plancherel factor `2*pi`; inversion and power-envelope integral have the stated constants. |
| 132–160 | PASS | Gaussian representation of `|z|^-1/2`, Fourier/Riesz coefficient `1/sqrt(2*pi)`, and the `12 sqrt(u/(2*pi))` envelope were recomputed. |
| 161–220 | PASS | Singular-value perturbation/rank, Schur spectral count including singular approximation, and strict diagonal dominance all close with the stated quantifiers. |
| 221–257 | PASS | Heat-flow proof of geometric rank-one BL has the correct sign, frame trace, Gaussian limit and approximation step. |
| 258–283 | PASS | Product projection cap `e^{d/2}` is valid. After `b_i=0` factors are omitted, the precise entropy step is `sum_{b_i>0}(1-b_i) <= sum_i(1-b_i)=d`; the source compresses this harmless inequality. Scalar consequence `sqrt(e)/|a|` is correct. |
| 284–303 | PASS | Scalar Fourier powers: with `m=floor(p/2)>=p/4`, inversion at zero plus the projection bound gives `2*pi*sqrt(2e)/sqrt(p)`. Difference-density cap one is valid and sharp. |
| 304–385 | PASS | Two-copy decoupling uses only original-coordinate independence. In the regularized determinant theorem the BL weights form a frame, the `d_i` powers cancel, `alpha=(2*pi*e)^2`, and fourth-root extraction gives exponent `-1/8`. |
| 386–403 | PASS | Cauchy–Binet volume expansion and order-`k` envelope are correct. `k=5` gives an integrable `|t|^-5/4` endpoint; `k=3` is used only with the Riesz weight. |
| 404–436 | PASS | Scalar-square profile/preimage length and definite-pair Jacobian `1/(2 sqrt(det B))` give the stated square-root and `pi` constants. |
| 437–484 | PASS | Hyperbolic two-coordinate change of variables, physical-coordinate tail control, and logarithmic density envelope preserve product independence correctly; no rotated-coordinate independence is asserted. |
| 485–527 | PASS | Quarter-power small-ball proof: diagonal/off-diagonal split, random physical cut, determinant tail, Gaussian smoothing coefficient and layer-cake logarithmic potential all check. |
| 528–544 | PASS | Ordered disjoint volume definition and no-pivot entry bound `|a_ij|^2<eta^2+eta<2eta` are correct. |
| 545–565 | PASS | Volume-sampled interpolation uses the bordered determinant identity; singular seeds correctly turn the aggregate count into an inequality. |
| 566–581 | PASS | Completion `A=D+R+E` has zero-diagonal `E`, global `rank R<=3r`, and restricted `rank R[L,L]<=r`; nonsymmetry is harmless because only singular-value/rank facts are used. |
| 582–620 | PASS | Spectral-to-volume proof closes: ratio selection, perturbation, forced diagonal coordinates in `L`, and exact diagonal-dominance slack are valid. |
| 621–631 | PASS | Fair physical cut pays each ordered disjoint minor with probability `4^-k`; expectation and existence conclusion are correct. |
| 632–653 | PASS | No-pivot order-three half potential and order-five density constants follow from the physical crossing volume without extra assumptions. |
| 654–675 | PASS | Both singular-kernel estimates follow from the stated substitutions/layer-cake argument. The source's coarse constants are valid. |
| 676–715 | PASS | Pivot truncated-half-potential branches are dependence-safe. Scalar Schur remainder uses one surviving direction; definite and indefinite pair branches have the stated uniform bounds. |
| 716–725 | PASS | Nine-eigenvalue full half-potential proposition correctly joins pivot/no-pivot cases and adds at most one outside the truncation window. |
| 726–768 | PASS | Main theorem exhausts no-pivot/scalar/definite/indefinite cases. Schur losses leave the required spectral counts; constants are below `10^4`; scaling by `Y=KX` gives exactly `K^2/s`. |
| 769–783 | PASS | Threshold accounting accurately distinguishes order-five density from order-three half-potential and does not claim continuity in pivot branches or a three-eigenvalue theorem. |
| 784–790 | UNCHECKED | Bibliographic attribution only; no theorem in the proof is invoked from these references because the needed statements are proved in the manuscript. |

## B02 adversarial normalization checks

1. **Scalar Fourier exponent is sharp.** For the admissible cap-one Gaussian `f(x)=exp(-pi x^2)`, under the manuscript convention
   `fhat(t)=exp(-t^2/(4*pi))` and exactly
   `int |fhat(t)|^p dt = 2*pi/sqrt(p)`.
   Therefore no law-uniform improvement can replace the `p^-1/2` exponent in the scalar Fourier-power lemma by a faster power. Only constants can improve by that route.

2. **Convolution cap one is sharp.** For `X~Unif[-1/2,1/2]`, `f<=1` and the difference density satisfies `(f*tilde f)(0)=int f^2=1`.

3. **Projection constant has a nontrivial lower benchmark.** For two independent `Unif[-1/2,1/2]` variables, `(X_1+X_2)/sqrt(2)` has density peak `sqrt(2)`. Thus a universal scalar projection constant cannot be below `sqrt(2)`; the manuscript's `sqrt(e)` is consistent.

4. **Order two alone cannot be a bounded-density endpoint.** For the same cap-one uniforms, `X^2` has density `s^-1/2` on `(0,1/4)`. Hence the density at zero of `X_1^2-X_2^2` contains `int_0^{1/4} ds/s=infinity`. This is a source-valid low-dimensional obstruction to any proposed `E_2`-only `L^infinity` receiver. It does not refute an eight- or nine-eigenvalue theorem, which must spend additional structure.

5. The determinant compiler's `-1/8` exponent therefore has the expected endpoint behavior: retaining order `k` gives `|t|^{-k/4}`. Order four is exactly `|t|^-1` and is not directly `L^1`; order five is the first direct density endpoint in that ungrouped compiler. The threshold-nine grouped receiver succeeds by a different product-Fourier mechanism, not by improving the scalar `p^-1/2` exponent.

## Downstream status

The pinned 17-eigenvalue manuscript remains PASS in this audit. A complete threshold-nine replacement is already present in the repository and was re-read in this invocation; I do not infer any theorem below nine. The separate improvement artifact from this run retunes the already-complete threshold-nine proof to a new constant `<536 K^2/s`. Multiplicity eight remains a GAP, and the unrestricted three-eigenvalue QFORM conjecture remains OPEN.

Model self-report: `GPT-5.6 Sol`. Reasoning effort configured/self-report: `UNKNOWN`. Provider reasoning-token and thinking-time telemetry: `null / not exposed`.
