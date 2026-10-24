# account01/B08 r17 — prepublication source refresh

This supplement is part of run `20260922T204004Z-account01-B08-qform-r17` and supersedes only the source-frontier discussion in Section 6 of `REPORT.md`; the derivations in Sections 2--5 remain as an independent supporting route. Full QFORM remains OPEN.

## Fresh designated-partner result

After the initial report was written, the designated partner account02/B08 completed run `B08-20260922T204103Z-1dd824`, theorem `QFORM-DOUBLE-INCIDENT-RANK2-GROUPED-L3-v1`, canonical source

`yspennstate/math-open-problems@c248abc9be918698c6d5a68108c615ba1c4790b3`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/B08-20260922T204103Z-1dd824/REPORT.md`.

That result directly spends the whole double-incident rank-two physical determinant bank and improves the exact-rank-two endpoint to

`||p_Q||_infinity < 7.711210 / sqrt(|a| gamma)`.

Accordingly this B08 run makes **no novelty claim** for exact-rank-two grouped payment; its half-Riesz proof is retained as an independent derivation and a check on the same mechanism.

## New application: the remaining tail is below 1.24 percent of the second core singular value

The fresh partner's strictly higher-rank survivor gives

`sum_(nu>=3) h_nu^2 / gamma^2 < 329/3218176`,                         (A.1)

and also

`x_1 x_2 > 41413921384333/62139940601856`,                            (A.2)

where `x_nu=min(1,h_nu^2/gamma^2)` and `h_1>=h_2>=...` are the singular values of the actual physical cross block `H`.

Since `x_1<=1`, (A.2) implies

`x_2 > p_* := 41413921384333/62139940601856`,

hence

`h_2/gamma > sqrt(p_*) = 0.8163713602...`.                            (A.3)

Let `H_2` be the top-two SVD truncation and `E=H-H_2`. From (A.1),

`||E||_F/gamma < sqrt(329/3218176) = 0.01011097539...`.                (A.4)

Combining (A.3) and (A.4) gives the source-valid quantitative refinement

`boxed( ||E||_F / sigma_2(H_2) < 0.012385265. )`                       (A.5)

Equivalently, the second core singular value is more than `80.74` times the entire Frobenius tail. In particular

`||E||_op / sigma_2(H_2) < 0.012385265`.                               (A.6)

This is an actual derivation from the named account02/B08 result and sharpens the earlier account01/B06 tube (`<5.683%` relative tail) to a `<1.239%` relative-tail survivor.

## Exact remaining implication

The frontier is therefore

`QFORM-DIFFUSE-BICOLOOP-1P24PCT-TAIL-STABILITY-v1`:

> For disjoint original-coordinate banks with arbitrary within-bank quadratic-affine terms and physical cross block `H=H_2+E`, where `rank(H_2)=2`, `sigma_2(H_2)>0.81637 gamma`, and `||E||_F<0.010111 gamma` (equivalently `||E||_F<0.012386 sigma_2(H_2)`), prove a dimension-free `L^3`, half-Riesz, or outer-square density estimate without moment/support assumptions and without replacing the tail phase by an arbitrary bounded phase; or convert the tail into an already-paid ridge/second-curvature branch.

The exact-rank-two endpoint is already paid by the fresh partner, so future work should not repeat that case. The obstruction is specifically stability under the tiny but genuinely cross-bank higher-rank phase. Coefficient smallness alone is not a valid perturbative argument for arbitrary fragmented/remote supports.

No claim of continuity is made for this branch. Full QFORM remains OPEN / not proved / not disproved.